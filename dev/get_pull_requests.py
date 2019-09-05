#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Leonardo Furtado"
__contact__ = "leonardofurtado@ieee.org"

import csv
import requests
import math
import time
from github import Github

# meu 53b800d95851420a05584f980bbe7d652461963a
# bot f5a0f7085200659632626e8ef5f0c5c769ba2032
g = Github("53b800d95851420a05584f980bbe7d652461963a")
output_file = open(r"../data/bases/spyder.csv", "a", encoding="utf8")
writer = csv.writer(output_file)
writer.writerow(
    [
        "login",
        "name",
        "email",
        "bio",
        "company",
        "blog",
        "location",
        "merged",
        "merged_by",
        "orgs",
    ]
)


def get_user_orgs(user):
    orgs = []
    for org in g.get_user(user).get_orgs():
        orgs.append(org.login)

    return orgs


def get_merged_by(user):
    if user:
        return user.login

    return None


def check_rate_limiting():
    g = Github("53b800d95851420a05584f980bbe7d652461963a")
    print(g.rate_limiting[0])
    while g.rate_limiting[0] < 10:
        print("sleeping, rate limit:", g.rate_limiting[0])
        time.sleep(600)
        g = Github("53b800d95851420a05584f980bbe7d652461963a")


def get_pull_requests_data(repository):
    repository = g.get_repo(repository)
    pulls = repository.get_pulls(state="closed")
    total_pages = math.ceil(pulls.totalCount // 30)
    for i in range(0, total_pages + 1):
        print(f"total: {total_pages}, page: {i}")
        for pull in pulls.get_page(i):
            try:
                check_rate_limiting()
                if pull.user.location != None:
                    writer.writerow(
                        [
                            pull.id,
                            pull.user.login,
                            pull.user.name,
                            pull.user.email,
                            pull.user.bio,
                            pull.user.company,
                            pull.user.blog,
                            pull.user.location,
                            pull.merged,
                            get_merged_by(pull.merged_by),
                            get_user_orgs(pull.user.login),
                        ]
                    )
            except requests.exceptions.HTTPError as error:
                print("requests.exceptions.HTTPError")
            except requests.exceptions.ConnectionError as error:
                print("requests.exceptions.ConnectionError")
            except requests.exceptions.Timeout as error:
                print("requests.exceptions.Timeout")
            except requests.exceptions.RequestException as error:
                print("requests.exceptions.RequestException")
            except github.GithubException.GithubException as error:
                print("github.GithubException.GithubException")
            except requests.exceptions.ReadTimeout as error:
                print("requests.exceptions.ReadTimeout")


get_pull_requests_data("spyder-ide/spyder")
