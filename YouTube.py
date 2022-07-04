import os
import sys
import json
import sqlalchemy as db
import pandas as pd
from pyyoutube import Api

def main():
    api = setupAPI()
    query = "dogs"
    videos = search(api, query, 5)
    engine = addDatabase(query, videos)
    printDatabase(engine, query)

def setupAPI(key=os.environ.get('YOUTUBE_API_KEY')):
    """Returns an API object if the key is valid"""
    api = Api(api_key=key)
    try:
        api.search_by_keywords(q="test")
    except:
        sys.exit("Invalid API key!")
    return api

def search(api, query, num_videos=5):
    """Returns a dictionary of size num_videos given an API object and search query"""
    videos = api.search_by_keywords(q=query, search_type=['video'], count=num_videos, limit=num_videos)
    videos = {
        "videos" : [video.to_json() for video in videos.items]
    }
    return videos

def addDatabase(query, videos):
    """Returns a database engine containing the list of videos"""
    engine = db.create_engine('sqlite:///videos.db')
    database = pd.DataFrame.from_dict(videos)
    database.to_sql((query + "_videos"), con=engine, if_exists='replace', index=False)
    return engine

def printDatabase(engine, query):
    """Prints the query table from the database"""
    query_result = engine.execute(f"SELECT * FROM {query}_videos;").fetchall()
    print(pd.DataFrame(query_result))

if __name__ == "__main__":
    main()
