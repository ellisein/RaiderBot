# Commands

COMMANDS = [
    "!명령어",
    "!캐릭터",
    "!경매장",
    "!어픽스",
    "!주차",
    "!로그",
    "!특성",
    "!아제특성",
    "!장신구",
    "!스탯",
]


# User-defined Constants

DEFAULT_REGION = "kr"
DEFAULT_REALM = "헬스크림"
DEFAULT_LANGUAGE = "ko"
DEFAULT_GUILD = "형님 보셨죠 이런게 바로 컨트롤이에요"
MYTHIC_PLUS_MIN_ITEM_LEVEL = 385
MAX_CHARACTER_LEVEL = 120


# Color

COLOR_ERROR = 0xFF7777
COLOR_INFO = 0x7777FF
COLOR_SUCCESS = 0x77FF77
COLOR_WAIT = 0xAAAAAA


# In-game Constants

RAID_DIFFICULTIES = {
    "lfr": 1,
    "flex": 2,
    "normal": 3,
    "heroic": 4,
    "mythic": 5,
}

MYTHIC_PLUS_RESULTS = {
    0: "소진",
    1: "시간내클리어+1", 
    2: "시간내클리어+2",
    3: "시간내클리어+3",
}

MYTHIC_PLUS_ROTATION = [
    ["경화", "피웅덩이", "괴저"],
    ["폭군", "파열", "변덕"],
    ["경화", "무리", "전율"],
    ["폭군", "분노", "괴저"],
    ["경화", "강화", "변덕"],
    ["폭군", "무리", "화산"],
    ["경화", "피웅덩이", "치명상"],
    ["폭군", "강화", "폭탄"],
    ["경화", "파열", "전율"],
    ["폭군", "분노", "화산"],
    ["경화", "무리", "폭탄"],
    ["폭군", "강화", "치명상"],
]

REALMS = {
    "아즈샤라": "Azshara",
    "듀로탄": "Durotan",
    "헬스크림": "Hellscream",
    "하이잘": "Hyjal",
    "알렉스트라자": "Alexstrasza",
    "데스윙": "Deathwing",
    "불타는군단": "Burning Legion",
    "스톰레이지": "Stormrage",
    "세나리우스": "Cenarius",
    "달라란": "Dalaran",
    "말퓨리온": "Malfurion",
    "노르간논": "Norgannon",
    "가로나": "Garona",
    "굴단": "Gul'dan",
    "줄진": "Zul'jin",
    "렉사르": "Rexxar",
    "와일드해머": "Wildhammer",
    "윈드러너": "Windrunner",
}

RAIDS = {
    "Uldir": "울디르",
    "Battle of Dazar'alor": "다자알로 전투",
}

ITEM_GROUPS = {
    "영약": [152641, 152640, 152639, 152638],
    "물약": [152557, 163223, 152561, 152559,
             163222, 163225, 152560, 163224],
    "요리": [154882, 154884, 154888, 166344,
             154886, 166804],
    "약초": [152505, 152508, 152510, 152511,
             152506, 152509, 152507],
    "광석": [152512, 152579, 152513],
}

ITEM_NAMES = {
    152641: "거스름너울의 영약",
    152640: "광대한 지평선의 영약",
    152639: "끝없는 심연의 영약",
    152638: "물결의 영약",
    152557: "강철피부 물약",
    163223: "민첩의 전투 물약",
    152561: "원기회복의 물약",
    152559: "일어나는 죽음의 물약",
    163222: "지능의 전투 물약",
    163225: "체력의 전투 물약",
    152560: "폭발하는 피의 물약",
    163224: "힘의 전투 물약",
    154882: "꿀 바른 뒷다리살",
    154884: "늪지 물고기와 튀김",
    154888: "선원의 파이",
    166344: "양념한 스테이크와 감자",
    154886: "양념한 집게발",
    166804: "보랄러스 선지 소시지",
    152505: "강봉오리",
    152508: "겨울의 입맞춤",
    152510: "닻풀",
    152511: "바다 줄기",
    152506: "별이끼",
    152509: "세이렌의 꽃가루",
    152507: "아쿤다의 이빨",
    152512: "모네라이트 광석",
    152579: "폭풍 은 광석",
    152513: "백금 광석",
}

