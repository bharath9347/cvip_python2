import random
import time

def gnrte_rndm_txt():
    paras = [
        "Success doesn't come from what you done eventually,it comes from what you done consistently ",
        "You don't have to be so extreme,just consistent",
        "Be the one who need help when you are in need of help",
        "Positive anything is better than negative nothing",
        "Make happy ,be happy"
    ]
    return random.choice(paras)

def calculate_the_typing_speed(initial_time, final_time, entered_text):
    wrds = entered_text.split()
    passed_time = final_time - initial_time
    mntes = passed_time / 60
    wpm = len(wrds) / mntes
    return wpm

def typing_speedtest():
    input("Press Enter to start the typing speed test...")
    started_time = time.time()
    text_to_enter = gnrte_rndm_txt()
    print("type the given one: ")
    print(text_to_enter)
    typed_text = input("My Text: ")
    finished_time = (time.time())
    wpm = calculate_the_typing_speed(started_time, finished_time, typed_text)
    print(f"Your typing speed is {wpm:.2f} WPM.")

if __name__ == "__main__":
    typing_speedtest()
