from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.post("/start_server")
def start_server():
    try:
        subprocess.Popen(["java", "-Xmx1024M", "-Xms1024M", "-jar", "minecraft_server.1.17.1.jar", "nogui"])
        return {"status": "Minecraft server started"}
    except Exception as e:
        return {"status": "error", "detail": str(e)}

@app.post("/stop_server")
def stop_server():
    try:
        # Assuming 'stop' command is enough for your Minecraft server
        subprocess.call(["screen", "-S", "minecraft", "-p", "0", "-X", "stuff", "stop^M"])
        return {"status": "Minecraft server stopped"}
    except Exception as e:
        return {"status": "error", "detail": str(e)}

