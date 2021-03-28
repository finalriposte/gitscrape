#!/usr/bin/env python3
from github import Github
import pygit2
import datetime
import os
from urllib.parse import urlparse

ACCESS_TOKEN = os.environ.get('GITTOKEN')

git_client = Github(ACCESS_TOKEN)

def main():
    searchwords = input('Enter keywords to search for: ')
    searchwords = [searchword.strip() for searchword in searchwords.split(',')]
    results = search_github(searchwords)
    clone_repos(results)


def search_github(keywords):
    date = get_date()
    query = '+'.join(keywords) + '+in:readme+in+description created:>' + str(date)
    print(query)
    result = git_client.search_repositories(query, 'stars', 'desc')
    print(f'Found {result.totalCount} repo(s)')
    return result


def get_date():
    date = datetime.date.today()-datetime.timedelta(365)
    return date


def clone_repos(results):
    repos = []
    for repo in results:
        if repo not in repos:
            repos.append(repo)

    for repo in repos:
        name = urlparse(str(repo.clone_url)).path.split('/')[1]
        #print(name)
        print(name + '/' + str(repo.name) + '\t\t\t' + repo.git_url)
        pygit2.clone_repository(repo.git_url, name + '/' + str(repo.name))


if __name__ == '__main__':
    main()
