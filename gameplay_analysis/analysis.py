import pandas as pd
from player.player import Player
import plotly.express as px
from tournament.tournament import Tournament
import io


class Analysis:
    def __init__(self):
        pass

    @staticmethod
    def player_mood_grapher(test_player, game_count):
        count = 0
        normal_player_quality = {
            'score_q': test_player['score_quality']['power_index'],
            'rebound_q': test_player['rebound_quality']['power_index'],
            'block_q': test_player['block_quality']['power_index'],
            'steal_q': test_player['steal_quality']['power_index'],
            'assist_q': test_player['assist_quality']['power_index']
        }
        score_list = []
        rebound_list = []
        block_list = []
        steal_list = []
        assist_list = []
        while count < game_count:
            player = Player(test_player).__dict__
            score_list.append(player['score_mood'])
            rebound_list.append(player['rebound_mood'])
            block_list.append(player['block_mood'])
            steal_list.append(player['steal_mood'])
            assist_list.append(player['assist_mood'])
            count = count + 1
        data = {
            'Score Mood': score_list,
            'Rebound Mood': rebound_list,
            'Block Mood': block_list,
            'Steal Mood': steal_list,
            'Assist Mood': assist_list
        }
        df = pd.DataFrame(data)
        fig = px.histogram(df)
        fig.show()
        # buffer = io.StringIO()
        # fig.write_html(buffer)
        # print(buffer.getvalue().encode())
        return df

    # remember second team needs to be expected to loose the game
    @staticmethod
    def match_mood_grapher(first_team, second_team):
        match_count = 0
        df_first = pd.DataFrame(columns=['Player', 'Score Mood', 'Rebound Mood', 'Block Mood', 'Steal Mood', 'Assist Mood'])
        while True:
            temp = Tournament.action_match(first_team, second_team)

            if temp[0] == first_team:
                first_team_mood = temp[1]
                p_one_name = temp[0][0]['name']
                data = [p_one_name, first_team_mood[0][0], first_team_mood[0][1], first_team_mood[0][2], first_team_mood[0][3], first_team_mood[0][4]]
                anan = pd.DataFrame(data)
                # df_second = pd.DataFrame(second_team_mood, index=[temp[4][0]['name'], temp[4][1]['name'], temp[4][2]['name']])
                # df_second.columns = ['Player', 'Score Mood', 'Rebound Mood', 'Block Mood', 'Steal Mood', 'Assist Mood']
                print(anan)
                break
            match_count = match_count + 1


        return None






