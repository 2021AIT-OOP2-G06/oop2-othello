$("#tbl1 td").bind('click', function(){
    $tag_td = $(this)[0];
    $tag_tr = $(this).parent()[0];
    console.log("%s, %s", $tag_tr.rowIndex, $tag_td.cellIndex);
    data={"lows":Number($tag_tr.rowIndex),"cols":Number($tag_td.cellIndex)}
    fetch('/url', {method: 'POST', body: data,})
    .then(function (response) {
        response.json().then((data) => {

            /*if (data.error) {
                // エラーの受信
                document.getElementById('notice').innerHTML = data.error
            }*/

            if (data.result) {
                // メッセージの受信

            }
        })
    });
});
