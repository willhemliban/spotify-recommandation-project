import numpy as np 
import sys
from sklearn.metrics import precision_score,confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
np.set_printoptions(threshold=sys.maxsize)
import pandas as pd
from pandas import DataFrame
import warnings
from sklearn.ensemble import RandomForestClassifier


warnings.filterwarnings('ignore')

# PARTIE : 1 
# On importe les données
df = pd.read_csv('data/train_data.csv', sep=',') 


# Separation en deux tableaux :
values = df[['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness',
       'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo',
       'duration_ms', 'time_signature']]

y=df['liked'].astype('int')

#nomralisation des valeur du tableau des caractéristique 
scaler = MinMaxScaler(feature_range=(0, 1))
scaledData = scaler.fit_transform(values)
df_scaled= DataFrame(scaledData)
# print(df_scaled.head())


#Entrainement pour determiner les features importantes ou inutiles pour plus tard 
# On va utiliser l'algo de random Forest popur cela
x_train,x_test,y_train,y_test=train_test_split(df_scaled,y,test_size=0.2,random_state=30)
feat_labels = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness',
       'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo',
       'duration_ms', 'time_signature']

forest = RandomForestClassifier(n_estimators=300,
                                random_state=1)
forest.fit(x_train, y_train)

importances = forest.feature_importances_

indices = np.argsort(importances)[::-1]

for f in range(x_train.shape[1]):
    print("%2d) %-*s %f" % (f + 1, 30, 
                            feat_labels[indices[f]], 
                            importances[indices[f]]))

#On peut voir que "mode" "key" et "time_signature" sont des carateristique pas importante avec un taux d'importance plus faible donc vas donc pas les retenir pour la suite 

# Partie creation et entrainement du model de prediction 
# On va dans ce cas utiliser le KNN pour notre probleme de classification
values = df[['danceability', 'energy', 'loudness',  'speechiness','acousticness','instrumentalness','liveness', 'valence', 'tempo','duration_ms']]
scaler = MinMaxScaler(feature_range=(0, 1))
refinedData = scaler.fit_transform(values)
df_refined= DataFrame(refinedData)


n_neighbors=4 # a l'aide d'une boucle nous 
scores=[]

model=KNeighborsClassifier(n_neighbors)
model.fit(df_refined,y)
precision_score=model.score(df_refined,y)
print('Score du model : '+str(precision_score)+' .')



df2 = pd.read_csv('data/test_data.csv', sep=',') 

def estimationLikedPlaylist(df,model):
    nb=0
    values = df[['danceability', 'energy', 'loudness',  'speechiness','acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo','duration_ms']]
    scaler = MinMaxScaler(feature_range=(0, 1))
    refinedData = scaler.fit_transform(values)
    df_refined= DataFrame(refinedData)
    y_pred=model.predict(df_refined)

    for i in y_pred:
        if i==1:
            nb+=1

    tab = df[['name','artist']]
    tab['liked']=pd.DataFrame(y_pred)
    pourc = nb*100/len(y_pred)

    print("Vous allez aimer "+str(nb)+"/"+str(len(y_pred))+" chansons.")
    print("Pourcentage de chances que vous aimiez cette playlist est de "+str(pourc)+" %.")
    print("Details des chansons aimées et ou pas ci-dessous :")
    print(tab)


estimationLikedPlaylist(df2,model)