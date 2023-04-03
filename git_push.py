import git

# replace the placeholders with your own values
repo_path = r"C:\WINDOWS\system32\config\systemprofile\AppData\Local\Jenkins\.jenkins\workspace\cloning"
# repo_path = r""
# repo_path = r""

stash_repo_url = 'https://<vishwa01234>github.com/vishwa01234/backup_jen.git'
# stash_username = 'your_username'
# stash_password = 'your_password'

# open the local repository
repo = git.Repo(repo_path)

# add all changes to the index
repo.git.add('--all')

# commit the changes with a message
commit_message = 'Commit message goes here'
repo.index.commit(commit_message)

# push the changes to the stash repository
remote = repo.remote(name='origin')
remote.push(refspec='HEAD', progress=None)                              #auth=("stash_username", "stash_password"))
