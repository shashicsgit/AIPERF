import uvicorn
from fastapi import FastAPI
from starlette.responses import FileResponse
app = FastAPI()

@app.get("/hello")
def read_root():
    return {"Hello": "World"}

@app.get("/data.json")
async def get_data():
    filename="C:\\Users\\shash\\Downloads\\data.json"
    return FileResponse(filename)

if __name__ == "__main__":
    uvicorn.run("Virtualization:app",host="127.0.0.1",port=8765,log_level="debug",reload=True)