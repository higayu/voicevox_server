# 📂 辞書とモデルの設置手順
## 1. プロジェクトにディレクトリを作成

まず /var/www/voicevox_server 配下に専用フォルダを作ります。

```bash
cd /var/www/voicevox_server
mkdir -p resources/dict
mkdir -p resources/models
```

## 2. OpenJTalk 辞書を配置

VOICEVOX は OpenJTalk の辞書を必要とします。
公式配布先はこちら：
👉 https://downloads.sourceforge.net/open-jtalk/open_jtalk_dic_utf_8-1.11.tar.gz

## ダウンロード & 展開
```bash
cd resources/dict
wget https://downloads.sourceforge.net/open-jtalk/open_jtalk_dic_utf_8-1.11.tar.gz
tar -xvzf open_jtalk_dic_utf_8-1.11.tar.gz
rm open_jtalk_dic_utf_8-1.11.tar.gz
```

## 3. VOICEVOX モデルファイルを配置

ずんだもんなどの .vvm モデルファイルをダウンロードして resources/models に置きます。

## ✅ 正しい入手先

モデルは VOICEVOX Core の GitHub リリースページ から入手できます：
👉 VOICEVOX Core Releases
リリースアーカイブには次のようなファイルが含まれています：
core.zip … 実行バイナリやライブラリ
model.zip … 複数の .vvm モデル（キャラクターごと）

```bash
cd /var/www/voicevox_server/resources/models

# 例：GitHub上の raw への直接リンクを使う
wget https://raw.githubusercontent.com/VOICEVOX/voicevox_vvm/main/vvms/0.vvm

# または、model.zip が提供されている場合
wget https://github.com/VOICEVOX/voicevox_core/releases/download/0.16.0/model-0.16.0.zip
unzip model-0.16.0.zip
rm model-0.16.0.zip
```

```bash
cd /var/www/voicevox_server/resources/models

# 四国めたん
wget https://raw.githubusercontent.com/VOICEVOX/voicevox_vvm/main/vvms/1.vvm

# 春日部つむぎ
wget https://raw.githubusercontent.com/VOICEVOX/voicevox_vvm/main/vvms/2.vvm

# 雨晴はう
wget https://raw.githubusercontent.com/VOICEVOX/voicevox_vvm/main/vvms/3.vvm
```

```bash
cd /var/www/voicevox_server/resources
git clone https://github.com/VOICEVOX/voicevox_vvm.git

mv voicevox_vvm/vvms/*.vvm models/
rm -rf voicevox_vvm
```