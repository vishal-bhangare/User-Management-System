from Models import UserRegistration, UserProfile, UserLogin, UpdatePassword
from fastapi import FastAPI, HTTPException, Depends
import firebase_admin
from firebase_admin import auth, credentials, firestore
import uvicorn
import pyrebase
import json
from datetime import datetime
from fastapi.requests import Request

app = FastAPI()
cred = credentials.Certificate("./serviceAccountKey.json")
firebase = firebase_admin.initialize_app(cred)
pb = pyrebase.initialize_app(json.load(open('firebase_config.json')))
db = firestore.client()

# Just for testing


@app.get('/hello')
def hello():
    return {"msg": "hello world"}

# User Registration


@app.post("/register")
def register_user(user: UserRegistration):
    try:
        # Create a user with Firebase Authentication
        user_record = auth.create_user(
            email=user.email,
            email_verified=False,
            password=user.password,
        )

        # Store user data in Firestore
        user_data = {
            "username": user.username,
            "email": user.email,
            "full_name": user.full_name,
            "created_at": datetime.now(),
        }
        db.collection("users").document(user_record.uid).set(user_data)

        return {"message": "User registered successfully!"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# User Login


@app.post("/login")
def login_user(data: UserLogin):
    try:
        # Authenticate the user with Firebase Authentication

        user = pb.auth().sign_in_with_email_and_password(data.email, data.password)
        return {"userId": user["localId"], "firebase_token": user['idToken']}
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=400, detail="Invalid email or password")

# Retrieve User Profile


@app.get("/profile")
def get_user_profile(request: Request):
    headers = request.headers
    jwt = headers.get("authorization")
    user = auth.verify_id_token(jwt)
    user_ref = db.collection("users").document(user["uid"])
    user_data = user_ref.get().to_dict()
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")
    return user_data


@app.delete("/profile")
def delete_user_account(request: Request):
    headers = request.headers
    jwt = headers.get("authorization")
    user = auth.verify_id_token(jwt)
    user_ref = db.collection("users").document(user["uid"])
    user_data = user_ref.get().to_dict()
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")
    # Delete the user from Firebase Authentication
    auth.delete_user(user["uid"])
    # Delete the user's profile from Firestore
    user_ref.delete()
    return {"message": "User account deleted successfully!"}


@app.post("/update_password")
async def update_password(data: UpdatePassword, request: Request):
    headers = request.headers
    jwt = headers.get("authorization")
    user = auth.verify_id_token(jwt)
    try:
        # Re-authenticate the user using their current password
        auth.update_user(
            user["uid"],
            password=data.new_password,
        )
        return {"message": "Password updated successfully"}

    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
