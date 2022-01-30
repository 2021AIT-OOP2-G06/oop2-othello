# 0: null
# 1: white
# 2: black

#grid 8x8

from tabnanny import check
import numpy as np
import time

grid = [
        [ 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 1, 2, 0, 0, 0],
        [ 0, 0, 0, 2, 1, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0],
    ]
change_check = [-1, 0, 1]

def selectCell(row,col,player):
    #ひっくり返せる石があるか確認、なければ何も置かずreturn
    if(Check(col,row,player)):
        return "NG"

    #置ける時
    if ((player==1) and (grid[row][col]==0)):
        grid[row][col] = 1
        Overturn(col,row,1)
    
    for i in range(8):
        print(grid[i])

    # CPU処理
    # 置ける場所候補の配列
    canput_x = []
    canput_y = []
    overturn = []
    for x in range(8):
        for y in range(8):
            if CPUCheck(x,y,2):
                canput_x.append(x)
                canput_y.append(y)
                overturn.append(Heuristic(x,y,2))
                print('discover = {linex} and {liney},Heuristic is {h}'.format(linex=x,liney=y,h=Heuristic(x,y,2)))

    if len(canput_x) == 0:
        return "PASS"
    else:
        idx = overturn.index(max(overturn))#一番返せる石が多い
        Overturn(canput_x[idx],canput_y[idx],2)
        return "OK"

    # 石をひっくり返す動作
def Overturn(x,y,player):
    # put_x = []
    # put_y = []
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
                # print('player:{player} line = {linex} and {liney}'.format(player=player,linex=line_x,liney=line_y))
                # 探索先に石があるとき、ひっくり返せるかの判定
                if 0 <= line_x < 8 and 0 <= line_y < 8:#端に到達したら終わり
                    searchStone = grid[int(line_y)][int(line_x)]#探索する石(null,自分，相手のどれかが入っている)
                    
                    # 自分の石が見つかったとき
                    if searchStone == player:
                        # print('player:{player} line = {linex} and {liney}:自分'.format(player=player,linex=line_x,liney=line_y))
                        if tmpx != [] and tmpy != []: #返せる石が間にある
                            # print("追加しました")
                            for i in range(len(tmpx)):
                                overturn_x.append(tmpx[i])
                                overturn_y.append(tmpy[i])
                            break
                        else:
                            break
                    # 相手の石が見つかったとき
                    elif searchStone == 3-player:
                        # print('player:{player} line = {linex} and {liney}:相手の石'.format(player=player,linex=line_x,liney=line_y))
                        #返せる可能性がある
                        tmpx.append(line_x)
                        tmpy.append(line_y)
                    #null
                    elif searchStone == 0:
                        # print('player:{player} line = {linex} and {liney}:null'.format(player=player,linex=line_x,liney=line_y))
                        break
                else:
                    break

    for i in range(len(overturn_y)):
        grid[overturn_y[i]][overturn_x[i]] = player #二次元配列なので行から指定しないといけない
        print('turning = {linex} and {liney}'.format(linex=overturn_x[i],liney=overturn_y[i]))
    grid[y][x] = player
    print('putted = {linex} and {liney}'.format(linex=x,liney=y))

#人間のCheck 置ける時False
def Check( x, y, player):
    # すでに石が置いてある時
    if grid[y][x] != 0:
        print("ここには置けません")
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
                    if searchStone == 1:
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
                    # 相手の石が見つかったとき
                    elif searchStone == 2:
                        #返せる可能性がある
                        tmpx.append(line_x)
                        tmpy.append(line_y)
                else:
                    break

    # 来た座標に置いた時、石をひっくり返せるかどうか
    for i in range(len(overturn_x)):
        if overturn_x[i] != 0:
            return False
    return True

#置けたらTrue
def CPUCheck(x,y,player):
    # すでに石が置いてある時
    if grid[y][x] != 0:
        #print("ここには置けません")
        return False

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
                    # print(searchStone)

                    # 自分の石が見つかったとき
                    if searchStone == player:
                        if tmpx != [] and tmpy != []: #返せる石が間にある
                            # print("追加しました")
                            return True
                            overturn_x.append(tmpx)
                            overturn_y.append(tmpy)
                            break
                        else:
                            break
                    # 相手の石
                    elif searchStone == 3-player:
                        #返せる可能性がある
                        tmpx.append(line_x)
                        tmpy.append(line_y)

                    #null
                    elif searchStone == 0:
                        break

                    elif searchStone != player:
                        if searchStone == 0:
                            break
                        else:
                            tmpx.append(line_x)
                            tmpy.append(line_y)
                    # 相手の石が見つかったとき
                else:
                    break
    return False

#評価値計算　ひっくりかえせる石の数を返す
def Heuristic(x,y,player):
    # put_x = []
    # # put_y = []
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
                # print('player:{player} line = {linex} and {liney}'.format(player=player,linex=line_x,liney=line_y))
                # 探索先に石があるとき、ひっくり返せるかの判定
                if 0 <= line_x < 8 and 0 <= line_y < 8:#端に到達したら終わり
                    searchStone = grid[int(line_y)][int(line_x)]#探索する石(null,自分，相手のどれかが入っている)
                    
                    # 自分の石が見つかったとき
                    if searchStone == player:
                        # print('player:{player} line = {linex} and {liney}:自分'.format(player=player,linex=line_x,liney=line_y))
                        if tmpx != [] and tmpy != []: #返せる石が間にある
                            # print("追加しました")
                            for i in range(len(tmpx)):
                                overturn_x.append(tmpx[i])
                                overturn_y.append(tmpy[i])
                            break
                        else:
                            break
                    # 相手の石が見つかったとき
                    elif searchStone == 3-player:
                        # print('player:{player} line = {linex} and {liney}:相手の石'.format(player=player,linex=line_x,liney=line_y))
                        #返せる可能性がある
                        tmpx.append(line_x)
                        tmpy.append(line_y)
                    #null
                    elif searchStone == 0:
                        # print('player:{player} line = {linex} and {liney}:null'.format(player=player,linex=line_x,liney=line_y))
                        break
                else:
                    break

    return len(overturn_y)