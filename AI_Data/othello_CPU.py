import copy

# 石の設定と辞書
BLACK = 1
WHITE = -1
STONE = {1:'BLACK', -1:'WHITE'}
OPPONENT = {BLACK: WHITE, WHITE: BLACK}
class Board:
    def __init__(self):
        # 8×8の何もない平面を作る。
        self.cells = []
        for i in range(8):
            self.cells.append([None for i in range(8)])

        # 4つの石を初期配置する
        self.cells[3][3] = WHITE
        self.cells[3][4] = BLACK
        self.cells[4][3] = BLACK
        self.cells[4][4] = WHITE

    # 石を置く処理
    def put(self, x, y, stone):
        flippable = self.list_flippable_disks(x, y, stone)
        self.cells[y][x] = stone
        for x,y in flippable:
            self.cells[y][x] = stone

        return True

    # ボードを表示する。
    def show_board(self,turn):
        print("--" * 20)
        print(str(turn) + "ターン目")
        print("  ", end="")   # ,end=""は改行を防ぐ。
        for i in range(8):
            print(i, end="")
            print(" ", end="")
        print("\n", end="")

        j = 0
        for i in self.cells:
            print(j, end="")
            print(" ", end="")
            j += 1
            for cell in i:
                if cell == WHITE:
                    print("W", end=" ")
                elif cell == BLACK:
                    print("B", end=" ")
                else:
                    print("*", end=" ")
            print("\n", end="")

    # 石を置くことができる場所を探す。
    def list_possible_cells(self, stone):
        possible = []
        for x in range(8):
            for y in range(8):
                if self.cells[y][x] is not None:
                    continue
                if self.list_flippable_disks(x, y, stone) == []:
                    continue
                else:
                    possible.append((x, y))
        return possible

    # ひっくり返せる石を探す。
    def list_flippable_disks(self, x, y, stone):
        PREV = -1
        NEXT = 1
        DIRECTION = [PREV, 0, NEXT]
        flippable = []

        for dx in DIRECTION:
            for dy in DIRECTION:
                if dx == 0 and dy == 0:
                    continue

                tmp = []
                depth = 0
                while(True):
                    depth += 1

                    # 方向 × 深さ(距離)を要求座標に加算し直線的な探査をする
                    rx = x + (dx * depth)
                    ry = y + (dy * depth)

                    # 調べる座標(rx, ry)がボードの範囲内ならば
                    if 0 <= rx < 8 and 0 <= ry < 8:

                        request = self.cells[ry][rx]

                        # Noneを獲得することはできない
                        if request is None:
                            break

                        if request == stone:  # 自分の石が見つかったとき
                            if tmp != []:      # 探査した範囲内に獲得可能な石があれば
                                flippable.extend(tmp) # flippableに追加
                            else:              #探査した範囲内に獲得可能な石がなければ
                                break

                        # 相手の石が見つかったとき
                        else:
                            tmp.append((rx, ry))  # 獲得可能な石として一時保存
                    else:
                        break
        return flippable
    
class Othello:

    # モード切替
    def mode_option(self, mode):
        if mode == 0:
            self.player1 = User(BLACK, "PLAYER1")
            self.player2 = User(WHITE, "PLAYER2")
        elif mode == 1:
            self.player1 = User(BLACK, "あなた")
            self.player2 = Mini_method(WHITE, "Mini-method")
        elif mode == 2:
            self.player1 = User(BLACK, "あなた")
            self.player2 = Max_method(WHITE, "Max-method")
        """この下に書き加えれば新しいモードを増やせる。今後はコンピュータ同士で戦わせたりしたい。"""

    # ゲームの進行
    def play(self):
        board = Board()
        turn = 1
        pass_turn = 0 # お互いにpassしかない硬直状態になったら終わらせるため。
        mode = int(input("mode select: 0)PvP 1)vs.Mini_method 2)vs.Max_method > "))
        self.mode_option(mode)

        while(True):
            board.show_board(turn)
            black_count = 0
            white_count = 0
            for x in range(8):
                for y in range(8):
                    if board.cells[y][x] == BLACK:
                        black_count += 1
                    elif board.cells[y][x] == WHITE:
                        white_count += 1

            # 石がすべて置かれた、または硬直状態、またはどちらかの全滅で決着とする。
            if (black_count + white_count == 64
                or pass_turn == 2
                or black_count == 0
                or white_count == 0):
                print("--" * 10+ "finished!!" + "--" * 10)
                if black_count > white_count:
                      print("WINNER BLACK!!")
                elif black_count < white_count:
                      print("WINNER WHITE!!")
                else:
                      print("Draw")

                print("results:  " + "B: " + str(black_count) + ", W: " + str(white_count))
                break

            # Player1のターン
            elif turn % 2 == 1:
                stone = BLACK
                possible = board.list_possible_cells(stone)
                if possible == []:  # 置ける場所がなければpass
                    pass
                else:  # 置ける場所があるならどこに置くか決める。
                    index = self.player1.main(possible)  # 判断材料としてpossibleを送る。

            # Player2のターン(Player1と同様)
            elif turn % 2 == 0:
                stone = WHITE
                possible = board.list_possible_cells(stone)
                if possible == []:
                    pass
                else:
                    index = self.player2.main(possible)

            # pass
            if possible == []:
                print("pass")
                pass_turn += 1
                pass
            # Playerが決めた場所に石を置く
            else:
                board.put(*possible[index],stone)
                self.player1.copy_board(possible,index,stone)
                self.player2.copy_board(possible,index,stone)
                pass_turn = 0

            turn += 1
            
