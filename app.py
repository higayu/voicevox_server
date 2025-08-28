from fastapi import FastAPI
from fastapi.responses import FileResponse
import numpy as np
import wave, tempfile

# まず FastAPI インスタンスを生成
app = FastAPI()

# その後でルート定義を書く
@app.get("/speak")
async def speak(text: str, style_id: int):
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    tmp_path = tmp.name
    tmp.close()

    with wave.open(tmp_path, 'w') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(24000)
        wf.writeframes(np.zeros(24000, dtype=np.int16).tobytes())

    return FileResponse(tmp_path, media_type="audio/wav", filename="dummy.wav")
