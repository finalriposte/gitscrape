# gitscrape
A script to help clone repos that match a list of keywords that you define based on a timeframe you wish to search for.

### requirements
To get best value out of this script I recommend using a git personal access token.
I have script this to run from an environment variable but may change this in the future.
Theoretically you could remove this is a requirement, but you might then have more issues with the API limits from Github.

### Usage
Firstly, make sure the script has the executable permission.
```
git clone https://github.com/finalriposte/gitscrape.git
```
```
cd gitscrape
```
```
chmod +x gitscrape.py
```
Make sure your Github Personal Access Token is configured to be an environment variable.  
```
GITTOKEN='token'; export GITTOKEN
```
This, of course, can be set to load on logging in to your shell.  
Once this is done the script can be run with the following syntax:
```./gitscrape.py --num 1 --search word1,word2```

The --num value is the days backward from the time the script is run, so 365 will be about a year.  
The --search is a comma separated list of words to search for.  

No support is offered for this script.
