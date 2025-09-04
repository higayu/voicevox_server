from fastapi import FastAPI
from fastapi.responses import FileResponse
import tempfile
from pathlib import Path

from voicevox_core.blocking import Onnxruntime, OpenJtalk, Synthesizer, VoiceModelFile

# パス設定
# プロジェクト内の resources を参照するように変更
dict_dir = "resources/dict/open_jtalk_dic_utf_8-1.11"
vvm_path = "resources/models/vvms/1.vvm"   # 四国めたん


# 初期化
onnxruntime = Onnxruntime.load_once()
open_jtalk = OpenJtalk(dict_dir)
synthesizer = Synthesizer(onnxruntime, open_jtalk)

# モデル読み込み
voice_model = VoiceModelFile.open(vvm_path)
synthesizer.load_voice_model(voice_model)

# デフォルトのスタイルID
style_id_default = voice_model.metas[0].styles[0].id

# FastAPI インスタンス
app = FastAPI()

@app.get("/speak")
async def speak(text: str, style_id: int = style_id_default):
    # 音声合成
    wave = synthesizer.synthesize(text, style_id)

    # 一時ファイルに保存
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        Path(tmp.name).write_bytes(wave)
        tmp_path = tmp.name

    return FileResponse(tmp_path, media_type="audio/wav", filename="speech.wav")
