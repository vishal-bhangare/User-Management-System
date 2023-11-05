Here's a comprehensive documentation for your FastAPI code:

# FastAPI Firebase Authentication API Documentation

This documentation provides an overview of the FastAPI-based API that integrates with Firebase for user registration, login, profile retrieval, account deletion, and password updates. The API exposes the following endpoints:

1. **Hello World Endpoint**

   - Endpoint: `/hello`
   - HTTP Method: GET
   - Description: A simple endpoint to test the API.
   - Response: A JSON response with a greeting message.

```python
{
    "msg": "hello world"
}
```

2. **User Registration Endpoint**

   - Endpoint: `/register`
   - HTTP Method: POST
   - Description: Register a new user by creating a Firebase Authentication user and storing user data in Firestore.
   - Request Data: A JSON object containing user registration data (see `UserRegistration` model in your code).
   - Response: A JSON response indicating the success or failure of the registration process.

```python
{
    "message": "User registered successfully!"
}
```

3. **User Login Endpoint**

   - Endpoint: `/login`
   - HTTP Method: POST
   - Description: Authenticate a user with Firebase Authentication using their email and password.
   - Request Data: A JSON object containing user login data (see `UserLogin` model in your code).
   - Response: A JSON response with the user's Firebase UID and ID token.

```python
{
    "userId": "user_uid",
    "firebase_token": "user_id_token"
}
```

4. **Retrieve User Profile Endpoint**

   - Endpoint: `/profile`
   - HTTP Method: GET
   - Description: Retrieve a user's profile information from Firestore using a valid JWT token.
   - Request Header: The `Authorization` header should contain a valid Firebase ID token.
   - Response: A JSON response with the user's profile information, including username, email, full name, and creation date.

```python
{
    "username": "user_username",
    "email": "user_email",
    "full_name": "user_full_name",
    "created_at": "user_creation_date"
}
```

5. **Delete User Account Endpoint**

   - Endpoint: `/profile`
   - HTTP Method: DELETE
   - Description: Delete a user's Firebase Authentication account and their profile data from Firestore.
   - Request Header: The `Authorization` header should contain a valid Firebase ID token.
   - Response: A JSON response indicating the successful deletion of the user's account.

```python
{
    "message": "User account deleted successfully!"
}
```

6. **Update Password Endpoint**

   - Endpoint: `/update_password`
   - HTTP Method: POST
   - Description: Update a user's password after re-authentication.
   - Request Data: A JSON object containing the new password (see `UpdatePassword` model in your code).
   - Request Header: The `Authorization` header should contain a valid Firebase ID token.
   - Response: A JSON response indicating the success or failure of the password update process.

```python
{
    "message": "Password updated successfully"
}
```

Please ensure that you have the necessary Firebase configurations and service account key files in place to use this API.

To run the API, execute the following command:

```bash
uvicorn your_script_name:app --host 127.0.0.1 --port 8000
```

Replace `your_script_name` with the name of the Python script where your code is located.
