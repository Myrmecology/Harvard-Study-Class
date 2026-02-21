# 💻 Terminal Commands Quick Reference

Essential command line operations for Unix/Linux/macOS and Windows.

---

## 📁 Navigation & File System

### **Basic Navigation**
```bash
# Print working directory (where am I?)
pwd

# List files and directories
ls                    # Basic list
ls -l                 # Long format (permissions, size, date)
ls -a                 # Show hidden files
ls -lah               # Long, all files, human-readable sizes
ls -R                 # Recursive (show subdirectories)

# Change directory
cd directory_name     # Go to directory
cd ..                 # Go up one level
cd ~                  # Go to home directory
cd /                  # Go to root directory
cd -                  # Go to previous directory

# Create directory
mkdir folder_name
mkdir -p path/to/nested/folder   # Create nested directories

# Remove directory
rmdir folder_name                 # Remove empty directory
rm -r folder_name                 # Remove directory and contents
rm -rf folder_name                # Force remove (DANGEROUS!)
```

### **File Operations**
```bash
# Create file
touch filename.txt                # Create empty file
echo "text" > file.txt            # Create file with content

# Copy files
cp source.txt destination.txt
cp -r source_dir/ dest_dir/       # Copy directory recursively

# Move/Rename files
mv old_name.txt new_name.txt      # Rename
mv file.txt /path/to/destination/ # Move

# Remove files
rm filename.txt                   # Remove file
rm -i file.txt                    # Remove with confirmation
rm *.txt                          # Remove all .txt files

# View file contents
cat file.txt                      # Display entire file
less file.txt                     # View file (scrollable)
head file.txt                     # First 10 lines
head -n 20 file.txt               # First 20 lines
tail file.txt                     # Last 10 lines
tail -f log.txt                   # Follow file (live updates)
```

---

## 🔍 Searching & Finding

### **Find Files**
```bash
# Find by name
find . -name "*.txt"              # Find all .txt files
find /path -name "file.txt"       # Find specific file
find . -type f -name "*.py"       # Find files only
find . -type d -name "folder"     # Find directories only

# Find by size
find . -size +10M                 # Files larger than 10MB
find . -size -1M                  # Files smaller than 1MB

# Find and execute
find . -name "*.txt" -delete      # Find and delete
```

### **Search File Contents**
```bash
# Search for text in files
grep "search_term" file.txt
grep -r "search_term" directory/  # Recursive search
grep -i "search" file.txt         # Case insensitive
grep -n "search" file.txt         # Show line numbers
grep -v "exclude" file.txt        # Invert match (exclude)
grep -c "count" file.txt          # Count matches

# Search multiple files
grep "text" *.txt
```

---

## 📝 Text Processing
```bash
# Word count
wc file.txt                       # Lines, words, characters
wc -l file.txt                    # Count lines only
wc -w file.txt                    # Count words only

# Sort
sort file.txt                     # Sort alphabetically
sort -r file.txt                  # Reverse sort
sort -n file.txt                  # Numerical sort

# Unique lines
uniq file.txt                     # Remove adjacent duplicates
sort file.txt | uniq              # Remove all duplicates

# Cut columns
cut -d',' -f1 file.csv            # First column (CSV)
cut -c1-10 file.txt               # First 10 characters

# Replace text
sed 's/old/new/' file.txt         # Replace first occurrence
sed 's/old/new/g' file.txt        # Replace all occurrences
```

---

## 🔗 Redirection & Pipes
```bash
# Output redirection
command > file.txt                # Overwrite file
command >> file.txt               # Append to file
command 2> error.txt              # Redirect errors
command &> all.txt                # Redirect output and errors

# Input redirection
command < input.txt

# Pipes (chain commands)
ls -l | grep ".txt"               # List only .txt files
cat file.txt | sort | uniq        # Sort and remove duplicates
ps aux | grep python              # Find Python processes
```

---

## 💾 Permissions & Ownership

### **File Permissions**
```bash
# View permissions
ls -l

# Change permissions
chmod 644 file.txt                # rw-r--r--
chmod 755 script.sh               # rwxr-xr-x
chmod +x script.sh                # Add execute permission
chmod -w file.txt                 # Remove write permission

# Permission numbers:
# 4 = read (r)
# 2 = write (w)
# 1 = execute (x)
# 7 = rwx, 6 = rw-, 5 = r-x, 4 = r--
```

### **Ownership**
```bash
# Change owner
sudo chown user file.txt
sudo chown user:group file.txt
sudo chown -R user directory/     # Recursive
```

---

## 🖥️ Process Management
```bash
# List processes
ps                                # Current terminal processes
ps aux                            # All processes
ps aux | grep python              # Find specific process

# Real-time process viewer
top                               # Interactive (press 'q' to quit)
htop                              # Enhanced version (if installed)

# Kill process
kill PID                          # Graceful shutdown
kill -9 PID                       # Force kill
killall process_name              # Kill by name

# Background processes
command &                         # Run in background
jobs                              # List background jobs
fg                                # Bring to foreground
bg                                # Resume in background
```

---

