from bs4 import BeautifulSoup
import requests

url = "https://boodmo.com/catalog/4328-filters/"

res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")

with open("output.txt", "w", encoding="utf-8") as file:
    # for para in p:
    file.write(soup.prettify() + "\n\n")

# for para in p:
#     print(para)