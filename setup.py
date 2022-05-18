import praw
import psycopg2
import re

#initialize reddit instance with ini params
reddit = praw.Reddit('bot')

#db connection
conn = psycopg2.connect(
    database='postgres',
    user='postgres',
    password='admin',
    host='localhost',
    port= '5432'
)

#Setting auto commit
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Initialize regular expression for card tagging
repattern = re.compile('\[\[(.*?)\]\]')
