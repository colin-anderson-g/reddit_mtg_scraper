import praw
import psycopg2
import re
import setup
import submissions
import comments
import cards

#Loop over the first 10 "hot" submissions in the macigtcg subreddit
for submission in setup.reddit.subreddit('magictcg').hot(limit=10):
    submissions.save(submission)

    for comment in submission.comments:
        if setup.repattern.search(comment.body):
            comments.save(comment, submission.id)

            for card in setup.repattern.finditer(comment.body):
                cards.save(comment, setup.repattern)
