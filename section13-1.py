import time
import datetime
import sqlite3
import winsound
import random

#DB연결 & Auto commit 설정

conn = sqlite3.connect('./resource/database.db', isolation_level=None)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS records (\
id INTEGER PRIMARY KEY AUTOINCREMENT, cor_cnt INTEGER, record text, regidata text)")

n = 1
cor_cnt = 0
starftime = time.strftime('%Y-%M-%d  %H-%M ')
start = time.time()

words = []  # 단어리스트

## 단어리스트를 txt파일로부터 읽어온다
with open('./resource/word.txt', 'r') as f:
    for c in f:
        words.append(c.strip())

## 단어게임 메인로직
while n <= 5:
    random.shuffle(words)
    q = random.choice(words)
    print('# question_{}:'.format(n), end=(''))
    print(q)  # 단어출력
    print('input: ', end=(''))
    i = input()  # 사용자입력
    print()
    if str(q.strip()) == str(i).strip():  # 입력확인
        print('pass!\n')
        winsound.PlaySound('./sound/good.wav', winsound.SND_FILENAME)
        cor_cnt += 1
    else:
        print('unpass!\n')
        winsound.PlaySound('./sound/bad.wav', winsound.SND_FILENAME)
    n += 1

print('맞은횟수: {}'.format(cor_cnt))

end = time.time()

print("진행시간: {}초".format(int(end-start)))
print()


cursor.execute("INSERT INTO records('cor_cnt','record','regidata') VALUES(?,?,?)",
               (cor_cnt, int(end-start), starftime))

conn.commit()

## 시작지점코드

if __name__ == '__main__':
    pass
