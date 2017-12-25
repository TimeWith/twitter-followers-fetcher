# Install
To install, just download and move the folder to your Desktop.

# Run
## Step 1
Setup your Twitter and Google API developer accounts, in order to acquire security credentials to access the APIs. 
### Twitter API
To setup the Twitter API, you need to create a Twitter Developer account and setup a new Developer App. 
Login with your Twitter Account here: https://apps.twitter.com/

Create a new application here:
![alt-text](https://github.com/adam-p/markdown-here/raw/master/assets/twitter_step_1.png)

Go to the 'Keys and Access Tokens' tab:
![alt-text](https://github.com/adam-p/markdown-here/raw/master/assets/twitter_step_2.png)

Create new Access Tokens:
![alt-text](https://github.com/adam-p/markdown-here/raw/master/assets/twitter_step_3.png)

Keep this page open in your browser, as you will need these tokens to configure your environment when you run the script for the first time.

### Google Sheets API
To setup the Google Sheets API, follow the `Step 1` from this guide, https://developers.google.com/sheets/api/quickstart/python

## Step 2
To run it, open the Terminal (on Mac/Linux) or CMD (on Windows). Navigate to the directory of the code.
### For Mac/Linux
```bash
$ cd ~/Desktop/twitter-followers-fetcher
```
### For Windows
```bash
$ cd C:\Users\< Your Username >\Desktop\twitter-followers-fetcher
```

## Step 3
First time you run the script, it will run the configuration setup to configure your environment. Run the script with the command below,
```bash
$ python run.py
```
After running the script, follow the on-screen instructions to configure your environment. After that the script will ask you to type in the Twitter accounts you want to get the followers from and also the Google Spreadsheet ID to store the results.
