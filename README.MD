Week 1 Python and Data Engineering Assessment
Project Overview
This project analyzes employee and department data using Python, NumPy, Pandas, Matplotlib, REST APIs, JSON, and Git.
Project Structure
data/ — Employee CSV and JSON data
src/ — Python task scripts
notebooks/ — Jupyter notebook and exported Python script
reports/ — Charts and analysis reports
requirements.txt — Required Python packages
Setup Instructions
Install Python and Git.
Clone this repository.
Create a virtual environment using python -m venv .venv.
Activate the virtual environment.
Install packages using python -m pip install -r requirements.txt.
Create a local .env file if API credentials are required.
Run the scripts from the project root.
Run the Assessment
Task 1: python src/task1.py
Task 2: python src/task2.py
Task 3: python src/task3.py
Notebook: jupyter notebook
Five Key Findings
The dataset contains eight employee records.
Five employees earn more than 50,000.
Chennai has four employees.
IT has the highest headcount, with three employees.
Marketing has no employees and appears in the outer join.
Data Cleaning
Two missing salaries were introduced in a separate test dataset and filled using the median. A duplicate record was also introduced and removed. The original employee CSV remains unchanged.
Charts
The project generates bar, histogram, scatter, and line charts in the reports/ directory.
Security
API credentials must be stored locally in .env. The .env file must not be committed to Git.
Conclusion
This project demonstrates Python fundamentals, object-oriented programming, data processing, API handling, data visualization, and version control.
jupyter : The term 'jupyter' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, 
or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ jupyter nbconvert --to script notebooks/analysis.ipynb --output-dir=n ...
+ ~~~~~~~
    + CategoryInfo          : ObjectNotFound: (jupyter:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
    