# Backend For User Creation and Authentication

A Fastapi backend for Creating, authenticating users and vaccine registration.

## Features

+ Supports OAuth 2.0
+ Unpacks Requests, extracts and verifies OAuth parameters from headers.
+ Supports GET, POST, UPDATE or DELETE request.
+ Written in Python, with minimal dependencies.
+ Using JWT auth token, it can protect other api routes.

## Non-Features
+ There is no usage of refresh tokens.
+ The backend does not provide any built-in user interface or frontend components. It solely focuses on the backend logic and 
  functionality related to user authentication and credential management.
+ The backend does not offer built-in functionality for managing user roles and permissions.

## Building

At first Clone the repository using : 
```
git clone 'url'
```

Backend auth can be built and run in two ways :
1. using your own machine
2. Using Docker

### If you have docker installed in your machine, you can run :
```
docker build -t image-name --build-arg  URL="DATABASE URL" --build-arg SECRET_TOKEN="SECRET TOKEN FOR JWT"  .
```
As soon as the building finishes, you can run :
```
docker run image-name:tag-name 
```
And the application should start running.


### Otherwise, you can install the dependencies at first using 
```
pip install -r requirements.txt
export URL="DATABASE URL"
export SECRET_TOKEN="SECRET TOKEN FOR JWT"
uvicorn app.main:app --reload
```


And the application should start running.

#### If you make some changes in the tables, you should run :
```
alembic revision --autogenerate -m "Revision Version"
alembic upgrade head
```

![image](https://github.com/here-for-the-experience/backend-user/assets/77661612/20d3b956-554c-4138-93bd-685f69fb925b)


## Understanding the Implementation 
  + The **/create** route defines the endpoint for creating a new user. The forgot_password and validate_code endpoints are used to 
  reset a user's password. The **/login** route is used to authenticate a user and generate an access token.
  + The **get_current_user** dependency is used to get the authenticated user from the request context. This dependency is used by the users router to restrict access to certain endpoints to authenticated users.
  + The **utils** module contains utility functions for hashing password, varifying password etc.
  + We have used sqlalchemy ORM to work with the database. The **models** module defines the database models for users and tokens.
  + The **schemas** module defines the schemas for users, tokens requests. The schemas are used to validate the data that is submitted to the endpoints.
  + We have used **alembic** to manage our database schema in a version-controlled way. This means that you can track changes to your schema over time, and easily roll back to a previous version if necessary.

## Usage

**create_access_token** function : 
```
def create_access_token(data : dict) :
    to_encode = data.copy()
    expire_time = datetime.utcnow() + timedelta(minutes = EXPIRATION_TIME)
    to_encode.update({ "exp" : expire_time })
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)
    return encoded_jwt
```

**verify_access_token** function :
```
def verify_access_token(token : str, credentials_exception) :
    try :
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id = payload.get("id")
        if not id :
            raise credentials_exception
        token_data = schemas.TokenData(id = id)
    except JWTError :
        raise credentials_exception
    return token_data
```

**get_current_user** function :
```
def get_current_user(token : str = Depends(oauth2_scheme)) :
    credentials_exception = HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, 
                                          detail = "Could not authenticate user",
                                          headers = { "WWW-authenticate" : "Bearer"}
                                          )
    token_data = verify_access_token(token, credentials_exception)
    
    return token_data
```
These three functions work together to authenticate user, create a jwt access token or decoding the token.

Sqlalchemy model to define the user table is given below :
```
class User(Base) :
    __tablename__ = "user_table"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    role_id = Column(Integer, nullable=False)
    address = Column(String)
    nid = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    verified = Column(Boolean, nullable=False, default=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
```



## Running Tests 
 Run :
```
pytest
```

## Reporting Problems 
You can send us a mail at :
+ iam.reduan@gmail.com
+ Raufun.nazin13@gmail.com
+ shakil.csedu@gmail.com

## Contributors 
+ Alve Reduan
+ Fahim Shakil
