# Import tkinter and the TypingTest class
import tkinter as tk
from typing_test import TypingTest

# Define the app launcher class
class TypingTestApp:
# Initialize and run the tkinter main loop
    def __init__(self):
        self.root = tk.Tk()
        self.test = TypingTest(self.root, duration=60)

    def run(self):
        self.root.mainloop()
# Entry point: run the app only if this file is executed directly
if __name__ == "__main__":
    app = TypingTestApp()
    app.run()