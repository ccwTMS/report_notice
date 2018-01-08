#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import smtpc

colleagues = {
	'Ale--hiu':0, 'Al--n':0, 'At---d':0, 'Br--e':0, 'C-':0,
	'Ch---tine':0, 'F--d':0, 'He--y':0, 'Ho--rd':0, 'Je--y':0, 'Li-m':0,
	'Mat--ew':0, 'Re--ay':0, 'Te--y':0, 'Ti--a':0, 'T-':0, 'We--e':0
}

mail = {
	'Ale--hiu':"Ale--hiu@a_too_nice_company.com.tw",
	'Al--n':"Al--n@a_too_nice_company.com.tw",
	'At---d':"At---d@a_too_nice_company.com.tw",
	'Br--e':"Br--e@a_too_nice_company.com.tw",
	'C-':"C-@a_too_nice_company.com.tw",
	'Ch---tine':"Ch---tine@a_too_nice_company.com.tw",
	'F--d':"F--d@a_too_nice_company.com.tw",
	'He--y':"He--y@a_too_nice_company.com.tw",
	'Ho--rd':"Ho--rd@a_too_nice_company.com.tw",
	'Je--y':"Je--y@a_too_nice_company.com.tw",
	'Li-m':"Li-m@a_too_nice_company.com.tw",
	'Mat--ew':"Mat--ew@a_too_nice_company.com.tw",
	'Re--ay':"Re--ay@a_too_nice_company.com.tw",
	'Te--y':"Te--y@a_too_nice_company.com.tw",
	'Ti--a':"Ti--a@a_too_nice_company.com.tw",
	'T-':"T-@a_too_nice_company.com.tw",
	'We--e':"We--e@a_too_nice_company.com.tw"
}

date_list = sys.argv[1].split('/')
date_folder = str(date_list[0])+"年"+str(date_list[1][1])+"月/"+str(date_list[1])+str(date_list[2])

target="smbclient -c \"cd "+date_folder+"/Thomas;ls\" //192.168.0.30/Projectstatus -U username%password |awk -F\"_\" '{ print $2 }' |awk -F\".\" '{ print $1 }'"

fd = os.popen(target)
ret = fd.read()
fd.close()

result = ret.split("\n")

for i in result:
	if colleagues.has_key(i) is True:
		colleagues[i]+=1

print "\n%s\n" % colleagues
print "Notify List:"
cnt = 0
for i in colleagues.keys():
	if colleagues[i] == 0:
		print "%s\t:%d, does not update weekly report." % (i,colleagues[i])
		cnt+=1
		if len(sys.argv) >=3 and sys.argv[2] == "-s":
			smtpc.smtpc(mail[i]+";thomas@a_too_nice_company.com.tw")
if cnt:
	print "%d colleagues forgot to update." % cnt
else:
	print "Have no one."
