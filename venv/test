import urllib.request
from bs4 import BeautifulSoup
userUrl = input("Enter Url: ")
webUrl  = urllib.request.urlopen(userUrl)
soup = BeautifulSoup(webUrl.read())
for script in soup(["script", "style","li", "nav"]): #You need to extract this <script> and <style> tags
    script.extract() #strip them off
print(soup.get_text('\n'))

