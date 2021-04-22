#!/usr/bin/env python3
from github import Github
import pygit2
import datetime
import os
import argparse
from urllib.parse import urlparse

"""
gitscrape
Automatically search and download repositories from Github.
Requires a Personal Access Token.
Command line options:
    --num - the number of days back to search
    --search - a comma separated list of words to search for
VERSION: 0.01
SUPPORT OF THIS CODE IS NOT OFFERED
"""

ACCESS_TOKEN = os.environ.get('GITTOKEN')
git_client = Github(ACCESS_TOKEN)

def main():
    parser = argparse.ArgumentParser(description = "Github repo scraper",
            usage = "gitscrape.py num_of_days_back_to_search keywords"
    )
    parser.add_argument("--num", help="Number of days back to search", type=int)
    parser.add_argument("--search", help="Comma separated list of words to search for.", type=str)
    args = parser.parse_args()
    days = args.num
    searchwords = args.search.split(",")
    search_github(searchwords, days)


def search_github(keywords, days):
    date = get_date(days)
    for word in keywords:
        query = '+' + word + '&created:>' + str(date)
        result = git_client.search_repositories(query, 'stars', 'desc')
        print(f'Found {result.totalCount} repo(s) for {word}')
        clone_repos(result, word)


def get_date(days):
    date = datetime.date.today()-datetime.timedelta(days)
    return date


def clone_repos(results, word):
    repos = [repo for repo in results]
    for repo in repos:
        try:
            name = urlparse(str(repo.clone_url)).path.split('/')[1]
            print(name + '/' + str(repo.name) + '\t\t\t' + repo.git_url)
            repo_url = repo.git_url
            repo_path = '/opt/scrape/' + word + '/' + name + '/' + str(repo.name)
            pygit2.clone_repository(repo_url, repo_path)
        except Exception as exc:
            print(exc)


if __name__ == '__main__':
    main()

