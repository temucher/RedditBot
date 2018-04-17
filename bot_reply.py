import praw, os, pdb, re, random

reddit = praw.Reddit('bot1')

if not os.path.isfile("post_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))


subreddit = reddit.subreddit("StarWars")


with open("quotes.txt", "r") as g:
    for line in g:
        quotes = line.strip()

for submission in subreddit.new(limit=100):
    if submission.id not in posts_replied_to:
        print("Got to here")
        if re.search("star wars", submission.title, re.IGNORECASE):
            print("Replied to post: " + submission.title)
            rand = random.randint(0, len(quotes))
            submission.reply(str(quotes[rand]))
            posts_replied_to.append(submission.id)

with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.writelines(post_id)
