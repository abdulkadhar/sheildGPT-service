# NOTE Dependencies for the fastapi
from typing import Union, List
from fastapi import FastAPI, Response, status
from pydantic import BaseModel


# SECTION Models Section Starts Here
class LoginUserModel(BaseModel):
    userName: str
    password: str


class LoginReturnResponseModel(BaseModel):
    userName: str
    statusMsg: str


class ErrorResponseModel(BaseModel):
    errorMsg: str


#!SECTION

# SECTION UserManagement Data
userData: List[LoginUserModel] = [
    LoginUserModel(userName="testuser1@gmail.com", password="Test@123"),
    LoginUserModel(userName="testuser2@gmail.com", password="Test@123"),
    LoginUserModel(userName="testuser3@gmail.com", password="Test@123"),
    LoginUserModel(userName="testuser4@gmail.com", password="Test@123"),
    LoginUserModel(userName="testuser5@gmail.com", password="Test@123"),
]
#!SECTION


# SECTION Controller
def isUserPresent(loginData: LoginUserModel) -> bool:
    return loginData in userData


#!SECTION


# NOTE Initializing the app
app = FastAPI()


# NOTE - Status Route
@app.get("/")
def read_root():
    return {"status": "The service is running !!!!"}


@app.post("/login")
def login(loginData: LoginUserModel, response: Response):

    isPresent = isUserPresent(loginData)
    if isPresent:
        response.status_code = status.HTTP_202_ACCEPTED
        return LoginReturnResponseModel(
            userName=loginData.userName, statusMsg="Login successfully !!!"
        )
    else:
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return ErrorResponseModel(errorMsg="Either username or password is incorrect")
