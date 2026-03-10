import random

# List of riddles and answers
riddles = [
    ("What has to be broken before you can use it?", "egg"),
    ("I’m tall when I’m young, and I’m short when I’m old. What am I?", "candle"),
    ("What month of the year has 28 days?", "all of them"),
    ("What is full of holes but still holds water?", "sponge"),
    ("What question can you never answer yes to?", "are you asleep"),
    ("What is always in front of you but can’t be seen?", "future"),
    ("What gets wetter the more it dries?", "towel"),
    ("What can you keep after giving to someone?", "your word"),
    ("What has many keys but can’t open a single lock?", "piano"),
    ("Where does today come before yesterday?", "dictionary")
]

print("🧠 Welcome to the Riddle Game!")
print("Get 3 riddles right in a row to win!\n")

score = 0

# Shuffle riddles to make the game random
random.shuffle(riddles)

for question, answer in riddles:
    print("Riddle:", question)
    user = input("Your answer: ").strip().lower()

    if user == answer:
        score += 1
        print("✅ Correct!")
        print(f"Streak: {score}\n")
    else:
        print(f"❌ Wrong! The correct answer was: {answer}\n")
        score = 0  # reset streak

    # Check win condition
    if score == 3:
        print("🎉 Congratulations! You got 3 riddles right in a row!")
        break
else:
    print("Game over! You didn’t reach a 3-riddle streak. Try again!")

print("\nThanks for playing! 🤗")