DUNGEONS = {
    "Siege of Boralus": "보랄러스 공성전",
    "Waycrest Manor": "웨이크레스트 저택",
    "The Underrot": "썩은굴",
    "Tol Dagor": "톨 다고르",
    "Freehold": "자유지대",
    "The MOTHERLODE!!": "왕노다지 광산!!",
    "Shrine of the Storm": "폭풍의 사원",
    "Atal'dazar": "아탈다자르",
    "Kings' Rest": "왕들의 안식처",
    "Temple of Sethraliss": "세스랄리스 사원",
}

CLASSES = {
    1: "전사",
    2: "성기사",
    3: "사냥꾼",
    4: "도적",
    5: "사제",
    6: "죽음의기사",
    7: "주술사",
    8: "마법사",
    9: "흑마법사",
    10: "수도사",
    11: "드루이드",
    12: "악마사냥꾼",
}

RACES = {
    1: "인간",
    2: "오크",
    3: "드워프",
    4: "나이트엘프",
    5: "언데드",
    6: "타우렌",
    7: "노움",
    8: "트롤",
    9: "고블린",
    10: "블러드엘프",
    11: "드레나이",
    24: "판다렌",
    25: "판다렌",
    26: "판다렌",
    27: "나이트본",
    28: "높은산타우렌",
    29: "공허엘프",
    30: "빛벼림드레나이",
    31: "잔달라트롤",
    32: "쿨티란",
    34: "검은무쇠드워프",
    36: "마그하르오크",
}

PROFESSIONS = (
    "가죽세공",
    "기계공학",
    "보석세공",
    "대장기술",
    "마법부여",
    "약초채집",
    "연금술",
    "무두질",
    "주문각인",
    "채광",
    "재봉술",
)

EMISSARY_QUESTS = {
    "Zandalari Empire": "잔달라 제국",
    "Voldunai": "볼두나이",
    "Talanji's Expedition": "탈란지의 원정대",
    "Champions of Azeroth": "아제로스의 용사들",
    "Tortollan Seekers": "토르톨란 탐구단"
}

STATS = {
    0: "마나",
    1: "체력",
    3: "민첩성",
    4: "힘",
    5: "지능",
    32: "치명타 및 극대화",
    36: "가속",
    40: "유연성",
    49: "특화",
}

ENCONTERS = {
    2265: "빛의 용사",
    2266: "밀림의 군주 그롱",
    2263: "비취 불꽃의 대가",
    2271: "금은보화",
    2268: "선택받은 자의 비밀의회",
    2272: "왕 라스타칸",
    2276: "땜장이왕 멕카토크",
    2280: "폭풍장벽 봉쇄군",
    2281: "여군주 제이나 프라우드무어"
}

WCL_CLASS_IDS = {
    "혈기 죽음의기사": (1, 1),
    "냉기 죽음의기사": (1, 2),
    "부정 죽음의기사": (1, 3),
    "조화 드루이드": (2, 1),
    "야성 드루이드": (2, 2),
    "수호 드루이드": (2, 3),
    "회복 드루이드": (2, 4),
    "야수 사냥꾼": (3, 1),
    "사격 사냥꾼": (3, 2),
    "생존 사냥꾼": (3, 3),
    "비전 마법사": (4, 1),
    "화염 마법사": (4, 2),
    "냉기 마법사": (4, 3),
    "양조 수도사": (5, 1),
    "운무 수도사": (5, 2),
    "풍운 수도사": (5, 3),
    "신성 성기사": (6, 1),
    "보호 성기사": (6, 2),
    "징벌 성기사": (6, 3),
    "수양 사제": (7, 1),
    "신성 사제": (7, 2),
    "암흑 사제": (7, 3),
    "암살 도적": (8, 1),
    "잠행 도적": (8, 3),
    "무법 도적": (8, 4),
    "정기 주술사": (9, 1),
    "고양 주술사": (9, 2),
    "복원 주술사": (9, 3),
    "고통 흑마법사": (10, 1),
    "악마 흑마법사": (10, 2),
    "파괴 흑마법사": (10, 3),
    "무기 전사": (11, 1),
    "분노 전사": (11, 2),
    "방어 전사": (11, 3),
    "파멸 악마사냥꾼": (12, 1),
    "복수 악마사냥꾼": (12, 2),
}

