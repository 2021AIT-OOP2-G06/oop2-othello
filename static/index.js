window.onload = function() {
    // 計算ボタンを押した際の動作を設定

    xhr = new XMLHttpRequest();

    // サーバからのデータ受信を行った際の動作
    xhr.onload = function(e) {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                var answer = document.getElementById('answer');
                answer.value = xhr.responseText;
            }
        }
    };
};

function post() {
    xhr.open('POST', 'calc.php', true);
    xhr.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
    // フォームに入力した値をリクエストとして設定
    var request = "arg1=" + arg1.value + "&arg2=" + arg2.value;
    xhr.send(request);
}