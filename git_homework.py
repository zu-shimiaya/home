import random

print("=== 3桁の数字当てゲーム ===")
print("これから数字当てゲームを作成します。")

answer = random.randint(100, 999)
max_attempts = 7
attempt = 1

print("正解の数字を作成しました。")
print("回答できる回数は", max_attempts, "回までです。")

while attempt <= max_attempts:
    guess_text = input(str(attempt) + "回目の回答：")

    if not guess_text.isdigit():
        print("数字を入力してください。")
        continue

    guess = int(guess_text)

    if guess < 100 or guess > 999:
        print("3桁の数字を入力してください。")
        continue

    print("あなたの回答は", guess, "です。")

    if guess == answer:
        print("正解です！")
        print(attempt, "回でクリアしました。")
        break
    else:
        print("不正解です。")

        if guess < answer:
            print("ヒント：正解はもっと大きい数字です。")
        else:
            print("ヒント：正解はもっと小さい数字です。")

        answer_str = str(answer)
        guess_str = str(guess)

        hit = 0
        for i in range(3):
            if answer_str[i] == guess_str[i]:
                hit += 1

        common = 0
        for number in set(guess_str):
            common += min(answer_str.count(number), guess_str.count(number))

        match = common - hit

        print("ヒット数：", hit)
        print("一致数：", match)

        remaining = max_attempts - attempt

        if remaining > 0:
            print("残り", remaining, "回です。")
        else:
            print("ゲームオーバーです。")
            print("正解は", answer, "でした。")

        attempt += 1