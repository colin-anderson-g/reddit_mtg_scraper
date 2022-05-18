import praw
import psycopg2
import re
import setup
import submission
import comment
import card

#Loop over the first 10 "hot" submissions in the macigtcg subreddit
for submission in setup.reddit.subreddit('magictcg').hot(limit=10):
    submission.save(submission)

    for comment in submission.comments:
        if setup.repattern.search(comment.body):
            comment.save(comment, submission.id)

            for card in setup.repattern.finditer(comment.body):
                card.save(comment, setup.repattern)
