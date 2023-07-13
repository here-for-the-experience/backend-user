from fastapi.testclient import TestClient
from ..main import app
from random import randrange

ENDPOINT = "http://127.0.0.1:8000"

client = TestClient(app)

def generate_user() :
    # Generate random user data for testing
    random_number = randrange(1, 100000)
    return {
        "name" : "Fahim Shakil",
        "email": f"test@example{random_number}.com",
        "password": "password123",
        "address" : "Dhaka, Bangladesh",
        "nid" : "583465746538736",
        "verified" : True,
        "phone_number" : "01913235959"
    }


def test_create_user():
    # Test the creation of a new user
    user_data = generate_user()
    response = client.post(ENDPOINT + "/users/create", json = user_data)
    assert response.status_code == 201
    user = response.json()
    assert user["email"] == user_data["email"]
    assert user["id"] != None
    

# def test_update_user():
#     # Test updating a user's password
#     user_data = generate_user()
#     response = client.post(ENDPOINT + "/users/create", json = user_data)
#     # Authenticate the user and obtain an access token
#     token = client.post(ENDPOINT + "/login", data = { "username" : user_data["email"], "password" : user_data["password"] })
#     token = token.json()
#     print(token)
#     assert token["access_token"] != None
#     assert token["token_type"] == "Bearer"
#     # Update the user's password with a new value
#     new_password = "newpassword456"
#     response = client.put("/users/update", data = { "password" : new_password }, headers = { "Authorization" : f"Bearer {token['access_token']}" })
#     assert response.status_code == 201
#     user = response.json()
#     assert user["email"] == user_data["email"]

def test_get_user_profile():
    # Test retrieving a user's profile
    user_data = generate_user()
    response = client.post(ENDPOINT + "/users/create", json = user_data)
    # Authenticate the user and obtain an access token
    token = client.post(ENDPOINT + "/login", data = { "username" : user_data["email"], "password" : user_data["password"] })
    token = token.json()
    # Retrieve the user's profile using the access token
    response = client.get(ENDPOINT + "/users/profile", headers = { "Authorization" : f"Bearer {token['access_token']}" })
    assert response.status_code == 200
    user = response.json()
    assert user["email"] == user_data["email"]
    

def test_user_forgot_password():
    # Test the "forgot password" functionality
    user_data = generate_user()
    response = client.post(ENDPOINT + "/users/create", json = user_data)
    user = response.json()
    response = client.post(ENDPOINT + "/users/forgot", data = { "email" : user["email"] })
    assert response.status_code == 200
    assert response.json()['message'] == 'Verification Code Sent successfully'
    

def test_user_validate():
    # Test validating a user's code
    response = client.post(ENDPOINT + "/users/validate", data = { "code_from_user" : 123 })
    assert response.status_code == 404
    assert response.json()['detail']['message'] == 'Invalid Code Provided'


# def test_cities() :
#     response = client.get(ENDPOINT + "/users/city")
#     assert response.status_code == 200
    
# def test_center() :
#     response = client.get(ENDPOINT + "/users/center")
#     assert response.status_code == 200
    



