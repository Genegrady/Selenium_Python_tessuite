
#Selenium test suite using Python and Browserstack

This test suite has 3 assertions testing the title of several websites across 5 browsers concurrently, then sending this information over to BrowserStack

When running this test, please make sure to have Python installed:

https://www.python.org/downloads/ 

Make sure you can run pip or pip3 commands and they are updated to the latest version:

If pip not installed:

sudo easy_install pip 

Check pip version:

pip --version

Upgrade pip if not up to date:
 sudo pip install --upgrade pip

Next, you will want to install selenium by running the following command:

pip install selenium

Docs:

https://selenium-python.readthedocs.io/installation.html 

This test is run through Jenkins, but can be run with the following command inside of your CLI:

Python3 path/sample-test.py
