#!/usr/bin/python

import sys
import smtplib
import getpass

def smtpc(toaddr,
	  smtp_server="authsmtp.a_too_nice_company.com.tw",
	  username = "thomas@a_too_nice_company.com.tw",
	  fromaddr = "thomas@a_too_nice_company.com.tw",
	  subject = "Please update your weekly report",
	  content = "As Title,\n\nThank you!!\n\nBest Regards,\nThomas#\r\n"):
	print toaddr
	
	msg="Message-ID: <51026060.0000002@a_too_nice_company.com.tw>\r\nReferences: <A22EB7A4-DC36-48D1-A5E7-9C88E9841821@a_too_nice_company.com.tw>\r\nIn-Reply-To: <A22EB7A4-DC36-48D1-A5E7-9C88E9841821@a_too_nice_company.com.tw>\r\nFrom: "+fromaddr+"\r\nTo: "+toaddr+"\r\nSubject: "+subject+"\r\nContent-Type: text/plain; charset=UTF-8; format=flowed\r\nContent-Transfer-Encoding: 8bit\r\n"+content
	to_list = toaddr.split(";")
	      
	server = smtplib.SMTP(smtp_server)
	server.set_debuglevel(1)
	passwd=getpass.getpass('Password:')
	server.login(username, passwd)
	server.sendmail(fromaddr, to_list, msg)
	server.quit()
	

if __name__ == '__main__':
	if len(sys.argv) > 1:
		smtpc(sys.argv[1]+";"+"thomas@a_too_nice_company.com.tw")
