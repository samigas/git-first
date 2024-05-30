import pickle
import os

filepath = 'data/score.bin'

def get_scores(s):
    print('[점수 입력]')
    i = 1
    while True:
        scores = input(f'#{i}?')
        i+=1
        if scores == '':
            break
        elif int(scores) >= 0:
            s.append(int(scores))
        else: break

def cul_scores(s):
    print('[점수출력]')
    print('개인점수:', end='')
    a = 0
    b = 0
    c = ''
    for i in s:
        a += i
        b += 1
        print(i, end=' ')
    print()
    ave_score = a / b
    print(f'평균:{ave_score}')

def save_scores(s):
    with open(filepath, 'wb') as file:
        pickle.dump(s, file)

def load_scores(s):
    if os.path.exists(filepath):
        with open(filepath, 'rb') as file:
            s = pickle.load(file)
            ave_num = 0
            a = 0
            print('[점수출력]')
            print('개인점수:', end ='')
            for i in s:
                ave_num += i
                print(i, end=' ')
                a+=1

            print()
            print(f'평균: {ave_num/a}')
        return False
                 
                 


            
score = []
if load_scores(score) != False:
    get_scores(score)
    save_scores(score)
    cul_scores(score)
