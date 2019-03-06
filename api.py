import asyncio
import aiohttp

import utils
from params import *


class RaiderIO:
    BASE = "https://raider.io/api/v1/"

    @classmethod
    async def get_character_info(cls, region, realm, name):
        url = cls.BASE + "characters/profile" \
              + "?region={}".format(region) \
              + "&realm={}".format(REALMS[realm]) \
              + "&name={}".format(name) \
              + "&fields=mythic_plus_scores,mythic_plus_weekly_highest_level_runs"
        response = await aiohttp.request("GET", url)
        return response


class Blizzard:
    pass


class Warcraftlogs:
    pass


class Bloodmallet:
    pass
