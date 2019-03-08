import asyncio
import aiohttp
from datetime import datetime

import discord
from discord.ext import commands

import utils
from params import *
from api import RaiderIO, Blizzard, Warcraftlogs, Bloodmallet


bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="World of Warcraft"))
    print("Logged in as {}".format(bot.user.name))

@bot.command(name="명령어", pass_context=True)
async def _command(ctx):
    await bot.send_message(ctx.message.channel,
        embed=discord.Embed(
            title="명령어", color=COLOR_INFO,
            description=", ".join(COMMANDS)))

@bot.command(name="캐릭터", pass_context=True)
async def _character(ctx, character_name:str):
    msg = await bot.send_message(ctx.message.channel,
        embed=discord.Embed(
            title="불러오는 중", color=COLOR_WAIT,
            description="캐릭터 정보를 불러오는 중입니다."))

    region = DEFAULT_REGION
    name, realm = utils.parse_character_name(character_name)
    realm = realm if realm else DEFAULT_REALM
    if not realm in REALMS:
        msg = await bot.edit_message(msg,
            embed=discord.Embed(
                title="실행 오류", color=COLOR_ERROR,
                description="존재하지 않는 서버 이름입니다."))
        return

    async def run():
        return await asyncio.gather(
            RaiderIO.get_character_info(region=region, realm=realm, name=name),
            Blizzard.get_character_info(realm=realm, name=name))
    res = await run()
    
    if None in res:
        msg = await bot.edit_message(msg,
            embed=discord.Embed(
                title="실행 오류", color=COLOR_ERROR,
                description="플레이어를 찾을 수 없습니다."))
        return

    embed = discord.Embed(
        title=name, color=COLOR_INFO,
        description="<{}>".format(res[1]["guild"]["name"]))
    embed.set_thumbnail(url="{}/{}".format(
        Blizzard.THUBNAIL_BASE, res[1]["thumbnail"]))
    embed.add_field(
        name="종족 및 직업",
        value="{} {}".format(RACES[res[1]["race"]], CLASSES[res[1]["class"]]))
    embed.add_field(
        name="아이템 레벨",
        value="최대 {}lv, 착용 {}lv".format(
            res[1]["items"]["averageItemLevel"],
            res[1]["items"]["averageItemLevelEquipped"]))
    embed.add_field(
        name="아제로스의 심장 레벨",
        value="{} (아이템 레벨 {}lv)".format(
            res[1]["items"]["neck"]["azeriteItem"]["azeriteLevel"],
            res[1]["items"]["neck"]["itemLevel"]))
    embed.add_field(
        name="착용중인 장신구",
        value="{}lv {}{}, {}lv {}{}".format(
            res[1]["items"]["trinket1"]["itemLevel"],
            "보홈 " if "gem0" in res[1]["items"]["trinket1"]["tooltipParams"] else "",
            res[1]["items"]["trinket1"]["name"],
            res[1]["items"]["trinket2"]["itemLevel"],
            "보홈 " if "gem0" in res[1]["items"]["trinket2"]["tooltipParams"] else "",
            res[1]["items"]["trinket2"]["name"]))
    embed.add_field(
        name="2차 스탯",
        value="치명타 {:.2f}%, 가속 {:.2f}%, 특화 {:.2f}%, 유연성 {:.2f}%".format(
            res[1]["stats"]["crit"],
            res[1]["stats"]["haste"],
            res[1]["stats"]["mastery"],
            res[1]["stats"]["versatilityDamageDoneBonus"]))
    embed.add_field(
        name="레이더 점수",
        value="현재 시즌 {}점".format(res[0]["mythic_plus_scores"]["all"]))
    embed.add_field(
        name="이번주 쐐기던전 최고기록",
        value="기록 없음" if len(res[0]["mythic_plus_weekly_highest_level_runs"]) == 0 \
            else "{} {}단 {}".format(
                DUNGEONS[res[0]["mythic_plus_weekly_highest_level_runs"][0]["dungeon"]],
                res[0]["mythic_plus_weekly_highest_level_runs"][0]["mythic_level"],
                MYTHIC_PLUS_RESULTS[res[0]["mythic_plus_weekly_highest_level_runs"][0]["num_keystone_upgrades"]]))
    embed.add_field(
        name="다자알로 전투 진행도",
        value="일반 {}/9, 영웅 {}/9, 신화 {}/9".format(
            res[0]["raid_progression"]["battle-of-dazaralor"]["normal_bosses_killed"],
            res[0]["raid_progression"]["battle-of-dazaralor"]["heroic_bosses_killed"],
            res[0]["raid_progression"]["battle-of-dazaralor"]["mythic_bosses_killed"]))
    
    spells = list()
    for part in ["head", "shoulder", "chest"]:
        powers = res[1]["items"][part]["azeriteEmpoweredItem"]["azeritePowers"]
        for power in powers:
            if power["tier"] == 3 or power["tier"] == 4:
                if power["spellId"] > 0:
                    spells.append(power["spellId"])

    async def get_spells(ids):
        tasks = list()
        for i in ids:
            tasks.append(Blizzard.get_spell_info(i))
        return await asyncio.gather(*tasks)
    spells = await get_spells(spells)
    spells = [spell["name"] for spell in spells]
    
    spells_summary = list()
    for spell in spells:
        spells_summary.append('{} x {}'.format(spells.count(spell), spell))
    spells_summary = list(set(spells_summary))
    embed.add_field(
        name="아제라이트 특성",
        value=", ".join(spells_summary))

    msg = await bot.edit_message(msg, embed=embed)

