import pandas as pd
import numpy as np

battles = pd.read_csv('data/battles.csv')
character_predictions = pd.read_csv('data/character-predictions.csv')

def q01_feature_engineering(df1,df2):
    df1['defender_count'] = 0
    df1['attacker_count'] = 0
    df1['att_comm_count'] = 0
    df2['no_of_books'] = 0
    for i in range(0,df1.shape[0]):
        for j in ['defender_1','defender_2','defender_3','defender_4']:
            if not str(df1.loc[i,j]) == 'nan':
                df1.loc[i,'defender_count'] = df1.loc[i,'defender_count'] + 1

        for k in ['attacker_1','attacker_2','attacker_3','attacker_4']:
            if not str(df1.loc[i,k]) == 'nan':
                df1.loc[i,'attacker_count'] = df1.loc[i,'attacker_count'] + 1

        df1.loc[i,'att_comm_count'] = len(str(df1.loc[i,'attacker_commander']).split(","))

    for i in range(0,df2.shape[0]):
        for j in ['book1','book2','book3','book4','book5']:
            if int(df2.loc[i,j]) == 1:
                df2.loc[i,'no_of_books'] = df2.loc[i,'no_of_books'] + 1

    return df1,df2

#q01_feature_engineering(battles,character_predictions)
