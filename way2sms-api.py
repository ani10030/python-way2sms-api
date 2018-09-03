import urllib2
import cookielib

def send_sms(content):
	# content is an array containing phone and message
	# example : content = ['9876543210','Hello, How are you']
	phone = content[0]
	message = content[1]

	print '--> Sending SMS to '+str(phone)
	username = '9876543210'	# This is your username for http://www.way2sms.com/
	passwd = 'password'		# This is your password for http://www.way2sms.com/

	#Adjusting length for SMS
	available_length = 160

	#Shorten SMS message to available length and append [..] at the end
	if len(message) > available_length:
		message = message[0:(available_length-4)]+'[..]'

	print '-- Message --'
	print message

	number = str(phone)
	
	#Logging into the SMS Site
	url = 'http://site24.way2sms.com/Login1.action?'
	data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'
	#For Cookies:
	cj = cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

	# Adding Header detail:
	opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')]

	try:
		usock = opener.open(url, data)
	except:
		return 'ERROR'

	jession_id = str(cj).split('~')[1].split(' ')[0]

	send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
	send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message
	opener.addheaders = [('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]

	try:
		sms_sent_page = opener.open(send_sms_url,send_sms_data)
	except:
		return 'ERROR'

	return 'SUCCESS'

# Send sample SMS #
sms_status = send_sms(['9999999999','Hello. This is a sample message'])
print sms_status