@bot.command(name="경매장", pass_context=True)
async def _auction(ctx):
    msg = await bot.send_message(ctx.message.channel,
        embed=discord.Embed(
            title="개발중", color=COLOR_INFO,
            description="아직 명령어가 추가되지 않았습니다."))
    return

    msg = await bot.send_message(ctx.message.channel,
        embed=discord.Embed(
            title="불러오는 중", color=COLOR_WAIT,
            description="경매장 정보를 불러오는 중입니다."))

    res = await Blizzard.get_auction_address(realm=DEFAULT_REALM)
    if not res:
        msg = await bot.edit_message(msg,
            embed=discord.Embed(
                title="실행 오류", color=COLOR_ERROR,
                description="경매장 서버에서 응답이 없습니다."))
        return

    auction = await Blizzard.get_data_from_url(res["files"][0]["url"])
    if not auction:
        msg = await bot.edit_message(msg,
            embed=discord.Embed(
                title="실행 오류", color=COLOR_ERROR,
                description="경매장 정보를 불러오는 데 실패했습니다."))
        return

    # TODO

@bot.command(name="어픽스", pass_context=True)
async def _affixes(ctx):
    msg = await bot.send_message(ctx.message.channel,
        embed=discord.Embed(
            title="불러오는 중", color=COLOR_WAIT,
            description="이번주 쐐기던전 어픽스 정보를 불러오는 중입니다."))

    res = await RaiderIO.get_weekly_affixes_info(
        region=DEFAULT_REGION, locale=DEFAULT_LANGUAGE)
    if not res:
        msg = await bot.edit_message(msg,
            embed=discord.Embed(
                title="실행 오류", color=COLOR_ERROR,
                description="쐐기던전 어픽스 정보를 불러오는 데 실패했습니다."))
        return

    embed = discord.Embed(title="이번주 쐐기던전 어픽스", color=COLOR_INFO, description="")
    for affix in res["affix_details"]:
        embed.add_field(name=affix["name"], value=affix["description"])
    msg = await bot.edit_message(msg, embed=embed)

