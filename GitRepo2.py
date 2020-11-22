import os
import subprocess
from selenium import webdriver
import time

username = 'harrisonBirkner'
password = 'GizkaFruit2402'
newRepoName = input('Repository Name: ')
repoDesc = input('Repository Description: ')

browser = webdriver.Chrome(executable_path='C:/chromedriver.exe')
browser.get('http://github.com/login')

browser.find_elements_by_xpath("//input[@name='login']")[0].send_keys(username)
browser.find_elements_by_xpath("//input[@name='password']")[0].send_keys(password)
browser.find_elements_by_xpath("//input[@name='commit']")[0].click()
browser.find_elements_by_xpath("/html/body/div[4]/div/aside[1]/div[2]/div[1]/div/h2/a")[0].click()
browser.find_element_by_xpath("//input[@id='repository_name']").send_keys(newRepoName)
browser.find_element_by_xpath("//input[@id='repository_description']").send_keys(repoDesc)
browser.find_element_by_xpath("//input[@id='repository_visibility_private']").click()
time.sleep(.5)
browser.find_elements_by_class_name("btn-primary")[0].click()

print("Succesfully created repository {}".format(newRepoName))

item = subprocess.Popen([r"C:\\CustomGitAutomation\\GitRepo2Helper.bat", newRepoName, repoDesc] , 
                         shell=True, stdout=subprocess.PIPE)