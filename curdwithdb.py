# from database import data

# print(data)

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def home():
#     return ("This is a Homepage...")

# @app.get("/users")
# def get_all_users():
#     return data

# @app.get("/users/{id}")
# def get_by_id(id):
#     if id.isdigit()
#       id = int(id)
#     else:
#         return {
#            "status" : False,
#            "message" : "User id not found."
#         }

#     for x in data:




from fastapi import FastAPI

# Initialize FastAPI application
app = FastAPI()


# 1
class ProductModel:

  def __init__(self, id, title, category, price, stock, brand):
    self.id = id
    self.title = title
    self.category = category
    self.price = price
    self.stock = stock
    self.brand = brand

  def __repr__(self):
    return f"{self.id} - {self.title} (₹{self.price})"


# 2. In-Memory Data Store & Initialization
data = []
products = [
    (1, "Wireless Bluetooth Headphones", "Electronics", 2999.00, 45, "Boat"),
    (2, "Ergonomic Office Chair", "Furniture", 8499.00, 12, "Green Soul"),
    (3, "Stainless Steel Water Bottle", "Home & Kitchen", 599.00, 150, "Milton"),
    (4, "Mechanical Gaming Keyboard", "Electronics", 4299.00, 25, "Redragon"),
    (5, "Running Shoes - Men", "Footwear", 2499.00, 30, "Puma"),
    (6, "Smart Fitness Band", "Electronics", 1999.00, 80, "Noise"),
    (7, "Cotton Casual Shirt", "Clothing", 1299.00, 60, "Allen Solly"),
    (8, "Ceramic Coffee Mug Set", "Home & Kitchen", 799.00, 40, "Clay Craft"),
    (9, "4K Ultra HD Smart TV 43-inch", "Electronics", 24999.00, 8, "Xiaomi"),
    (10, "Leather Laptop Backpack", "Bags", 3199.00, 20, "Wildcraft"),
    (11, "Analog Wrist Watch", "Accessories", 1899.00, 35, "Titan"),
    (12, "Non-Stick Cookware Set", "Home & Kitchen", 3499.00, 18, "Prestige"),
    (13, "Wireless Gaming Mouse", "Electronics", 1499.00, 50, "Logitech"),
    (14, "Denim Jeans - Slim Fit", "Clothing", 1999.00, 42, "Levi's"),
    (15, "Noise Cancelling Earbuds", "Electronics", 4999.00, 28, "Realme"),
]

for p in products:
  data.append(
      ProductModel(
          id=p[0],
          title=p[1],
          category=p[2],
          price=p[3],
          stock=p[4],
          brand=p[5],
      )
  )


# --- 3. FastAPI CRUD Endpoints ---


@app.get("/products")
def get_all_products():
  """GET /products: Retrieve all products."""
  return {"total_products": len(data), "products": data}


@app.get("/products/{id}")
def get_product_by_id(id: int):
  """GET /products/{id}: Find a product by its ID."""
  for product in data:
    if product.id == id:
      return {"status": "success", "product": product}

  return {
      "error": "Product not found",
      "status_code": 404,
      "message": f"No product exists with ID {id}",
  }


@app.post("/products/add")
def add_product(title: str, category: str, price: float, stock: int, brand: str):
  """POST /products/add: Create a new product with auto-incremented ID."""
  new_id = len(data) + 1

  new_product = ProductModel(
      id=new_id,
      title=title,
      category=category,
      price=price,
      stock=stock,
      brand=brand,
  )

  data.append(new_product)
  return {
      "message": "Product added successfully!",
      "status_code": 201,
      "product": new_product,
  }


@app.delete("/products/{id}")
def delete_product(id: int):
  """DELETE /products/{id}: Remove a product by ID."""
  for product in data:
    if product.id == id:
      data.remove(product)
      return {
          "message": f"Product with ID {id} has been deleted successfully.",
          "status_code": 200,
      }

  return {
      "error": "Product not found",
      "status_code": 404,
      "message": f"Cannot delete. Product with ID {id} does not exist.",
  }


@app.put("/products/{id}")
def update_product(
    id: int, title: str = None, price: float = None, stock: int = None
):
  """PUT /products/{id}: Update price, stock, or title preserving existing values."""
  for product in data:
    if product.id == id:
      if title is not None:
        product.title = title
      if price is not None:
        product.price = price
      if stock is not None:
        product.stock = stock

      return {
          "message": f"Product with ID {id} updated successfully.",
          "product": product,
      }

  return {
      "error": "Product not found",
      "status_code": 404,
      "message": f"Cannot update. Product with ID {id} does not exist.",
  }

@app.get("/products/category/{category_name}")   
def filter_based_on_category(category_name)  :
   data_to_return = []
   for x in data:
     if x.category == category_name:
       data_to_return.append(x)
   return {"status": True, "message": "Data fetched done." , "data":data_to_return}
