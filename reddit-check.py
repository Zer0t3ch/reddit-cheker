#!/usr/bin/python
import traceback as tb
import praw
import sys
import os


version = [ 0, 1 ]


usr_agent = "redditChecker/{0}.{1} by zer0t3ch".format(version[0], version[1])
r = praw.Reddit(user_agent=usr_agent)


if len(sys.argv) > 1:
	com = sys.argv[1]
else:
	print("Missing a command")
	sys.exit(1)


auth_file = "./reddit-auth.creds"
creds = [ ]
with open(auth_file, 'r') as fil:
	for l in fil:
		creds.append(l.strip())
	fil.close()
r.login(creds[0], creds[1])


# TODO: Add unknown command output

####################################################
####################################################

def get_unread():
	msgs = [ ]
	unread_messages = r.get_unread()
	for msg in unread_messages:
		msgs.append(msg)
	return "You have {0} unread messages".format(len(msgs))

##########################

commands = {
	'unread' : get_unread
}

####################################################
####################################################


ret = ""
try:
	ret = commands[com]()
except Exception,e:
	ret = e


print(ret)
