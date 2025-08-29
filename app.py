from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
import tempfile, wave
from pathlib import Path
import numpy as np

from voicevox_core.blocking import Onnxruntime, OpenJtalk, Synthesizer, VoiceModelFile

# パス設定
dict_dir = "resources/dict/open_jtalk_dic_utf_8-1.11"
vvm_path = "resources/models/0.vvm"

onnxruntime = Onnxruntime.load_once()
open_jtalk = OpenJtalk(dict_dir)
synthesizer = Synthesizer(onnxruntime, open_jtalk)

voice_model = VoiceModelFile.open(vvm_path)
synthesizer.load_voice_model(voice_model)
style_id = 3  # ずんだもんノーマル固定
print(f"固定利用: ずんだもん - style_id={style_id}")

app = FastAPI()

# 📌 HTML / 静的ファイルをマウント
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/speak")
async def speak(text: str):
    try:
        wav = synthesizer.tts(text, style_id)
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
        tmp_path = tmp.name
        tmp.close()

        if isinstance(wav, bytes):
            with open(tmp_path, "wb") as f:
                f.write(wav)
        else:
            with wave.open(tmp_path, "wb") as wf:
                wf.setnchannels(1)
                wf.setsampwidth(2)
                wf.setframerate(24000)
                wf.writeframes(wav.astype(np.int16).tobytes())

        return FileResponse(tmp_path, media_type="audio/wav", filename="speech.wav")

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.get("/speak2")
async def speak_v2(text: str):
    try:
        wav: np.ndarray = synthesizer.tts(text, style_id)

        # 一時ファイルに保存
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
        tmp_path = tmp.name
        tmp.close()

        # ndarray → PCM16 WAV 書き込み
        with wave.open(tmp_path, "wb") as wf:
            wf.setnchannels(1)          # モノラル
            wf.setsampwidth(2)          # 16bit PCM
            wf.setframerate(24000)      # サンプリングレート
            wf.writeframes((wav * 32767).astype(np.int16).tobytes())

        return FileResponse(tmp_path, media_type="audio/wav", filename="speech.wav")

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
