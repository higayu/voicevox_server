from voicevox_core.blocking import Synthesizer, Onnxruntime, OpenJtalk, VoiceModelFile
import glob

# パス設定
dict_dir = "/opt/voicevox_setup/voicevox_core/dict/open_jtalk_dic_utf_8-1.11"
vvm_dir = "/opt/voicevox_setup/voicevox_core/models/vvms"

# 初期化
onnxruntime = Onnxruntime.load_once()
open_jtalk = OpenJtalk(dict_dir)
synthesizer = Synthesizer(onnxruntime, open_jtalk)

# 全モデルをロード
for vvm_path in glob.glob(f"{vvm_dir}/*.vvm"):
    voice_model = VoiceModelFile.open(vvm_path)
    synthesizer.load_voice_model(voice_model)

# キャラ情報を一覧表示
for meta in synthesizer.metas():
    print("キャラ:", meta.name)
    for style in meta.styles:
        print("  スタイル:", style.name, "→ style_id:", style.id)
