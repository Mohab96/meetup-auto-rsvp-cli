# Preview

![preview](demo.mp4)

# Introduction

This is a simple CLI tool that can be used to RSVP events from groups the user is a member of automatically. The tool is written in Python and uses Selenium to automate the process of RSVPing events. The tool is designed to be used with Meetup.com, a popular platform for organizing events. The tool can be used to RSVP events from multiple groups at once, saving the user time and effort.

# Installation

- Clone the repository
- Install the required dependencies using `pip install -r requirements.txt`
- Create `.env` and fill it with data as explained in `.env.example`.

# Usage

Everytime you want to RSVP events open the terminal and run this command `python script.py`.

# Important note

- This script works only with accounts that are created using the email and password, accounts created using Google, Facebook, etc. will not work.
- If the user wants to RSVP events from multiple groups not all the groups he joined, he can add the group name in the `GROUPS` list in the `.env` file.

# Automatic Execution

To run the script automatically every 30 minutes, follow these steps:

1. Replace `path\to\your\script.py` in `run_script.bat` file with the actual path to `script.py`.

2. Replace `path\to\your\run_script.bat` in `run_script_silently.vbs` file with the actual path to your `run_script.bat` file.

3. To make this script run at startup, put the `run_script_silently.vbs` file in the Windows startup folder. You can open this folder by pressing `Win+R`, typing `shell:startup`, and hitting `Enter`. Then, just copy `run_script_silently.vbs` file into this folder.
