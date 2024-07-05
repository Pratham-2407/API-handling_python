# import requests

# def fetch_random_products_freeapi():
#     url = "https://api.freeapi.app/api/v1/public/randomproducts?page=1&limit=10&inc=category%2Cprice%2Cthumbnail%2Cimages%2Ctitle%2Cid&query=mens-watches"
#     response = requests.get(url)
#     data = response.json()

#     if data["success"] and "data" in data:
#         products = data["data"]["data"]  # Access the list of products within the "data" field
#         for product in products:
#             category = product["category"]
#             price = product["price"]
#             title = product["title"]
#             print(f"Category: {category} \nPrice: {price} \nTitle: {title}\n")
#     else:
#         raise Exception("Failed to fetch product data")

# def main():
#     try:
#         fetch_random_products_freeapi()
#     except Exception as e:
#         print(str(e))

# if __name__ == "__main__":
#     main()


import requests
import random

def fetch_random_product_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomproducts?page=1&limit=10&inc=category%2Cprice%2Cthumbnail%2Cimages%2Ctitle%2Cid&query=mens-watches"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        products = data["data"]["data"]  # Access the list of products within the "data" field
        random_product = random.choice(products)  # Select a random product from the list
        category = random_product["category"]
        price = random_product["price"]
        title = random_product["title"]
        print(f"Category: {category} \nPrice: {price} \nTitle: {title}\n")
    else:
        raise Exception("Failed to fetch product data")

def main():
    try:
        fetch_random_product_freeapi()
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
