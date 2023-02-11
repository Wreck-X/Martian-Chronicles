# Martian-Chronicles
This is an application for fetching the mars rover images using the nasa API and emailing them to one or more emails

# Getting started

First install the required libraries

```bash
pip install -r requirements.txt
```

Enable a gmail api for the app at https://developers.google.com/gmail/api/quickstart/python/ and get a credentials.json file and store it in the project directory

For Launching the gui
```bash
python3 Martian_chronicles.py
```

- For sending multiple emails seperate the emails with commas

- Make sure to change the chdir path in buttons.py to your needs for the gui to work

# Features

- Downloading Rover images
- Show the Rover images in the gui
- Emailing Rover Images
- Can select between 3 rovers curiosity,spirit and Opportunity
- Can select a date for the images taken on that earth date
- will provide the images if the said rover has taken images on that earth date