CLASS_SPECS = {
    "혈기 죽음의기사": "death_knight_blood",
    "냉기 죽음의기사": "death_knight_frost",
    "부정 죽음의기사": "death_knight_unholy",
    "조화 드루이드": "druid_balance",
    "야성 드루이드": "druid_feral",
    "수호 드루이드": "druid_guardian",
    "회복 드루이드": "druid_restoration",
    "야수 사냥꾼": "hunter_beast_mastery",
    "사격 사냥꾼": "hunter_marksmanship",
    "생존 사냥꾼": "hunter_survival",
    "비전 마법사": "mage_arcane",
    "화염 마법사": "mage_fire",
    "냉기 마법사": "mage_frost",
    "양조 수도사": "monk_brewmaster",
    "운무 수도사": "monk_mistweaver",
    "풍운 수도사": "monk_windwalker",
    "신성 성기사": "paladin_holy",
    "보호 성기사": "paladin_protection",
    "징벌 성기사": "paladin_retribution",
    "수양 사제": "priest_discipline",
    "신성 사제": "priest_holy",
    "암흑 사제": "priest_shadow",
    "암살 도적": "rogue_assassination",
    "잠행 도적": "rogue_subtlety",
    "무법 도적": "rogue_outlaw",
    "정기 주술사": "shaman_elemental",
    "고양 주술사": "shaman_enhancement",
    "복원 주술사": "shaman_restoration",
    "고통 흑마법사": "warlock_affliction",
    "악마 흑마법사": "warlock_demonology",
    "파괴 흑마법사": "warlock_destruction",
    "무기 전사": "warrior_arms",
    "분노 전사": "warrior_fury",
    "방어 전사": "warrior_protection",
    "파멸 악마사냥꾼": "demon_hunter_havoc",
    "복수 악마사냥꾼": "demon_hunter_vengeance",
}

CLASS_ABBREVIATIONS = {
    "혈기 죽음의기사": ["혈죽", "죽탱"],
    "냉기 죽음의기사": ["냉죽"],
    "부정 죽음의기사": ["부죽"],
    "조화 드루이드": ["조드"],
    "야성 드루이드": ["야드", "얃"],
    "수호 드루이드": ["수드", "곰탱", "쑫"],
    "회복 드루이드": ["회드"],
    "야수 사냥꾼": ["야냥"],
    "사격 사냥꾼": ["격냥"],
    "생존 사냥꾼": ["생냥"],
    "비전 마법사": ["비법"],
    "화염 마법사": ["화법"],
    "냉기 마법사": ["냉법"],
    "양조 수도사": ["양조"],
    "운무 수도사": ["운무"],
    "풍운 수도사": ["풍운", "공옾"],
    "신성 성기사": ["신기"],
    "보호 성기사": ["보기"],
    "징벌 성기사": ["징기"],
    "수양 사제": ["수사"],
    "신성 사제": ["신사"],
    "암흑 사제": ["암사"],
    "암살 도적": ["암살"],
    "잠행 도적": ["잠행"],
    "무법 도적": ["무법"],
    "정기 주술사": ["정술"],
    "고양 주술사": ["고술"],
    "복원 주술사": ["복술"],
    "고통 흑마법사": ["고흑"],
    "악마 흑마법사": ["악흑"],
    "파괴 흑마법사": ["파흑"],
    "무기 전사": ["무전"],
    "분노 전사": ["분전"],
    "방어 전사": ["방전", "전탱"],
    "파멸 악마사냥꾼": ["악딜", "악사"],
    "복수 악마사냥꾼": ["악탱"],
}

CLASS_TANKS = [
    "death_knight_blood",
    "druid_guardian",
    "monk_brewmaster",
    "paladin_protection",
    "warrior_protection",
    "demon_hunter_vengeance",
]

CLASS_HEALS = [
    "druid_restoration",
    "monk_mistweaver",
    "paladin_holy",
    "priest_discipline",
    "priest_holy",
    "shaman_restoration",
]

