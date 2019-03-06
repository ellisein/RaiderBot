import asyncio
import aiohttp
from urllib import parse

import utils
from params import *


def encode(base, url):
    parsed = parse.urlparse(url)
    parsed = parse.parse_qs(parsed.query)
    encoded = "{}?{}".format(base, parse.urlencode(parsed, doseq=True))
    return encoded

class RaiderIO:
    BASE = "https://raider.io/api/v1/"

    @classmethod
    async def get_character_info(cls, region, realm, name):
        query = "?region={}".format(region) \
                + "&realm={}".format(REALMS[realm]) \
                + "&name={}".format(name) \
                + "&fields=mythic_plus_scores,mythic_plus_weekly_highest_level_runs"
        url = encode(cls.BASE + "characters/profile", query)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return None


class Blizzard:
    pass


class Warcraftlogs:
    pass


class Bloodmallet:
    pass
