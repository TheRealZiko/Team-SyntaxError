import random

class TriviaGame:
    def __init__(self):
        self.players = []
        self.scores = {}

    def welcome_players(self):
        
        while True:
            name = input("Enter your name (or 'q' to start the game): ")
            if name.lower() == 'q':
                break
            self.players.append(name)
            self.scores[name] = 0
        print(f"Welcome, {', '.join(self.players)}! Let's play Trivia!")

    def get_difficulty(self):
        
        while True:
            try:
                level = int(input("Select a difficulty level (1-5): "))
                if 1 <= level <= 5:
                    return level
                else:
                    print("Invalid difficulty level. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5.")

    def get_question(self, difficulty):
    
        pass

    def check_answer(self, player, answer, correct_answer):
        """
        Checks the player's answer and updates the score accordingly.
        """
        if answer.lower() == correct_answer.lower():
            print(f"{player} got the answer correct!")
            self.scores[player] += (difficulty * 100)
        else:
            print(f"{player} is incorrect. The correct answer is {correct_answer}.")

    def run_game(self):
        
        while True:
            if sum(self.scores.values()) >= 2000:
                winner = max(self.scores, key=self.scores.get)
                print(f"{winner} has reached 2000 points and won the game!")
                break

            for player in self.players:
                difficulty = self.get_difficulty()
                question, options, correct_answer = self.get_question(difficulty)
                print(f"{player}, here is a level {difficulty} question:")
                print(question)
                for option in options:
                    print(f"- {option}")
                answer = input("Enter your answer: ")
                self.check_answer(player, answer, correct_answer)
                print(f"Current scores: {', '.join(f'{k}: {v}' for k, v in self.scores.items())}")

if __name__ == "__main__":
    game = TriviaGame()
    game.welcome_players()
    game.run_game()
