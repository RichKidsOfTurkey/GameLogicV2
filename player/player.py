import random


def percentage_chance():
    chance = random.randint(0, 100)
    return chance / 100


class Stats:

    def __init__(self):
        self.common_score = round(((random.randint(150, 855))/100), 2)
        self.uncommon_score = round(((random.randint(855, 1560))/100), 2)
        self.rare_score = round(((random.randint(1560, 2265))/100), 2)
        self.legendary_score = round(((random.randint(2265, 2970))/100), 2)

        self.common_rebound = round(((random.randint(0, 378))/100), 2)
        self.uncommon_rebound = round(((random.randint(378, 755))/100), 2)
        self.rare_rebound = round(((random.randint(755, 1133))/100), 2)
        self.legendary_rebound = round(((random.randint(1133, 1510))/100), 2)

        self.common_block = round(((random.randint(0, 65))/100), 2)
        self.uncommon_block = round(((random.randint(70, 140))/100), 2)
        self.rare_block = round(((random.randint(140, 210))/100), 2)
        self.legendary_block = round(((random.randint(210, 280))/100), 2)

        self.common_steal = round(((random.randint(0, 65))/100), 2)
        self.uncommon_steal = round(((random.randint(65, 110))/100), 2)
        self.rare_steal = round(((random.randint(110, 155))/100), 2)
        self.legendary_steal = round(((random.randint(155, 200))/100), 2)

        self.common_assist = round(((random.randint(30, 173))/100), 2)
        self.uncommon_assist = round(((random.randint(173, 515))/100), 2)
        self.rare_assist = round(((random.randint(515, 758))/100), 2)
        self.legendary_assist = round(((random.randint(758, 1000))/100), 2)


