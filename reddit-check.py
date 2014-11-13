#!/usr/bin/python
import praw
import sys
import os

version[0] = 0
version[1] = 1

usr_agent = "redditChecker/{0}.{1} by zer0t3ch".format(version[0], version[1])
r = praw.Reddit(user_agent=usr_agent)

com = sys.argv[1]
auth_file = "./reddit-auth.creds"
creds = [ ]
with open(auth_file, 'r') as fil:
	for line in xrange(2):
		creds[line] = fil[line].strip()
	fil.close()
r.login(creds[0], creds[1])

# TODO: Add unknown command output

####################################################
####################################################

commands = {
	'unread' : get_unread
}

##########################

def get_unread():
	n = len(r.get_unread())
	return "You have {0} unread messages".format(n)

####################################################
####################################################

commands[com]()
