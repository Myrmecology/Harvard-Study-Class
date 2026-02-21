# 🔀 Git Workflow Guide

Practical guide for using Git in real projects and collaborative environments.

---

## 🚀 Basic Daily Workflow

### **Start Your Day**
```bash
# 1. Pull latest changes
git pull origin main

# 2. Create feature branch
git checkout -b feature/your-feature-name

# 3. Start coding!
```

### **During Development**
```bash
# Check what changed
git status

# Stage changes
git add filename.txt
git add .                 # All files

# Commit frequently (small, logical commits)
git commit -m "Add user validation"

# Continue working...
git add .
git commit -m "Fix validation edge case"
```

### **End of Session**
```bash
# Push your branch
git push origin feature/your-feature-name

# Or set upstream on first push
git push -u origin feature/your-feature-name
```

---

## 🌿 Branching Strategy

### **Common Branch Types**
```
main (or master)     → Production-ready code
develop              → Integration branch
feature/feature-name → New features
bugfix/bug-name      → Bug fixes
hotfix/fix-name      → Urgent production fixes
release/v1.0.0       → Release preparation
```

### **Creating Branches**
```bash
# Feature branch from main
git checkout main
git pull
git checkout -b feature/user-authentication

# Bugfix branch
git checkout -b bugfix/login-error

# Release branch
git checkout -b release/v1.0.0
```

---

## 🔄 Merging Workflow

### **Method 1: Merge (Preserves History)**
```bash
# Switch to target branch
git checkout main

# Merge feature branch
git merge feature/user-authentication

# Push
git push origin main

# Delete feature branch
git branch -d feature/user-authentication
git push origin --delete feature/user-authentication
```

### **Method 2: Rebase (Linear History)**
```bash
# On feature branch
git checkout feature/user-authentication

# Rebase on main
git rebase main

# Resolve conflicts if any, then:
git add .
git rebase --continue

# Force push (rebase rewrites history)
git push --force origin feature/user-authentication
```

### **When to Use What?**
- **Merge**: Collaborative branches, preserve complete history
- **Rebase**: Personal branches, clean linear history

---

## 🔧 Handling Conflicts

### **Conflict Occurs**
```bash
# During merge
git merge feature/other-branch
# CONFLICT (content): Merge conflict in file.txt

# View conflicted files
git status
```

### **Resolving Conflicts**
```bash
# 1. Open conflicted file in editor
# Look for conflict markers:

<<<<<<< HEAD
Your changes
=======
Their changes
>>>>>>> feature/other-branch

# 2. Edit file to resolve conflict (remove markers)

# 3. Stage resolved file
git add file.txt

# 4. Complete merge
git commit
```

### **Abort if Needed**
```bash
# Cancel merge
git merge --abort

# Cancel rebase
git rebase --abort
```

---

## 📝 Commit Message Best Practices

### **Good Format**
```
[Type]: Brief description (50 chars max)

Optional detailed explanation (wrap at 72 chars).
Explain what and why, not how.

- Bullet points if needed
- Reference issue: Fixes #123
```

### **Commit Types**
```
feat:     New feature
fix:      Bug fix
docs:     Documentation changes
style:    Formatting, no code change
refactor: Code restructure, no feature change
test:     Adding tests
chore:    Maintenance tasks
```

### **Examples**
```bash
git commit -m "feat: Add user authentication with JWT"

git commit -m "fix: Resolve null pointer in login validation

- Check for empty username before processing
- Add unit tests for edge cases
- Fixes #42"

git commit -m "docs: Update README with installation steps"
```

---

## 🔙 Undoing Changes

### **Before Commit**
```bash
# Discard changes in working directory
git restore file.txt
git checkout -- file.txt

# Unstage file (keep changes)
git restore --staged file.txt
git reset HEAD file.txt

# Discard all changes
git restore .
```

### **After Commit (Local)**
```bash
# Undo last commit, keep changes staged
git reset --soft HEAD~1

# Undo last commit, keep changes unstaged
git reset HEAD~1

# Undo last commit, discard changes (CAREFUL!)
git reset --hard HEAD~1

# Amend last commit
git commit --amend -m "New message"
```

### **After Push (Remote)**
```bash
# Create new commit that undoes changes
git revert <commit-hash>
git push origin main

# Force push (DANGEROUS - rewrites history)
git reset --hard HEAD~1
git push --force origin main
# ⚠️ Only on personal branches!
```

---

## 🗂️ Stashing Workflow

### **Save Work in Progress**
```bash
# Stash current changes
git stash

# Stash with descriptive message
git stash save "WIP: working on feature X"

# Include untracked files
git stash -u
```

### **Retrieve Stashed Work**
```bash
# List stashes
git stash list

# Apply most recent stash (keep in stash)
git stash apply

# Apply specific stash
git stash apply stash@{2}

# Apply and remove from stash
git stash pop

# Drop stash
git stash drop stash@{0}
```

