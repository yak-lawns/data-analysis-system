# main.py

from data_processor import DataProcessor
from data_visualizer import DataVisualizer
from report_generator import ReportGenerator

# Sample data
data = [1, 2, 3, 4, 5]

# Process data
processor = DataProcessor(data)
processor.process_data()

# Visualize data
visualizer = DataVisualizer(processor.data)
visualizer.visualize_data()

# Generate report
report_generator = ReportGenerator(processor.data)
report = report_generator.generate_report()
print(report)
