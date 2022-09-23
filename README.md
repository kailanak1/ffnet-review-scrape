# ffnet-review-scrape

An MVP script for scraping reviews from ff.net. 

## How to use 

1. Fork and clone 
2. Install the necessary packages. You may need to install web-driver manually. 
3. Under the URL variable, use the fanfiction.net review url. It will looks something like https://www.fanfiction.net/r/<story_id>/
4. Reviews will output to the console in an object. 

## Limitations 
This script is still an MVP. There may be edgecases that it does not account for. If the story you're trying to scrape reviews for has more than 15 reviews, you will need to put in the pages one by one. 

## Acknowledgements 

Parts of [smilli's fanfiction scraper project](https://github.com/smilli/fanfiction) were used in this project. 
