from voicevox_core.blocking import Onnxruntime, OpenJtalk, Synthesizer, VoiceModelFile

onnxruntime_path = "/opt/voicevox_setup/voicevox_core/onnxruntime/lib/libvoicevox_onnxruntime.so.1.17.3"
dict_dir = "/opt/voicevox_setup/voicevox_core/dict/open_jtalk_dic_utf_8-1.11"
vvm_path = "/opt/voicevox_setup/voicevox_core/models/vvms/1.vvm"

onnxruntime = Onnxruntime.load_once()
open_jtalk = OpenJtalk(dict_dir)
synthesizer = Synthesizer(onnxruntime, open_jtalk)

voice_model = VoiceModelFile.open(vvm_path)
print("モデル情報:", voice_model.metas)

synthesizer.load_voice_model(voice_model)

# モデル情報から style_id を取得
style_id = voice_model.metas[0].styles[0].id
print("使う style_id:", style_id)

query = synthesizer.create_audio_query("おはようございます", style_id=style_id)
wave = synthesizer.synthesis(query, style_id=style_id)

with open("test.wav", "wb") as f:
    f.write(wave)

print("✅ test.wav を出力しました！")
