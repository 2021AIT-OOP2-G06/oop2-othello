import numpy as np
class othello:
    def __init__(self):
        #オセロの初期配置
        self.list = np.zeros((8,8),dtype = int)
        #1が黒、2が白、0が空白
        self.list[3][3] = 1
        self.list[4][4] = 1
        self.list[3][4] = 2
        self.list[4][3] = 2
        # 1（黒）が先行
        self.player = 1

         #dx[0]とdy[0]、dx[1]とdy[1]が組み合わせになっている
        #ひっくり返すことができるx座標
        self.overturn_x = []
        #ひっくり返すことができるy座標
        self.overturn_y = []
        #Putで検出した座標
        self.put_x = []
        self.put_y = []

    #オセロの碑が置いてあるマスの座標が来た場合の処理
    def Check(self,x,y):
        if self.list[x][y] !=0:
            print("ここには置けません")
            return False
        for i in range(len(self.put_x)):
            if self.put_x[i] == x and self.put_y[i] == y:
                print("ここにおけます")
                self.list[x][y] = self.player
                return True
        print("ここに置けません")
        return False

    
    #取得した座標にオセロの石を置いたとき、何個ひっくり返せるかの判定
    #取得された座標はのself.overturn_x、self.overturn_yに格納される
    #引数はx座標、y座標、プレイヤーの番号
    def Reverce(self,x,y):
        self.overturn_x = []
        self.overturn_y = []
        kensa = [-1,0,1]

        #置いたマスの縦、横、ななめのひっくり返せる石の座標の取得
        #取得された座標はのself.overturn_x、self.overturn_yに格納される
        for xx in kensa:
            for yy in kensa:
                #xxとyyが置いた石の座標と被ったときの処理を飛ばす
                if xx ==0 and yy == 0:
                    continue
                tmpx = []
                tmpy = []
                takasa = 0
                #直線の石を調べる
                while(True):
                    takasa += 1
                    #x座標とy座標の石を直線的に探す
                    tyokusen_x = x + (xx * takasa)
                    tyokusen_y = y + (yy * takasa)
                    #rxとryに石はあるのかの判定と、ひっくり返せるかの判定
                    if 0 <= tyokusen_x < 8 and 0 <= tyokusen_y <8:
                        osero = self.list[int(tyokusen_x)][int(tyokusen_y)]
                        #自分の石が見つかったとき
                        if osero == self.player:
                            if tmpx != [] and tmpy != []:
                                #print("追加しました")
                                self.overturn_x.append(tmpx)
                                self.overturn_y.append(tmpy)
                        #相手の石が見つかったとき
                        elif osero != self.player:
                            if osero == 0:
                                break
                            else:
                                tmpx.append(tyokusen_x)
                                tmpy.append(tyokusen_y)
                    else:
                        break


        

    
    #プレイヤーがオセロを置くことができる位置を検出
    #パスする場面かどうかも判断する
    #検出された座標はself.put_x,self.put_yに置く
    def Put(self):
        self.put_x = []
        self.put_y = []
        #パスした回数 2回連続でゲームセット
        pa = 0
        #print(self.list)
        for x in range(8):
            for y in range(8):
                #石が置いてあるマスの場合
                #print(self.list[x][y])
                if self.list[int(x)][int(y)] != 0:
                    continue
                #この座標に置いた場合のひっくり返せる石をさがす
                #print(x,y)
                self.Reverce(x,y)
                if  self.overturn_x == [] and self.overturn_y == []:
                    continue
                else:
                    self.put_x.append(x)
                    self.put_y.append(y)

    #石をひっくり返す動作
    def Overturn (self,x,y):
        self.Reverce(x,y)
        #print(self.overturn_x[0])
        #print(self.overturn_y[0])
        #for i in range(len(self.overturn_x)):
            #xx =self.overturn_x[0]
            #yy = self.overturn_y[0]
            #print(xx,yy)
            #print(len(self.list))
            #self.list[xx][yy] = player
            #print(i)
        xx = self.overturn_x[0]
        yy = self.overturn_y[0]
        print(type(xx))
        print(xx,yy)
        print(x)
        #print(self.list[xx][yy])
        #self.list[3][4] = self.player
        self.list[xx][yy] = self.player
        #if player == 1:
            #player = 2
        #else :
            #player = 1

    #パスをする場面かどうか
    def Pass(self):
        pa =0
        if self.overturn_x == []:
            pa += 1
        else :
            pa = 0
    #勝ち負けの判定

        


                

        




if __name__ == '__main__':
    #マスに対応する２次元リストを生成
    #list = np.zeros((8,8),dtype = int)
    #list[3][3] = 1
    #list[4][4] = 1
    #list[3][4] = 2
    #list[4][3] = 2
    app = othello()
    print(app.list)
    app.Put()
    print(app.put_x)
    print(app.put_y)
    #print(app.overturn_y)
    print("x座標の入力")
    valx = input()
    print("y座標の入力")
    valy = input()
    app.Check(int(valx),int(valy))
    app.Overturn(int(valx),int(valy))
    print(app.list)
    #app.Reverce(int(valx),int(valy),app.player)
    #print(app.overturn_x)
    #print(app.overturn_y)

    #while(True):
        #valx = input()
        #valy = input()
        #print(list)