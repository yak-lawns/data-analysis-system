# data_processor.py

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def process_data(self):
        # Implement data processing logic here
        # For simplicity, let's just double each data point
        self.data = [x * 2 for x in self.data]
