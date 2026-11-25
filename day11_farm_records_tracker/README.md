Day 11 – Farm Records Tracker

Overview

A simple Python application that helps farmers record and manage daily farm activities using CSV files.

This project was built as part of my 30-Day Python Challenge (Week 2, Day 11).

Features

Create a farm records CSV file automatically.

Add new farm activity records.

View previously saved farm records.

Store records permanently using CSV files.

Validate quantity inputs to reject invalid numbers and negative values.

Interactive menu for navigating the application.

Technologies Used

Python

CSV module

OS module

File handling

Functions

Loops and conditionals

Exception handling (try and except)

Record Fields

Each farm record contains:

Date

Activity

Item

Quantity

Unit

Notes

How to Run

Make sure Python is installed.

Open a terminal in the project folder.

Run:

python farm_records_tracker.py

Project Structure

day11_farm_records_tracker/
├── farm_records_tracker.py
├── farm_records.csv
└── README.md

What I Learned

Reading and writing CSV files.

Using csv.writer() and csv.DictReader().

Creating reusable Python functions.

Using loops to build interactive menus.

Validating user input with try and except.

Saving and retrieving records from files.

Future Improvements

Add milk production records.

Add farm expense tracking.

Calculate daily and weekly totals.

30-Day Python Challenge – Day 11 Complete