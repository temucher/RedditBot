import praw, os, random

reddit = praw.Reddit('bot1')

if not os.path.isfile("post_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))


subreddit = reddit.subreddit("test")
# StarWars+PrequelMemes+SequelMemes


def getQuote():
    rand = random.randint(0, len(quotes)-1)
    return quotes[rand]


with open("quotes.txt", "r") as g:
    quotes = [line.strip() for line in g]


for submission in subreddit.new(limit=10):
    if submission.id not in posts_replied_to:
        print(submission.id)
        print(posts_replied_to)
        if "jar jar" in submission.title.lower():
            print("Replied to post: " + submission.title)
            submission.reply(getQuote())
            posts_replied_to.append(submission.id)
        for comment in submission.comments:
            if "jar jar" in comment.body.lower():
                print("Replied to comment: " + comment.id)
                comment.reply(getQuote())


with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.writelines(post_id)
