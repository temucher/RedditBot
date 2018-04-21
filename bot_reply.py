import praw, os, random

# get environment variables
CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
PASSWORD = os.environ.get('PASSWORD')
USER_AGENT = os.environ.get('USER_AGENT')
USERNAME = os.environ.get('USERNAME')



def botLogin():
    # create reddit instance with parameters from environment variables and log in
    reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                         password=PASSWORD, user_agent=USER_AGENT, username=USERNAME)
    subreddit = reddit.subreddit('StarWars+PrequelMemes+SequelMemes')
    # change this back
    # StarWars+PrequelMemes+SequelMemes
    return subreddit


def getQuote():
    with open("quotes.txt", "r") as g:
        quotes = [line.strip() for line in g]
    rand = random.randint(0, len(quotes)-1)
    return quotes[rand]


def main(subreddit):
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = [line.strip() for line in f]

    with open("comments_replied_to.txt") as f:
        comments_replied_to = [line.strip() for line in f]

    # look at the top new submissions, find posts and comments that
    #  haven't been commented on by this bot
    for submission in subreddit.new(limit=400):  # potentially change limit here?
        if submission.id not in posts_replied_to:
            print(submission.id)
            print(posts_replied_to)
            if "jar jar" in submission.title.lower():
                print("Replied to post: " + submission.title)
                submission.reply(getQuote() + "\n\n Beep boop I am a bot | Here is the [code](https://github.com/temucher/RedditBot)")
                posts_replied_to.append(submission.id)

        for comment in submission.comments:
            if comment.id not in comments_replied_to:
                if "jar jar" in comment.body.lower():
                    print("Replied to comment: " + comment.id)
                    comment.reply(getQuote() + "\n\n Beep boop I am a bot | Here is the [code](https://github.com/temucher/RedditBot)")
                    comments_replied_to.append(comment.id)

    # add post and comment id's to files so that next time this
    # is run, we don't comment on the same posts/comments
    with open("posts_replied_to.txt", "w") as f:
        f.write('\n'.join(posts_replied_to))

    with open("comments_replied_to.txt", "w") as f:
        f.write('\n'.join(comments_replied_to))


subreddit = botLogin()
main(subreddit)
