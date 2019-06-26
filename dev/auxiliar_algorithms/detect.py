from github import Github
g = Github("88f206d8d9b6090916476014b7596bf8d44cf758")
repo = g.get_repo("laravel/laravel")
resultado = repo.get_pulls(state="closed")
for result in resultado.get_page(85):
    print(result.user.login)
