import unittest
import os
import random
import pandas as pd

class Question:
    def __init__(self, csv_file_path):
        """
        Args:
            csv_file_path (str): Path to the CSV file containing trivia questions.
        """
        self.csv_file_path = csv_file_path
        self.questions = self.load_questions()

    def load_questions(self):
        """Loads trivia questions from the CSV file into a Pandas DataFrame."""
        if not os.path.exists(self.csv_file_path):
            raise FileNotFoundError(f"{self.csv_file_path} does not exist.")
        
        df = pd.read_csv(self.csv_file_path)
        if not {"Question", "Correct Answer", "Option A", "Option B", "Option C"}.issubset(df.columns):
            raise ValueError("CSV file is missing required columns.")
        
        questions = []
        for _, row in df.iterrows():
            questions.append({
                "text": row["Question"],
                "correct_answer": row["Correct Answer"],
                "incorrect_answers": [row["Option A"], row["Option B"], row["Option C"]],
            })
        return questions

    def get_random_question(self):
        """Fetches and removes a random question from the pool."""
        if self.questions:
            return self.questions.pop(random.randint(0, len(self.questions) - 1))
        return None

    def reset_questions(self):
        """Reloads the question pool from the CSV file."""
        self.questions = self.load_questions()


class TriviaGame:
    def __init__(self, database, num_questions):
        self.database = database
        self.num_questions = num_questions
        self.player_scores = {"Player 1": 0, "Player 2": 0}

    def ask_question(self, question, player=None):
        """Asks a question to a player and evaluates their answer."""
        print(f"Question: {question['text']}")
        options = ["A", "B", "C", "D"]
        answers = question["incorrect_answers"] + [question["correct_answer"]]
        random.shuffle(answers)

        for i, option in enumerate(options):
            print(f"{option}: {answers[i]}")

        answer = input(f"{player}, enter your answer (A/B/C/D): ").strip().upper() if player else input("Enter your answer (A/B/C/D): ").strip().upper()
        if answers[options.index(answer)] == question["correct_answer"]:
            print("Correct!\n")
            return 1
        else:
            print(f"Wrong! The correct answer was: {question['correct_answer']}\n")
            return 0

    def play_single_player(self):
        """Handles single-player gameplay."""
        print("\nStarting Single Player Mode!")
        for _ in range(self.num_questions):
            question = self.database.get_random_question()
            if not question:
                print("No more questions available.")
                break
            self.player_scores["Player 1"] += self.ask_question(question)
        print(f"Final Score: {self.player_scores['Player 1']}\n")

    def play_two_player(self):
        """Handles two-player gameplay."""
        print("\nStarting Two Player Mode!")
        for i in range(self.num_questions):
            player = "Player 1" if i % 2 == 0 else "Player 2"
            question = self.database.get_random_question()
            if not question:
                print("No more questions available.")
                break
            self.player_scores[player] += self.ask_question(question, player)

        print("\nFinal Scores:")
        print(f"Player 1: {self.player_scores['Player 1']}")
        print(f"Player 2: {self.player_scores['Player 2']}")
        if self.player_scores["Player 1"] > self.player_scores["Player 2"]:
            print("Player 1 wins!")
        elif self.player_scores["Player 1"] < self.player_scores["Player 2"]:
            print("Player 2 wins!")
        else:
            print("It's a tie!\n")


class TriviaGameMenu:
    def __init__(self, database):
        self.database = database

    def display_menu(self):
        """Displays the main menu."""
        while True:
            print("Welcome to Trivia!")
            print("1. View Instructions")
            print("2. Start Game")
            print("3. Exit")
            choice = input("Enter your choice (1-3): ").strip()
            
            if choice == "1":
                self.view_instructions()
            elif choice == "2":
                self.start_game()
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def view_instructions(self):
        """Displays game instructions."""
        print("\nInstructions:")
        print("1. Answer trivia questions by entering the corresponding letter (A/B/C/D).")
        print("2. Each correct answer earns 1 point.")
        print("3. In Two Player mode, players take turns answering questions.")
        print("4. The player with the highest score at the end wins!\n")

    def start_game(self):
        """Starts the trivia game."""
        num_players = int(input("Enter the number of players (1 or 2): "))
        num_questions = int(input("Enter the number of questions: "))
        self.database.reset_questions()  # Reset the question pool
        game = TriviaGame(self.database, num_questions)

        if num_players == 1:
            game.play_single_player()
        elif num_players == 2:
            game.play_two_player()
        else:
            print("Invalid number of players. Returning to menu.")

class QuestionDataBase:
db = QuestionDataBase()
db.add_question("What is the capital of France?", "Paris")
db.add_question("What is the highest mountain in the world?", "Mount Everest")

answer = db.get_answer("What is the capital of France?")
print(answer)  

questions = db.list_all_questions()
print(questions) 

db.remove_question("What is the capital of France?")
answer = db.get_answer("What is the capital of France?")
print(answer)  


if __name__ == "__main__":
    csv_path = "questions.csv"  # Update with your CSV file path
    question_bank = Question(csv_path)
    menu = TriviaGameMenu(question_bank)
    menu.display_menu()
