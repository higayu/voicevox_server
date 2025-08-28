from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
import tempfile   # ← 忘れず追加！
import wave
from pathlib import Path
import numpy as np

from voicevox_core.blocking import Onnxruntime, OpenJtalk, Synthesizer, VoiceModelFile

# パス設定
dict_dir = "/opt/voicevox_setup/voicevox_core/dict/open_jtalk_dic_utf_8-1.11"
vvm_path = "/opt/voicevox_setup/voicevox_core/models/vvms/0.vvm"  # 四国めたん＆ずんだもんの vvm

# 初期化
onnxruntime = Onnxruntime.load_once()
open_jtalk = OpenJtalk(dict_dir)
synthesizer = Synthesizer(onnxruntime, open_jtalk)

# モデル読み込み（style_id=3 を固定: ずんだもん ノーマル）
voice_model = VoiceModelFile.open(vvm_path)
synthesizer.load_voice_model(voice_model)
style_id = 3
print(f"固定利用: 四国めたん - style_id={style_id}")

# FastAPI
app = FastAPI()

@app.get("/speak")
async def speak(text: str):
    try:
        wav = synthesizer.tts(text, style_id)

        # 一時ファイルに保存
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
        tmp_path = tmp.name
        tmp.close()

        if isinstance(wav, bytes):
            # そのまま保存
            with open(tmp_path, "wb") as f:
                f.write(wav)
        else:
            # ndarray の場合
            with wave.open(tmp_path, "wb") as wf:
                wf.setnchannels(1)
                wf.setsampwidth(2)
                wf.setframerate(24000)
                wf.writeframes(wav.astype(np.int16).tobytes())

        return FileResponse(tmp_path, media_type="audio/wav", filename="speech.wav")

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
