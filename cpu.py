# 0: null
# 1: white
# 2: black

#grid 8x8

from tabnanny import check
import numpy as np

grid = [
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [9, 0, 0, 0, 0, 0, 0, 0, 0, 9],
        [9, 0, 0, 0, 0, 0, 0, 0, 0, 9],
        [9, 0, 0, 0, 0, 0, 0, 0, 0, 9],
        [9, 0, 0, 0, 1, 2, 0, 0, 0, 9],
        [9, 0, 0, 0, 2, 1, 0, 0, 0, 9],
        [9, 0, 0, 0, 0, 0, 0, 0, 0, 9],
        [9, 0, 0, 0, 0, 0, 0, 0, 0, 9],
        [9, 0, 0, 0, 0, 0, 0, 0, 0, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
    ]
change_check = [-1, 0, 1]

def selectCell(row,col,player):
    #ひっくり返せる石があるか確認、なければ何も置かずreturn
    if(Check(col,row,player)):
        return "NG"

    #置ける時
    if ((player==1) and (grid[row][col]==0)):
        grid[row][col] = 1
        Overturn(col,row,player)
    # elif((player==2) and (grid[row][col]==0)):
    #     grid[row][col] = 2
    #     Overturn(col,row,player)
            #isValid(row, col,player)
            #print(grid)
        #return "OK"
    #else:
        #return "ok"
    #ここにputの処理を書くと動くかも？
    Put(player)
    rng = np.random.default_rng(np.random.randint(0,1))

    while(True):
        randx = int(rng.integers(low=0, high=7, size=1))
        randy = int(rng.integers(low=0, high=7, size=1))
        print('random = {randx} and {randy}'.format(randx=randx,randy=randy))
        if ((grid[randx][randy]==0)):
            if CPUCheck(randx,randy,2):
                Overturn(randx,randy,2)
                break
    

    next_player = 3 - player

    if(Put(next_player)):
        return "PASS"
    else :
        return "OK"

    # 石をひっくり返す動作
def Overturn(x,y,player):
    # ひっくり返せる座標を取得
    #self.Reverce(x, y)
    overturn_x = []
    overturn_y = []

    # 置いたマスの縦、横、ななめのひっくり返せる石の座標の取得
    # 取得された座標はのself.overturn_x、self.overturn_yに格納される
    for check_x in change_check:
        for check_y in change_check:
            # check_xとcheck_yが置いた石の座標と被ったときの処理を飛ばす
            if check_x == 0 and check_y == 0:
                continue
            tmpx = []
            tmpy = []
            dist = 0
            # 直線の石を調べる
            while(True):
                dist += 1
                # x座標とy座標の石を直線的に探す
                line_x = x + (check_x * dist)
                line_y = y + (check_y * dist)
                print('player:{player} line = {linex} and {liney}'.format(player=player,linex=line_x,liney=line_y))
                
                # 探索先に石があるとき、ひっくり返せるかの判定
                if 0 <= line_x < 8 and 0 <= line_y < 8:#端に到達したら終わり
                    searchStone = grid[int(line_y)][int(line_x)]#探索する石(null,自分，相手のどれかが入っている)
                    
                    # 自分の石が見つかったとき
                    if searchStone == player:
                        if tmpx != [] and tmpy != []: #返せる石が間にある
                            # print("追加しました")
                            overturn_x.append(tmpx)
                            overturn_y.append(tmpy)
                            break
                        else:
                            break
                    #null
                    elif searchStone == 0:
                        break

                    #はし
                    elif searchStone == 9:
                        break

                    # 相手の石が見つかったとき
                    elif searchStone != player:
                        #返せる可能性がある
                        tmpx.append(line_x)
                        tmpy.append(line_y)
                    
                else:
                    break

        # x座標とy座標を格納
    check_x = overturn_x
    check_y = overturn_y
        # 石をひっくり返す
    for i in range(len(overturn_y)):
        for j in range(len(overturn_y[i])):
                # print(self.overturn_x[i][j])
                # print(self.overturn_y[i][j])
            grid[check_y[i][j]][check_x[i][j]] = player
    grid[y][x] = player
    # print(overturn_x)
    # print(overturn_y)
    # print(grid[overturn_x][overturn_y])
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
    
        # 置いたマスの縦、横、ななめのひっくり返せる石の座標の取得
        # 取得された座標はのself.overturn_x、self.overturn_yに格納される
    for check_x in change_check:
        for check_y in change_check:
                # check_xとcheck_yが置いた石の座標と被ったときの処理を飛ばす
            if check_x == 0 and check_y == 0:
                continue
            tmpx = []
            tmpy = []
            dist = 0
                # 直線の石を調べる
            while(True):
                dist += 1
                    # x座標とy座標の石を直線的に探す
                line_x = x + (check_x * dist)
                line_y = y + (check_y * dist)
                # 探索先に石があるとき、ひっくり返せるかの判定
                if 0 <= line_x < 8 and 0 <= line_y < 8:#端に到達したら終わり
                    searchStone = grid[int(line_y)][int(line_x)]#探索する石(null,自分，相手のどれかが入っている)
                    
                    # 自分の石が見つかったとき
                    if searchStone == player:
                        if tmpx != [] and tmpy != []: #返せる石が間にある
                            # print("追加しました")
                            overturn_x.append(tmpx)
                            overturn_y.append(tmpy)
                            break
                        else:
                            break
                    #null
                    elif searchStone == 0:
                        break

                    #はし
                    elif searchStone == 9:
                        break

                    # 相手の石が見つかったとき
                    elif searchStone != player:
                        #返せる可能性がある
                        tmpx.append(line_x)
                        tmpy.append(line_y)
                    
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
            change_check = [-1, 0, 1]

        # 置いたマスの縦、横、ななめのひっくり返せる石の座標の取得
        # 取得された座標はのself.overturn_x、self.overturn_yに格納される
            for check_x in change_check:
                for check_y in change_check:
                # check_xとcheck_yが置いた石の座標と被ったときの処理を飛ばす
                    if check_x == 0 and check_y == 0:
                        
                        continue
                    tmpx = []
                    tmpy = []
                    dist = 0
                # 直線の石を調べる
                    while(True):
                        dist += 1
                        # x座標とy座標の石を直線的に探す
                        line_x = x + (check_x * dist)
                        line_y = y + (check_y * dist)
                        # 探索先に石があるとき、ひっくり返せるかの判定
                        if 0 <= line_x < 8 and 0 <= line_y < 8:#端に到達したら終わり
                            searchStone = grid[int(line_y)][int(line_x)]#探索する石(null,自分，相手のどれかが入っている)
                            
                            # 自分の石が見つかったとき
                            if searchStone == player:
                                if tmpx != [] and tmpy != []: #返せる石が間にある
                                    # print("追加しました")
                                    overturn_x.append(tmpx)
                                    overturn_y.append(tmpy)
                                    break
                                else:
                                    break
                            #null
                            elif searchStone == 0:
                                break

                            #はし
                            elif searchStone == 9:
                                break

                            # 相手の石が見つかったとき
                            elif searchStone != player:
                                #返せる可能性がある
                                tmpx.append(line_x)
                                tmpy.append(line_y)
                            
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

#置けたらFalse
def CPUCheck(x,y,player):
    # すでに石が置いてある時
    # if grid[y][x] != 0:
    #     #print("ここには置けません")
    #     return False

    overturn_x = []
    overturn_y = []
    change_check = [-1, 0, 1]

        # 置いたマスの縦、横、ななめのひっくり返せる石の座標の取得
        # 取得された座標はのself.overturn_x、self.overturn_yに格納される
    for check_x in change_check:
        for check_y in change_check:
                # check_xとcheck_yが置いた石の座標と被ったときの処理を飛ばす
            if check_x == 0 and check_y == 0:
                continue
            tmpx = []
            tmpy = []
            dist = 0 #x,yからの距離
            
            # 直線の石を調べる
            while(True):
                dist += 1
                    # x座標とy座標の石を直線的に探す
                line_x = x + (check_x * dist)
                line_y = y + (check_y * dist)
                    # rxとryに石はあるのかの判定と、ひっくり返せるかの判定
                # 探索先に石があるとき、ひっくり返せるかの判定
                if 0 <= line_x < 8 and 0 <= line_y < 8:#端に到達したら終わり
                    searchStone = grid[int(line_y)][int(line_x)]#探索する石(null,自分，相手のどれかが入っている)
                    print(searchStone)
                    # 自分の石が見つかったとき
                    if searchStone == player:
                        if tmpx != [] and tmpy != []: #返せる石が間にある
                            # print("追加しました")
                            overturn_x.append(tmpx)
                            overturn_y.append(tmpy)
                            break
                        else:
                            break
                    #null
                    elif searchStone == 0:
                        break

                    #はし
                    elif searchStone == 9:
                        break

                    # 相手の石が見つかったとき
                    elif searchStone != player:
                        #返せる可能性がある
                        tmpx.append(line_x)
                        tmpy.append(line_y)
                    
                else:
                    break
        
        # 来た座標に置いた時、石をひっくり返せるかどうか
    for i in range(len(overturn_x)):
        if overturn_x[i] != 0:
            #print("ここにおけます")
            #grid[y][x] = player
            return True
    #print("ここに置けません")
    return False