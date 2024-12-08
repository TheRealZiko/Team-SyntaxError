import unittest
import os
import random
import csv

class Question:

    def __init__(self, csv_file_path):
        """""
        Args:
            csv_file_path (str): Serves as a path to the CSV file that contains the trivia questions.
        """
        self.csv_file_path = csv_file_path
        self.questions = []
        self.load_questions()

    def load_questions(self):
        """Loads in the trivia questions from the csv file"""
        with open(self.csv_file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.questions.append({
                    "text": row["Question"],
                    "correct_answer": row["Correct Answer"],
                    "incorrect_answers": [row["Option A"], row["Option B"], row["Option C"]],
                })

    def get_random_question(self):
        """Returns a single random question and removes it from the pool.

        Returns:
            dict: A randomly selected question.
        """
        if self.questions:
            return self.questions.pop(random.randint(0, len(self.questions) - 1))
        return None

class TriviaGameMenu:

    def __init__(self, database):
        self.database = database

    def display_menu(self):
        print("Welcome to Trivia!")
        print("Please choose an option:")
        print("1. View Instructions")
        print("2. Start Game")
        print("3. Exit")

    def view_instructions(self):
        print("Instructions:")
        print("1. Answer trivia questions by entering the corresponding letter!")
        print("2. Each correct answer earns points based on difficulty.")
        print("3. The player with the highest score wins!")

    def start_game(self, num_players):
        num_questions = int(input("Enter the number of questions: "))
        game = TriviaGame(self.database, num_questions)
        if num_players == 1:
            game.play_single_player()
        elif num_players == 2:
            game.play_two_player()
        else:
            print("Invalid number of players.")
        

class TriviaGame:
    """handles the gameplay logic for the trivia game.

    Attributes:
        database (QuestionDatabase): An instance of the QuestionDatabase class for retrieving questions.
        num_questions (int): The total number of questions for the game session.
        player_scores (dict): A dictionary storing scores for each player.
    """

    def __init__(self, database, num_questions):
        self.database = database
        self.num_questions = num_questions
        self.player_scores = {"Player 1": 0, "Player 2": 0}

    def ask_question(self, question):
        """presents a question to the current player and evaluates their answer.

        Args:
            question (dict): The question data, including text, answers, and difficulty.
        
        Returns:
            int: Points earned for the question based on its difficulty.
        """
        print(f"Question: {question['text']}")
        options = ["A", "B", "C", "D"]
        answers = question["incorrect_answers"] + [question["correct_answer"]]
        random.shuffle(answers)

        for i, option in enumerate(options):
            print(f"{option}: {answers[i]}")

        answer = input("Enter your answer (A/B/C/D): ").strip().upper()
        if answers[options.index(answer)] == question["correct_answer"]:
            difficulty_points = {"easy": 10, "medium": 20, "hard": 30}
            return difficulty_points[question["difficulty"]]
        return 0

    def determine_winner(self):
        """determines the winner of the game based on player scores.

        Returns:
            str: A message indicating the winner or if the game is tied.
        """
        scores = self.player_scores
        if scores["Player 1"] > scores["Player 2"]:
            return "Player 1 wins!"
        elif scores["Player 1"] < scores["Player 2"]:
            return "Player 2 wins!"
        return "It's a tie!"

class QuestionDatabase:
    """manages the database of trivia questions stored in .csv files.

    Attributes:
        db_directory (str): The directory where the .csv files are stored.
    """

    def __init__(self, db_directory):
        """initializes the QuestionDatabase with the directory path for .csv files.

        Args:
            db_directory (str): The directory where the .csv files are stored.
        """
        pass

    def add_question(self, question_text, correct_answer, incorrect_answers, difficulty, topic):
        """adds a new question to the database.

        Args:
            question_text (str): The text of the question.
            correct_answer (str): The correct answer for the question.
            incorrect_answers (list[str]): A list of three incorrect answers.
            difficulty (str): The difficulty level of the question ('easy', 'medium', 'hard').
            topic (str): The topic category for the question.

        Side effects:
            Writes a new question into the appropriate .csv file.
        """
        pass

    def delete_question(self, question_id):
        """deletes a question from the database.

        Args:
            question_id (int): The unique identifier of the question to delete.

        Side effects:
            Removes the specified question from the .csv file.
        """
        pass

    def get_questions(self, difficulty=None, topic=None):
        """retrieves questions from the database based on the specified difficulty and/or topic.

        Args:
            difficulty (str, optional): The difficulty level to filter by.
            topic (str, optional): The topic category to filter by.

        Returns:
            list: A list of questions matching the specified criteria.
        """
        pass

# Unit Tests
class TestTriviaGame(unittest.TestCase):
    def setUp(self):
        """Sets up the test database and game instance."""
        self.mock_database = QuestionDatabase("test_db")
        self.game = TriviaGame(self.mock_database, 5)

    def test_ask_question(self):
        """Test whether or not points are awarded correctly based on the questions difficulty"""
        question = {
            "text": "What is 2+2?",
            "correct_answer": "4",
            "incorrect_answers": ["3", "5", "6"],
            "difficulty": "easy",
        }
        # Simulate user input by calling the method with predefined answers
        player_answer = "4"  # Correct answer
        points = self.game.ask_question(question)
        self.assertEqual(points, 10)  # Easy question awards 10 points

        player_answer = "3"  # Incorrect answer
        points = self.game.ask_question(question)
        self.assertEqual(points, 0)  # No points for an incorrect answer

    def test_determine_winner(self):
        """Test if the winner is determined correctly based on scores"""
        self.game.player_scores = {"Player 1": 30, "Player 2": 20}
        result = self.game.determine_winner()
        self.assertEqual(result, "Player 1 wins!")

        self.game.player_scores = {"Player 1": 20, "Player 2": 20}
        result = self.game.determine_winner()
        self.assertEqual(result, "It's a tie!")

class TestQuestionDatabase(unittest.TestCase):
    def setUp(self):
        """Set up a test database directory"""
        self.test_db_directory = "test_databases"
        os.makedirs(self.test_db_directory, exist_ok=True)
        self.database = Question(self.test_db_directory)

    def tearDown(self):
        """Clean up the test database directory"""
        for file in os.listdir(self.test_db_directory):
            os.remove(os.path.join(self.test_db_directory, file))
        os.rmdir(self.test_db_directory)

    def test_add_question(self):
        """Test if a question is added correctly to the .csv file"""
        self.database.add_question(
            "What is the capital of France?",
            "Paris",
            ["London", "Rome", "Berlin"],
            "medium",
            "Geography",
        )
        file_path = os.path.join(self.test_db_directory, "Geography.csv")
        self.assertTrue(os.path.exists(file_path))

        with open(file_path, "r") as file:
            lines = file.readlines()
        self.assertIn("What is the capital of France?,Paris,London|Rome|Berlin,medium\n", lines)

    def test_delete_question(self):
        """Test if a question is deleted correctly from the .sv file"""
        self.database.add_question(
            "What is the capital of Spain?",
            "Madrid",
            ["Barcelona", "Seville", "Valencia"],
            "medium",
            "Geography",
        )
        file_path = os.path.join(self.test_db_directory, "Geography.csv")
        self.database.delete_question(1)
        with open(file_path, "r") as file:
            lines = file.readlines()
        self.assertEqual(len(lines), 0)

    def test_get_questions(self):
        """Test if questions are retrieved correctly based on criteria"""
        self.database.add_question(
            "What is the capital of Italy?",
            "Rome",
            ["Milan", "Naples", "Turin"],
            "hard",
            "Geography",
        )
        questions = self.database.get_questions(difficulty="hard", topic="Geography")
        self.assertEqual(len(questions), 1)
        self.assertEqual(questions[0]["correct_answer"], "Rome")

class TestTriviaGameMenu(unittest.TestCase):
    def setUp(self):
        """Set up a mock database and menu instance"""
        self.database = QuestionDatabase("test_databases")
        os.makedirs("test_databases", exist_ok=True)
        self.menu = TriviaGameMenu(self.database)

    def tearDown(self):
        """Clean up the test database directory"""
        for file in os.listdir("test_databases"):
            os.remove(os.path.join("test_databases", file))
        os.rmdir("test_databases")

    def test_start_game(self):
        """Test if the game starts correctly for the specified number of players"""
        # Simulate the start game functionality by initializing game logic
        game = self.menu.start_game(1)
        self.assertIsInstance(game, TriviaGame)

    def test_view_instructions(self):
        """Test if the instructions are displayed correctly"""
        instructions = self.menu.view_instructions()
        expected_instructions = """
        Welcome to the Trivia Game!
        Instructions:
        1. Choose a topic and difficulty level.
        2. Answer questions to earn points.
        3. The player with the most points wins.
        """
        self.assertEqual(instructions, expected_instructions.strip())
        
    if __name__ == "__main__":
        database = Question("Trivia Questions - Questions.csv")
        menu = TriviaGameMenu(database)
        menu.display_menu()
