from fastapi import APIRouter, HTTPException
from app.database.database import connect_to_database
from app.user.models import User
from app.utils.helper import get_user_status

router = APIRouter()

# Create a new user
@router.post("/")
async def create_user(user: User):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (user.name, user.age))
    conn.commit()
    new_user_id = cursor.lastrowid
    conn.close()
    return {"id": new_user_id, "name": user.name, "age": user.age}

# Get a specific user by ID
@router.get("/{user_id}")
async def read_user(user_id: int):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, age FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user[0], "name": user[1], "age": user[2], "status": get_user_status(user[2])}

# Application logic example
