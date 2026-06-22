# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The first time I ran the time the 'hints' it was giving me was not helpful so I didn't get up getting the right answer until I checked the devleoper log.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  1. The 'Go Lower' and 'Go Higher' hints weren't accurate like when I entered 10 and got 'Go Lower' even though the secret word was 16 and got 'Go Higher' when I entered 20. 
  2. If you've won the game and guessed the right number, after clicking 'new game' the old winning message persists and doesn't diappear for the new game. So even the user has clicked 'new game', the message 'You already won. Start new game to play again' message still appears even though the developer logs show a new secret number has been assigned for a new session. 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|  10   | 'Go Higher' Hint  | 'Go Lower' Hint |   None 
|  20   | 'Go Lower' Hint   |'Go Higher' Hint |   None
|  'New  Game' | Default Game View | Win Message from last session persists | None

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude Code for this project, with a bit of reguglar Claude Chat

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
One AI suggestion that was correct was fixing handling the bug when a user starts a new game but cannot enter any new inputs and the 'You already won. Start a new game to play again.' persists from the last session. Claude Code suggested to fix the new game handler by also resetting the 'st.session_state.status' so the game remains in "won" state. 

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
One example where the AI suggestion was misleading was when fixing the high/low input issue. Claude suggested that I needed to change my app.py because for Python 3 one secion of my code is causing a TypeError by doing a string comparison instead of a nuemric one. Although I understood after some follow-up questions why the change made sense it was misleading at first because it wasn't clear why that specific change was needed especially since it was not in the logic for the high/low bug. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I would quit the current local host and then run it again to test whether the bug was fixed

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
One test I used was pytest was called 'test_guess_higher_than_secret_shows_go_lower_message' which calls check_guess with the guess as '20' and the secret as '16'. It verifies that the outcome label is 'Too High' which would catch the bug where the labels were swapped previously. Mainly this is testing when a player guesses too high, does the game correctly tell them to go lower

- Did AI help you design or understand any tests? How?
Yes I used the AI to understand how to write the syntax, content, and function of the test. Also I was asking how to properly run in it my terminal as I didn't know how to do to that before.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
I think Streamlit 'reruns' the code anytime a user interaction happends which would make the exprience sometimes feel wonky. I would describe to a friend as someone who reads a chapter of a book and before they start the next chapter, they reread all the previous chapters rather than just moving forward to the new chapter.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
I want to pursure specific prompting techinques to ensure I am feeding the AI the most efficient and helpful prompt for the task I am looking for.

- What is one thing you would do differently next time you work with AI on a coding task?
Next time, I would like to spend more time going over the AI's suggestions of code rewrites/deletions. Sometimes I wanted more explanation before diving into the exact coding so I think I might adopt a prompting format where  I plan the task beforehand.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project highlighted to me AI generated code needs to be reviewed in order to be effective and explainable for a collaborative enviroment. 
