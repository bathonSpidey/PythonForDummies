from typing import Union
from routes.api import router
from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

"""
Task 1: If you currently run this file and open 0.0.0.0:8000/docs in your browser, you will have an internal server error in the GET method
Resolve it. Hint: You have to pass a User model in the response model
Task 2: Extend the api with post, put and delete function. Yu have to somehow make a database so that you can keep the entries.
Hint: You might have to dig deeper into FastAPI docs and see something called rules.  
"""
app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    


