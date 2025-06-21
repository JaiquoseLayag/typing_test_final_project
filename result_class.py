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