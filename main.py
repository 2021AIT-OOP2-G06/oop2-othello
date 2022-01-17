from dataclasses import replace
from flask import Flask, request, render_template
from templates.othello import othello
app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # 日本語などのASCII以外の文字列を返したい場合は、こちらを設定しておく
class playothello(othello):
    def __init__(self):
        super().__init__()


# http://127.0.0.1:5000/
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/action', methods = ["POST"])
def action():
    othello_play = othello()
    othello_play.Put()
    othello_play.Pass()
        # パス
    if othello_play.pa == 1:
        othello_play.sendjson
        return "パス"
        # ゲーム終了
    elif othello_play.pa == 2:
        #print("ゲーム終了です")
        #othello_play.WinLose()
        othello_play.sendjson
        return "ゲーム終了"
    #x座標とy座標の取得
    #ここに入力
    zahyou = request.args.get('cell')
    x = 0
    y = 0
    print(f"リクエスト{zahyou}")
    #print(zahyou)

    check = othello_play.Check(int(x), int(y))
    if check:
        othello_play.sendjson
        return "置けない"
        # 石をひっくり返す
    othello_play.Overturn(int(x), int(y))
    othello_play.sendjson
    return "処理完了"

@app.route('/pages/')
def pages():
    return render_template("toppage.html")


if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)
