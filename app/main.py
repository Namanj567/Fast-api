from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Employee API Running"
    }


@app.get("/employees")
def employees():
    return [
        {
            "id":1,
            "name":"Naman",
            "department":"DevOps"
        },
        {
            "id":2,
            "name":"Rahul",
            "department":"Cloud"
        },
        {
                    "id":3,
                    "name":"Priya",
                    "department":"Security"
                },
                {
                                    "id":4,
                                    "name":"Amit",
                                    "department":"Networkin"
                                }
    ]