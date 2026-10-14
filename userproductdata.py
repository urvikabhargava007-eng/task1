class StudentModel:

    def __init__(self, id, name, email, phone, city, state, password="Password@123"):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.city = city
        self.state = state
        self.password = password

    def __repr__(self):
        return f"User({self.id}): {self.name}"


class ProductModel:

    def __init__(self, id, title, category, price, stock, brand):
        self.id = id
        self.title = title
        self.category = category
        self.price = price
        self.stock = stock
        self.brand = brand

    def __repr__(self):
        return f"Product({self.id}): {self.title} - ₹{self.price}"

class OrderModel:

    def __init__(self, id, user_id, product_id, quantity, payment_mode="UPI", status="COMPLETED"):
        self.id = id
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity
        self.payment_mode = payment_mode
        self.status = status

    def __repr__(self):
        return f"Order({self.id}): User {self.user_id} bought Product {self.product_id} (Qty: {self.quantity})"


# DATA DUMP


users_data = [
    StudentModel(1, "Sneha Gupta", "sneha.gupta@student.in", "+91 98987 65432", "Bengaluru", "Karnataka"),
    StudentModel(2, "Rahul Verma", "rahul.verma@student.in", "+91 97123 48765", "Kolkata", "West Bengal"),
    StudentModel(3, "Divya Nair", "divya.nair@student.in", "+91 98555 12345", "Kochi", "Kerala"),
    StudentModel(4, "Amit Joshi", "amit.joshi@student.in", "+91 98222 33445", "Pune", "Maharashtra"),
    StudentModel(5, "Pooja Reddy", "pooja.reddy@student.in", "+91 98888 99000", "Hyderabad", "Telangana"),
]

products_data = [
    ProductModel(101, "Smart LED TV 32-inch", "Electronics", 18999.00, 15, "Samsung"),
    ProductModel(102, "Wooden Dining Table", "Furniture", 12999.00, 5, "Hometown"),
    ProductModel(103, "Electric Kettle 1.5L", "Home & Kitchen", 1299.00, 45, "Prestige"),
    ProductModel(104, "Wireless Mouse", "Electronics", 799.00, 60, "Dell"),
    ProductModel(105, "Casual Canvas Shoes", "Footwear", 1499.00, 40, "Bata"),
]

orders_data = [
    OrderModel(id=1001, user_id=1, product_id=101, quantity=1, payment_mode="UPI"),
    OrderModel(id=1002, user_id=1, product_id=103, quantity=2, payment_mode="Credit Card"),
    OrderModel(id=1003, user_id=2, product_id=102, quantity=1, payment_mode="Net Banking"),
    OrderModel(id=1004, user_id=3, product_id=104, quantity=1, payment_mode="UPI"),
    OrderModel(id=1005, user_id=3, product_id=105, quantity=1, payment_mode="COD"),
    OrderModel(id=1006, user_id=5, product_id=101, quantity=2, payment_mode="UPI"),
]