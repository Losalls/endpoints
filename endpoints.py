from fastapi import FastAPI
from starlette.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()
app.mount("/html", StaticFiles(directory="html"))

@app.get("/housevop")
async def housevop():
    return FileResponse('html/housevop.html')

@app.get("/flatsbuy")
async def flatsbuy():
    return FileResponse('html/flasbuy.html')

@app.get("/integradev")
async def integradev():
    return FileResponse('html/integradev.html')

@app.get("/laslesvpn")
async def laslesvpn():
    return FileResponse('html/laslesvpn.html')

@app.get("/marketika")
async def marketika():
    return FileResponse('html/marketika.html')

@app.get("/metallolom")
async def metallolom():
    return FileResponse('html/metallolom.html')

@app.get("/ovoshi")
async def ovoshi():
    return FileResponse('html/ovoshi.html')

@app.get("/wd")
async def wd():
    return FileResponse('html/wd.html')

@app.get("/yaustalpisatprogrammi")
async def yaustalpisatprogrammi():
    return FileResponse('html/yaustalpisatprogrammi.html')

@app.get("/yoklmn")
async def yoklmn():
    return FileResponse('html/yoklmn.html')

@app.get("/zapisnamrt")
async def zapisnamrt():
    return FileResponse('html/zapisnamrt.html')

uvicorn.run(app)