# report_generator.py

class ReportGenerator:
    def __init__(self, data):
        self.data = data

    def generate_report(self):
        # Implement report generation logic here
        report = f"Data Report:\n\nData: {self.data}\n"
        return report
