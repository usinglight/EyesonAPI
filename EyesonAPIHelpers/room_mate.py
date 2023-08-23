# Import required modules
import requests
import sqlite3
import random
import string

# Eyeson API endpoints
CREATE_ROOM_ENDPOINT = 'https://api.eyeson.team/rooms'
GET_ROOM_ENDPOINT = 'https://api.eyeson.team/rooms/{room_id}'
DELETE_ROOM_ENDPOINT = 'https://api.eyeson.team/rooms/{room_id}'

# Database to store generated links and room IDs  
db = sqlite3.connect('links.db')
cursor = db.cursor()

# Function to generate random string for unique links
def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

# Function to create a room if it doesn't exist
# Otherwise, return the existing room ID
def get_or_create_room(link):
    room_id = cursor.execute('SELECT room_id FROM links WHERE link=?', (link,)).fetchone()
    if room_id:
        return room_id[0]
    
    # Create new room
    data = {'name': 'My Room'} 
    headers = {'Authorization': 'API_KEY'}
    response = requests.post(CREATE_ROOM_ENDPOINT, json=data, headers=headers)
    room_id = response.json()['id']
    
    # Store link and room ID mapping
    cursor.execute('INSERT INTO links VALUES(?, ?)', (link, room_id))
    db.commit()
    
    return room_id

# Usage:
# Generate random link
link = generate_random_string(10) 

# Get or create room
room_id = get_or_create_room(link)

# Retrieve room details
response = requests.get(GET_ROOM_ENDPOINT.format(room_id=room_id))

# Delete room after usage
requests.delete(DELETE_ROOM_ENDPOINT.format(room_id=room_id))