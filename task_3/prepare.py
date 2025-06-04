import numpy as np
import pandas as pd

def prepare():
    with open("./task_3/top250_raw.csv") as file:
        dt = pd.read_csv(file)

    votes =[]
    for i in dt["votes"]:
        if i[-1]=="K":
            votes.append(int(float(i[:-1])*1000))
        if i[-1]=="M":
            votes.append(int(float(i[:-1])*1000000))

    dt["votes"]=votes
    dt["title"]=dt["title"].astype("string")
    dt["genres"]=dt["genres"].astype("category")
    dt["runtime"]=pd.to_timedelta(
        dt['runtime']
        .str.replace('h', ' hours')
        .str.replace('m', ' minutes')
    )

    decade = []
    for i in dt["year"]:
        decade.append(str(i//10)+"0-e")

    dt["decade"]=decade

    return dt

def group():
    dt = prepare()
    res = dt.groupby(dt["decade"]).agg(
        avg_rating=("rating", "mean"),
        median_runtime=("runtime", "median")
    )
    print(res)


