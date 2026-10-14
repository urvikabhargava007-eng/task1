class CarModel:

  def __init__(
      self,
      id,
      brand,
      model,
      year,
      color,
      registration_number,
      owner_name,
      email,
      phone,
      city,
      state,
  ):
    self.id = id
    self.brand = brand
    self.model = model
    self.year = year
    self.color = color
    self.registration_number = registration_number
    self.owner_name = owner_name
    self.email = email
    self.phone = phone
    self.city = city
    self.state = state

  def __repr__(self):
    return (
        f"{self.id} - {self.brand} {self.model}]"
    )


data = []

data.append(
    CarModel(
        id=1,
        brand="Hyundai",
        model="Creta",
        year=2023,
        color="Pearl White",
        registration_number="DL 01 AB 1234",
        owner_name="Rahul Sharma",
        email="rahul.sharma@car.in",
        phone="+91 98765 43210",
        city="New Delhi",
        state="Delhi",
    )
)

data.append(
    CarModel(
        id=2,
        brand="Tata",
        model="Nexon",
        year=2022,
        color="Foliage Green",
        registration_number="MH 02 CD 5678",
        owner_name="Priya Verma",
        email="priya.verma@car.in",
        phone="+91 98234 56781",
        city="Mumbai",
        state="Maharashtra",
    )
)

data.append(
    CarModel(
        id=3,
        brand="Maruti Suzuki",
        model="Swift",
        year=2024,
        color="Sizzling Red",
        registration_number="GJ 01 EF 9012",
        owner_name="Amit Singh",
        email="amit.singh@car.in",
        phone="+91 97654 32109",
        city="Ahmedabad",
        state="Gujarat",
    )
)

data.append(
    CarModel(
        id=4,
        brand="Mahindra",
        model="Thar",
        year=2023,
        color="Desert Fury",
        registration_number="RJ 14 GH 3456",
        owner_name="Neha Gupta",
        email="neha.gupta@car.in",
        phone="+91 98456 78901",
        city="Jaipur",
        state="Rajasthan",
    )
)

data.append(
    CarModel(
        id=5,
        brand="Kia",
        model="Seltos",
        year=2022,
        color="Intense Red",
        registration_number="KA 03 IJ 7890",
        owner_name="Vikram Patel",
        email="vikram.patel@car.in",
        phone="+91 98123 45670",
        city="Bengaluru",
        state="Karnataka",
    )
)

data.append(
    CarModel(
        id=6,
        brand="Toyota",
        model="Fortuner",
        year=2024,
        color="Attitude Black",
        registration_number="TN 07 KL 2345",
        owner_name="Anjali Mehta",
        email="anjali.mehta@car.in",
        phone="+91 99087 65432",
        city="Chennai",
        state="Tamil Nadu",
    )
)

data.append(
    CarModel(
        id=7,
        brand="Honda",
        model="City",
        year=2021,
        color="Radiant Red",
        registration_number="MH 12 MN 6789",
        owner_name="Rohan Joshi",
        email="rohan.joshi@car.in",
        phone="+91 97432 10987",
        city="Pune",
        state="Maharashtra",
    )
)

data.append(
    CarModel(
        id=8,
        brand="Tata",
        model="Punch",
        year=2023,
        color="Atomic Orange",
        registration_number="UP 32 OP 4321",
        owner_name="Sneha Kapoor",
        email="sneha.kapoor@car.in",
        phone="+91 98321 09876",
        city="Lucknow",
        state="Uttar Pradesh",
    )
)

data.append(
    CarModel(
        id=9,
        brand="Hyundai",
        model="Venue",
        year=2022,
        color="Fiery Red",
        registration_number="WB 02 QR 8765",
        owner_name="Arjun Malhotra",
        email="arjun.malhotra@car.in",
        phone="+91 96543 21098",
        city="Kolkata",
        state="West Bengal",
    )
)

data.append(
    CarModel(
        id=10,
        brand="MG",
        model="Hector",
        year=2023,
        color="Glaze Red",
        registration_number="TS 08 ST 1357",
        owner_name="Pooja Yadav",
        email="pooja.yadav@car.in",
        phone="+91 93321 87654",
        city="Hyderabad",
        state="Telangana",
    )
)

data.append(
    CarModel(
        id=11,
        brand="Mahindra",
        model="Scorpio-N",
        year=2024,
        color="Dazzling Silver",
        registration_number="KL 07 UV 2468",
        owner_name="Karan Shah",
        email="karan.shah@car.in",
        phone="+91 91234 56789",
        city="Kochi",
        state="Kerala",
    )
)

data.append(
    CarModel(
        id=12,
        brand="Maruti Suzuki",
        model="Baleno",
        year=2022,
        color="Opulent Silver",
        registration_number="BR 01 WX 3690",
        owner_name="Meera Nair",
        email="meera.nair@car.in",
        phone="+91 92345 67890",
        city="Patna",
        state="Bihar",
    )
)

