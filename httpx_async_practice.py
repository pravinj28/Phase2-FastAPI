import asyncio
import httpx
from starlette.background import BackgroundTask
from starlette.responses import StreamingResponse


#async def main():
    #async with httpx.AsyncClient() as client:
        #r = await client.get("https://www.example.com/")
        #print(r)
        #print(r.status_code)
        #print(r.text[:200])   # First 200 characters


#asyncio.run(main())

#For situations when context block usage is not practical, 
#it is possible to enter "manual mode" by sending a Request instance using client.send(..., stream=True).

#Example in the context of forwarding the response to a streaming web endpoint with Starlette:


#client = httpx.AsyncClient()

#async def home(request):
    #req = client.build_request("GET", "https://www.example.com")
    #r = await client.send(req, stream=True)
    #return StreamingResponse(r.aiter_text(), background= BackgroundTask(r.close))

async def fetch_github(username):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://api.github.com/users/{username}")
        return response.json()
    
async def main():
    data = await fetch_github("pravinj28")
    print(data["name"])
    print(data["public_repos"])

asyncio.run(main())