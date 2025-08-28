document.getElementById("tts-form").addEventListener("submit", async function(e) {
    e.preventDefault();

    const text = document.getElementById("text").value;
    const player = document.getElementById("player");

    if (!text) {
        alert("テキストを入力してください");
        return;
    }

    try {
        const response = await fetch(`/voicevox/speak?text=${encodeURIComponent(text)}`);

        if (!response.ok) {
            alert("エラー: " + response.status);
            return;
        }

        const blob = await response.blob();
        const url = URL.createObjectURL(blob);
        player.src = url;
        player.play();
    } catch (err) {
        alert("通信エラー: " + err);
    }
});