data.append(
    CarModel(
        id=13,
        brand="Volkswagen",
        model="Virtus",
        year=2023,
        color="Carbon Steel Grey",
        registration_number="PB 65 YZ 1122",
        owner_name="Sahil Khan",
        email="sahil.khan@car.in",
        phone="+91 93456 78901",
        city="Chandigarh",
        state="Punjab",
    )
)

data.append(
    CarModel(
        id=14,
        brand="Skoda",
        model="Slavia",
        year=2024,
        color="Crystal Blue",
        registration_number="MP 04 AA 3344",
        owner_name="Isha Agarwal",
        email="isha.agarwal@car.in",
        phone="+91 94567 89012",
        city="Bhopal",
        state="Madhya Pradesh",
    )
)

data.append(
    CarModel(
        id=15,
        brand="Toyota",
        model="Innova Hycross",
        year=2023,
        color="Super White",
        registration_number="KA 04 BB 5566",
        owner_name="Dev Mishra",
        email="dev.mishra@car.in",
        phone="+91 95678 90123",
        city="Bengaluru",
        state="Karnataka",
    )
)

data.append(
    CarModel(
        id=16,
        brand="Tata",
        model="Harrier",
        year=2022,
        color="Sunlit Yellow",
        registration_number="GJ 05 CC 7788",
        owner_name="Aarav Sen",
        email="aarav.sen@car.in",
        phone="+91 96789 01234",
        city="Surat",
        state="Gujarat",
    )
)

data.append(
    CarModel(
        id=17,
        brand="Renault",
        model="Kwid",
        year=2021,
        color="Zanskar Blue",
        registration_number="OD 02 DD 9900",
        owner_name="Divya Roy",
        email="divya.roy@car.in",
        phone="+91 97890 12345",
        city="Bhubaneswar",
        state="Odisha",
    )
)

data.append(
    CarModel(
        id=18,
        brand="Jeep",
        model="Compass",
        year=2023,
        color="Exotica Red",
        registration_number="AP 31 EE 1213",
        owner_name="Manish Kumar",
        email="manish.kumar@car.in",
        phone="+91 98901 23456",
        city="Visakhapatnam",
        state="Andhra Pradesh",
    )
)

data.append(
    CarModel(
        id=19,
        brand="Citroen",
        model="C3",
        year=2024,
        color="Zesty Orange",
        registration_number="MH 31 FF 1415",
        owner_name="Swati Das",
        email="swati.das@car.in",
        phone="+91 99012 34567",
        city="Nagpur",
        state="Maharashtra",
    )
)

data.append(
    CarModel(
        id=20,
        brand="BMW",
        model="X1",
        year=2024,
        color="Alpine White",
        registration_number="KL 01 GG 1617",
        owner_name="Kunal Reddy",
        email="kunal.reddy@car.in",
        phone="+91 90123 45678",
        city="Thiruvananthapuram",
        state="Kerala",
    )
)

from fastapi import FastAPI , status, Response

app = FastAPI()

@app.get("/")
def home():
  return "This is a homepage."

@app.get("/health")
def health():
  return {"status" : "True"}

@app.get("/cars")
def all_cars():
    return {"status": "True" , "data":data ,"message": "Cars list fetched successfully."}
   

@app.get("/car_by_id/{id}")
def car_by_id(id:int, resp:Response):

   for x in data:
     if x.id == id:
       return {"status": "True" , "data":x ,"message": "Car fetched successfully."}
   resp.status_code = status.HTTP_204_NO_CONTENT
   return {"status": "False" ,"message": "Car id not found."}
     

@app.post("/create_car")
def create_car(car_data:dict):
#    {
#            "model":"Compass",
#            "brand":"Maruti Suzuki",
#            "year":2023,
#            "color":"Red",
#            "registration_number":"UP 85 EE 1213",
#            "owner_name":"Manish Kumavat",
#            "email":"manish.kumavat@car.in",
#            "phone":"+91 98901 56756",
#            "city":"Agra",
#            "state":"Uttar Pradesh"
#     }


    if not all([ 
              car_data.get("brand"),
              car_data.get("model"),
              car_data.get("year"),
              car_data.get("color"),
              car_data.get("registration_number"),
              car_data.get("owner_name"),
              car_data.get("email"),
              car_data.get("phone"),
              car_data.get("city"),
              car_data.get("state")
          ]):

          return {"status": False, "message": "You are missing one of the values."}
    
    data.append(
     CarModel(
       id = len(data) + 1,
       brand = car_data["brand"],
       model = car_data["model"],
       year = car_data["year"],
       color = car_data["color"],
       registration_number = car_data["registration_number"],
       owner_name = car_data["owner_name"],
       email = car_data["email"],
       phone = car_data["phone"],
       city = car_data["city"],
       state = car_data["state"],
     )
   )
    return {"status": "True","message": "Car added successfully."}






