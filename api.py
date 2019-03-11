import asyncio
import aiohttp
from urllib import parse
from datetime import datetime, timedelta

import utils
from params import *


def encode(base, url):
    parsed = parse.urlparse(url)
    parsed = parse.parse_qs(parsed.query)
    encoded = "{}?{}".format(base, parse.urlencode(parsed, doseq=True))
    return encoded

class RaiderIO:
    BASE = "https://raider.io/api/v1"

    @classmethod
    async def get_character_info(cls, region, realm, name):
        query = "?region={}".format(region) \
                + "&realm={}".format(REALMS[realm]) \
                + "&name={}".format(name) \
                + "&fields=gear,raid_progression,mythic_plus_scores,mythic_plus_weekly_highest_level_runs"
        url = encode("{}/characters/profile".format(cls.BASE), query)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return None

    @classmethod
    async def get_weekly_affixes_info(cls, region, locale):
        query = "?region={}".format(region) \
                + "&locale={}".format(locale)
        url = encode("{}/mythic-plus/affixes".format(cls.BASE), query)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return None


class Blizzard:
    BASE = "https://kr.api.blizzard.com"
    OAUTH_BASE = "https://kr.battle.net/oauth/token"
    THUBNAIL_BASE = "https://render-kr.worldofwarcraft.com/character"
    ACCESS_TOKEN = ""
    last_updated = None

    @classmethod
    async def change_access_token(cls):
        if cls.last_updated:
            if datetime.now() - cls.last_updated < timedelta(0, 60, 0):
                return True
        query = "?grant_type=client_credentials" \
                + "&client_id={}".format(utils.get_keys()["blizzard"]["id"]) \
                + "&client_secret={}".format(utils.get_keys()["blizzard"]["secret"])
        url = encode(cls.OAUTH_BASE, query)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    token = await response.json()
                    cls.ACCESS_TOKEN = token["access_token"]
                    cls.last_updated = datetime.now()
                    return True
                else:
                    return False

    @classmethod
    async def get_data_from_url(cls, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return None

    @classmethod
    async def get_character_info(cls, realm, name):
        if not await cls.change_access_token():
            return None
        query = "?access_token={}".format(cls.ACCESS_TOKEN) \
                + "&fields=items,stats,talents,guild"
        url = encode("{}/wow/character/{}/{}".format(cls.BASE, REALMS[realm], name), query)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return None

    @classmethod
    async def get_guild_members(cls, realm, name):
        if not await cls.change_access_token():
            return None
        query = "?access_token={}".format(cls.ACCESS_TOKEN) \
                + "&fields=members"
        url = encode("{}/wow/guild/{}/{}".format(cls.BASE, REALMS[realm], name), query)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return None

    @classmethod
    async def get_auction_address(cls, realm):
        if not await cls.change_access_token():
            return None
        query = "?access_token={}".format(cls.ACCESS_TOKEN)
        url = encode("{}/wow/auction/data/{}".format(cls.BASE, REALMS[realm]), query)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return None

    @classmethod
    async def get_token_price(cls):
        if not await cls.change_access_token():
            return None
        query = "?access_token={}".format(cls.ACCESS_TOKEN) \
                + "&namespace=dynamic-kr&locale=ko_KR"
        url = encode("{}/data/wow/token/index".format(cls.BASE), query)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return None

    @classmethod
    async def get_spell_info(cls, spell_id):
        if not await cls.change_access_token():
            return None
        query = "?access_token={}".format(cls.ACCESS_TOKEN)
        url = encode("{}/wow/spell/{}".format(cls.BASE, spell_id), query)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return None


class Warcraftlogs:
    BASE = "https://www.warcraftlogs.com/v1"

    @classmethod
    async def get_rankings(cls, region, class_name, difficulty, encounter):
        class_id, spec_id = WCL_CLASS_IDS[class_name]
        metric = "hps" if CLASS_SPECS[class_name] in CLASS_HEALS else "dps"
        query = "?api_key={}".format(utils.get_keys()["warcraftlogs"]["token"]) \
                + "&region={}".format(region) \
                + "&class={}".format(class_id) \
                + "&spec={}".format(spec_id) \
                + "&difficulty={}".format(difficulty) \
                + "&metric={}".format(metric)
        url = encode("{}/rankings/encounter/{}".format(cls.BASE, encounter), query)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return None

    @classmethod
    async def get_reports(cls, region, realm, guild_name):
        query = "?api_key={}".format(utils.get_keys()["warcraftlogs"]["token"])
        url = encode("{}/reports/guild/{}/{}/{}".format(
            cls.BASE, guild_name, realm, region), query)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return None
