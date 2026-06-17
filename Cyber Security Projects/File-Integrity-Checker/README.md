# File Integrity Checker

A Python-based cybersecurity project that monitors file integrity using SHA-256 hashing.

## Features

* Generates SHA-256 hashes
* Stores original file hash
* Detects file modifications
* Alerts when file integrity changes

## How to Run

```bash
python file_integrity_checker.py
```

Enter the filename when prompted.

## Example

Original file:

* Hash stored successfully

Modified file:

* WARNING: File has been modified!

## Technologies Used

* Python
* hashlib
