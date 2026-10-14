class UserModel:

    def __init__( self, id, name, email, password, role="customer", is_active=True):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.role = role
        self.is_active = is_active

    def __repr__(self):
        return f"{self.id} - {self.name} ({self.email})"

users = [
    (1, "Aarav Sharma", "aarav@example.com", "Aarav@123", "customer", True),
    (2, "Divya Verma", "divya@example.com", "Divya@123", "customer", True),
    (3, "Manish Kumar", "manish@example.com", "Manish@123", "admin", True),
    (4, "Swati Das", "swati@example.com", "Swati@123", "customer", True),
    (5, "Kunal Reddy", "kunal@example.com", "Kunal@123", "seller", True),
    (6, "Tanvi Joshi", "tanvi@example.com", "Tanvi@123", "customer", True),
    (7, "Rajat Verma", "rajat@example.com", "Rajat@123", "customer", False),
    (8, "Nisha Pillai", "nisha@example.com", "Nisha@123", "seller", True),
    (9, "Varun Nair", "varun@example.com", "Varun@123", "customer", True),
    (10, "Deepika Sen", "deepika@example.com", "Deepika@123", "customer", True),
    (11, "Kabir Khan", "kabir@example.com", "Kabir@123", "admin", True),
    (12, "Simran Kaur", "simran@example.com", "Simran@123", "customer", True),
    (13, "Nikhil Rao", "nikhil@example.com", "Nikhil@123", "seller", False),
    (14, "Pooja Das", "poojadas@example.com", "Pooja@123", "customer", True),
    (15, "Akash Iyer", "akash@example.com", "Akash@123", "customer", True),
]

data = []

for u in users:
    data.append(
        UserModel(
            id=u[0],
            name=u[1],
            email=u[2],
            password=u[3],
            role=u[4],
            is_active=u[5]
        )
    )


from fastapi import FastAPI, status, Response, Form

app = FastAPI()

@app.get("/")
def home():
    return "This is homepage."

@app.get("/health")
def health():
    return {"status": True}

@app.get("/users")
def all_data():
    return data


@app.post( "/create" )
def create(response:Response, name:str=Form(), email=Form(), password=Form(), role=Form()):

    if not all([ name, email, password, role ]):
        response.status_code = status.HTTP_409_CONFLICT
        return {"status": False, "message": "Missing Values for one of these mail, name, password or role."}

    if "@" not in email and "." not in email:
        response.status_code = status.HTTP_409_CONFLICT
        return {"status": False, "message": "Invalid Mail ID."}

    data.append(
        UserModel(
            id=len(data) + 1,
            name=name,
            email=email,
            password=password,
            role=role
        )
    )

    return {"status": True, "message": "User Created Done."}


@app.put( "/update" )
def update(response:Response, id:int, name:str=Form(default=None), email=Form(default=""), password=Form(default=None), role=Form(default=None)):

    if "@" not in email and "." not in email and email:
        response.status_code = status.HTTP_409_CONFLICT
        return {"status": False, "message": "Invalid Mail ID."}

    for x in data:
        if x.id == id:
            if name: x.name = name
            if email: x.email = email
            if password: x.password = password
            if role: x.role = role
            return {"status": True, "message": "User Updated Done."}

    response.status_code = status.HTTP_204_NO_CONTENT
    return {"status": False, "message": "Invalid ID."}

@app.delete( "/delete" )
def delete(response:Response, id:int):
    for x in data:
        if x.id == id:
            data.remove(x)
            return {"status": True, "message": "User Deleted Done."}

    response.status_code = status.HTTP_204_NO_CONTENT
    return {"status": False, "message": "Invalid ID."}
