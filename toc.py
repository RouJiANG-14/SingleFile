from github import Github

# Authenticate yourself 
g = Github("yourusername", "yourauthtoken")

# Find your repository and path of README.md
repo=g.get_user().get_repo("your repo")
file = repo.get_contents("README.md")

# The new contents of your README.md
content = "your updated README file contents"

# Update README.md
repo.update_file("README.md", "commit message", content, file.sha)
