# Import necessary built-in modules
import random
import time 

# Define a class to manage and return random words
class WordGenerator:
    def __init__(self):
# Store word list
        self.words = [
            'python', 'keyboard', 'function', 'variable', 'loop', 'syntax', 'object',
            'method', 'inheritance', 'class', 'string', 'integer', 'boolean', 'tuple',
            'list', 'dictionary', 'module', 'package', 'exception', 'lambda', 'return',
            'encapsulation', 'recursion', 'framework', 'backend', 'frontend',
            'compiler', 'interpreter', 'debugging', 'iteration', 'algorithm',
            'development', 'deployment', 'parameter', 'argument', 'constructor',
            'destructor', 'virtual', 'static', 'mutable'
        ]
# Return one random word each time
    def get_word(self):
        return random.choice(self.words)

# Define a class to handle result calculation
class Result:
# Store correct answers, total attempts, and time elapsed
     def __init__(self, correct, total, time_elapsed):
        self.correct = correct
        self.total = total
        self.time_elapsed = time_elapsed
# Calculate WPM (words per minute)
    def words_per_minute(self):
        return round((self.correct / self.time_elapsed) * 60, 2) if self.time_elapsed > 0 else 0
# Calculate typing accuracy
     def accuracy(self):
        return round((self.correct / self.total) * 100, 2) if self.total > 0 else 0

# Define the main typing test class
# Build the GUI interface (labels, entry box, buttons)
# Initialize counters and timer
# Start the typing test when user clicks Start
# Display words and handles typing logic
# Check typed words for correctness
# Update feedback and stats
# Count down the time using after()
# End the test and show final results

# Define the app launcher class
# Initialize and run the tkinter main loop

# Entry point: run the app only if this file is executed directly
