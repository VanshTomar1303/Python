import requests
import json

url=f"www.themealdb.com/api/json/v1/1/random.php"

r =requests.get(url)
foodDic=json.loads(r.text)

print(f"Food Name={foodDic["meals"]["strMeal"]}")