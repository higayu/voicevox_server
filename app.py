from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
import uvicorn
import tempfile
from pathlib import Path
from voicevox_core import AccelerationMode, Synthesizer, OpenJtalk

import asyncio

# VOICEVOX Core の初期化
onnxruntime = "/opt/voicevox_setup/voicevox_core/onnxruntime/lib/libvoicevox_onnxruntime.so.1.17.3"
dict_dir = "/opt/voicevox_setup/voicevox_core/dict/open_jtalk_dic_utf_8-1.11"
vvm_path = "/opt/voicevox_setup/voicevox_core/models/vvms/1.vvm"

open_jtalk = OpenJtalk(dict_dir)
synthesizer = Synthesizer(
    AccelerationMode.AUTO,
    open_jtalk
)
synthesizer.load_voice_model(vvm_path)

app = FastAPI()

@app.get("/speak")
async def speak(text: str = Query(...), style_id: int = Query(14)):
    """テキストから音声を合成して WAV を返す"""
    audio_query = synthesizer.create_audio_query(text, style_id)
    wave = synthesizer.synthesis(audio_query, style_id)

    tmp_wav = Path(tempfile.mktemp(suffix=".wav"))
    with open(tmp_wav, "wb") as f:
        f.write(wave)

    return FileResponse(tmp_wav, media_type="audio/wav", filename="output.wav")


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8082, reload=False)
