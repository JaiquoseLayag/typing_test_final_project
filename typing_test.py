# Import necessary built-in modules
import time 
import tkinter as tk

from word_generator import WordGenerator
from result_class import Result


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
# Display current word to type
        self.word_label = tk.Label(master, text="", font=('Arial', 18, 'bold'))
        self.word_label.pack(pady=5)
        self.entry = tk.Entry(master, font=('Arial', 14))
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.check_word)
# Label to show remaining time
        self.timer_label = tk.Label(master, text=f"Time left: {self.remaining_time}s", font=('Arial', 12))
        self.timer_label.pack()
        self.feedback = tk.Label(master, text="", font=('Arial', 12))
        self.feedback.pack()
 # Label to show final result
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

    if typed_word == displayed_word:
        self.correct += 1
        self.total += 1
        self.feedback.config(text="Correct!", fg='green')

        # Move to the next word
        self.entry.delete(0, tk.END)
        self.word_label.config(text=self.generator.get_word())
    else:
        self.total += 1
        self.feedback.config(text=f"Wrong! Try again.", fg='red')

        # Keep the same word; let user retype
        self.entry.delete(0, tk.END)
# Count down the time using after()
    def update_timer(self):
        if self.remaining_time > 0 and self.test_running:
            self.remaining_time -= 1
            self.timer_label.config(text=f"Time left: {self.remaining_time}s")
            self.master.after(1000, self.update_timer)
        else:
            self.end_test()
# End the test and show final results
    def end_test(self):
        self.test_running = False
        self.entry.config(state='disabled')
        elapsed_time = time.time() - self.start_time
        result = Result(self.correct, self.total, elapsed_time)
        self.feedback.config(text="Time's up!", fg='blue')
        self.stats.config(text=f"WPM: {result.words_per_minute()} | Accuracy: {result.accuracy()}%")
        self.restart_btn.config(text="Restart Test")