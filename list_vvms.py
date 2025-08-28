from pathlib import Path
from voicevox_core.blocking import Onnxruntime, OpenJtalk, Synthesizer, VoiceModelFile

dict_dir = "/opt/voicevox_setup/voicevox_core/dict/open_jtalk_dic_utf_8-1.11"
vvms_dir = Path("/opt/voicevox_setup/voicevox_core/models/vvms")

onnxruntime = Onnxruntime.load_once()
open_jtalk = OpenJtalk(dict_dir)
synthesizer = Synthesizer(onnxruntime, open_jtalk)

for vvm_file in vvms_dir.glob("*.vvm"):
    voice_model = VoiceModelFile.open(str(vvm_file))
    synthesizer.load_voice_model(voice_model)
    print(f"=== {vvm_file.name} ===")
    for meta in voice_model.metas:
        print(f"キャラ: {meta.name}")
        for style in meta.styles:
            print(f"  スタイル: {style.name} (style_id={style.id})")