@bot.command(name="주차", pass_context=True)
async def _weekly_mythic_plus(ctx):
    msg = await bot.send_message(ctx.message.channel,
        embed=discord.Embed(
            title="불러오는 중", color=COLOR_WAIT,
            description="길드원 목록을 불러오는 중입니다."))

    res = await Blizzard.get_guild_members(realm=DEFAULT_REALM, name=DEFAULT_GUILD)
    if not res:
        msg = await bot.edit_message(msg,
            embed=discord.Embed(
                title="실행 오류", color=COLOR_ERROR,
                description="길드원 목록을 불러오는 데 실패했습니다."))
        return

    members = list()
    for member in res["members"]:
        if member["character"]["level"] == MAX_CHARACTER_LEVEL:
            members.append(member["character"]["name"])
    if len(members) == 0:
        msg = await bot.edit_message(msg,
            embed=discord.Embed(
                title="실행 오류", color=COLOR_ERROR,
                description="길드원 중 {}레벨 캐릭터가 없습니다.".format(MAX_CHARACTER_LEVEL)))
        return

    async def run(names):
        tasks = list()
        for i in names:
            tasks.append(RaiderIO.get_character_info(DEFAULT_REGION, DEFAULT_REALM, i))
        return await asyncio.gather(*tasks)
    members = await run(members)
    remained = list()
    for member in members:
        if member is None:
            continue
        if member["gear"]["item_level_equipped"] > MYTHIC_PLUS_MIN_ITEM_LEVEL:
            runs = member["mythic_plus_weekly_highest_level_runs"]
            if len(runs) == 0 or runs[0]["mythic_level"] < 10:
                remained.append(member["name"])

    embed = discord.Embed(
        title="주차 안한 길드원 목록", color=COLOR_INFO,
        description=", ".join(remained) if len(remained) > 0 else "모든 길드원이 이번주에 주차를 완료하였습니다.")
    embed.set_footer(text="아이템 레벨 {} 이상 캐릭터만 표시됩니다.".format(MYTHIC_PLUS_MIN_ITEM_LEVEL))
    msg = await bot.edit_message(msg, embed=embed)

@bot.command(name="로그", pass_context=True)
async def _raid_logs(ctx):
    msg = await bot.send_message(ctx.message.channel,
        embed=discord.Embed(
            title="불러오는 중", color=COLOR_WAIT,
            description="로그 정보를 불러오는 중입니다."))

    res = await Warcraftlogs.get_reports(
        region=DEFAULT_REGION, realm=DEFAULT_REALM, guild_name=DEFAULT_GUILD)
    if not res:
        msg = await bot.edit_message(msg,
            embed=discord.Embed(
                title="실행 오류", color=COLOR_ERROR,
                description="로그 정보를 불러오는 데 실패했습니다."))
        return

    if len(res) < 1:
        msg = await bot.edit_message(msg,
        embed=discord.Embed(
            title="실행 오류", color=COLOR_ERROR,
            description="길드 레이드 로그 기록이 없습니다."))
        return

    embed = discord.Embed(
        title="길드 레이드 로그", color=COLOR_INFO,
        description="<{}>".format(DEFAULT_GUILD))
    embed.set_footer(text="가장 최근의 세 개 기록만 표시됩니다.")
    for report in res[:3]:
        date = datetime.fromtimestamp(int(report["start"]/1000))
        embed.add_field(
            name="{}년 {}월 {}일 - {}".format(date.year, date.month, date.day, report["title"]),
            value="https://www.warcraftlogs.com/reports/{}".format(report["id"]))
    msg = await bot.edit_message(msg, embed=embed)

