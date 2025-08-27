# voicevox_server.py
from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
from pathlib import Path
from voicevox_core import AccelerationMode, Synthesizer
from voicevox_core.open_jtalk import OpenJtalk

import uvicorn

# VOICEVOX Core 初期化
core = VoicevoxCore(
    acceleration_mode=AccelerationMode.AUTO,
    open_jtalk_dict_dir=Path("/opt/voicevox_setup/voicevox_core/dict/open_jtalk_dic_utf_8-1.11")
)

# API サーバ定義
app = FastAPI()

# /speak エンドポイント
@app.get("/speak")
def speak(
    text: str = Query(..., description="読み上げたい文章"),
    style_id: int = Query(14, description="キャラクターのstyle_id（例: 14=冥鳴ひまり ノーマル）")
):
    # 音声クエリ作成
    audio_query = core.audio_query(text, style_id)

    # 音声合成
    wav = core.synthesis(audio_query, style_id)

    # 一時ファイルに保存
    out_file = Path("output.wav")
    with open(out_file, "wb") as f:
        f.write(wav)

    return FileResponse(out_file, media_type="audio/wav", filename="output.wav")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8082)
