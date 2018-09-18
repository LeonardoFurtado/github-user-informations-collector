"""
Description.

Script that saves information in a CSV file to
multiple pull requests from a repository.
"""
from github import Github
import csv

# Using acess token
g = Github("Your token here")

# Using username and password
# g = Github("user", "password")

repository = "mongodb/mongo"
file_countries = "country.csv"

count = 0
LIMIT = 1000
data = open(r'output.csv', 'a', encoding='utf8')
writer = csv.writer(data)
repo = g.get_repo(repository)


def get_country(city, file):
    """Through the name of the city, find your country."""
    with open(file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            if(city == row[0] or city == row[1] or city == row[2] or
               city == row[3]):
                return row[2]
    return "Undefine"


for repo in repo.get_pulls(state="closed"):
    writer.writerow([repo.user.name, repo.user.login, repo.user.location,
                    repo.user.blog, repo.merged, get_country(str(repo.user.
                     location).split(",")[0].lower(), file_countries)])
    count += 1
    print(count)
    if count == LIMIT:
        break
