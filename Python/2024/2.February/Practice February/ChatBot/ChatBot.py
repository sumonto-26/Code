# Date ==> 15 February

import json
import time
from difflib import get_close_matches

def load_data(file_path: str) -> dict:
    try:
        with open(file_path, "r") as file:
            data: dict = json.load(file)
        return data
    except (json.JSONDecodeError, FileNotFoundError):
        return {}

def save_data(file_path: str, data: dict):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)

def find_best_answer(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question: str, data: dict) -> str | None:
    for q in data.get("questions", []):
        if q.get("question") == question:
            return q.get("answer")
    return None

def chat_bot():
    data: dict = load_data("ChatBot/Data.json") # json file name

    while True:
        user_input: str = input("\nYou: ")

        if any(keyword in user_input.lower() for keyword in ("quit", "stop", "bye", "exit")):
            print("Good bye")
            break



        best_match: str | None = find_best_answer(user_input, [q.get("question", "") for q in data.get("questions", [])])

        if best_match:
            answer: str | None = get_answer_for_question(best_match, data)
            if answer:
                print(f"Bot: {answer}")
            else:
                print("Bot: I found a similar question, but I don't have an answer. Can you teach me?")
                new_answer: str = input("Type the answer or \"skip\" to skip: ")

                if "questions" not in data:
                    data["questions"] = []

                if new_answer.lower() != "skip":
                    data["questions"].append({"question": best_match, "answer": new_answer})
                    save_data("Data.json", data)
                    print("Bot: Thank you! I learned a new response!")
                else:
                    print("Bot: Okay, I'll try to improve next time.")
        else:
            print("Bot: I don't know the answer. Can you teach me?")
            new_answer: str = input("Type the answer or \"skip\" to skip: ")

            if "questions" not in data:
                data["questions"] = []

            if new_answer.lower() != "skip":
                data["questions"].append({"question": user_input, "answer": new_answer})
                save_data("Data.json", data)
                print("...")
                time.sleep(1)
                print("Bot: Thank you! I learned a new response!")

if __name__ == "__main__":
    chat_bot()
