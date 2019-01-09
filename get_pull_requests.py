import csv
import math
from github import Github

g = Github("token")
output_file = open(r'cpython.csv', 'a', encoding='utf8')
writer = csv.writer(output_file)
repository = g.get_repo("python/cpython")

result = repository.get_pulls(state="closed")

def get_pull_requests_data():
    page = math.ceil(result.totalCount//30)
    for i in range(0, page):
        print(i)
        for k in result.get_page(i):
            writer.writerow([k.user.name, k.user.login, k.user.blog, k.merged, k.user.location])


get_pull_requests_data()
