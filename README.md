# PRODIGY_CS_03
# Password Strength Checker

## Overview

This project is a Python-based password assessment tool that evaluates a password’s strength based on several criteria, including:

- Length
- Presence of uppercase and lowercase letters
- Presence of numbers
- Presence of special characters
- Whether the password appears in a list of common passwords

It provides feedback and suggestions to help users create stronger passwords.

## Features

> - Checks if the password exists in a common_password.txt file (list of weak passwords).
> - Evaluates password based on:

- Minimum length (8 characters recommended)
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters
> - Returns a score from 0 to 5 and a strength label:
- Very Weak
- Weak
- Good
- Strong
> - Gives suggestions for improving the password.
## Project Structure
project/
│
├── password_checker.py      # Main program
├── common_password.txt      # List of common passwords
└── README.md                # Documentation

## How It Works
The user enters a password.
The program:
- Checks if it’s in the list of common passwords.
- Assigns points for meeting security criteria.
- Displays a strength rating and recommendations.
If the password is common, the program advises immediate change.

## Example
```bash
============PASSWORD COMPLEXITY CHECKER=========

Enter your password:
Password123

Weak password - score: 3/5

______Suggestions for your password_________
- Add special characters ($%^&*)

```
## How to Run

Install Python 3.
Place your common_password.txt file in the same directory.
Run:
```bash
python password_checker.py
```
## License
This project is for educational purposes and can be adapted for real-world security checks.

## Author

Developed by **DIAWARA Nana** as a simple Python cryptography project with prodigy infotech.
