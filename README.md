# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

This game is about guessing a random secret number within 8 guesses. Based on each input from the user, the game gives user a hint(lower or higher) to get closer to the real secret number. One bug I found was when the hint should be 'Go Lower' the game would return 'Go Higher' and vice versa. To fix this, I had to fix check_guess method to make sure it was following the right message logic. Another bug I found was that after a user won the game, the new game wouldn't let the user enter new guesses. To fix this part, I had to new game handler to make sure that it stayed in the 'won' state. I used the help of Claude Code for all three of bug fixes. 

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User Enters a guess of 24
2. Game Returns Message: 'Go HIGHER!'
3. User Enters a guess of 55
4. Game Returns Message: 'Go HIGHER!'
5. User Enters a guess of 98
6. Game Returns Message: 'Go LOWER!'
7. User Enters a guess of 95
8. User Wins Game with correct secret number and a celebratory message pops up

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
