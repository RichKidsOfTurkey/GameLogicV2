import json
import random
import plotly.express as px
import matplotlib.pyplot as plt
import collections
from player.player import Player
from itertools import islice
from gameplay_analysis.analysis import Analysis
from tournament.tournament import Tournament

# 50% common        1535 players
# 30% uncommon      922  players
# 15% rare          461  players
# 05% legendary     154  players
teammm = [
        {
            "name": "Bessie",
            "score_quality": {
                "power_index": 1,
                "rarity": "common"
            },
            "rebound_quality": {
                "power_index": 1,
                "rarity": "common"
            },
            "block_quality": {
                "power_index": 2,
                "rarity": "uncommon"
            },
            "steal_quality": {
                "power_index": 1,
                "rarity": "common"
            },
            "assist_quality": {
                "power_index": 1,
                "rarity": "common"
            },
            "average_quality": [
                "common",
                1.2
            ],
            "player_index": 47204
        },
        {
            "name": "Joseph",
            "score_quality": {
                "power_index": 4,
                "rarity": "legendary"
            },
            "rebound_quality": {
                "power_index": 1,
                "rarity": "common"
            },
            "block_quality": {
                "power_index": 3,
                "rarity": "rare"
            },
            "steal_quality": {
                "power_index": 3,
                "rarity": "rare"
            },
            "assist_quality": {
                "power_index": 2,
                "rarity": "uncommon"
            },
            "average_quality": [
                "rare",
                2.6
            ],
            "player_index": 255164
        },
        {
            "name": "Elijah",
            "score_quality": {
                "power_index": 2,
                "rarity": "uncommon"
            },
            "rebound_quality": {
                "power_index": 1,
                "rarity": "common"
            },
            "block_quality": {
                "power_index": 1,
                "rarity": "common"
            },
            "steal_quality": {
                "power_index": 2,
                "rarity": "uncommon"
            },
            "assist_quality": {
                "power_index": 2,
                "rarity": "uncommon"
            },
            "average_quality": [
                "uncommon",
                1.6
            ],
            "player_index": 199921
        }
    ]
common_team = [
        {
            "name": "yaryar",
            "score_quality": {
                "power_index": 1,
                "rarity": "common"
            },
            "rebound_quality": {
                "power_index": 1,
                "rarity": "common"
            },
            "block_quality": {
                "power_index": 2,
                "rarity": "uncommon"
            },
            "steal_quality": {
                "power_index": 1,
                "rarity": "common"
            },
            "assist_quality": {
                "power_index": 1,
                "rarity": "common"
            },
            "average_quality": [
                "common",
                1.2
            ],
            "player_index": 47204
        },
        {
            "name": "Bessie",
            "score_quality": {
                "power_index": 1,
                "rarity": "common"
            },
            "rebound_quality": {
                "power_index": 1,
                "rarity": "common"
            },
            "block_quality": {
                "power_index": 2,
                "rarity": "uncommon"
            },
            "steal_quality": {
                "power_index": 1,
                "rarity": "common"
            },
            "assist_quality": {
                "power_index": 1,
                "rarity": "common"
            },
            "average_quality": [
                "common",
                1.2
            ],
            "player_index": 47204
        },
        {
            "name": "anan",
            "score_quality": {
                "power_index": 1,
                "rarity": "common"
            },
            "rebound_quality": {
                "power_index": 1,
                "rarity": "common"
            },
            "block_quality": {
                "power_index": 2,
                "rarity": "uncommon"
            },
            "steal_quality": {
                "power_index": 1,
                "rarity": "common"
            },
            "assist_quality": {
                "power_index": 1,
                "rarity": "common"
            },
            "average_quality": [
                "common",
                1.2
            ],
            "player_index": 47204
        }
    ]
