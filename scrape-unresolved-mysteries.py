import praw
import re
# It's here that you add your personal credentials. For what this script does, at this point in time you do not need to pass your Reddit username and password.
reddit = praw.Reddit(user_agent='Comment Extraction (by /u/USERNAME)',
                     client_id='CLIENT_ID', client_secret="CLIENT_SECRET",
                     username='REDDIT_USERNAME', password='REDDIT_PASSWORD')
# The ID for this particular submission for unresolved mysteries is 9014d6, but you can change it to whatever comment ID is on another thread
submission = reddit.submission(id='9014d6')
from praw.models import MoreComments
submission.comments.replace_more(limit=None)
toplevelcount=0
# Below you enter where you want to save the file. Encoding in UTF-8 because sometimes there are issues with parsing these comments.
with open('unresolved-mysteries.html', 'w', encoding='utf-8') as f:
	# Create HTML and table. It's pretty long, but I wanted to get everything done in here without any "post-production"
	print("""<!DOCTYPE html>
	<html>
		<head>
			<title>A visualisation of data from r/UnresolvedMysteries - www.ininitefunspace.net</title>
			<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
			<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
			<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
			<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
			<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
			<style>
				@import url(https://fonts.googleapis.com/css?family=Open+Sans);
				body {
					font-family:Open Sans;
				}
				a, a:hover, a:active, a:visited {
					color:#212529;
				}
				.jumbotron {
					padding: 30px;
					text-align: center;
					background:#f1f1f1;
				}
				.blockquote2 {
					font-size: 1em;
					width:100%;
					margin:15px auto;
					font-family:Open Sans;
					font-style:italic;
					color: #555555;
					padding:1.2em 1.4em 1.2em 1.8em;
					border-left:8px solid #78C0A8 ;
					line-height:1.4;
					position: relative;
					background:#f1f1f1;
					}
				.card:hover {
					background:#fcfcfc;
					}

				@media (min-width: 300px) { 
					.card-columns {
						column-count: 2;
						}
					}
				@media (min-width: 1024px) { 
					.card-columns {
						column-count: 3;
						}
					}
			</style>
		</head>
		<body>
			<div class="container-fluid">
				<div class="jumbotron">
					<h1>A visualisation of /r/UnresolvedMysteries responses</h1>
				</div>
				<div class="container">
					<p>
					In July 2018, <a href="https://reddit.com/user/twelvedayslate" target="_blank">/u/twelvedayslate</a> posted on <a href="https://www.reddit.com/r/UnresolvedMysteries/comments/9014d6/can_we_have_an_agreedisagree_post_on_all_mysteries/?ref=share&ref_source=link" target="_blank">r/UnresolvedMysteries</a> (a sub-Reddit dedicated to unsolved mysteries) asking for people to post an opinion about a mystery and for people to agree or disagree.</p>
					<p>I thought it'd be interesting to collate the reponses and view them in a more visual manner.<p>
					<div class="alert alert-info" role="alert"><h5>Notes</h5>Data was scraped from Reddit using <a href="http://praw.readthedocs.io/en/latest/" target="_blank">PRAW</a>. Only second level responses were counted - I don't think there was anything but discussion underneath that. 
					<hr>
					Some questions actually posited two or more opinions, so there are some replies that say "agree with the first part, disagree with the second". In this sort of case, the reply counts as both agree and disagree. There's no simple way to get around that, so if an opinion has more votes than total comments, the opinion is marked with a &#9888; symbol and a note.
					<hr>
					There are a few top-level posts that aren't in the spirit of what <a href="https://reddit.com/user/twelvedayslate" target="_blank">/u/twelvedayslate</a> was asking for. I haven't edited anything, everything was been gathered and calculated automatically, so be aware that any comments that may be out of place (or are a bit whacky!) were in the original thread.
					<hr>
					Everything below is an opinion somebody posted on Reddit, and the opinions are not endorsed by me (hell, I'm only interested in heists and nautical mysteries). A couple of people posted on the original thread that they thought making a game of this was in bad taste, but I don't believe the OP or anyone else intended this as a game or something to be taken lightly - it's just a method to see where people stand on mysteries.</div>
				
				<p>Sort by: <button id="mostreplies" class="btn btn-secondary">Most Replies</button> <button id="popular" class="btn btn-secondary">Popular</button> <button id="unpopular" class="btn btn-secondary">Unpopular</button> <input id="myInput" class="form-control-sm" type="text" placeholder="Search..."></div>
				<script>
					$('#mostreplies').click(function() {
						var divList = $(".card");
						divList.sort(function(a, b){ return $(b).data("comment-count")-$(a).data("comment-count")});
						$(".card-columns").html(divList);
					});
					$('#popular').click(function() {
						var divList = $(".card");
						divList.sort(function(a, b){ return $(b).data("perc-agree")-$(a).data("perc-agree")});
						$(".card-columns").html(divList);
					});
					$('#unpopular').click(function() {
						var divList = $(".card");
						divList.sort(function(a, b){ return $(b).data("perc-disagree")-$(a).data("perc-disagree")});
						$(".card-columns").html(divList);
					});
				</script>
				<script>
					$(document).ready(function(){
						$("#myInput").on("keyup", function() {
							var value = $(this).val().toLowerCase();
						$(".card").filter(function() {
						$(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
					});
					});
					});
				</script></p>
	<div class="card-columns">""", file=f)
	secondlevelcount=0
	for top_level_comment in submission.comments:		
		agreecount=0
		disagreecount=0
		commentcount=0
		percagree=0
		perdisagree=0
		toplevelcount=toplevelcount+1
		torn=False
		for second_level_comment in top_level_comment.replies:
				commentcount=commentcount+1
				secondlevelcount=secondlevelcount+1
				if  re.search(r'\bagree\b', second_level_comment.body, re.I):
					agreecount=agreecount+1
				if  re.search(r'\bagreed\b', second_level_comment.body, re.I):
					agreecount=agreecount+1
				if  re.search(r'\bdisagree\b', second_level_comment.body, re.I):
					disagreecount=disagreecount+1
		# If there is 100% agreement, we'd need to divide by 0. So in this case, we make percagree 100% manually. But we must correct this below for comments with no replies.
		if disagreecount != 0:
			percagree=(agreecount/(agreecount+disagreecount))*100
		else:
			percagree=100
		percdisagree=100-percagree
		# This ensures that posts with no votes don't have 100% agreement.
		if (agreecount+disagreecount) < 1:
			percagree=0
			perdisagree=0
		# Some people agree and disagree, usually because the top-level-poster has argued two things... we catch these as the agree/disagree counts will exceed the number of comments.
		if (agreecount+disagreecount) > commentcount:
			torn=True
		print('<div class="card p-3" data-perc-agree="'+str(percagree)+'" data-perc-disagree="'+str(percdisagree)+'" data-comment-count="'+str(commentcount)+'"><p><blockquote class="blockquote mb-0 card-body">'+top_level_comment.body+'</p>', file=f)
		print("""<div class="progress">
			<div class="progress-bar bg-success" role="progressbar" style="width: """+str(percagree)+"""%" aria-valuemin="0" aria-valuemax="100"></div>
			<div class="progress-bar bg-danger" role="progressbar" style="width: """+str(percdisagree)+"""%" aria-valuemin="0" aria-valuemax="100"></div>
			</div><hr /><p class="card-text"><small class="text-muted">Agree: <span class="agree">"""+str(agreecount)+"""</span> | Disagree: <span class="disagree">"""+str(disagreecount)+"""</span> | Total replies: <span class="replies">"""+str(commentcount)+'</span></p><p><a href="https://reddit.com'+top_level_comment.permalink+'" target="_blank">Link</a></p>', file=f)
		if torn is True:
			print('<p>&#9888; Some people seem to both agree and disagree with this opinion</p>', file=f)
		print('</blockquote></small></div>'+'\n', file=f)
	print('</div><section id="footer"><div class="container"><div class="col-xs-12 col-sm-12 col-md-12 mt-2 mt-sm-2 text-center"><p>Number of top level comments: '+str(toplevelcount)+'</p><p>Number of replies processed: '+str(secondlevelcount)+'</p><p>Posted on: 31<sup>st</sup> July 2018 | Find the code on <a href="https://github.com/apmurdoch/unresolved-mysteries-survey" target="_blank">Github</a></p></div></div></div></div></section></body>', file=f)