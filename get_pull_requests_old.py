import csv
import math
from github import Github

# g = Github("88f206d8d9b6090916476014b7596bf8d44cf758")
g = Github("fc6bddfd45c7809d604739d89a8662847602088a")
data = open(r'ruby.csv', 'a', encoding='utf8')
writer = csv.writer(data)
repo = None
while repo == None:
    try:
        # g = Github("88f206d8d9b6090916476014b7596bf8d44cf758")
        g = Github("fc6bddfd45c7809d604739d89a8662847602088a")
        repo = g.get_repo("ruby/ruby")
    except:
        print(repo)

resultado = repo.get_pulls(state="closed")

def get_pull_requests_data():
    count = 0
    total_pages = math.ceil(resultado.totalCount//30)
    for i in range(total_pages-1, total_pages):
        print(i)
        for result in resultado.get_page(i):
            writer.writerow([result.user.name, result.user.login, result.user.
                            blog, result.merged, result.user.location])
            count += 1

get_pull_requests_data()
