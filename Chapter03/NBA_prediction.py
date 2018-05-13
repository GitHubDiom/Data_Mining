import pandas as pd
from sklearn.cross_validation import cross_val_score
from sklearn.tree import DecisionTreeClassifier
import numpy as np
from collections import defaultdict


def find_WonTeam_LastBattle(home_team,visitor_team,row):
    teams = tuple(sorted([home_team,visitor_team]))
    dataset.at[index , "HomeTeamWon_LastBattle"] = True if last_match_winner[teams] == home_team else False
    last_match_winner[teams] =home_team if row['Homewin'] else visitor_team


def find_HeigherRank(home_team,visitor_team, index , row , standings):
    home_rank = standings[standings['Team']==home_team]['Rk'].values[0]
    visitor_rank = standings[standings['Team'] == visitor_team ]['Rk'].values[0]
    dataset.at[index ,"HomeTeamRanksHeigher"] = True if home_rank < visitor_rank else False
    

def find_HomeLastWon(home_team,visitor_team,index , row):
    dataset.at[index , "HomeWonLast"] = WonLast_asHome[home_team]
    dataset.at[index , "VisitorWonLast"] = WonLast_asHome[visitor_team]
    WonLast_asHome[home_team] = row['Homewin']
    WonLast_asHome[visitor_team] = not row['Homewin']

'''
    分类特征为主场队伍是否胜利
    潜在特征：
        1. 队伍上次比赛情况
            (1). 主场队伍上次比赛的情况           'HomeLastWon'
            (2). 客场队伍上次比赛的情况           'VisitorLastWon'
        2. 两支队伍上次交手的情况，队伍相同，不考虑上次交手的主客场     'HomeTeamWonLastBattel
        3. 主场队伍在上赛季最终排名是否高于客场队伍     'HomeRanksHeigher'
'''
data_filename = './NBA_Data.csv'
dataset = pd.read_csv(data_filename,parse_dates = ['Date'])
dataset.columns = ["Date", "Start (ET)", "Visitor Team", "VisitorPts", "Home Team", "HomePts",  "Score Type","OT?","Attend","Notes"]
dataset['Homewin'] = dataset['HomePts']>dataset['VisitorPts']


dataset["HomeWonLast"] = False
dataset["VisitorWonLast"] = False
WonLast_asHome = defaultdict(bool)
dataset['HomeTeamRanksHeigher'] = False
standing_file = './NBA_2013_Standings.csv'
standings = pd.read_csv(standing_file)
last_match_winner = defaultdict(str)
dataset['HomeTeamWon_LastBattle'] = False

for index , row in dataset.iterrows():
    home_team = row['Home Team']
    visitor_team = row['Visitor Team']
    find_HomeLastWon(home_team, visitor_team, index, row)
    find_HeigherRank(home_team, visitor_team, index, row, standings)
    find_WonTeam_LastBattle(home_team, visitor_team, row)

Y_true = dataset['Homewin'].values
X_previous_win = dataset[['HomeTeamRanksHeigher','HomeTeamWon_LastBattle','HomeWonLast','VisitorWonLast']].values
estimator = DecisionTreeClassifier(random_state=14)
scores = cross_val_score(estimator , X_previous_win , Y_true , scoring = 'accuracy')
print(np.mean(scores)*100)
