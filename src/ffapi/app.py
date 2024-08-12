from typing import Union

from fastapi import FastAPI, HTTPException
import pandas as pd

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/sample")
def sample_data():
    df = pd.read_parquet('/home/oddsummer/code/fastapi/data')
    sample_df = df.sample(n=5)
    r = sample_df.to_dict(orient='records')
    return r


@app.get("/movie/{movie_cd}")
def movie_meta(movie_cd: int):
    df = pd.read_parquet('/home/oddsummer/code/fastapi/data')
    
    # df에서 movieCd == movie_cd 인 row 조회 df[['a']==b]
    meta_df = df[['movieCd' == movie_cd]]
    
    if meta_df.empty:
        raise HTTPException(status_code=404, detail="영화를 찾을 수 없습니다.")

    # 조회된 데이터 .to_dict로 만들어서 return
    r = meta_df.iloc[0].to_dict()
    return r


