# 🔀 Git Quick Reference Cheatsheet

Essential Git commands for version control.

---

## 🚀 Setup & Configuration

### **Initial Setup**
```bash
# Set your identity
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Check configuration
git config --list

# Set default editor
git config --global core.editor "code --wait"

# Set default branch name
git config --global init.defaultBranch main
```

### **Initialize Repository**
```bash
# Create new repository
git init

# Clone existing repository
git clone https://github.com/user/repo.git
git clone https://github.com/user/repo.git my-folder
```

---

## 📝 Basic Workflow

### **Check Status**
```bash
# View current status
git status

# Short status
git status -s
```

### **Staging Changes**
```bash
# Stage specific file
git add filename.txt

# Stage all changes
git add .
git add -A

# Stage all files of a type
git add *.py

# Remove from staging (unstage)
git restore --staged filename.txt
git reset filename.txt
```

### **Committing**
```bash
# Commit with message
git commit -m "Your commit message"

# Stage and commit in one step
git commit -am "Message"

# Amend last commit
git commit --amend -m "New message"

# Amend without changing message
git commit --amend --no-edit
```

---

## 📜 Viewing History
```bash
# View commit history
git log

# Compact one-line log
git log --oneline

# View last N commits
git log -n 5

# View with graph
git log --graph --oneline --all

# View changes in commits
git log -p

# View commits by author
git log --author="Name"

# View file history
git log -- filename.txt
```

---

## 🔄 Undoing Changes

### **Discard Changes**
```bash
# Discard changes in working directory
git restore filename.txt
git checkout -- filename.txt

# Discard all changes
git restore .
```

### **Undo Commits**
```bash
# Undo last commit, keep changes staged
git reset --soft HEAD~1

# Undo last commit, keep changes unstaged
git reset HEAD~1
git reset --mixed HEAD~1

# Undo last commit, discard changes (DANGEROUS!)
git reset --hard HEAD~1

# Revert commit (creates new commit)
git revert <commit-hash>
```

---

## 🌿 Branches

### **Create & Switch**
```bash
# List branches
git branch

# Create new branch
git branch feature-name

# Switch to branch
git checkout feature-name
git switch feature-name

# Create and switch in one step
git checkout -b feature-name
git switch -c feature-name

# Delete branch
git branch -d feature-name

# Force delete branch
git branch -D feature-name

# Rename current branch
git branch -m new-name
```

### **Merging**
```bash
# Merge branch into current branch
git merge feature-name

# Merge with no fast-forward
git merge --no-ff feature-name

# Abort merge
git merge --abort
```

---

## 🔗 Remote Repositories

### **Managing Remotes**
```bash
# List remotes
git remote -v

# Add remote
git remote add origin https://github.com/user/repo.git

# Remove remote
git remote remove origin

# Rename remote
git remote rename old-name new-name

# Change remote URL
git remote set-url origin https://new-url.git
```

### **Pushing & Pulling**
```bash
# Push to remote
git push origin main

# Push and set upstream
git push -u origin main

# Push all branches
git push --all

# Pull from remote
git pull origin main

# Fetch without merging
git fetch origin

# Pull with rebase
git pull --rebase origin main
```

---

## 🏷️ Tags
```bash
# List tags
git tag

# Create lightweight tag
git tag v1.0.0

# Create annotated tag
git tag -a v1.0.0 -m "Version 1.0.0"

# Tag specific commit
git tag v1.0.0 <commit-hash>

# Push tag to remote
git push origin v1.0.0

# Push all tags
git push --tags

# Delete tag
git tag -d v1.0.0

# Delete remote tag
git push origin --delete v1.0.0
```

---

## 🔍 Viewing Changes
```bash
# View unstaged changes
git diff

# View staged changes
git diff --staged
git diff --cached

# View changes in specific file
git diff filename.txt

# Compare branches
git diff branch1..branch2

# Compare commits
git diff commit1 commit2
```

---

## 🗂️ Stashing
```bash
# Stash current changes
git stash

# Stash with message
git stash save "Work in progress"

# List stashes
git stash list

# Apply most recent stash
git stash apply

# Apply specific stash
git stash apply stash@{2}

# Apply and remove from stash
git stash pop

# Remove stash
git stash drop stash@{0}

# Clear all stashes
git stash clear

# Show stash contents
git stash show -p stash@{0}
```

---

## 🔧 Useful Commands

### **Clean Working Directory**
```bash
# Show what will be removed
git clean -n

# Remove untracked files
git clean -f

# Remove untracked files and directories
git clean -fd
```

### **Show Specific Commit**
```bash
# Show commit details
git show <commit-hash>

# Show specific file in commit
git show <commit-hash>:path/to/file
```

### **Blame (Who changed what)**
```bash
# Show who changed each line
git blame filename.txt

# Show for specific lines
git blame -L 10,20 filename.txt
```

### **Search**
```bash
# Search in commits
git log --all --grep="search term"

# Search in code
git grep "search term"
```

---

## 🚨 Common Scenarios

### **Fix Last Commit Message**
```bash
git commit --amend -m "Correct message"
```

### **Add Forgotten Files to Last Commit**
```bash
git add forgotten-file.txt
git commit --amend --no-edit
```

### **Undo Last Push (DANGEROUS!)**
```bash
git reset --hard HEAD~1
git push --force origin main
# ⚠️ Only do this if you're sure!
```

### **Sync Fork with Original Repository**
```bash
git remote add upstream https://github.com/original/repo.git
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

### **Create Branch from Specific Commit**
```bash
git checkout -b branch-name <commit-hash>
```

### **Cherry-Pick Commit**
```bash
git cherry-pick <commit-hash>
```

---

## 📋 .gitignore Patterns
```bash
# Ignore specific file
filename.txt

# Ignore all files with extension
*.log

# Ignore directory
node_modules/
__pycache__/

# Ignore files in all directories
**/*.pyc

# Exception (don't ignore)
!important.log

# Ignore files only in root
/config.json

# Comments
# This is a comment
```

---

## 🎯 Best Practices

### **Commit Messages**
```
✅ GOOD:
"Add user authentication feature"
"Fix bug in login validation"
"Update README with installation steps"

❌ BAD:
"Fixed stuff"
"Update"
"asdf"
```

### **Commit Often, Push Regularly**
- Make small, focused commits
- Commit working code
- Push at least daily
- Pull before you push

### **Branch Naming**
```
feature/user-auth
bugfix/login-error
hotfix/critical-bug
docs/update-readme
```

---

## ⚙️ Useful Aliases

Add to `~/.gitconfig`:
```bash
[alias]
    st = status
    co = checkout
    br = branch
    ci = commit
    lg = log --graph --oneline --all
    unstage = reset HEAD --
    last = log -1 HEAD
    visual = log --graph --oneline --decorate --all
```

Use as:
```bash
git st      # Instead of git status
git co main # Instead of git checkout main
```

---

## 🆘 Emergency Commands

### **I committed to wrong branch!**
```bash
git reset HEAD~1           # Undo commit, keep changes
git stash                  # Save changes
git checkout correct-branch
git stash pop             # Apply changes
git commit -m "Message"
```

### **I need to undo everything!**
```bash
git reset --hard origin/main  # Reset to remote state
```

### **Recover deleted commit**
```bash
git reflog                # Find commit hash
git checkout <hash>       # Restore commit
```

---

## 📚 Resources

- [Official Git Documentation](https://git-scm.com/doc)
- [GitHub Git Cheatsheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials)
- [Oh Shit, Git!?!](https://ohshitgit.com/) - Fix common mistakes

---

**Keep this handy while learning Git!**

*Updated: February 2026*