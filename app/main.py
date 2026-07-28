from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "\n Employee API Running succesfully"
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
                
    ]