# Task 1: Advanced BMI Calculator

## Project Overview

The Advanced BMI Calculator is a Python-based application designed to calculate and visualize Body Mass Index (BMI). Developed as part of an internship with **Oasis Infobyte**, this project features a graphical user interface (GUI) built using Tkinter and data management with SQLite3. The application provides users with an intuitive way to monitor their BMI and view trends over time.

## Features

- **User Input Validation**: Ensures that the input values for weight and height are positive and valid.
- **BMI Calculation and Categorization**: Computes BMI and classifies it into categories such as Underweight, Normal Weight, Overweight, and Obesity.
- **Data Storage**: Saves user data including weight, height, BMI, and the date in an SQLite database.
- **Data Visualization**: Uses Matplotlib to display historical BMI trends through graphs.

## Getting Started

### Prerequisites

- Python 3.x
- Tkinter
- SQLite3
- Matplotlib
- Pandas

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/advanced-bmi-calculator.git
    cd advanced-bmi-calculator
    ```

2. Install required libraries:
    ```bash
    pip install matplotlib pandas
    ```

### Usage

1. Run the application:
    ```bash
    python bmi_calculator.py
    ```

2. Enter weight and height values into the respective input fields.
3. Click on "Calculate BMI" to get the BMI result and category.
4. Click on "Show BMI Trend" to visualize the historical BMI data.

### Code Overview

- `bmi_calculator.py`: Contains the main application code including GUI setup, BMI calculation, data storage, and visualization.
- `bmi_data.db`: SQLite database file used to store user data.

## Project Details

- **User Input Validation**: Checks if the height and weight are positive values and handles errors gracefully.
- **BMI Calculation**: Uses the formula `BMI = weight (kg) / (height (m))^2` to compute the BMI.
- **Categorization**: Classifies BMI into Underweight, Normal Weight, Overweight, and Obesity based on predefined ranges.
- **Data Storage**: Utilizes SQLite3 to store and manage BMI records.
- **Data Visualization**: Employs Matplotlib to create graphs of BMI trends over time.


## Acknowledgments

- **Oasis Infobyte**: For providing the opportunity to work on this project.
- **Matplotlib**: For enabling data visualization.
- **SQLite3**: For managing the database.
