# coding: utf-8
# Your code here!

# 盤上のステータス(0=未設置、1=黒、2=白)
ban_state = {'not_set':0,'B':1,'W':2}
# 走査方向のマップ
direction_map = {'up':[-1,0],'up_right':[-1,1],'right':[0,1],'low_right':[1,1],'low':[1,0],'low_left':[1,-1],'left':[0,-1],'up_left':[-1,-1],}
# 盤を初期化
ban = [[0 for i in range(8)] for j in range(8)]
ban[3][3]=2
ban[3][4]=1
ban[4][3]=1
ban[4][4]=2
# 石のカウンター
stone_counter = {'B':2,'W':2,'rev':{'B':'W','W':'B'}}
black_count = 2
white_count = 2
# パスした時の情報を保持
pass_stone = {'stone':'','x':0,'y':0}
# 配置可能フラグ
placeable_flg = {'B':True,'W':True}
# 次のストーンを取得するか判断するフラグ
next_flg = True
# 裏返し制御ロジック
def turn_over_logic(stone,x,y):
    global black_count
    global white_count
    x -= 1
    y -= 1
    # ストーンがおかれた場所を更新
    ban[x][y] = ban_state[stone]
    # 現在のストーンがおけるか置けないかを判断するフラグ
    stone_judg_flg = False
    # 走査方向を順番に走査
    for direction in direction_map:
        # 現在地を初期化
        direction_current = [x,y]
        while True:
            # 走査方向のマップから現在地をインクリメント
            print(direction)
            print('インクリ前 x={} y={}'.format(direction_current[0],direction_current[1]))
            print('インクリ値 x={} y={}'.format(direction_map[direction][0],direction_map[direction][1]))
            print('インクリ後 x={} y={}'.format(direction_current[0] + direction_map[direction][0],direction_current[1] + direction_map[direction][1]))
            direction_current[0] += direction_map[direction][0]
            direction_current[1] += direction_map[direction][1]
            # 現在地の状態が未設置または同じストーンの場合は処理終了
            if  ban[direction_current[0]][direction_current[1]] == 0 or ban[direction_current[0]][direction_current[1]] == ban_state[stone] :
                break
            # 現在地の状態が相手のストーンの場合はcountupして盤状態を変更（相手のストーンをひっくり返す）
            else:
                print('石 {}'.format(stone))
                print('変更前　{}'.format(ban[direction_current[0]][direction_current[1]]))
                if not stone_judg_flg:
                    stone_judg_flg = True
                stone_counter[stone] += 1
                stone_counter[stone_counter['rev'][stone]] -= 1
                if stone == 'B':
                    ban[direction_current[0]][direction_current[1]] = 1
                    black_count += 1
                    white_count -= 1
                else:
                    ban[direction_current[0]][direction_current[1]] = 2
                    white_count += 1
                    black_count -= 1
                print('変更後　{}'.format(ban[direction_current[0]][direction_current[1]]))
                print('変更後 黒{} 白{}'.format(black_count,white_count))
    return stone_judg_flg
# 結果表示
def result():
    global black_count
    global white_count
    print(black_count,white_count)
    print('{0:0=2}-{1:0=2} The {2} won!'.format(black_count,white_count,'black' if black_count > white_count else 'white'))
    # 確認用盤表示
    for result in ban:
        print(''.join([str(n) for n in result]))

play_count = int(input())
for i in range(play_count):
    # 次のストーンを取得
    next_stone = [int(j) if j.isdecimal() else j for j in input().rstrip().split(' ') ]
    stone_judg_flg = turn_over_logic(*next_stone)

    # ストーンがおけなかった場合
    if not stone_judg_flg:
        # 黒または白の配置可能フラグを更新
        placeable_flg[next_stone[0]] = False
        if not placeable_flg['B'] and not placeable_flg['W']:
            break
        if placeable_flg['B'] and placeable_flg['W']:
            pass_stone['stone'] = next_stone[0]
            pass_stone['x'] = next_stone[1]
            pass_stone['y'] = next_stone[2]
        else:
            passstone_judg_flg = turn_over_logic(*pass_stone.values())
            if not passstone_judg_flg:
                break
            else:
                placeable_flg[pass_stone[0]] = True
result()
