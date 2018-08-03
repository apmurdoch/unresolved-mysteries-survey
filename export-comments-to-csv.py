import praw
import csv
# It's here that you add your personal credentials. For what this script does, at this point in time you do not need to pass your Reddit username and password.
reddit = praw.Reddit(user_agent='Comment Extraction (by /u/USERNAME)',
                     client_id='CLIENT_ID', client_secret="CLIENT_SECRET",
                     username='REDDIT_USERNAME', password='REDDIT_PASSWORD')
# The ID for this particular submission for unresolved mysteries is 9014d6, but you can change it to whatever comment ID is on another thread
submission = reddit.submission(id='9014d6')
from praw.models import MoreComments
submission.comments.replace_more(limit=None)

# Below you enter where you want to save the file. Encoding in UTF-8 because sometimes there are issues with parsing these comments.
with open('unresolved-mysteries-full.csv', 'w', newline='', encoding='utf-8') as csvfile:
	theoutput = csv.writer(csvfile, delimiter=',')
	theoutput.writerow(['Top Level Comment']+['Second Level Comments']+['Link']+['Score'])
	for top_level_comment in submission.comments:
		theoutput.writerow([top_level_comment.body]+['']+['https://reddit.com'+top_level_comment.permalink]+[top_level_comment.score])
		for second_level_comment in top_level_comment.replies:
			theoutput.writerow(['']+[second_level_comment.body]+['']+[second_level_comment.score])