# すべてのPlayer(人とコンピューター)に共通するクラス
class BasePlayer:

    # 自分の名前と石の色を把握する。
    def __init__(self,stone,name):
        self.stone = stone
        self.name = name
        self.board = Board()
        self.copy_cells = []

    # 実際の盤面のコピーを作る。(CPU用)
    def copy_board(self,possible,index,stone):
        self.board.put(*possible[index],stone)
        self.copy_cells = copy.deepcopy(self.board.cells)

    # 計算後に盤面をもとに戻す。(CPU用)
    def reset_board(self):
        self.board.cells = copy.deepcopy(self.copy_cells)

# 人の入力を受け付けて石を置く。(人)
class User(BasePlayer):

    def main(self,possible):
        print("player: " + self.name + " (" + STONE[self.stone] + ")")
        print("put to: ", end="[")   # ,end=""は改行を防ぐ。
        for i in range(len(possible) - 1): # 選択肢を表示する。
            print(str(i) + ":" + str(possible[i]), end=", ")
        print(str(len(possible) - 1) + ":" + str(possible[len(possible) - 1]) + "]")
        index = int(input("choose: "))  #Userが石を置く場所を選ぶ。
        print("You put:" + str(possible[index]))
        return index  # 選ばれた選択肢の番号を返す。
    
# 次相手が打つ手のパターン(opponent_possible)が少なくなるように石を置く。(CPU)
class Mini_method(BasePlayer):

    def main(self,possible):
        min_count = 30
        index = 0  # 最悪0番目の選択肢を選ぶ。(バグ防止)

        # 選択肢をしらみつぶしに調べていく。
        for i in range(len(possible)):
            self.board.put(*possible[i],self.stone)  # i番目の選択肢で仮で置いてみる。
            # その時の相手が取れる選択肢を調べる。
            opponent_possible = self.board.list_possible_cells(OPPONENT[self.stone])

            # 角トラレタクナイ
            if ((0,0) in opponent_possible
                or (0,7) in opponent_possible
                or (7,0) in opponent_possible
                or (7,7) in opponent_possible):
                pass  #角が取られる選択肢を捨てる。

            # 相手の選択肢(opponent_possible)が最小のときのiを保存する。
            elif len(opponent_possible) <= min_count:
                min_count = len(opponent_possible) # より少ないものがあれば最小値を更新。
                index = i  # 自分の手(i)をindexに保存。
            # 相手の選択肢が最小じゃないならスルー。
            else:
                pass

            self.reset_board()  # 仮で置いた石をリセット。

        # CPUが選んだ選択肢などを表示。
        print("player: " + self.name + " (" + STONE[self.stone] + ")")
        print("put to: ", end="[")
        for i in range(len(possible) - 1):
            print(str(i) + ":" + str(possible[i]), end=", ")
        print(str(len(possible) - 1) + ":" + str(possible[len(possible) - 1]) + "]")
        print("choose: " + str(index), end=":")
        print(possible[index])

        return index  # 選ばれた選択肢の番号を返す。
    
# 次の自分の打つ手(next_possible)が多くなるように石を置く。(CPU)
class Max_method(BasePlayer):

    def main(self,possible):
        max_count = 0
        count = 0
        index = 0  # 最悪0番目の選択肢を選ぶ。(バグ防止)

        # 選択肢をしらみつぶしに調べていく。
        for i in range(len(possible)):
            self.board.put(*possible[i],self.stone)  # i番目の選択肢で仮で置いてみる。
            # その時の相手が取れる選択肢の個数を調べる。後でもう一度書くのはリセットされてしまうため。
            # ここでopponent_possibleを調べるのはjの繰り返しの上限を決めるため。
            opponent_possible = self.board.list_possible_cells(OPPONENT[self.stone])
            self.reset_board()  # 一旦リセット。

            # 角トラレタクナイ
            if ((0,0) in opponent_possible
                or (0,7) in opponent_possible
                or (7,0) in opponent_possible
                or (7,7) in opponent_possible):
                continue  #角が取られる選択肢を捨てる。
            else:
                pass

            # 自分の手(i)に対する相手の手(j)を調べる。
            for j in range(len(opponent_possible)):
                self.board.put(*possible[i],self.stone)  #リセットされているのでもう一度。
                opponent_possible = self.board.list_possible_cells(OPPONENT[self.stone])
                # 相手の手(j)を仮で置く。
                self.board.put(*opponent_possible[j],OPPONENT[self.stone])
                # その次の自分の打つ手(next_possible)を調べる。
                next_possible = self.board.list_possible_cells(self.stone)
                count += len(next_possible) # i番目のnext_possibleの長さを合計する。
                self.reset_board() # 一旦リセット。

            # next_possibleの合計(count)が最大のiを保存する。
            if count >= max_count:
                max_count = count  #より大きいものがあれば最大値を更新。
                index = i  # 自分の手(i)をindexに保存。
            # 相手の選択肢が最小じゃないならスルー。
            else:
                pass

        # CPUが選んだ選択肢などを表示。
        print("player: " + self.name + " (" + STONE[self.stone] + ")")
        print("put to: ", end="[")
        for i in range(len(possible) - 1):
            print(str(i) + ":" + str(possible[i]), end=", ")
        print(str(len(possible) - 1) + ":" + str(possible[len(possible) - 1]) + "]")
        print("choose: " + str(index), end=":")
        print(possible[index])

        return index  # 選ばれた選択肢の番号を返す。
    # メイン文
if __name__ == "__main__":
    Othello().play()