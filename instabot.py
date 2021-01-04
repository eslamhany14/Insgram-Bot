from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import random
import string

#comments
comments = [ 'nice ', 'I like it' , 'interesting ', ' hi',   'Oooohh ', 'hacker', ]

posts=0
#Chromedriver path
browser = webdriver.Chrome(executable_path= r"C:\Users\Kareem Yasser\Downloads\chromedriver_win32\chromedriver.exe")  
browser.get(('https://www.instagram.com/accounts/login/?source=auth_switcher'))
sleep(2) 
	
# Likes and Comments the first 4 posts
def likeAndComm(): 
	global posts
	for y in range (1,3):
		for x in range(1,3):
			post = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/div/div['+str(y)+']/div['+str(x)+']') 
			browser.implicitly_wait(1) 
			post.click()
			sleep(2)
			postLike = browser.find_element_by_xpath('//div/span[@class]/*[name()="svg"][@aria-label="Like"]').click() 
			sleep(2)
			print("click1 --> like post")
			sleep(3)
			comment = browser.find_element_by_xpath('//div[@class="QBdPU "]/*[name()="svg"][@aria-label="Comment"]').click() 
			print("click2 --> write comment")
			comment = browser.find_element_by_xpath('//div/form[@class="X7cDz"]/*[name()="textarea"][@aria-label="Add a comment…"]').send_keys(random.choice(comments))	
			print("send1 --> send comment")
			sleep(3)
			sendComment = browser.find_element_by_xpath('//button[@type=\"submit\"]') 
			sendComment.click()
			print("click3 --> close post")
			sleep(4)
			posts+=1
			closePost=browser.find_element_by_xpath('//div[@class="QBdPU "]/*[name()="svg"][@aria-label="Close"]')
			closePost.click()
			sleep(3)
		print ('Nr. of posts: ' +str(posts))
	
	sleep(5)
	browser.get('https://www.instagram.com/')
	
		
def start():
	username = browser.find_element_by_name('username')
	username.send_keys('nogaa463@gmail.com') 
	password = browser.find_element_by_name('password')
	password.send_keys('engyahmed12') 
	nextButton = browser.find_element_by_xpath("//button[@type=\"submit\"]")
	nextButton.click()
	sleep(4)
	notification = browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]")
	notification.click()
	browser.get('https://www.instagram.com/explore/')
	sleep(6)
	likeAndComm() 
	sleep(5)
	

#Run the program.	
start()
