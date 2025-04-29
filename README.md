# University-Project
This repository contains the files for a university project focused on managing and analyzing exam schedules and course conflicts. It includes an HTML-based exam timetable and a Python script for storing and analyzing course conflict data using the Neo4j graph database.
-----------------
This repository contains the files for a university project. It includes:

* `complete_exam_timetable.html`: An HTML file containing the exam timetable.
* `Neo4j.py`: A Python script to store course conflict data in a Neo4j graph database.

## Description

The project aims to manage and analyze university course schedules and potential conflicts. 
The `complete_exam_timetable.html` file provides a visual representation of the exam schedule. 
The `Neo4j.py` script processes course data to identify conflicts and stores this information in a graph database for further analysis and optimization of scheduling.

## Files Included

* **`complete_exam_timetable.html`**:
    *     This file displays the exam timetable in a user-friendly HTML format.
    *     It includes styling (CSS) to present the schedule clearly with color-coded periods and room usage information.

* **`Neo4j.py`**:
    *     This Python script uses the `neo4j` library to interact with a Neo4j graph database.
    *     It takes course data (presumably from a separate source, like a CSV or DataFrame) and creates nodes for courses and relationships for conflicts based on shared students.
    *     It's designed to help visualize and analyze course conflicts to improve scheduling.

## Usage

* To view the exam timetable, simply open the `complete_exam_timetable.html` file in any web browser.
* To run the `Neo4j.py` script, you need to have Python installed, along with the `neo4j` and `pandas` libraries.  You also need a running Neo4j database instance.  Modify the connection details in the script to match your Neo4j setup.

## Dependencies

* `neo4j` (Python library for Neo4j)
* `pandas` (Python library for data manipulation, if used in conjunction with this script)

## Author

Your Name  (Replace with your name)

## License

[Specify License, e.g., MIT License] (Optional)
