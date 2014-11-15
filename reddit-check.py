#!/usr/bin/python
from iniparse import INIConfig as ini
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


auth_file = os.path.join(os.path.dirname(__file__), "auth.ini")
creds = ini(open(auth_file))
r.login(creds.reddit['username'], creds.reddit['password'])


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
