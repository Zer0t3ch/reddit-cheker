#!/usr/bin/python
import praw
import sys
import os

version[0] = 0
version[1] = 1
usr_agent = "redditChecker/{0}.{1} by zer0t3ch".format(version[0], version[1])
reddit = praw.Reddit(user_agent=usr_agent)

com = sys.argv[1]

# TODO: Add credential loading from a file
# TODO: Add message checker command
# TODO: Add unknown command output

print("Not ready for use")
