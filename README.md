# ffnet-review-scrape

A Python script for scraping reviews from fanfiction.net. 

I am not affiliated with fanfiction.net. 

## How to use 

1. Fork and clone 
2. Install the necessary packages. You may need to install web-driver manually. 
3. Under the URL variable, use the first page of the fanfiction.net review url. It will look something like ```https://www.fanfiction.net/r/<story_id>/``` or ```https://www.fanfiction.net/r/<story_id>/0/1```.
4. Reviews will output to the console in an object. 

## Limitations 

This script was not tested on stories with a large amount of reviews. 

## Acknowledgements 

Parts of [smilli's fanfiction scraper project](https://github.com/smilli/fanfiction) were used in this project. 

## License 

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