CLASS_ICONS = {
    "혈기 죽음의기사": "https://wow.zamimg.com/images/wow/icons/large/spell_deathknight_bloodpresence.jpg",
    "냉기 죽음의기사": "https://wow.zamimg.com/images/wow/icons/large/spell_deathknight_frostpresence.jpg",
    "부정 죽음의기사": "https://wow.zamimg.com/images/wow/icons/large/spell_deathknight_unholypresence.jpg",
    "조화 드루이드": "https://wow.zamimg.com/images/wow/icons/large/spell_nature_starfall.jpg",
    "야성 드루이드": "https://wow.zamimg.com/images/wow/icons/large/ability_druid_catform.jpg",
    "수호 드루이드": "https://wow.zamimg.com/images/wow/icons/large/ability_racial_bearform.jpg",
    "회복 드루이드": "https://wow.zamimg.com/images/wow/icons/large/spell_nature_healingtouch.jpg",
    "야수 사냥꾼": "https://wow.zamimg.com/images/wow/icons/large/ability_hunter_bestialdiscipline.jpg",
    "사격 사냥꾼": "https://wow.zamimg.com/images/wow/icons/large/ability_hunter_focusedaim.jpg",
    "생존 사냥꾼": "https://wow.zamimg.com/images/wow/icons/large/ability_hunter_camouflage.jpg",
    "비전 마법사": "https://wow.zamimg.com/images/wow/icons/large/spell_holy_magicalsentry.jpg",
    "화염 마법사": "https://wow.zamimg.com/images/wow/icons/large/spell_fire_firebold02.jpg",
    "냉기 마법사": "https://wow.zamimg.com/images/wow/icons/large/spell_frost_frostbolt02.jpg",
    "양조 수도사": "https://wow.zamimg.com/images/wow/icons/large/monk_stance_drunkenox.jpg",
    "운무 수도사": "https://wow.zamimg.com/images/wow/icons/large/monk_stance_wiseserpent.jpg",
    "풍운 수도사": "https://wow.zamimg.com/images/wow/icons/large/monk_stance_whitetiger.jpg",
    "신성 성기사": "https://wow.zamimg.com/images/wow/icons/large/spell_holy_holybolt.jpg",
    "보호 성기사": "https://wow.zamimg.com/images/wow/icons/large/ability_paladin_shieldofthetemplar.jpg",
    "징벌 성기사": "https://wow.zamimg.com/images/wow/icons/large/spell_holy_auraoflight.jpg",
    "수양 사제": "https://wow.zamimg.com/images/wow/icons/large/spell_holy_powerwordshield.jpg",
    "신성 사제": "https://wow.zamimg.com/images/wow/icons/large/spell_holy_guardianspirit.jpg",
    "암흑 사제": "https://wow.zamimg.com/images/wow/icons/large/spell_shadow_shadowwordpain.jpg",
    "암살 도적": "https://wow.zamimg.com/images/wow/icons/large/ability_rogue_eviscerate.jpg",
    "잠행 도적": "https://wow.zamimg.com/images/wow/icons/large/ability_stealth.jpg",
    "무법 도적": "https://wow.zamimg.com/images/wow/icons/large/ability_backstab.jpg",
    "정기 주술사": "https://wow.zamimg.com/images/wow/icons/large/spell_nature_lightning.jpg",
    "고양 주술사": "https://wow.zamimg.com/images/wow/icons/large/spell_nature_lightningshield.jpg",
    "복원 주술사": "https://wow.zamimg.com/images/wow/icons/large/spell_nature_magicimmunity.jpg",
    "고통 흑마법사": "https://wow.zamimg.com/images/wow/icons/large/spell_shadow_deathcoil.jpg",
    "악마 흑마법사": "https://wow.zamimg.com/images/wow/icons/large/spell_shadow_metamorphosis.jpg",
    "파괴 흑마법사": "https://wow.zamimg.com/images/wow/icons/large/spell_shadow_rainoffire.jpg",
    "무기 전사": "https://wow.zamimg.com/images/wow/icons/large/ability_warrior_savageblow.jpg",
    "분노 전사": "https://wow.zamimg.com/images/wow/icons/large/ability_warrior_innerrage.jpg",
    "방어 전사": "https://wow.zamimg.com/images/wow/icons/large/ability_warrior_defensivestance.jpg",
    "파멸 악마사냥꾼": "https://wow.zamimg.com/images/wow/icons/large/ability_demonhunter_specdps.jpg",
    "복수 악마사냥꾼": "https://wow.zamimg.com/images/wow/icons/large/ability_demonhunter_spectank.jpg",
}
