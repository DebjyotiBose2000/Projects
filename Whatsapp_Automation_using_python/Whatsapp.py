from selenium import webdriver

driver = webdriver.Chrome(r"C:\Users\Debjyoti\Downloads\chromedriver.exe")
driver.get('https://web.whatsapp.com')
name = input("Enter the Person/Group Name:")
msg=input("Enter the Message:")
count = input("Enter the no. of Times:")
input("Enter any Value after scanning the QR Code")
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]

for i in range(int(count)):
    message.send_keys(msg)
    s = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
    s.click()