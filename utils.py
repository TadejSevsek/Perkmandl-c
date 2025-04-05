import os

def check_first_time_play():
    if not os.path.exists("tutorial_flag.txt"):
        with open("tutorial_flag.txt", "w") as f:
            f.write("False")
        return True  
    with open("tutorial_flag.txt", "r") as f:
        flag = f.read().strip()
    if flag == "False":
        return True
    return False

def mark_tutorial_completed():
    with open("tutorial_flag.txt", "w") as f:
        f.write("True")

def get_high_score():
    try:
        with open("highscore.txt", "r") as f:
            return int(f.read().strip())
    except (FileNotFoundError, ValueError):
        return 0

def save_high_score(score):
    with open("highscore.txt", "w") as f:
        f.write(str(score))