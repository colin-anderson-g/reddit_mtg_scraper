import praw
import psycopg2
import uuid
from setup import cursor
from setup import repattern


def save(comment, repattern):
    for card in repattern.finditer(comment.body):
        cursor.execute('insert into mtg.card_tag values(%s,%s,%s)',
                       (uuid.uuid4().hex, comment.id, card.group(1)))


def find_by_id(id):
    return cursor.execute('select * from mtg.comment where id = %s', id).fetchall()
