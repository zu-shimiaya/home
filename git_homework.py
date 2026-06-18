import random

print("=== 3桁の数字当てゲーム ===")
print("これから数字当てゲームを作成します。")

answer = random.randint(100, 999)
guess = input("3桁の数字を入力してください：")

if guess == answer:
    print("正解です！")
else:
    print("不正解です。")