# 0: null
# 1: white
# 2: black

#grid 8x8

from tabnanny import check


grid = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 2, 0, 0, 0],
        [0, 0, 0, 2, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]

def selectCell(row,col,player):
    #ひっくり返せる石があるか確認、なければ何も置かずreturn
    check = Check(col,row,player)
    if(check):
        return "NG"

    if ((player==1) and (grid[row][col]==0)):
        grid[row][col] = 1
            #isValid(row, col,player)
        Overturn(col,row,player)
            #print(grid)
        #return "OK"
    elif((player==2) and (grid[row][col]==0)):
        grid[row][col] = 2
        Overturn(col,row,player)
            #isValid(row, col,player)
            #print(grid)
        #return "OK"
    #else:
        #return "ok"
    if player == 1:
        yer = 2
    else :
        yer = 1

    pas = Put(yer)
    if(pas):
        return "PASS"
    else :
        return "OK"

    # 石をひっくり返す動作
def Overturn(x,y,player):
    # ひっくり返せる座標を取得
    #self.Reverce(x, y)
    overturn_x = []
    overturn_y = []
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
                    osero = grid[int(tyokusen_y)][int(tyokusen_x)]
                    # 自分の石が見つかったとき
                    if osero == player:
                        if tmpx != [] and tmpy != []:
                            # print("追加しました")
                            overturn_x.append(tmpx)
                            overturn_y.append(tmpy)
                            break
                        else:
                            break
                        # 相手の石が見つかったとき
                    elif osero != player:
                        if osero == 0:
                            break
                        else:
                            tmpx.append(tyokusen_x)
                            tmpy.append(tyokusen_y)
                else:
                    break
        # x座標とy座標を格納
    xx = overturn_x
    yy = overturn_y
        # 石をひっくり返す
    for i in range(len(overturn_y)):
        for j in range(len(overturn_y[i])):
                # print(self.overturn_x[i][j])
                # print(self.overturn_y[i][j])
            grid[yy[i][j]][xx[i][j]] = player
    print(overturn_x)
    print(overturn_y)
        # プレイヤーの交代
        #if player == 1:
            #player = 2
        #else:
            #player = 1
def Check( x, y, player):
    # すでに石が置いてある時
    if grid[y][x] != 0:
        #print("ここには置けません")
        return True

    overturn_x = []
    overturn_y = []
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
                    osero = grid[int(tyokusen_y)][int(tyokusen_x)]
                        # 自分の石が見つかったとき
                    if osero == player:
                        if tmpx != [] and tmpy != []:
                                # print("追加しました")
                            overturn_x.append(tmpx)
                            overturn_y.append(tmpy)
                            break
                        else:
                            break
                        # 相手の石が見つかったとき
                    elif osero != player:
                        if osero == 0:
                            break
                        else:
                            tmpx.append(tyokusen_x)
                            tmpy.append(tyokusen_y)
                else:
                    break
        
        # 来た座標に置いた時、石をひっくり返せるかどうか
    for i in range(len(overturn_x)):
        if overturn_x[i] != 0:
            #print("ここにおけます")
            #grid[y][x] = player
            return False
    #print("ここに置けません")
    return True

def Put(player):
    put_x = []
    put_y = []
    for x in range(8):
        for y in range(8):
                # 石が置いてあるマスの場合
                # print(self.list[x][y])
            if grid[int(y)][int(x)] != 0:
                continue
                # この座標に置いた場合のひっくり返せる石をさがす
                # print(x,y)
                #self.Reverce(x, y)
            overturn_x = []
            overturn_y = []
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
                            osero = grid[int(tyokusen_y)][int(tyokusen_x)]
                        # 自分の石が見つかったとき
                            if osero == player:
                                if tmpx != [] and tmpy != []:
                                # print("追加しました")
                                    overturn_x.append(tmpx)
                                    overturn_y.append(tmpy)
                                    break
                                else:
                                    break
                        # 相手の石が見つかったとき
                            elif osero != player:
                                if osero == 0:
                                    break
                                else:
                                    tmpx.append(tyokusen_x)
                                    tmpy.append(tyokusen_y)
                        else:
                            break

            if overturn_x == [] and overturn_y == []:
                continue
            else:
                put_x.append(x)
                put_y.append(y)

    if put_x == []:
        return True
    else :
        return False
