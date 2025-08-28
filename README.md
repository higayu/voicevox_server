# 実装する手順

```bash
sudo apt update
sudo apt install -y build-essential git curl unzip libsndfile1

cd /opt
sudo mkdir -p voicevox_core && cd voicevox_core
pip install https://github.com/VOICEVOX/voicevox_core/releases/download/0.16.1/voicevox_core-0.16.1-cp310-abi3-manylinux_2_34_x86_64.whl

cd /opt
sudo mkdir -p voicevox_setup
cd voicevox_setup

# downloader を取得
sudo curl -sSfL https://github.com/VOICEVOX/voicevox_core/releases/latest/download/download-linux-x64 -o download
sudo chmod +x download

# VOICEVOX Core + dict + onnxruntime をまとめてダウンロード＆展開
sudo ./download
```

```bash
ls -lh /opt/voicevox_setup/voicevox_core
find /opt/voicevox_setup/voicevox_core -name "*.whl"
```

# Rust インストーラー
```bash
# Rust インストーラを取得
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# 完了したら環境変数を読み込み
source $HOME/.cargo/env
```

```bash
# 仮想環境の作成
python3 -m venv venv

source venv/bin/activate
git clone https://github.com/VOICEVOX/voicevox_core.git
cd /home/kali/voicevox_server/voicevox_core/crates/voicevox_core_python_api

cd voicevox_core/crates/voicevox_core_python_api
sudo apt install python3-maturin
maturin develop --release

sudo apt install patchelf
# もしくは
pip install patchelf

export LD_LIBRARY_PATH=/opt/voicevox_setup/voicevox_core/onnxruntime/lib:$LD_LIBRARY_PATH
uvicorn main:app --reload

echo 'export LD_LIBRARY_PATH=/opt/voicevox_setup/voicevox_core/onnxruntime/lib:$LD_LIBRARY_PATH' >> ~/.bashrc
source ~/.bashrc
```

