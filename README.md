# unresolved-mysteries-survey
In July 2018, /u/twelvedayslate posted on r/UnresolvedMysteries (a sub-Reddit dedicated to unsolved mysteries) asking for people to post an opinion about a mystery and for people to agree or disagree.

The goal, I guess, was to see which side of the fence people sat on with various theories behind mysteries. There was an incredible response with over 4,500 replies.

I still thought it'd be interesting to view the responses in a more visual manner.
## Requirements
* Python
* [PRAW](http://praw.readthedocs.io/)
* [Reddit API Access](https://www.reddit.com/dev/api/)

## Getting Started
Very simple:
* Fill in your credentials
```
reddit = praw.Reddit(user_agent='Comment Extraction (by /u/USERNAME)',
                     client_id='CLIENT_ID', client_secret="CLIENT_SECRET",
                     username='REDDIT_USERNAME', password='REDDIT_PASSWORD')
```
* And enter the target thread:
```
submission = reddit.submission(id='9014d6')
```
* You can also change the output location:
```
with open('unresolved-mysteries.html', 'w', encoding='utf-8') as f:
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details