rare_team = [
        {
            "name": "Meme",
            "score_quality": {
                "power_index": 4,
                "rarity": "legendary"
            },
            "rebound_quality": {
                "power_index": 1,
                "rarity": "common"
            },
            "block_quality": {
                "power_index": 3,
                "rarity": "rare"
            },
            "steal_quality": {
                "power_index": 3,
                "rarity": "rare"
            },
            "assist_quality": {
                "power_index": 2,
                "rarity": "uncommon"
            },
            "average_quality": [
                "rare",
                2.6
            ],
            "player_index": 255164
        },
        {
            "name": "Amcik",
            "score_quality": {
                "power_index": 4,
                "rarity": "legendary"
            },
            "rebound_quality": {
                "power_index": 1,
                "rarity": "common"
            },
            "block_quality": {
                "power_index": 3,
                "rarity": "rare"
            },
            "steal_quality": {
                "power_index": 3,
                "rarity": "rare"
            },
            "assist_quality": {
                "power_index": 2,
                "rarity": "uncommon"
            },
            "average_quality": [
                "rare",
                2.6
            ],
            "player_index": 255164
        },
        {
            "name": "Tassak",
            "score_quality": {
                "power_index": 4,
                "rarity": "legendary"
            },
            "rebound_quality": {
                "power_index": 1,
                "rarity": "common"
            },
            "block_quality": {
                "power_index": 3,
                "rarity": "rare"
            },
            "steal_quality": {
                "power_index": 3,
                "rarity": "rare"
            },
            "assist_quality": {
                "power_index": 2,
                "rarity": "uncommon"
            },
            "average_quality": [
                "rare",
                2.6
            ],
            "player_index": 255164
        }
    ]
lego_team = [
    {
        "name": "S2mle100Lesh",
        "score_quality": {
            "power_index": 4,
            "rarity": "legendary"
        },
        "rebound_quality": {
            "power_index": 4,
            "rarity": "legendary"
        },
        "block_quality": {
            "power_index": 4,
            "rarity": "legendary"
        },
        "steal_quality": {
            "power_index": 4,
            "rarity": "legendary"
        },
        "assist_quality": {
            "power_index": 4,
            "rarity": "legendary"
        },
        "average_quality": [
            "legendary",
            3.6
        ],
        "player_index": 305939
    },
    {
        "name": "LeroyJenkins",
        "score_quality": {
            "power_index": 4,
            "rarity": "legendary"
        },
        "rebound_quality": {
            "power_index": 4,
            "rarity": "legendary"
        },
        "block_quality": {
            "power_index": 4,
            "rarity": "legendary"
        },
        "steal_quality": {
            "power_index": 4,
            "rarity": "legendary"
        },
        "assist_quality": {
            "power_index": 2,
            "rarity": "uncommon"
        },
        "average_quality": [
            "legendary",
            3.6
        ],
        "player_index": 305939
    },
    {
        "name": "BigDickLanm",
        "score_quality": {
            "power_index": 4,
            "rarity": "legendary"
        },
        "rebound_quality": {
            "power_index": 4,
            "rarity": "legendary"
        },
        "block_quality": {
            "power_index": 4,
            "rarity": "legendary"
        },
        "steal_quality": {
            "power_index": 4,
            "rarity": "legendary"
        },
        "assist_quality": {
            "power_index": 2,
            "rarity": "uncommon"
        },
        "average_quality": [
            "legendary",
            3.6
        ],
        "player_index": 305939
    }
]

def group_elements(lst, chunk_size):
    lst = iter(lst)
    return iter(lambda: tuple(islice(lst, chunk_size)), ())




def set_matches():
    pass


lego_player = {
        "name": "S2mle100Lesh",
        "score_quality": {
            "power_index": 3,
            "rarity": "rare"
        },
        "rebound_quality": {
            "power_index": 3,
            "rarity": "rare"
        },
        "block_quality": {
            "power_index": 3,
            "rarity": "rare"
        },
        "steal_quality": {
            "power_index": 3,
            "rarity": "rare"
        },
        "assist_quality": {
            "power_index": 3,
            "rarity": "rare"
        },
        "average_quality": [
            "legendary",
            3.6
        ],
        "player_index": 305939
    }

# temp = Analysis.match_mood_grapher(rare_team, lego_team)
Analysis.player_mood_grapher(lego_player, 100)



