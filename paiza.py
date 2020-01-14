# coding: utf-8
# Your code here!

# �Տ�̃X�e�[�^�X(0=���ݒu�A1=���A2=��)
ban_state = {'not_set':0,'B':1,'W':2}
# ���������̃}�b�v
direction_map = {'up':[-1,0],'up_right':[-1,1],'right':[0,1],'low_right':[1,1],'low':[1,0],'low_left':[1,-1],'left':[0,-1],'up_left':[-1,-1],}
# �Ղ�������
ban = [[0 for i in range(8)] for j in range(8)]
ban[3][3]=2
ban[3][4]=1
ban[4][3]=1
ban[4][4]=2
# �΂̃J�E���^�[
stone_counter = {'B':2,'W':2,'rev':{'B':'W','W':'B'}}
black_count = 2
white_count = 2
# �p�X�������̏���ێ�
pass_stone = {'stone':'','x':0,'y':0}
# �z�u�\�t���O
placeable_flg = {'B':True,'W':True}
# ���̃X�g�[�����擾���邩���f����t���O
next_flg = True
# ���Ԃ����䃍�W�b�N
def turn_over_logic(stone,x,y):
    global black_count
    global white_count
    x -= 1
    y -= 1
    # �X�g�[���������ꂽ�ꏊ���X�V
    ban[x][y] = ban_state[stone]
    # ���݂̃X�g�[���������邩�u���Ȃ����𔻒f����t���O
    stone_judg_flg = False
    # �������������Ԃɑ���
    for direction in direction_map:
        # ���ݒn��������
        direction_current = [x,y]
        while True:
            # ���������̃}�b�v���猻�ݒn���C���N�������g
            print(direction)
            print('�C���N���O x={} y={}'.format(direction_current[0],direction_current[1]))
            print('�C���N���l x={} y={}'.format(direction_map[direction][0],direction_map[direction][1]))
            print('�C���N���� x={} y={}'.format(direction_current[0] + direction_map[direction][0],direction_current[1] + direction_map[direction][1]))
            direction_current[0] += direction_map[direction][0]
            direction_current[1] += direction_map[direction][1]
            # ���ݒn�̏�Ԃ����ݒu�܂��͓����X�g�[���̏ꍇ�͏����I��
            if  ban[direction_current[0]][direction_current[1]] == 0 or ban[direction_current[0]][direction_current[1]] == ban_state[stone] :
                break
            # ���ݒn�̏�Ԃ�����̃X�g�[���̏ꍇ��countup���ĔՏ�Ԃ�ύX�i����̃X�g�[�����Ђ�����Ԃ��j
            else:
                print('�� {}'.format(stone))
                print('�ύX�O�@{}'.format(ban[direction_current[0]][direction_current[1]]))
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
                print('�ύX��@{}'.format(ban[direction_current[0]][direction_current[1]]))
                print('�ύX�� ��{} ��{}'.format(black_count,white_count))
    return stone_judg_flg
# ���ʕ\��
def result():
    global black_count
    global white_count
    print(black_count,white_count)
    print('{0:0=2}-{1:0=2} The {2} won!'.format(black_count,white_count,'black' if black_count > white_count else 'white'))
    # �m�F�p�Օ\��
    for result in ban:
        print(''.join([str(n) for n in result]))

play_count = int(input())
for i in range(play_count):
    # ���̃X�g�[�����擾
    next_stone = [int(j) if j.isdecimal() else j for j in input().rstrip().split(' ') ]
    stone_judg_flg = turn_over_logic(*next_stone)

    # �X�g�[���������Ȃ������ꍇ
    if not stone_judg_flg:
        # ���܂��͔��̔z�u�\�t���O���X�V
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
