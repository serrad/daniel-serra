from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:3000",
]
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Item(BaseModel):
    title: str
    description: str
    address: str
    phone: str
    latitude: float
    longitude: float

@app.get("/")
def read_root():
    
    conn = sqlite3.connect('restos.db')
    if(conn):
        
        #Crée la table restaurant si elle n'existe pas
        cur = conn.cursor()
        listOfTables = cur.execute(
        "SELECT name FROM sqlite_schema WHERE type='table' AND name='restaurant'").fetchall()
        if listOfTables == []:
            conn.execute('''CREATE TABLE restaurant
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                address CHAR(50),
                phone CHAR(50),
                latitude REAL,
                longitude REAL)''')
            
        restaurants = []
        cursor = conn.execute("SELECT id, title, description, address, phone, latitude, longitude FROM restaurant")
        for row in cursor:
            info = "<h1 class='text-xl'><strong>" + row[1] + "</strong></h1><br>" + row[2] + "<br>" + row[3] + "<br>" + row[4]
            restaurants.append({'id' : row[0], 'title' : row[1], 'infoText' : info, 'description' : row[2], 'address' : row[3], 'phone' : row[4], 'position': {'lat' : row[5], 'lng' : row[6]}})
        conn.close()
        return restaurants
    else:
        return {"Hello": "No database"}
        
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    restaurants = []
    conn = sqlite3.connect('restos.db')
    if(conn):
        cursor = conn.execute("SELECT id, title, description, address, phone FROM restaurant WHERE id=" + str(item_id))
        for row in cursor:
            restaurants.append({'id' : row[0], 'title' : row[1], 'description' : row[2], 'address' : row[3], 'phone' : row[4]})
        conn.close()
        if(len(restaurants) > 0):
            return restaurants[0]
        else:
            return {"No results"}   
    else:
        return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    
    conn = sqlite3.connect('restos.db')
    if(conn):
        conn.execute("UPDATE restaurant SET title = ?, description = ?, address = ?, phone = ?, latitude = ?, longitude = ? WHERE id = ?", (item.title, item.description, item.address, item.phone, str(item.latitude), str(item.longitude), item_id))
        conn.commit()
        conn.close()
        return {"Success"}  
    else:
        return {"Error"}

@app.post("/items")
def create_item(item: Item):
    
    conn = sqlite3.connect('restos.db')
    if(conn):
        conn.execute("INSERT INTO restaurant (title, description, address, phone, latitude, longitude) VALUES (?, ?, ?, ?, ?, ?)", (item.title, item.description, item.address, item.phone, str(item.latitude), str(item.longitude)))
        conn.commit()
        conn.close()
        return {"Success"}  
    else:
        return {"Error"}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
   
    conn = sqlite3.connect('restos.db')
    if(conn):
        conn.execute("DELETE FROM restaurant WHERE id=" + str(item_id))
        conn.commit()
        conn.close()
        return {"Success"}  
    else:
        return {"Error"}