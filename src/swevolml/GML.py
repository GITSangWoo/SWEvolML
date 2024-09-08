import os
import sys
import pandas as pd
import math
import random
from sklearn.neighbors import KNeighborsClassifier


home_path = os.path.expanduser('~')
data_path=f"{home_path}/data/GML/"
file_path=f"{home_path}/data/GML/gml.csv"

if os.path.exists(file_path):
    df=pd.read_csv(file_path) 
else:
    df=pd.DataFrame(
        {
        'length' : [],
        'weight': [],
        'MLanswer' : [],
        'ranswer': [],
        }
    )

length,weight= map(float, input("길이와 무게를 입력하세요:").split())

if len(df) == 0:
    fanswer = random.randint(0,1)
    df.loc[len(df)] = [length,weight,fanswer,0]
    if fanswer==1.0:
        print("일단은 도미")
    else :
        print("일단은 빙어")
    
    print("============")
    answer=input("정답을 입력하세요(y or n) :")
    if answer == 'y':
        print("역시 그렇군요")
        df.loc[len(df)-1:len(df), "ranswer"] = fanswer
    else : 
        if fanswer == 1.0:
            df.loc[len(df)-1:len(df), "ranswer"] = 0
            print("강해져서 돌아오겠습니다")
        else :
            df.loc[len(df)-1:len(df), "ranswer"] = 1
            print("강해져서 돌아오겠습니다")
    
   
else:
    kn=KNeighborsClassifier(n_neighbors=int((math.sqrt(len(df)))))
    kn.fit(df.iloc[:,0:2].values,df.loc[:,'ranswer'])
    pred=int(kn.predict([[length,weight]])[0])
    if  pred == 1.0:
        df.loc[len(df)] = [length,weight,pred,0]
        print("도미")
    else :
        df.loc[len(df)] = [length,weight,pred,0]
        print("빙어")
    answer=input("정답을 입력하세요(y or n):")
    if answer == 'y':
        print("역시 그렇군요")
        df.loc[len(df)-1:len(df), "ranswer"] = pred
    else : 
        if pred == 1.0:
            df.loc[len(df)-1:len(df), "ranswer"] = 0
            print("강해져서 돌아오겠습니다")
        else :
            df.loc[len(df)-1:len(df), "ranswer"] = 1
            print("강해져서 돌아오겠습니다")

print("정답율:",round((len(df[df['MLanswer']==df['ranswer']])/len(df))*100,2),"%")

os.makedirs(os.path.dirname(data_path), exist_ok = True)
df.to_csv(file_path,index=False)








    