### **Use Case Example**
```bash
# Working on feature
git add .
git stash save "Half-done feature implementation"

# Switch to fix urgent bug
git checkout main
git checkout -b hotfix/urgent-bug
# Fix bug, commit, push

# Return to feature
git checkout feature/my-feature
git stash pop
# Continue working
```

---

## 🏷️ Tagging Releases

### **Create Tags**
```bash
# Lightweight tag
git tag v1.0.0

# Annotated tag (recommended)
git tag -a v1.0.0 -m "Release version 1.0.0"

# Tag specific commit
git tag -a v1.0.0 <commit-hash> -m "Release 1.0.0"
```

### **Push Tags**
```bash
# Push single tag
git push origin v1.0.0

# Push all tags
git push --tags
```

### **List and Delete**
```bash
# List tags
git tag
git tag -l "v1.*"

# Delete local tag
git tag -d v1.0.0

# Delete remote tag
git push origin --delete v1.0.0
```

---

## 👥 Collaborative Workflow

### **Pull Request (PR) Process**
```bash
# 1. Create feature branch
git checkout -b feature/new-feature

# 2. Make changes and commit
git add .
git commit -m "feat: Add new feature"

# 3. Push to remote
git push -u origin feature/new-feature

# 4. Create Pull Request on GitHub/GitLab
# 5. Team reviews code
# 6. Make requested changes
git add .
git commit -m "Address review comments"
git push

# 7. Once approved, merge via web interface
# 8. Delete branch locally
git checkout main
git pull
git branch -d feature/new-feature
```

### **Code Review Tips**
- Keep PRs small and focused
- Write clear PR descriptions
- Respond to feedback constructively
- Test before requesting review

---

## 🔍 Useful Commands

### **View History**
```bash
# Compact log
git log --oneline --graph --all

# Changes in last 5 commits
git log -n 5 -p

# Who changed what
git blame file.txt

# Search commits
git log --grep="bug fix"

# File history
git log --follow file.txt
```

### **Comparing Changes**
```bash
# Unstaged changes
git diff

# Staged changes
git diff --staged

# Between branches
git diff main..feature/branch

# Changes in specific file
git diff file.txt

# Changes between commits
git diff commit1 commit2
```

### **Cleaning Up**
```bash
# Remove untracked files (dry run)
git clean -n

# Remove untracked files
git clean -f

# Remove untracked files and directories
git clean -fd

# Prune remote-tracking branches
git remote prune origin

# Delete merged branches
git branch --merged | grep -v "\*" | xargs -n 1 git branch -d
```

---

## 🚨 Emergency Scenarios

### **"I Committed to Wrong Branch!"**
```bash
# On wrong branch
git reset HEAD~1          # Undo commit
git stash                 # Save changes

# Switch to correct branch
git checkout correct-branch
git stash pop             # Apply changes
git add .
git commit -m "Message"
```

### **"I Need to Undo a Public Commit!"**
```bash
# Use revert (safe for shared branches)
git revert <commit-hash>
git push origin main
```

### **"I Accidentally Deleted a Branch!"**
```bash
# Find commit hash
git reflog

# Recreate branch
git checkout -b branch-name <commit-hash>
```

### **"I Need to Split a Commit!"**
```bash
# Reset to before commit
git reset HEAD~1

# Stage and commit in parts
git add file1.txt
git commit -m "First part"

git add file2.txt
git commit -m "Second part"
```

---

## 📋 .gitignore Tips

### **Common Patterns**
```bash
# Python
__pycache__/
*.pyc
venv/
.env

# Node.js
node_modules/
package-lock.json

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db

# Project specific
config/secrets.json
logs/
*.log
```

### **After Adding .gitignore**
```bash
# Remove already tracked files
git rm -r --cached .
git add .
git commit -m "Update .gitignore"
```

---

## ✅ Daily Checklist

**Morning:**
- [ ] `git pull origin main`
- [ ] Create/switch to feature branch
- [ ] Check branch: `git branch`

**During Work:**
- [ ] Commit frequently with clear messages
- [ ] `git status` regularly
- [ ] Test before committing

**Before Leaving:**
- [ ] Push your branch
- [ ] Create PR if feature ready
- [ ] Stash WIP if incomplete

---

## 🎯 Best Practices Summary

1. **Commit often** - Small, logical commits
2. **Pull frequently** - Stay synced with team
3. **Branch for everything** - Don't work on main
4. **Write clear messages** - Future you will thank you
5. **Review before pushing** - `git diff --staged`
6. **Test before committing** - Don't break builds
7. **Use .gitignore** - Don't commit secrets/build files
8. **Communicate** - Let team know about major changes

---

**Practice these workflows to build Git mastery!**

*Last updated: February 2026*