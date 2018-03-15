import requests
import pandas as pd
from sqlalchemy import create_engine

from pandas import DataFrame, Series
import sqlite3 as db
import numpy as np

"""
A command line application that parses json from newsapi.org
"""


def cli():

    greeting()

    news_request = requests.get(
        "https://newsapi.org/v1/articles?source=the-next-web&sortBy=latest&apiKey=8ddc75bfec6b470a85fb69bccce7afbb")

    """
    Test is the response code from api is OK. 
    """
    if news_request.status_code != 200:
        print("Something wrong")
        exit(1)
    else:
        convert_df(news_request)


def display(news_request):
    main_dict = news_request.json()
    article_list = main_dict['articles']

    for article in article_list:
        print('\n')
        print (article['description'])

def convert_df(news_request):
    main_dict = news_request.json()
    article_list = main_dict['articles']
    #df = pd.read_csv(io.StringIO(article_list))
    df = pd.DataFrame(article_list)
    print (df)
    save_db(df)

def save_db(df):

    print("Saving in database")
    db_engine = create_engine('sqlite:///sqlite.db')
    df.to_sql('news', db_engine, if_exists='append')

    print("Content of db")
    news_df = pd.read_sql_query('SELECT * FROM news LIMIT 3', db_engine)
    news_df.head()



def save_excel(df):
    writer = pd.ExcelWriter('output.xlsx')
    df.to_excel(writer,'Sheet1')
    writer.save()





def greeting():
    print("Hi there, I'm Vortex, your news buddy! You can count on me to keep you posted.")
    #user_name = input('> What\'s your name?: ')
    user_name = "Vinod"
    print('\nIt\'s nice to meet you {}. I\'ll have the latest news stories for you in a jiff: \n'.format(user_name))
    print('-' * 100)


if __name__ == '__main__':
    cli()