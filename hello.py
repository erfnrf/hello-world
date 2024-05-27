from fastapi import FastAPI

app = FastAPI()

@app.get('/')

def javab():
    return "HelloWorld"

