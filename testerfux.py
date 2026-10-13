import requests
import pandas as pd


url = "https://dummyjson.com/products"


response = requests.get(url)
data = response.json()

products = data["products"]


clean_data = []

for index, row in enumerate(products, start=1) :

    clean_row = {
        "id": row["id"],
        "title": row["title"],
        "category": row["category"],
        "price": row["price"],
        "brand":row.get("brand", "unknown")
        }
    clean_data.append(clean_row)

df = pd.DataFrame(clean_data, index=range(1, len(clean_data)+1))

print(df[df["brand"]=="unknown"])