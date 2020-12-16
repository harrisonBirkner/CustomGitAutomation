import os
import time
import subprocess
from selenium import webdriver
from dotenv import load_dotenv

def repoInput():
    envList = ['v', 'c', 'j', 'n']
    newRepoName = input('Repository Name: ')
    repoDesc = input('Repository Description: ')
    envPick = input('Environment ([V]isual Studio, VS [C]ode, intelli[J] or [N]one): ').lower()

    while envPick not in envList:
        envPick = input('Environment (v, c, j or n): ').lower()

    return newRepoName, repoDesc, envPick

def repoCreation(newRepoName, repoDesc):
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
    browser.quit()
    print("Succesfully created repository {}".format(newRepoName))

def main():
    newRepoName, repoDesc, envPick = repoInput()
    repoCreation(newRepoName, repoDesc)
    os.makedirs(path + newRepoName)
    subprocess.Popen([r"C:\\CustomGitAutomation\\GitRepo2Helper.bat", newRepoName, repoDesc, envPick, username, path] , 
                             shell=True)

load_dotenv()
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
path = os.getenv("FILEPATH")

main()