<<<<<<< HEAD
$("#tbl1 td").bind('click', function(){
    $tag_td = $(this)[0];
    $tag_tr = $(this).parent()[0];
    console.log("%s, %s", $tag_tr.rowIndex, $tag_td.cellIndex);
    data={"lows":Number($tag_tr.rowIndex),"cols":Number($tag_td.cellIndex)}
    fetch('/action', {method: 'POST', body: data,})
    .then(function (response) {
        response.json().then((data) => {
            for(let i=0;i<64;i++){
                if(data[i].stone==1){
                    document.getElementById(data[i].position).innerHTML="●"
                }else if(data[i].stone==-1){
                    document.getElementById(data[i].position).innerHTML="◯"
                }
            }
        })
    });
});
=======
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
    xhr.open('POST', '.json', true);
    xhr.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
    // フォームに入力した値をリクエストとして設定
    var request = "arg1=" + arg1.value + "&arg2=" + arg2.value;
    xhr.send(request);
}
>>>>>>> main