class Player(Stats):
    # general chances for player mood
    common_stat_chances = [0.2925, 0.09, 0.0225]
    uncommon_stat_chances = [0.82, 0.2235, 0.0435]
    rare_stat_chances = [0.9665, 0.8165, 0.08]
    legendary_stat_chances = [0.9775, 0.93, 0.8375]

    def __init__(self, player):
        super().__init__()
        self.score_q = player[['score_quality'][0]]['power_index']
        self.rebound_q = player[['rebound_quality'][0]]['power_index']
        self.block_q = player[['block_quality'][0]]['power_index']
        self.steal_q = player[['steal_quality'][0]]['power_index']
        self.assist_q = player[['assist_quality'][0]]['power_index']
        self._score()
        self._rebound()
        self._block()
        self._steal()
        self._assist()

    # Mood of the player will affect overall game stats
    def _score(self):
        mood = percentage_chance()
        # common
        if self.score_q == 1:
            if mood >= Player.common_stat_chances[0]:
                self.score_mood = 1
                self.score_out = self.common_score
            elif Player.common_stat_chances[0] > mood >= Player.common_stat_chances[1]:
                self.score_mood = 2
                self.score_out = self.uncommon_score
            elif Player.common_stat_chances[1] > mood >= Player.common_stat_chances[2]:
                self.score_mood = 3
                self.score_out = self.rare_score
            elif Player.common_stat_chances[2] > mood:
                self.score_mood = 4
                self.score_out = self.legendary_score
        # uncommon
        elif self.score_q == 2:
            if mood >= Player.uncommon_stat_chances[0]:
                self.score_mood = 1
                self.score_out = self.common_score
            elif Player.uncommon_stat_chances[0] > mood >= Player.uncommon_stat_chances[1]:
                self.score_mood = 2
                self.score_out = self.uncommon_score
            elif Player.uncommon_stat_chances[1] > mood >= Player.uncommon_stat_chances[2]:
                self.score_mood = 3
                self.score_out = self.rare_score
            elif Player.uncommon_stat_chances[2] > mood:
                self.score_mood = 4
                self.score_out = self.legendary_score
        # rare
        elif self.score_q == 3:
            if mood >= Player.rare_stat_chances[0]:
                self.score_mood = 1
                self.score_out = self.common_score
            elif Player.rare_stat_chances[0] > mood >= Player.rare_stat_chances[1]:
                self.score_mood = 2
                self.score_out = self.uncommon_score
            elif Player.rare_stat_chances[1] > mood >= Player.rare_stat_chances[2]:
                self.score_mood = 3
                self.score_out = self.rare_score
            elif Player.rare_stat_chances[2] > mood:
                self.score_mood = 4
                self.score_out = self.legendary_score
        # legendary
        elif self.score_q == 4:
            if mood >= Player.legendary_stat_chances[0]:
                self.score_mood = 1
                self.score_out = self.common_score
            elif Player.legendary_stat_chances[0] > mood >= Player.legendary_stat_chances[1]:
                self.score_mood = 2
                self.score_out = self.uncommon_score
            elif Player.legendary_stat_chances[1] > mood >= Player.legendary_stat_chances[2]:
                self.score_mood = 3
                self.score_out = self.rare_score
            elif Player.legendary_stat_chances[2] > mood:
                self.score_mood = 4
                self.score_out = self.legendary_score
        else:
            self.score_out = None
            self.score_mood = None

    def _rebound(self):
        mood = percentage_chance()
        # common
        if self.rebound_q == 1:
            if mood >= Player.common_stat_chances[0]:
                self.rebound_mood = 1
                self.rebound_out = self.common_rebound
            elif Player.common_stat_chances[0] > mood >= Player.common_stat_chances[1]:
                self.rebound_mood = 2
                self.rebound_out = self.uncommon_rebound
            elif Player.common_stat_chances[1] > mood >= Player.common_stat_chances[2]:
                self.rebound_mood = 3
                self.rebound_out = self.rare_rebound
            elif Player.common_stat_chances[2] > mood:
                self.rebound_mood = 4
                self.rebound_out = self.legendary_rebound
        # uncommon
        elif self.rebound_q == 2:
            if mood >= 0.75:
                self.rebound_mood = 1
                self.rebound_out = self.common_rebound
            elif Player.uncommon_stat_chances[0] > mood >= Player.uncommon_stat_chances[1]:
                self.rebound_mood = 2
                self.rebound_out = self.uncommon_rebound
            elif Player.uncommon_stat_chances[1] > mood >= Player.uncommon_stat_chances[2]:
                self.rebound_mood = 3
                self.rebound_out = self.rare_rebound
            elif Player.uncommon_stat_chances[2] > mood:
                self.rebound_mood = 4
                self.rebound_out = self.legendary_rebound
        # rare
        elif self.rebound_q == 3:
            if mood >= Player.rare_stat_chances[0]:
                self.rebound_mood = 1
                self.rebound_out = self.common_rebound
            elif Player.rare_stat_chances[0] > mood >= Player.rare_stat_chances[1]:
                self.rebound_mood = 2
                self.rebound_out = self.uncommon_rebound
            elif Player.rare_stat_chances[1] > mood >= Player.rare_stat_chances[2]:
                self.rebound_mood = 3
                self.rebound_out = self.rare_rebound
            elif Player.rare_stat_chances[2] > mood:
                self.rebound_mood = 4
                self.rebound_out = self.legendary_rebound
        # legendary
        elif self.rebound_q == 4:
            if mood >= Player.legendary_stat_chances[0]:
                self.rebound_mood = 1
                self.rebound_out = self.common_rebound
            elif Player.legendary_stat_chances[0] > mood >= Player.legendary_stat_chances[1]:
                self.rebound_mood = 2
                self.rebound_out = self.uncommon_rebound
            elif Player.legendary_stat_chances[1] > mood >= Player.legendary_stat_chances[2]:
                self.rebound_mood = 3
                self.rebound_out = self.rare_rebound
            elif Player.legendary_stat_chances[2] > mood:
                self.rebound_mood = 4
                self.rebound_out = self.legendary_rebound
        else:
            self.rebound_out = None
            self.rebound_mood = None

    def _block(self):
        mood = percentage_chance()
        # common
        if self.block_q == 1:
            if mood >= Player.common_stat_chances[0]:
                self.block_mood = 1
                self.block_out = self.common_rebound
            elif Player.common_stat_chances[0] > mood >= Player.common_stat_chances[1]:
                self.block_mood = 2
                self.block_out = self.uncommon_rebound
            elif Player.common_stat_chances[1] > mood >= Player.common_stat_chances[2]:
                self.block_mood = 3
                self.block_out = self.rare_rebound
            elif Player.common_stat_chances[2] > mood:
                self.block_mood = 4
                self.block_out = self.legendary_rebound
        # uncommon
        elif self.block_q == 2:
            if mood >= Player.uncommon_stat_chances[0]:
                self.block_mood = 1
                self.block_out = self.common_block
            elif Player.uncommon_stat_chances[0] > mood >= Player.uncommon_stat_chances[1]:
                self.block_mood = 2
                self.block_out = self.uncommon_block
            elif Player.uncommon_stat_chances[1] > mood >= Player.uncommon_stat_chances[2]:
                self.block_mood = 3
                self.block_out = self.rare_block
            elif Player.uncommon_stat_chances[2] > mood:
                self.block_mood = 4
                self.block_out = self.legendary_block
        # rare
        elif self.block_q == 3:
            if mood >= Player.rare_stat_chances[0]:
                self.block_mood = 1
                self.block_out = self.common_block
            elif Player.rare_stat_chances[0] > mood >= Player.rare_stat_chances[1]:
                self.block_mood = 2
                self.block_out = self.uncommon_block
            elif Player.rare_stat_chances[1] > mood >= Player.rare_stat_chances[2]:
                self.block_mood = 3
                self.block_out = self.rare_block
            elif Player.rare_stat_chances[2] > mood:
                self.block_mood = 4
                self.block_out = self.legendary_block
        # legendary
        elif self.block_q == 4:
            if mood >= Player.legendary_stat_chances[0]:
                self.block_mood = 1
                self.block_out = self.common_block
            elif Player.legendary_stat_chances[0] > mood >= Player.legendary_stat_chances[1]:
                self.block_mood = 2
                self.block_out = self.uncommon_block
            elif Player.legendary_stat_chances[1] > mood >= Player.legendary_stat_chances[2]:
                self.block_mood = 3
                self.block_out = self.rare_block
            elif Player.legendary_stat_chances[2] > mood:
                self.block_mood = 4
                self.block_out = self.legendary_block
        else:
            self.block_out = None
            self.block_mood = None

    def _steal(self):
        mood = percentage_chance()
        # common
        if self.steal_q == 1:
            if mood >= Player.common_stat_chances[0]:
                self.steal_mood = 1
                self.steal_out = self.common_steal
            elif Player.common_stat_chances[0] > mood >= Player.common_stat_chances[1]:
                self.steal_mood = 2
                self.steal_out = self.uncommon_steal
            elif Player.common_stat_chances[1] > mood >= Player.common_stat_chances[2]:
                self.steal_mood = 3
                self.steal_out = self.rare_steal
            elif Player.common_stat_chances[2] > mood:
                self.steal_mood = 4
                self.steal_out = self.legendary_steal
        # uncommon
        elif self.steal_q == 2:
            if mood >= Player.uncommon_stat_chances[0]:
                self.steal_mood = 1
                self.steal_out = self.common_steal
            elif Player.uncommon_stat_chances[0] > mood >= Player.uncommon_stat_chances[1]:
                self.steal_mood = 2
                self.steal_out = self.uncommon_steal
            elif Player.uncommon_stat_chances[1] > mood >= Player.uncommon_stat_chances[2]:
                self.steal_mood = 3
                self.steal_out = self.rare_steal
            elif Player.uncommon_stat_chances[2] > mood:
                self.steal_mood = 4
                self.steal_out = self.legendary_steal
        # rare
        elif self.steal_q == 3:
            if mood >= Player.rare_stat_chances[0]:
                self.steal_mood = 1
                self.steal_out = self.common_steal
            elif Player.rare_stat_chances[0] > mood >= Player.rare_stat_chances[1]:
                self.steal_mood = 2
                self.steal_out = self.uncommon_steal
            elif Player.rare_stat_chances[1] > mood >= Player.rare_stat_chances[2]:
                self.steal_mood = 3
                self.steal_out = self.rare_steal
            elif Player.rare_stat_chances[2] > mood:
                self.steal_mood = 4
                self.steal_out = self.legendary_steal
        # legendary
        elif self.steal_q == 4:
            if mood >= Player.legendary_stat_chances[0]:
                self.steal_mood = 1
                self.steal_out = self.common_steal
            elif Player.legendary_stat_chances[0] > mood >= Player.legendary_stat_chances[1]:
                self.steal_mood = 2
                self.steal_out = self.uncommon_steal
            elif Player.legendary_stat_chances[1] > mood >= Player.legendary_stat_chances[2]:
                self.steal_mood = 3
                self.steal_out = self.rare_steal
            elif Player.legendary_stat_chances[2] > mood:
                self.steal_mood = 4
                self.steal_out = self.legendary_steal
        else:
            self.steal_out = None
            self.steal_mood = None

    def _assist(self):
        mood = percentage_chance()
        # common
        if self.steal_q == 1:
            if mood >= Player.common_stat_chances[0]:
                self.assist_mood = 1
                self.assist_out = self.common_assist
            elif Player.common_stat_chances[0] > mood >= Player.common_stat_chances[1]:
                self.assist_mood = 2
                self.assist_out = self.uncommon_assist
            elif Player.common_stat_chances[1] > mood >= Player.common_stat_chances[2]:
                self.assist_mood = 3
                self.assist_out = self.rare_assist
            elif Player.common_stat_chances[2] > mood:
                self.assist_mood = 4
                self.assist_out = self.legendary_assist
        # uncommon
        elif self.steal_q == 2:
            if mood >= Player.uncommon_stat_chances[0]:
                self.assist_mood = 1
                self.assist_out = self.common_assist
            elif Player.uncommon_stat_chances[0] > mood >= Player.uncommon_stat_chances[1]:
                self.assist_mood = 2
                self.assist_out = self.uncommon_assist
            elif Player.uncommon_stat_chances[1] > mood >= Player.uncommon_stat_chances[2]:
                self.assist_mood = 3
                self.assist_out = self.rare_assist
            elif Player.uncommon_stat_chances[2] > mood:
                self.assist_mood = 4
                self.assist_out = self.legendary_assist
        # rare
        elif self.steal_q == 3:
            if mood >= Player.rare_stat_chances[0]:
                self.assist_mood = 1
                self.assist_out = self.common_assist
            elif Player.rare_stat_chances[0] > mood >= Player.rare_stat_chances[1]:
                self.assist_mood = 2
                self.assist_out = self.uncommon_assist
            elif Player.rare_stat_chances[1] > mood >= Player.rare_stat_chances[2]:
                self.assist_mood = 3
                self.assist_out = self.rare_assist
            elif Player.rare_stat_chances[2] > mood:
                self.assist_mood = 4
                self.assist_out = self.legendary_assist
        # legendary
        elif self.steal_q == 4:
            if mood >= Player.legendary_stat_chances[0]:
                self.assist_mood = 1
                self.assist_out = self.common_assist
            elif Player.legendary_stat_chances[0] > mood >= Player.legendary_stat_chances[1]:
                self.assist_mood = 2
                self.assist_out = self.uncommon_assist
            elif Player.legendary_stat_chances[1] > mood >= Player.legendary_stat_chances[2]:
                self.assist_mood = 3
                self.assist_out = self.rare_assist
            elif Player.legendary_stat_chances[2] > mood:
                self.assist_mood = 4
                self.assist_out = self.legendary_assist
        else:
            self.assist_out = None
            self.assist_mood = None

    def play_match(self):
        out = {
            'score': [self.score_out, self.score_mood],
            'rebound': [self.rebound_out, self.rebound_mood],
            'block': [self.block_out, self.block_mood],
            'steal': [self.steal_out, self.steal_mood],
            'assist': [self.assist_out, self.assist_mood]
        }

        return out
