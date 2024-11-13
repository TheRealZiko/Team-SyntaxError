import unittest

class TriviaGameMenu:
    """manages the text-based menu system for the trivia game.

    Attributes:
        database (QuestionDatabase): An instance of the QuestionDatabase class for managing questions.
    """

    def __init__(self, database):
        pass

    def display_menu(self):
        """displays the main menu options to the user.
        
        Side effects:
            Prints the menu options to the console.
        """
        pass

    def view_instructions(self):
        """displays the game instructions to the user.

        Side effects:
            Prints the instructions to the console.
        """
        pass

    def start_game(self, num_players):
        """starts the trivia game for the specified number of players.

        Args:
            num_players (int): The number of players (1 or 2).
        
        Side effects:
            Initializes and runs the game session.
        """
        pass

class TriviaGame:
    """handles the gameplay logic for the trivia game.

    Attributes:
        database (QuestionDatabase): An instance of the QuestionDatabase class for retrieving questions.
        num_questions (int): The total number of questions for the game session.
        player_scores (dict): A dictionary storing scores for each player.
    """

    def __init__(self, database, num_questions):
        pass

    def ask_question(self, question):
        """presents a question to the current player and evaluates their answer.

        Args:
            question (dict): The question data, including text, answers, and difficulty.
        
        Returns:
            int: Points earned for the question based on its difficulty.
        """
        pass

    def determine_winner(self):
        """determines the winner of the game based on player scores.

        Returns:
            str: A message indicating the winner or if the game is tied.
        """
        pass

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