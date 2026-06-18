import random

print("=== 3桁の数字当てゲーム ===")
print("これから数字当てゲームを作成します。")

answer = random.randint(100, 999)
guess = input("3桁の数字を入力してください：")

while True:
    guess = int(input("3桁の数字を入力してください："))

    print("あなたの回答は", guess, "です。")

    if guess == answer:
        print("正解です！")
        break
    else:
        print("不正解です。もう一度入力してください。")