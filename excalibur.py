import os

import requests


def list_repos():
    # lists all public repositories within a user profile (does not require github token)
    request = requests.get(f'https://api.github.com/users/{username}/repos')
    response = request.json()

    for i in range(len(response)):
        print(response[i]['name'])
        # print(response[i]['svn_url'])


def renamer():
    # changes author info and committer info (requires github token)
    repo = input('Enter a repository you would like to change the author information:\n')
    new_name = input('Enter the new author name (You can also enter the username):\n')
    new_email = input('Enter the new email address:\n')

    os.system(f"git clone --bare https://github.com/{username}/{repo}.git &> /dev/null")

    os.system(f"""cd {repo}.git
                git filter-branch --env-filter '
                export GIT_COMMITTER_NAME="{new_name}"
                export GIT_COMMITTER_EMAIL="{new_email}"
                export GIT_AUTHOR_NAME="{new_name}"
                export GIT_AUTHOR_EMAIL="{new_email}"
                '
                git push --force --tags origin 'refs/heads/*'
                cd {repo}.git
                cd ../
                rm -rf {repo}.git
                """)


if __name__ == '__main__':
    username = input('Enter your GitHub username:\n')
    renamer()
