from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_guess_higher_than_secret_shows_go_lower_message():
    # Bug fix: when guess > secret, message must say "Go LOWER!" not "Go HIGHER!"
    # Example: secret=16, guess=20 — player needs to guess lower
    outcome, message = check_guess(20, 16)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_lower_than_secret_shows_go_higher_message():
    # Bug fix: when guess < secret, message must say "Go HIGHER!" not "Go LOWER!"
    # Example: secret=16, guess=10 — player needs to guess higher
    outcome, message = check_guess(10, 16)
    assert outcome == "Too Low"
    assert "HIGHER" in message
