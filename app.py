from fastapi import FastAPI
from fastapi.responses import FileResponse
import tempfile, wave
import numpy as np
from pathlib import Path

from voicevox_core.blocking import Onnxruntime, OpenJtalk, Synthesizer, VoiceModelFile

# ライブラリの初期化
onnxruntime_path = "/opt/voicevox_setup/voicevox_core/onnxruntime/lib/libvoicevox_onnxruntime.so.1.17.3"
dict_dir = "/opt/voicevox_setup/voicevox_core/dict/open_jtalk_dic_utf_8-1.11"
vvm_path = "/opt/voicevox_setup/voicevox_core/models/vvms/1.vvm"

onnxruntime = Onnxruntime.load_once()
open_jtalk = OpenJtalk(dict_dir)
synthesizer = Synthesizer(onnxruntime, open_jtalk)

# モデル読み込み
voice_model = VoiceModelFile.open(vvm_path)
synthesizer.load_voice_model(voice_model)

# FastAPI インスタンス
app = FastAPI()


@app.get("/speak")
async def speak(text: str, style_id: int):
    # 音声合成
    audio_query = synthesizer.create_audio_query(text, style_id)
    wav = synthesizer.synthesis(audio_query)

    # 一時ファイルに保存
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    tmp_path = tmp.name
    tmp.close()

    with wave.open(tmp_path, 'w') as wf:
        wf.setnchannels(1)         # モノラル
        wf.setsampwidth(2)         # 16bit
        wf.setframerate(24000)     # 24kHz
        wf.writeframes(wav.tobytes())

    return FileResponse(tmp_path, media_type="audio/wav", filename="speech.wav")