@bot.command(name="특성", pass_context=True)
async def _talents(ctx, character_name:str):
    msg = await bot.send_message(ctx.message.channel,
        embed=discord.Embed(
            title="불러오는 중", color=COLOR_WAIT,
            description="특성 정보를 불러오는 중입니다."))

    name, realm = utils.parse_character_name(character_name)
    realm = realm if realm else DEFAULT_REALM
    if not realm in REALMS:
        msg = await bot.edit_message(msg,
            embed=discord.Embed(
                title="실행 오류", color=COLOR_ERROR,
                description="존재하지 않는 서버 이름입니다."))
        return

    res = await Blizzard.get_character_info(realm=realm, name=name)
    if not res:
        msg = await bot.edit_message(msg,
            embed=discord.Embed(
                title="실행 오류", color=COLOR_ERROR,
                description="특성 정보를 불러오는 데 실패했습니다."))
        return

    embed = discord.Embed(
        title="{}-{}의 특성 정보".format(name, realm),
        color=COLOR_INFO, description="")
    for talent in res["talents"]:
        if "spec" in talent and len(talent["talents"]) > 0:
            talents = list()
            for i in range(len(talent["talents"])):
                selected = False
                for t in talent["talents"]:
                    if t["tier"] == i:
                        selected = True
                        talents.append("({}) {}".format(t["column"]+1, t["spell"]["name"]))
                        break
                if not selected:
                    talents.append("\n")
            embed.add_field(
                name=talent["spec"]["name"],
                value="\n".join(talents))
    msg = await bot.edit_message(msg, embed=embed)

@bot.command(name="아제특성", pass_context=True)
async def _azerite_traits(ctx, class_name:str):
    msg = await bot.send_message(ctx.message.channel,
        embed=discord.Embed(
            title="불러오는 중", color=COLOR_WAIT,
            description="로그 정보를 불러오는 중입니다."))

    kr_class_name = ""
    for spec in CLASS_ABBREVIATIONS:
        if class_name in CLASS_ABBREVIATIONS[spec]:
            kr_class_name = spec
            break
    if kr_class_name == "":
        msg = await bot.edit_message(msg,
            embed=discord.Embed(
                title="실행 오류", color=COLOR_ERROR,
                description="알 수 없는 직업 이름입니다."))
        return

    res = await Warcraftlogs.get_rankings(
        region=DEFAULT_REGION,
        class_name=kr_class_name,
        difficulty=RAID_DIFFICULTIES["heroic"],
        encounter=2266)
    if not res:
        msg = await bot.edit_message(msg,
            embed=discord.Embed(
                title="실행 오류", color=COLOR_ERROR,
                description="로그 정보를 불러오는 데 실패했습니다."))
        return

    azerite = dict()
    used_once = dict()
    for r in res["rankings"]:
        if "azeritePowers" in r:
            powers = []
            decounted = False
            for power in r["azeritePowers"]:
                if power["ring"] >= 3:
                    if not power["id"] in powers:
                        powers.append(power["id"])
                        if power["id"] in azerite:
                            azerite[power["id"]] += 1.0
                            used_once[power["id"]] += 1
                        else:
                            azerite[power["id"]] = 1.0
                            used_once[power["id"]] = 1
                    else:
                        azerite[power["id"]] += 0.3
                        if not decounted:
                            used_once[power["id"]] -= 1
                            decounted = True
    azerite = sorted(azerite.items(), key=lambda x:x[1], reverse=True)
    msg_info = list()

    traits = list()
    for idx, a in enumerate(azerite[:7]):
        traits.append(a[0])
    async def get_spells(ids):
        tasks = list()
        for i in ids:
            tasks.append(Blizzard.get_spell_info(i))
        return await asyncio.gather(*tasks)
    spells = await get_spells(traits)
    spells = [spell["name"] for spell in spells]
    if None in spells:
        msg = await bot.edit_message(msg,
            embed=discord.Embed(
                title="실행 오류", color=COLOR_ERROR,
                description="아제라이트 특성 정보를 불러오는 데 실패했습니다."))
        return

    for i in range(7):
        msg_info.append({"index": i+1, "name": spells[i],
                         "score": round(azerite[i][1], 1),
                         "unique": used_once[azerite[i][0]]})
    embed = discord.Embed(
        title="{}의 추천 아제라이트 특성".format(kr_class_name), color=COLOR_INFO,
        description="\n".join(["{}. **{}** ({}점){}".format( \
            t["index"], t["name"], t["score"], \
            "" if t["name"] == "미덥지 못한 서약" else \
            " - 한 개만 필수로 착용" if t["score"] > 70 and t["score"] - t["unique"] < 15 else \
            " - 높은 우선순위로 최대 세 개 착용" if t["score"] > 110 else \
            " - 세 개 모두 있을 때만 착용" if t["score"] > 60 and t["unique"] < 15 else "") \
            for t in msg_info]))
    embed.set_thumbnail(url=CLASS_ICONS[kr_class_name])
    if CLASS_SPECS[kr_class_name] in CLASS_TANKS:
        embed.set_footer(text="방어 전담 직업군은 단일 네임드 딜량을 기준으로 집계됩니다.")
    elif CLASS_SPECS[kr_class_name] in CLASS_HEALS:
        embed.set_footer(text="치유 전담 직업군은 밀집 진형 레이드 힐량을 기준으로 집계됩니다.")
    else:
        embed.set_footer(text="공격 전담 직업군은 단일 네임드 딜량을 기준으로 집계됩니다.")
    msg = await bot.edit_message(msg, embed=embed)

