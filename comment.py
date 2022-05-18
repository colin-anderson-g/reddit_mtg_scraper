import praw
import psycopg2
from setup import cursor


def save(comment, submission_id):
    cursor.execute('insert into mtg.comment values(%s,%s,%s,%s,%s)',
                   (comment.id, submission_id, comment.author.name,
                    comment.body, comment.score))


def get(id):
    return cursor.execute('select * from mtg.comment where id = %s', id).fetchall()