# 使用出来るキャラ
curl "http://192.168.1.221:8082/speak?text=%E3%81%8A%E3%81%AF%E3%82%88%E3%81%86%20%E3%81%94%E3%81%96%E3%81%84%E3%81%BE%E3%81%99&style_id=14" -o test_proxy.wav
```bash
(venv) gym-sever@gym-sever:/var/www/voicevox_server$ python list_vvms.py
=== 21.vvm ===
キャラ: 猫使アル
  スタイル: つよつよ (style_id=110)
  スタイル: へろへろ (style_id=111)
キャラ: 猫使ビィ
  スタイル: つよつよ (style_id=112)
キャラ: 東北ずん子
  スタイル: ノーマル (style_id=107)
キャラ: 東北きりたん
  スタイル: ノーマル (style_id=108)
キャラ: 東北イタコ
  スタイル: ノーマル (style_id=109)
=== 13.vvm ===
キャラ: 春歌ナナ
  スタイル: ノーマル (style_id=54)
キャラ: 猫使アル
  スタイル: ノーマル (style_id=55)
  スタイル: おちつき (style_id=56)
  スタイル: うきうき (style_id=57)
キャラ: 猫使ビィ
  スタイル: ノーマル (style_id=58)
  スタイル: おちつき (style_id=59)
  スタイル: 人見知り (style_id=60)
=== 16.vvm ===
キャラ: 後鬼
  スタイル: 人間（怒り）ver. (style_id=87)
  スタイル: 鬼ver. (style_id=88)
=== 3.vvm ===
キャラ: 波音リツ
  スタイル: ノーマル (style_id=9)
  スタイル: クイーン (style_id=65)
キャラ: 中国うさぎ
  スタイル: ノーマル (style_id=61)
  スタイル: おどろき (style_id=62)
  スタイル: こわがり (style_id=63)
  スタイル: へろへろ (style_id=64)
=== 12.vvm ===
キャラ: †聖騎士 紅桜†
  スタイル: ノーマル (style_id=51)
キャラ: 雀松朱司
  スタイル: ノーマル (style_id=52)
キャラ: 麒ヶ島宗麟
  スタイル: ノーマル (style_id=53)
=== 4.vvm ===
キャラ: 玄野武宏
  スタイル: ノーマル (style_id=11)
キャラ: 剣崎雌雄
  スタイル: ノーマル (style_id=21)
=== 8.vvm ===
キャラ: WhiteCUL
  スタイル: ノーマル (style_id=23)
  スタイル: たのしい (style_id=24)
  スタイル: かなしい (style_id=25)
  スタイル: びえーん (style_id=26)
=== s0.vvm ===
キャラ: 四国めたん
  スタイル: ノーマル (style_id=3002)
  スタイル: あまあま (style_id=3000)
  スタイル: ツンツン (style_id=3006)
  スタイル: セクシー (style_id=3004)
  スタイル: ヒソヒソ (style_id=3037)
キャラ: ずんだもん
  スタイル: ノーマル (style_id=3003)
  スタイル: あまあま (style_id=3001)
  スタイル: ツンツン (style_id=3007)
  スタイル: セクシー (style_id=3005)
  スタイル: ヒソヒソ (style_id=3038)
  スタイル: ヘロヘロ (style_id=3075)
  スタイル: なみだめ (style_id=3076)
キャラ: 春日部つむぎ
  スタイル: ノーマル (style_id=3008)
キャラ: 雨晴はう
  スタイル: ノーマル (style_id=3010)
キャラ: 波音リツ
  スタイル: ノーマル (style_id=3009)
  スタイル: クイーン (style_id=3065)
  スタイル: ノーマル (style_id=6000)
  スタイル: ノーマル (style_id=6000)
キャラ: 玄野武宏
  スタイル: ノーマル (style_id=3011)
  スタイル: 喜び (style_id=3039)
  スタイル: ツンギレ (style_id=3040)
  スタイル: 悲しみ (style_id=3041)
キャラ: 白上虎太郎
  スタイル: ふつう (style_id=3012)
  スタイル: わーい (style_id=3032)
  スタイル: びくびく (style_id=3033)
  スタイル: おこ (style_id=3034)
  スタイル: びえーん (style_id=3035)
キャラ: 青山龍星
  スタイル: ノーマル (style_id=3013)
  スタイル: 熱血 (style_id=3081)
  スタイル: 不機嫌 (style_id=3082)
  スタイル: 喜び (style_id=3083)
  スタイル: しっとり (style_id=3084)
  スタイル: かなしみ (style_id=3085)
キャラ: 冥鳴ひまり
  スタイル: ノーマル (style_id=3014)
キャラ: 九州そら
  スタイル: ノーマル (style_id=3016)
  スタイル: あまあま (style_id=3015)
  スタイル: ツンツン (style_id=3018)
  スタイル: セクシー (style_id=3017)
キャラ: もち子さん
  スタイル: ノーマル (style_id=3020)
  スタイル: セクシー／あん子 (style_id=3066)
  スタイル: 泣き (style_id=3077)
  スタイル: 怒り (style_id=3078)
  スタイル: 喜び (style_id=3079)
  スタイル: のんびり (style_id=3080)
キャラ: 剣崎雌雄
  スタイル: ノーマル (style_id=3021)
キャラ: WhiteCUL
  スタイル: ノーマル (style_id=3023)
  スタイル: たのしい (style_id=3024)
  スタイル: かなしい (style_id=3025)
  スタイル: びえーん (style_id=3026)
キャラ: 後鬼
  スタイル: 人間ver. (style_id=3027)
  スタイル: ぬいぐるみver. (style_id=3028)
キャラ: No.7
  スタイル: ノーマル (style_id=3029)
  スタイル: アナウンス (style_id=3030)
  スタイル: 読み聞かせ (style_id=3031)
キャラ: ちび式じい
  スタイル: ノーマル (style_id=3042)
キャラ: 櫻歌ミコ
  スタイル: ノーマル (style_id=3043)
  スタイル: 第二形態 (style_id=3044)
  スタイル: ロリ (style_id=3045)
キャラ: 小夜/SAYO
  スタイル: ノーマル (style_id=3046)
キャラ: ナースロボ＿タイプＴ
  スタイル: ノーマル (style_id=3047)
  スタイル: 楽々 (style_id=3048)
  スタイル: 恐怖 (style_id=3049)
キャラ: †聖騎士 紅桜†
  スタイル: ノーマル (style_id=3051)
キャラ: 雀松朱司
  スタイル: ノーマル (style_id=3052)
キャラ: 麒ヶ島宗麟
  スタイル: ノーマル (style_id=3053)
キャラ: 春歌ナナ
  スタイル: ノーマル (style_id=3054)
キャラ: 猫使アル
  スタイル: ノーマル (style_id=3055)
  スタイル: おちつき (style_id=3056)
  スタイル: うきうき (style_id=3057)
キャラ: 猫使ビィ
  スタイル: ノーマル (style_id=3058)
  スタイル: おちつき (style_id=3059)
キャラ: 中国うさぎ
  スタイル: ノーマル (style_id=3061)
  スタイル: おどろき (style_id=3062)
  スタイル: こわがり (style_id=3063)
  スタイル: へろへろ (style_id=3064)
キャラ: 栗田まろん
  スタイル: ノーマル (style_id=3067)
キャラ: あいえるたん
  スタイル: ノーマル (style_id=3068)
キャラ: 満別花丸
  スタイル: ノーマル (style_id=3069)
  スタイル: 元気 (style_id=3070)
  スタイル: ささやき (style_id=3071)
  スタイル: ぶりっ子 (style_id=3072)
  スタイル: ボーイ (style_id=3073)
キャラ: 琴詠ニア
  スタイル: ノーマル (style_id=3074)
=== 14.vvm ===
キャラ: 栗田まろん
  スタイル: ノーマル (style_id=67)
キャラ: あいえるたん
  スタイル: ノーマル (style_id=68)
キャラ: 満別花丸
  スタイル: ノーマル (style_id=69)
  スタイル: 元気 (style_id=70)
  スタイル: ささやき (style_id=71)
  スタイル: ぶりっ子 (style_id=72)
  スタイル: ボーイ (style_id=73)
キャラ: 琴詠ニア
  スタイル: ノーマル (style_id=74)
=== 17.vvm ===
キャラ: Voidoll
  スタイル: ノーマル (style_id=89)
=== 2.vvm ===
キャラ: 九州そら
  スタイル: ノーマル (style_id=16)
  スタイル: あまあま (style_id=15)
  スタイル: ツンツン (style_id=18)
  スタイル: セクシー (style_id=17)
=== 5.vvm ===
キャラ: 四国めたん
  スタイル: ささやき (style_id=36)
  スタイル: ヒソヒソ (style_id=37)
キャラ: ずんだもん
  スタイル: ささやき (style_id=22)
  スタイル: ヒソヒソ (style_id=38)
キャラ: 九州そら
  スタイル: ささやき (style_id=19)
=== 0.vvm ===
キャラ: 四国めたん
  スタイル: ノーマル (style_id=2)
  スタイル: あまあま (style_id=0)
  スタイル: ツンツン (style_id=6)
  スタイル: セクシー (style_id=4)
キャラ: ずんだもん
  スタイル: ノーマル (style_id=3)
  スタイル: あまあま (style_id=1)
  スタイル: ツンツン (style_id=7)
  スタイル: セクシー (style_id=5)
キャラ: 春日部つむぎ
  スタイル: ノーマル (style_id=8)
キャラ: 雨晴はう
  スタイル: ノーマル (style_id=10)
=== 20.vvm ===
キャラ: ユーレイちゃん
  スタイル: ノーマル (style_id=102)
  スタイル: 甘々 (style_id=103)
  スタイル: 哀しみ (style_id=104)
  スタイル: ささやき (style_id=105)
  スタイル: ツクモちゃん (style_id=106)
=== 9.vvm ===
キャラ: 白上虎太郎
  スタイル: ふつう (style_id=12)
  スタイル: わーい (style_id=32)
  スタイル: びくびく (style_id=33)
  スタイル: おこ (style_id=34)
  スタイル: びえーん (style_id=35)
=== 11.vvm ===
キャラ: 櫻歌ミコ
  スタイル: ノーマル (style_id=43)
  スタイル: 第二形態 (style_id=44)
  スタイル: ロリ (style_id=45)
キャラ: ナースロボ＿タイプＴ
  スタイル: ノーマル (style_id=47)
  スタイル: 楽々 (style_id=48)
  スタイル: 恐怖 (style_id=49)
  スタイル: 内緒話 (style_id=50)
=== 1.vvm ===
キャラ: 冥鳴ひまり
  スタイル: ノーマル (style_id=14)
=== 19.vvm ===
キャラ: 離途
  スタイル: ノーマル (style_id=99)
  スタイル: シリアス (style_id=101)
キャラ: 黒沢冴白
  スタイル: ノーマル (style_id=100)
=== 15.vvm ===
キャラ: ずんだもん
  スタイル: ヘロヘロ (style_id=75)
  スタイル: なみだめ (style_id=76)
キャラ: 青山龍星
  スタイル: ノーマル (style_id=13)
  スタイル: 熱血 (style_id=81)
  スタイル: 不機嫌 (style_id=82)
  スタイル: 喜び (style_id=83)
  スタイル: しっとり (style_id=84)
  スタイル: かなしみ (style_id=85)
  スタイル: 囁き (style_id=86)
キャラ: もち子さん
  スタイル: ノーマル (style_id=20)
  スタイル: セクシー／あん子 (style_id=66)
  スタイル: 泣き (style_id=77)
  スタイル: 怒り (style_id=78)
  スタイル: 喜び (style_id=79)
  スタイル: のんびり (style_id=80)
キャラ: 小夜/SAYO
  スタイル: ノーマル (style_id=46)
=== 7.vvm ===
キャラ: 後鬼
  スタイル: 人間ver. (style_id=27)
  スタイル: ぬいぐるみver. (style_id=28)
=== 6.vvm ===
キャラ: No.7
  スタイル: ノーマル (style_id=29)
  スタイル: アナウンス (style_id=30)
  スタイル: 読み聞かせ (style_id=31)
=== 18.vvm ===
キャラ: ぞん子
  スタイル: ノーマル (style_id=90)
  スタイル: 低血圧 (style_id=91)
  スタイル: 覚醒 (style_id=92)
  スタイル: 実況風 (style_id=93)
キャラ: 中部つるぎ
  スタイル: ノーマル (style_id=94)
  スタイル: 怒り (style_id=95)
  スタイル: ヒソヒソ (style_id=96)
  スタイル: おどおど (style_id=97)
  スタイル: 絶望と敗北 (style_id=98)
=== 10.vvm ===
キャラ: 玄野武宏
  スタイル: 喜び (style_id=39)
  スタイル: ツンギレ (style_id=40)
  スタイル: 悲しみ (style_id=41)
キャラ: ちび式じい
  スタイル: ノーマル (style_id=42)
(venv) gym-sever@gym-sever:/var/www/voicevox_server$ 
  ```

# html追加する場合
```bash
pip install jinja2
pip install jinja2 python-multipart
```