from player.player import Player


class Tournament:
    def __init__(self):
        pass

    @staticmethod
    def action_match(first_team, second_team):
        temp_first = [Player(first_team[0]).__dict__, Player(first_team[1]).__dict__, Player(first_team[2]).__dict__]
        temp_second = [Player(second_team[0]).__dict__, Player(second_team[1]).__dict__,
                       Player(second_team[2]).__dict__]
        first_score, second_score = 0, 0
        first_rebound, second_rebound = 0, 0
        first_block, second_block = 0, 0
        first_steal, second_steal = 0, 0
        first_assist, second_assist = 0, 0

        first_team_wins = []
        second_team_wins = []
        first_team_moods = []
        second_team_moods = []

        for player in temp_first:
            temp = [player['score_mood'], player['rebound_mood'], player['block_mood'], player['steal_mood'], player['assist_mood']]
            first_team_moods.append(temp)
            first_score = first_score + player['score_out']
            first_rebound = first_rebound + player['rebound_out']
            first_block = first_block + player['block_out']
            first_steal = first_steal + player['steal_out']
            first_assist = first_assist + player['assist_out']

        for player in temp_second:
            temp = [player['score_mood'], player['rebound_mood'], player['block_mood'], player['steal_mood'], player['assist_mood']]
            second_team_moods.append(temp)
            second_score = second_score + player['score_out']
            second_rebound = second_rebound + player['rebound_out']
            second_block = second_block + player['block_out']
            second_steal = second_steal + player['steal_out']
            second_assist = second_assist + player['assist_out']

        # score comparing
        if first_score > second_score:
            first_team_wins.append(1)
            second_team_wins.append(0)
        elif second_score > first_score:
            first_team_wins.append(0)
            second_team_wins.append(1)
        elif first_score == second_score:
            first_team_wins.append(0)
            second_team_wins.append(0)

        # rebound comparing
        if first_rebound > second_rebound:
            first_team_wins.append(1)
            second_team_wins.append(0)
        elif first_rebound < second_rebound:
            first_team_wins.append(0)
            second_team_wins.append(1)
        elif first_rebound == second_rebound:
            first_team_wins.append(0)
            second_team_wins.append(0)

        # block comparing
        if first_block > second_block:
            first_team_wins.append(1)
            second_team_wins.append(0)
        elif first_block < second_block:
            first_team_wins.append(0)
            second_team_wins.append(1)
        elif first_block == second_block:
            first_team_wins.append(0)
            second_team_wins.append(0)

        # steal comparing
        if first_steal > second_steal:
            first_team_wins.append(1)
            second_team_wins.append(0)
        elif first_steal < second_steal:
            first_team_wins.append(0)
            second_team_wins.append(1)
        elif first_steal == second_steal:
            first_team_wins.append(0)
            second_team_wins.append(0)

        # assist comparing
        if first_assist > second_assist:
            first_team_wins.append(1)
            second_team_wins.append(0)
        elif first_assist < second_assist:
            first_team_wins.append(0)
            second_team_wins.append(1)
        elif first_assist == second_assist:
            first_team_wins.append(0)
            second_team_wins.append(0)

        sum_first = sum(first_team_wins)
        sum_second = sum(second_team_wins)
        if sum_first > sum_second:
            winner = first_team
        elif sum_second > sum_first:
            winner = second_team
        else:
            winner = 0
        return winner, first_team_moods, second_team_moods, first_team, second_team

