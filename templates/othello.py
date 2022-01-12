import numpy as np
from numpy.core.fromnumeric import size


class othello:

    def __init__(self):
        # オセロの初期配置
        self.list = np.zeros((8, 8), dtype=int)
        # 1が黒、2が白、0が空白
        self.list[3][3] = 1
        self.list[4][4] = 1
        self.list[3][4] = 2
        self.list[4][3] = 2
        # 1（黒）が先行
        self.player = 1

        # dx[0]とdy[0]、dx[1]とdy[1]が組み合わせになっている
        # ひっくり返すことができるx座標
        self.overturn_x = []
        # ひっくり返すことができるy座標
        self.overturn_y = []
        # Putで検出した座標
        self.put_x = []
        self.put_y = []
        # 連続したパスの回数、2でゲームセット
        self.pa = 0

    # オセロの石が置いてあるマスの座標が来た場合の処理
    def Check(self, x, y):
        # すでに石が置いてある時
        if self.list[y][x] != 0:
            print("ここには置けません")
            return True
        # 来た座標に置いた時、石をひっくり返せるかどうか
        for i in range(len(self.put_x)):
            if self.put_x[i] == x and self.put_y[i] == y:
                print("ここにおけます")
                self.list[y][x] = self.player
                return False
        print("ここに置けません")
        return True

    # 取得した座標にオセロの石を置いたとき、何個ひっくり返せるかの判定
    # 取得された座標はのself.overturn_x、self.overturn_yに格納される
    # 引数はx座標、y座標、プレイヤーの番号
    def Reverce(self, x, y):
        self.overturn_x = []
        self.overturn_y = []
        kensa = [-1, 0, 1]

        # 置いたマスの縦、横、ななめのひっくり返せる石の座標の取得
        # 取得された座標はのself.overturn_x、self.overturn_yに格納される
        for xx in kensa:
            for yy in kensa:
                # xxとyyが置いた石の座標と被ったときの処理を飛ばす
                if xx == 0 and yy == 0:
                    continue
                tmpx = []
                tmpy = []
                takasa = 0
                # 直線の石を調べる
                while(True):
                    takasa += 1
                    # x座標とy座標の石を直線的に探す
                    tyokusen_x = x + (xx * takasa)
                    tyokusen_y = y + (yy * takasa)
                    # rxとryに石はあるのかの判定と、ひっくり返せるかの判定
                    if 0 <= tyokusen_x < 8 and 0 <= tyokusen_y < 8:
                        osero = self.list[int(tyokusen_y)][int(tyokusen_x)]
                        # 自分の石が見つかったとき
                        if osero == self.player:
                            if tmpx != [] and tmpy != []:
                                # print("追加しました")
                                self.overturn_x.append(tmpx)
                                self.overturn_y.append(tmpy)
                                break
                            else:
                                break
                        # 相手の石が見つかったとき
                        elif osero != self.player:
                            if osero == 0:
                                break
                            else:
                                tmpx.append(tyokusen_x)
                                tmpy.append(tyokusen_y)
                    else:
                        break

    # プレイヤーがオセロを置くことができる位置を検出
    # パスする場面かどうかも判断する
    # 検出された座標はself.put_x,self.put_yに置く

    def Put(self):
        self.put_x = []
        self.put_y = []
        for x in range(8):
            for y in range(8):
                # 石が置いてあるマスの場合
                # print(self.list[x][y])
                if self.list[int(y)][int(x)] != 0:
                    continue
                # この座標に置いた場合のひっくり返せる石をさがす
                # print(x,y)
                self.Reverce(x, y)
                if self.overturn_x == [] and self.overturn_y == []:
                    continue
                else:
                    self.put_x.append(x)
                    self.put_y.append(y)

    # 石をひっくり返す動作
    def Overturn(self, x, y):
        # ひっくり返せる座標を取得
        self.Reverce(x, y)
        # x座標とy座標を格納
        xx = self.overturn_x
        yy = self.overturn_y
        # 石をひっくり返す
        for i in range(len(self.overturn_y)):
            for j in range(len(self.overturn_y[i])):
                # print(self.overturn_x[i][j])
                # print(self.overturn_y[i][j])
                self.list[yy[i][j]][xx[i][j]] = self.player
        # プレイヤーの交代
        if self.player == 1:
            self.player = 2
        else:
            self.player = 1

    # パスをする場面かどうか
    def Pass(self):
        # print("pass発動")
        if self.put_x == []:
            self.pa += 1
            if self.pa == 1:
                print(f"{app.player}はパスです")
            if self.player == 1:
                self.player = 2
            else:
                self.player = 1
        else:
            self.pa = 0
    # 勝ち負けの判定

    def WinLose(self):
        black = 0
        white = 0
        for x in range(8):
            for y in range(8):
                if self.list[y][x] == 1:
                    black += 1
                elif self.list[y][x] == 2:
                    white += 1

        if black > white:
            # print("黒の勝ちです")
            print("黒の勝ちです")
        elif white > black:
            print("白の勝ちです")
        else:
            print("同点です")


if __name__ == '__main__':
    app = othello()
    while(True):
        print(app.list)
        print(app.player)
        # app.playerが石を置ける座標を検出する
        app.Put()
        print(app.put_x)
        print(app.put_y)

        # パスかどうかの判断
        app.Pass()
        # パス
        if app.pa == 1:
            continue
        # ゲーム終了
        elif app.pa == 2:
            print("ゲーム終了です")
            app.WinLose()
            break

        print("x座標の入力")
        valx = input()
        print("y座標の入力")
        valy = input()

        # 座標の位置に石を置けるかの判断
        if valx == "" or valy == "":
            continue
        check = app.Check(int(valx), int(valy))
        if check:
            continue

        # 石をひっくり返す
        app.Overturn(int(valx), int(valy))
