import unittest

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
    def test_ask_question(self):
        """test if points are awarded correctly based on question difficulty.
        """
        pass

    def test_determine_winner(self):
        """test if the winner is determined correctly based on scores.
        """
        pass


class TestQuestionDatabase(unittest.TestCase):
    def test_add_question(self):
        """test if a question is added correctly to the .csv file.
        """
        pass

    def test_delete_question(self):
        """test if a question is deleted correctly from the .csv file.
        """
        pass

    def test_get_questions(self):
        """test if questions are retrieved correctly based on criteria.
        """
        pass


class TestTriviaGameMenu(unittest.TestCase):
    def test_start_game(self):
        """test if the game starts correctly for the specified number of players.
        """
        pass

    def test_view_instructions(self):
        """test if the instructions are displayed correctly.
        """
        pass
