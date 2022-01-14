window.onload = function() {
    // 石置いた動作
    document.getElementById('put_stone').onclick = function() {
        post();
    };
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
    // 石を置いた時の動作
    xhr.open('POST', 'stone_state.json', true);
    xhr.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
    // 石を置いた座標を取得してJSONとして送信する
    // var i
    var request = ;
    xhr.send(request);
}