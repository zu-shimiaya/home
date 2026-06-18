import random

print("=== 3桁の数字当てゲーム ===")
print("これから数字当てゲームを作成します。")

answer = random.randint(100, 999)
max_attempts = 7

print("回答できる回数は", max_attempts, "回までです。")

for attempt in range(1, max_attempts + 1):
    guess = int(input(str(attempt) + "回目の回答："))

    print("あなたの回答は", guess, "です。")

    if guess == answer:
        print("正解です！")
        break
    else:
        print("不正解です。")

        remaining = max_attempts - attempt

        if remaining > 0:
            print("残り", remaining, "回です。")
        else:
            print("ゲームオーバーです。")
            print("正解は", answer, "でした。")