# Import random for random word selection
import random
from difficulty_manager import DifficultyManager

# Define a class to manage and return random words
class WordGenerator:
    def __init__(self, difficulty="medium"):
        self.manager = DifficultyManager()
        self.words = self.manager.get_words(difficulty)

    def get_word(self):
        return random.choice(self.words)