# Student Support Office Case Study

This project automates basic student data checking for a university support office.

## Problem Solved

- Identify students with marks less than 12.
- Validate student email format using regex.
- Generate a summary report file.
- Provide terminal output as proof of execution.

## Project Files

- `caseStudy.py` - Main Python script
- `students.csv` - Input data file
- `report.txt` - Generated report output

## Requirements

- Python 3.x

## How to Run

From the project folder, run:

```bash
c:/python314/python.exe caseStudy.py
```

If your Python path is different, use:

```bash
python caseStudy.py
```

## Email Validation Regex

```regex
^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$
```

## Sample Terminal Output

```text
=== Student Data Check ===
Total students processed: 6

Students with marks less than 12:
- Bilal Ahmed (mark: 9)
- Sara Noor (mark: 11)
- Mina Ali (mark: 7)

Students with invalid email format:
- Sara Noor (email: sara.noor@uni)
- Mina Ali (email: mina ali@uni.edu)

Report generated: report.txt
```

## Report Output

The script creates `report.txt` containing:

- Total students processed
- Students with marks below 12
- Students with invalid email format

## Suggested Evidence for Submission

- Screenshot of terminal command and output
- Screenshot of generated `report.txt`