@bot.command(name="장신구", pass_context=True)
async def _trinkets(ctx, class_name:str):
    msg = await bot.send_message(ctx.message.channel,
        embed=discord.Embed(
            title="불러오는 중", color=COLOR_WAIT,
            description="로그 정보를 불러오는 중입니다."))

    kr_class_name = ""
    for spec in CLASS_ABBREVIATIONS:
        if class_name in CLASS_ABBREVIATIONS[spec]:
            kr_class_name = spec
            break
    if kr_class_name == "":
        msg = await bot.edit_message(msg,
            embed=discord.Embed(
                title="실행 오류", color=COLOR_ERROR,
                description="알 수 없는 직업 이름입니다."))
        return

    res = await Warcraftlogs.get_rankings(
        region=DEFAULT_REGION,
        class_name=kr_class_name,
        difficulty=RAID_DIFFICULTIES["heroic"],
        encounter=2266)
    if not res:
        msg = await bot.edit_message(msg,
            embed=discord.Embed(
                title="실행 오류", color=COLOR_ERROR,
                description="로그 정보를 불러오는 데 실패했습니다."))
        return

    samples = list()
    trinkets = dict()
    for character in res["rankings"]:
        if character["regionName"] == "KR":
            if character["serverName"] == "":
                continue
            samples.append((character["serverName"].replace(" ", ""), character["name"]))

    async def run(characters):
        tasks = list()
        for realm, name in characters:
            tasks.append(Blizzard.get_character_info(realm, name))
        return await asyncio.gather(*tasks)
    samples = await run(samples)
    samples_count = 0


    for sample in samples:
        if not sample:
            continue
        if not sample["items"]["trinket1"]["name"] in trinkets:
            trinkets[sample["items"]["trinket1"]["name"]] = 0
        trinkets[sample["items"]["trinket1"]["name"]] += 1
        if not sample["items"]["trinket2"]["name"] in trinkets:
            trinkets[sample["items"]["trinket2"]["name"]] = 0
        trinkets[sample["items"]["trinket2"]["name"]] += 1
        samples_count += 1

    if samples_count < 10:
        msg = await bot.edit_message(msg,
            embed=discord.Embed(
                title="실행 오류", color=COLOR_ERROR,
                description="블리자드 API로부터 정보를 불러오는 데 실패했습니다."
        ))
        return
    trinkets = sorted(trinkets.items(), key=lambda x:x[1], reverse=True)

    recommended_trinkets = list()
    for idx, trinket in enumerate(trinkets[:5]):
        recommended_trinkets.append("{}. {} ({}%)".format(
            idx+1, trinket[0], round(trinket[1]/samples_count*100, 1)))

    embed = discord.Embed(
        title="{}의 추천 장신구".format(kr_class_name), color=COLOR_INFO,
        description="\n".join(recommended_trinkets))
    embed.set_thumbnail(url=CLASS_ICONS[kr_class_name])
    if CLASS_SPECS[kr_class_name] in CLASS_TANKS:
        embed.set_footer(text="방어 전담 직업군은 단일 네임드 딜량을 기준으로 집계됩니다.")
    elif CLASS_SPECS[kr_class_name] in CLASS_HEALS:
        embed.set_footer(text="치유 전담 직업군은 밀집 진형 레이드 힐량을 기준으로 집계됩니다.")
    else:
        embed.set_footer(text="공격 전담 직업군은 단일 네임드 딜량을 기준으로 집계됩니다.")
    msg = await bot.edit_message(msg, embed=embed)

