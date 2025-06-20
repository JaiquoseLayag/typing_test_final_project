# Import necessary built-in modules
import random
import time 
import tkinter as tk

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
class TypingTest:
# Build the GUI interface (labels, entry box, buttons)
    def __init__(self, master, duration=60):
        self.master = master
        self.master.title("Typing Speed Test - Timed Mode")
# Initialize counters and timer
        self.duration = duration
        self.remaining_time = duration
        self.correct = 0
        self.total = 0
        self.test_running = False
        self.start_time = None
        self.generator = WordGenerator()
        self.label = tk.Label(master, text="Type the word below before time runs out:", font=('Arial', 14))
        self.label.pack(pady=10)
        self.word_label = tk.Label(master, text="", font=('Arial', 18, 'bold'))
        self.word_label.pack(pady=5)
        self.entry = tk.Entry(master, font=('Arial', 14))
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.check_word)
        self.timer_label = tk.Label(master, text=f"Time left: {self.remaining_time}s", font=('Arial', 12))
        self.timer_label.pack()
        self.feedback = tk.Label(master, text="", font=('Arial', 12))
        self.feedback.pack()
        self.stats = tk.Label(master, text="", font=('Arial', 12))
        self.stats.pack(pady=10)
        self.restart_btn = tk.Button(master, text="Start Test", command=self.start_test)
        self.restart_btn.pack(pady=5)
        self.entry.config(state='disabled')
# Start the typing test when user clicks Start
    def start_test(self):
        self.correct = 0
        self.total = 0
        self.remaining_time = self.duration
        self.test_running = True
        self.start_time = time.time()
# Display words and handles typing logic
        self.word_label.config(text=self.generator.get_word())
        self.feedback.config(text="")
        self.stats.config(text="")
        self.timer_label.config(text=f"Time left: {self.remaining_time}s")
        
        self.entry.config(state='normal')
        self.entry.delete(0, tk.END)
        self.entry.focus()
        self.update_timer()
# Check typed words for correctness
    def check_word(self, event=None):
        if not self.test_running:
            return

        typed_word = self.entry.get().strip()
        displayed_word = self.word_label.cget("text")
        self.total += 1

        if typed_word == displayed_word:
            self.correct += 1
            self.feedback.config(text="Correct!", fg='green')
        else:
            self.feedback.config(text=f"Wrong! ({displayed_word})", fg='red')
            
        self.entry.delete(0, tk.END)
        self.word_label.config(text=self.generator.get_word())

# Count down the time using after()
# End the test and show final results

# Define the app launcher class
# Initialize and run the tkinter main loop

# Entry point: run the app only if this file is executed directly
