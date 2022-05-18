import praw
import psycopg2
from setup import reddit
from setup import cursor


def save(submission):
    cursor.execute('insert into mtg.submission values(%s,%s,%s,%s,%s)',
                   (submission.id, submission.title, submission.author.name,
                    submission.subreddit.name, submission.score))


def get(id):
    return cursor.execute('select * from mtg.submission where id = %s', id).fetchall()