## 🌐 Network Commands
```bash
# Check internet connection
ping google.com
ping -c 4 google.com              # Send 4 packets only

# Download files
curl https://example.com/file     # Display output
curl -O https://example.com/file  # Save file
wget https://example.com/file     # Download file

# Network info
ifconfig                          # Network interfaces (macOS/Linux)
ip addr                           # Network addresses (Linux)
ipconfig                          # Windows

# Check ports
netstat -an | grep LISTEN         # List listening ports
lsof -i :8000                     # Check what's using port 8000
```

---

## 📦 Archives & Compression
```bash
# Create tar archive
tar -cvf archive.tar files/       # Create archive
tar -czvf archive.tar.gz files/   # Create compressed (.gz)
tar -cjvf archive.tar.bz2 files/  # Create compressed (.bz2)

# Extract tar archive
tar -xvf archive.tar              # Extract
tar -xzvf archive.tar.gz          # Extract .gz
tar -xjvf archive.tar.bz2         # Extract .bz2

# Zip files
zip archive.zip file1 file2
zip -r archive.zip directory/     # Recursive

# Unzip files
unzip archive.zip
unzip archive.zip -d directory/   # Extract to directory
```

---

## 🔐 SSH & Remote Access
```bash
# Connect to remote server
ssh user@hostname
ssh user@192.168.1.100
ssh -p 2222 user@host             # Specific port

# Copy files to/from remote
scp file.txt user@host:/path/     # Copy to remote
scp user@host:/path/file.txt .    # Copy from remote
scp -r folder/ user@host:/path/   # Copy directory

# Generate SSH key
ssh-keygen -t rsa -b 4096
ssh-keygen -t ed25519             # Recommended (2026)

# Copy SSH key to server
ssh-copy-id user@host
```

---

## 💡 Useful Shortcuts

### **Command Line Editing**
```
Ctrl + A          # Move to beginning of line
Ctrl + E          # Move to end of line
Ctrl + U          # Delete from cursor to beginning
Ctrl + K          # Delete from cursor to end
Ctrl + W          # Delete word before cursor
Ctrl + L          # Clear screen
Ctrl + R          # Search command history
Ctrl + C          # Cancel current command
Ctrl + D          # Exit terminal
```

### **Navigation**
```
Tab               # Auto-complete
Tab Tab           # Show all possibilities
!!                # Repeat last command
!$                # Last argument of previous command
cd -              # Go to previous directory
```

---

## 📋 System Information
```bash
# System info
uname -a                          # System information
hostname                          # Computer name
uptime                            # System uptime
whoami                            # Current username
date                              # Current date/time

# Disk usage
df -h                             # Disk space (human readable)
du -sh folder/                    # Directory size
du -sh *                          # Size of all items

# Memory usage
free -h                           # RAM usage (Linux)
vm_stat                           # Memory stats (macOS)

# CPU info
lscpu                             # CPU information (Linux)
sysctl -n machdep.cpu.brand_string  # CPU info (macOS)
```

---

## 🐍 Python Specific
```bash
# Python version
python --version
python3 --version

# Run Python file
python script.py
python3 script.py

# Python interactive mode
python
python3

# Install packages
pip install package_name
pip install -r requirements.txt
pip freeze > requirements.txt     # Save installed packages

# Virtual environment
python -m venv venv               # Create venv
source venv/bin/activate          # Activate (macOS/Linux)
venv\Scripts\activate             # Activate (Windows)
deactivate                        # Deactivate
```

---

## 🪟 Windows Specific Commands

### **PowerShell/CMD Equivalents**
```powershell
# Navigation
dir                               # List files (like ls)
cd                                # Change directory
pwd                               # Print working directory

# File operations
copy source dest                  # Copy (like cp)
move source dest                  # Move (like mv)
del file.txt                      # Delete (like rm)
mkdir folder                      # Create directory

# Other
cls                               # Clear screen (like clear)
type file.txt                     # View file (like cat)
find "text" file.txt              # Search (like grep)
tasklist                          # List processes (like ps)
taskkill /PID 1234                # Kill process
```

---

## 🆘 Emergency Commands
```bash
# Find large files
find / -type f -size +100M 2>/dev/null

# Free up disk space
sudo du -sh /* | sort -h          # Find what's using space

# Check what's using a port
lsof -i :8000                     # macOS/Linux
netstat -ano | findstr :8000      # Windows

# Force quit unresponsive program
killall -9 program_name

# Check if command exists
which python
command -v python
```

---

## 📚 Getting Help
```bash
# Command manual
man command                       # Detailed manual
command --help                    # Quick help
command -h                        # Short help

# Search manual
man -k keyword                    # Search for keyword
apropos keyword                   # Same as man -k

# Info pages
info command
```

---

## 🎯 Pro Tips

1. **Use Tab completion** - Save time typing
2. **Use aliases** - Create shortcuts for common commands
3. **Use history** - Press ↑ to recall previous commands
4. **Be careful with `rm -rf`** - Can delete everything!
5. **Use `sudo` wisely** - Only when necessary
6. **Read error messages** - They usually tell you what's wrong

---

## 🔧 Creating Aliases

Add to `~/.bashrc` or `~/.zshrc`:
```bash
alias ll='ls -lah'
alias ..='cd ..'
alias ...='cd ../..'
alias gs='git status'
alias gp='git push'
alias py='python3'
alias venv='python3 -m venv venv && source venv/bin/activate'
```

Then run: `source ~/.bashrc` or restart terminal.

---

**Practice these commands daily to build muscle memory!**

*Updated: February 2026*