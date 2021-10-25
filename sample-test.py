from threading import Thread
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from concurrent.futures import ThreadPoolExecutor
import os

username = os.getenv("BROWSERSTACK_USERNAME")
access_key = os.getenv("BROWSERSTACK_ACCESS_KEY")
build_name = os.getenv("BROWSERSTACK_BUILD_NAME")
browserstack_local = os.getenv("BROWSERSTACK_LOCAL")
browserstack_local_identifier = os.getenv("BROWSERSTACK_LOCAL_IDENTIFIER")

#Your script will execute on each of the browser, device and OS combinations
caps=[{
      'os_version': '10',
      'os': 'Windows',
      'browser': 'chrome',
      'browser_version': 'latest',
      'name': 'BStack-[Jenkins] Sample Test', # test name
      'build': build_name, # CI/CD job name using BROWSERSTACK_BUILD_NAME env variable
      'browserstack.local': browserstack_local,
      'browserstack.localIdentifier': browserstack_local_identifier,
      'browserstack.user': username,
      'browserstack.key': access_key
      },
      {
      'os_version': '10',
      'os': 'Windows',
      'browser': 'Edge',
      'browser_version': 'latest',
      'name': 'BStack-[Jenkins] Sample Test', # test name
      'build': build_name, # CI/CD job name using BROWSERSTACK_BUILD_NAME env variable
      'browserstack.local': browserstack_local,
      'browserstack.localIdentifier': browserstack_local_identifier,
      'browserstack.user': username,
      'browserstack.key': access_key
      },
      {
      'os_version': 'Big Sur',
      'os': 'OS X',
      'browser': 'Safari',
      'browser_version': 'latest',
      'name': 'BStack-[Jenkins] Sample Test', # test name
      'build': build_name, # CI/CD job name using BROWSERSTACK_BUILD_NAME env variable
      'browserstack.local': browserstack_local,
      'browserstack.localIdentifier': browserstack_local_identifier,
      'browserstack.user': username,
      'browserstack.key': access_key
      },
      {
      'device': 'Samsung Galaxy S20',
      'os_browser': '11.0',
      'real_mobile': 'true',
      'name': 'BStack-[Jenkins] Sample Test', # test name
      'build': build_name, # CI/CD job name using BROWSERSTACK_BUILD_NAME env variable
      'browserstack.local': browserstack_local,
      'browserstack.localIdentifier': browserstack_local_identifier,
      'browserstack.user': username,
      'browserstack.key': access_key
      },
      {
      'device': 'iPhone 12 Pro',
      'os_browser': '14',
      'real_mobile': 'true',
      'name': 'BStack-[Jenkins] Sample Test', # test name
      'build': build_name, # CI/CD job name using BROWSERSTACK_BUILD_NAME env variable
      'browserstack.local': browserstack_local,
      'browserstack.localIdentifier': browserstack_local_identifier,
      'browserstack.user': username,
      'browserstack.key': access_key
}]	 

#run_session function searches for 'BrowserStack' on google.com
def run_session(caps):
  driver = webdriver.Remote(
      command_executor='https://hub-cloud.browserstack.com/wd/hub',
      desired_capabilities=caps)
  driver.get("https://www.google.com")
  if not "Google" in driver.title:
      raise Exception("Unable to load google page!")
  elem = driver.find_element_by_name("q")
  elem.send_keys("BrowserStack")
  elem.submit()
  try:
      WebDriverWait(driver, 5).until(EC.title_contains("BrowserStack"))
      driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Title matched!"}}')
  except TimeoutException:
      driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Title not matched"}}')
  print(driver.title)
  driver.quit()

def testOne(caps):
  driver = webdriver.Remote(
      command_executor='https://hub-cloud.browserstack.com/wd/hub',
      desired_capabilities=caps)
  driver.get("https://bing.com")
  try:
      WebDriverWait(driver, 5).until(EC.title_contains("Bing"))
      driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Title matched!"}}')
  except TimeoutException:
      driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Title not matched"}}'); 
  print(driver.title == "Bing")
  driver.quit()

def testTwo(caps):
  driver = webdriver.Remote(
      command_executor='https://hub-cloud.browserstack.com/wd/hub',
      desired_capabilities=caps)
  driver.get("https://stackoverflow.com/")
  try:
      WebDriverWait(driver, 5).until(EC.title_contains("Python"))
      driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Title matched!"}}')
  except TimeoutException:
      driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Title not matched"}}'); 
  print(driver.title == "Python")
  driver.quit()
  

#The `ThreadPoolExecutor` function takes `max_workers` as an argument which represents the number of threads in threadpool and execute multiple sessions on each of the thread as and when each session completes execution.
with ThreadPoolExecutor(max_workers=2) as executor:
	executor.map(run_session, caps)

with ThreadPoolExecutor(max_workers=2) as executor:
	executor.map(testOne, caps)

with ThreadPoolExecutor(max_workers=2) as executor:
	executor.map(testTwo, caps)
