import asyncio
import re
import subprocess
import websockets
#thanks devix7 for this idea.
async def websocket_handler(websocket, path):
    while True:
        message = await websocket.recv()
        print(f"Received message: {message}")
        converted_url = convert_url(message)
        if converted_url:
            print(f"Converted URL: {converted_url}")
            subprocess.run(['termux-open-url', converted_url])
def convert_url(url):
    roblox_pattern = re.compile(r"https://www\.roblox\.com/games/(?P<placeid>\d+)\?privateServerLinkCode=(?P<linkcode>\w+)")
    share_pattern = re.compile(r"https://www\.roblox\.com/share\?code=(?P<accesscode>\w+)&type=Server")
    roblox_match = roblox_pattern.match(url)
    share_match = share_pattern.match(url)
    if roblox_match:
        placeid = roblox_match.group("placeid")
        linkcode = roblox_match.group("linkcode")
        return f"roblox://placeID={placeid}&linkCode={linkcode}"
    elif share_match:
        accesscode = share_match.group("accesscode")
        return f"roblox://accessCode={accesscode}"
    else:
        return None
start_server = websockets.serve(websocket_handler, 'localhost', 1337)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
