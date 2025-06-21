# Import random for random word selection
import random

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