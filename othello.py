# 0: null
# 1: white
# 2: black

#grid 8x8

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
    #valicion = invalido(row,col)
    #if(valicion == True):
    if ((player==1) and (grid[row][col]==0)):
        grid[row][col] = 1
            #isValid(row, col,player)
        Overturn(col,row,player)
            #print(grid)
        return "OK"
    elif((player==2) and (grid[row][col]==0)):
        grid[row][col] = 2
        Overturn(col,row,player)
            #isValid(row, col,player)
            #print(grid)
        return "OK"
    #else:
        #return "ok"

    #石が置けない場合

    

#redirecciona a los posibles movimientos
def isValid(row,col,player):
        horizontal(row,col,player)
        vertical(row, col, player)
        diagonal(row, col, player)

def horizontal(row,col,player):
        lenG = lenGrid()
        if(row<=lenG-1 and col<=lenG-1):
            if(player==1):
                if (col+1 <= lenG-1):
                    if(grid[row][col+1]==2):
                        grid[row][col+1] = 1
                        horizontal(row, col+1, player)
                else:
                    if (grid[row][col] == 2):
                        grid[row][col] = 1
                        horizontal(row, col, player)

            if (player == 2):
                if (col+1 <= lenG-1):
                    if (grid[row][col+1] == 1):
                        grid[row][col+1] = 2
                        horizontal(row, col+1, player)
                else:
                    if (grid[row][col] == 1):
                        grid[row][col] = 2
                        horizontal(row,col, player)

        if(row>=0 and col>=0):
            if(player==1):
                if (col-1 >= 0):
                    if(grid[row][col-1]==2):
                        grid[row][col-1] = 1
                        horizontal(row, col-1, player)
                else:
                    if (grid[row][col] == 2):
                        grid[row][col] = 1
                        horizontal(row, col, player)
            if (player == 2):
                if(col-1 >= 0):
                    if (grid[row][col-1] == 1):
                        grid[row][col-1] = 2
                        horizontal(row, col-1, player)
                else:
                    if (grid[row][col] == 1):
                        grid[row][col] = 2
                        horizontal(row,col, player)

def vertical(row,col,player):
    #垂直
    lenG=lenGrid()
    if(row>= 0 and col>=0 ):
        up=grid[row-1][col]
        if (player == 1):
            if (up == 2):
                grid[row-1][col] = 1
                vertical(row-1,col, player)
        if (player == 2):
            if (up == 1):
                grid[row-1][col] = 2
                vertical(row-1, col, player)
    if(row <= lenG-1 and col <= lenG-1):
        if(row+1 <= lenG-1):
            dow=grid[row+1][col]
            if (player == 1):
                if (dow == 2):
                    grid[row+1][col] = 1
                    vertical(row+1,col, player)
            if (player == 2):
                if (dow == 1):
                    grid[row+1][col] = 2
                    vertical(row+1,col, player)
        else:
            actual = grid[row][col]
            if (player == 1):
                    if (actual == 2):
                        grid[row][col] = 1
                        vertical(row, col, player)
            if (player == 2):
                if (actual == 1):
                    grid[row][col] = 2
                    vertical(row, col, player)

def diagonal(row,col,player):
    lenG = lenGrid()
    if (player == 1):
        if (row >= 0 and col >= 0):
            if(row-1 >= 0 and col+1 <= lenG-1):
                    upDer = grid[row - 1][col + 1]
                    if (upDer  == 2):
                        grid[row-1][col+1] = 1
                        diagonal(row-1,col+1,player)
        if (row >= 0 and col >= 0):
            if (row-1>= 0 and col-1>=0):
                upIzq = grid[row-1][col-1]
                if (upIzq == 2):
                    grid[row-1][col-1] = 1
                    diagonal(row-1,col-1,player)
        if (row <= lenG - 1 and col <= lenG - 1):
            if (row+1<= lenG-1 and col+1 <= lenG-1):
                dowDer = grid[row+1][col+1]
                if (dowDer == 2):
                    grid[row+1][col+1] = 1
                    diagonal(row+1,col+1,player)
        if (row <= lenG - 1 and col <= lenG - 1):
            if (row + 1 <= lenG-1 and col - 1 >= 0):
                dowIzq = grid[row + 1][col - 1]
                if (dowIzq == 2):
                    grid[row+1][col-1] = 1
                    diagonal(row+1,col-1,player)

    if (player == 2):
        if (row >= 0 and col >= 0):
            if(row-1 >= 0 and col+1 <= lenG-1):
                    upDer = grid[row - 1][col + 1]
                    if (upDer  == 1):
                        grid[row-1][col+1] = 2
                        diagonal(row-1,col+1,player)
        if (row >= 0 and col >= 0):
            if (row-1>= 0 and col-1>=0):
                upIzq = grid[row-1][col-1]
                if (upIzq == 1):
                    grid[row-1][col-1] = 2
                    diagonal(row-1,col-1,player)
        if (row <= lenG - 1 and col <= lenG - 1):
            if (row+1<= lenG-1 and col+1 <= lenG-1):
                dowDer = grid[row+1][col+1]
                if (dowDer == 1):
                    grid[row+1][col+1] = 2
                    diagonal(row+1,col+1,player)

        if (row <= lenG - 1 and col <= lenG - 1):
            if (row + 1 <= lenG-1 and col - 1 >= 0):
                dowIzq = grid[row + 1][col - 1]
                if (dowIzq == 1):
                    grid[row+1][col-1] = 2
                    diagonal(row+1,col-1,player)

def invalido(row,col):
    #無効
    lenG=lenGrid()
    if (row >= 0):
        if(row-1 >= 0):
            if(grid[row-1][col]!=0 ):
                return True
    if(row <= lenG-1):
        if(row+1 <= lenG-1):
            if(grid[row+1][col]):
                return True
    if(col <= lenG-1):
        if(col+1 <= lenG-1):
            if(grid[row][col+1] != 0):
                return True
    if(col >= 0):
        if(col-1 >= 0):
            if(grid[row][col-1] != 0):
                return True
    if(row >= 0 and col >= 0):
        if(row-1 >= 0 and col-1 >= 0):
            if(grid[row-1][col-1] != 0):
                return True
    if (row <= lenG-1 and col  <= lenG-1):
        if (row + 1 <= lenG-1 and col + 1 <= lenG-1):
            if (grid[row + 1][col + 1] != 0):
                return True
    if (row >= 0 and col <= lenG - 1):
        if (row - 1 >=  0 and col + 1 <= lenG - 1):
            if (grid[row - 1][col + 1] != 0):
                return True

    if (row <= lenG-1 and col >= 0):
        if (row + 1 <= lenG-1 and col - 1 >= 0):
            if (grid[row + 1][col - 1] != 0):
                return True

def lenGrid():
    cont=0
    for x in grid:
        cont+=1
    return cont

def Reverce(self, x, y):
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
                    if osero == self.player:
                        if tmpx != [] and tmpy != []:
                            # print("追加しました")
                            overturn_x.append(tmpx)
                            overturn_y.append(tmpy)
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