@bot.command(name="스탯", pass_context=True)
async def _secondary_stats(ctx, class_name:str):
    msg = await bot.send_message(ctx.message.channel,
        embed=discord.Embed(
            title="불러오는 중", color=COLOR_WAIT,
            description="로그 정보를 불러오는 중입니다."))

    kr_class_name = ""
    for spec in CLASS_ABBREVIATIONS:
        if class_name in CLASS_ABBREVIATIONS[spec]:
            kr_class_name = spec
            break
    if kr_class_name == "":
        msg = await bot.edit_message(msg,
            embed=discord.Embed(
                title="실행 오류", color=COLOR_ERROR,
                description="알 수 없는 직업 이름입니다."))
        return

    res = await Warcraftlogs.get_rankings(
        region=DEFAULT_REGION,
        class_name=kr_class_name,
        difficulty=RAID_DIFFICULTIES["heroic"],
        encounter=2266)
    if not res:
        msg = await bot.edit_message(msg,
            embed=discord.Embed(
                title="실행 오류", color=COLOR_ERROR,
                description="로그 정보를 불러오는 데 실패했습니다."))
        return

    samples = list()
    stats = {"치명": 0, "가속": 0, "특화": 0, "유연": 0}
    for character in res["rankings"]:
        if character["regionName"] == "KR":
            if character["serverName"] == "":
                continue
            samples.append((character["serverName"].replace(" ", ""), character["name"]))

    async def run(characters):
        tasks = list()
        for realm, name in characters:
            tasks.append(Blizzard.get_character_info(realm, name))
        return await asyncio.gather(*tasks)
    samples = await run(samples)
    samples_count = 0
    for sample in samples:
        if not sample:
            continue
        samples_count += 1
        stats["치명"] += sample["stats"]["critRating"]
        stats["가속"] += sample["stats"]["hasteRating"]
        stats["특화"] += sample["stats"]["masteryRating"]
        stats["유연"] += sample["stats"]["versatility"]

    if samples_count < 10:
        msg = await bot.edit_message(msg,
            embed=discord.Embed(
                title="실행 오류", color=COLOR_ERROR,
                description="블리자드 API로부터 정보를 불러오는 데 실패했습니다."
        ))
        return
    stats = sorted(stats.items(), key=lambda x:x[1], reverse=True)
    recent_value = 0
    stats_priority = ""
    for stat in stats:
        stat_value = stat[1] / samples_count
        if recent_value == 0:
            stats_priority += stat[0]
        elif recent_value - stat_value < 50:
            stats_priority += " = {}".format(stat[0])
        elif recent_value - stat_value < 300:
            stats_priority += " > {}".format(stat[0])
        else:
            stats_priority += " >> {}".format(stat[0])
        recent_value = stat_value

    embed = discord.Embed(
        title="{}의 스탯 우선순위".format(kr_class_name), color=COLOR_INFO,
        description=stats_priority)
    embed.set_thumbnail(url=CLASS_ICONS[kr_class_name])
    if CLASS_SPECS[kr_class_name] in CLASS_TANKS:
        embed.set_footer(text="방어 전담 직업군은 단일 네임드 딜량을 기준으로 집계됩니다.")
    elif CLASS_SPECS[kr_class_name] in CLASS_HEALS:
        embed.set_footer(text="치유 전담 직업군은 밀집 진형 레이드 힐량을 기준으로 집계됩니다.")
    else:
        embed.set_footer(text="공격 전담 직업군은 단일 네임드 딜량을 기준으로 집계됩니다.")
    msg = await bot.edit_message(msg, embed=embed)


if __name__ == "__main__":
    keys = utils.get_keys()
    bot.run(keys["discord"]["main"])
