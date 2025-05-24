# Text Classification for Sentiment Analysis

This is a beginner-friendly program that can tell whether a piece of text is positive or negative. It's perfect for learning the basics of machine learning using Python and scikit-learn.

## What Does This Program Do?

This program reads text and decides if the message is positive or negative. Think of it like teaching a computer to understand emotions in text, similar to how we understand emoji meanings! 

The program uses three main parts:
1. A tool to convert words into numbers that the computer can understand
2. A simple learning model that learns patterns from examples
3. A friendly interface where you can type sentences and get results

## What You Need to Install

You need Python installed on your computer and two extra packages:

First package: pandas (for handling data)
Second package: scikit-learn (for machine learning)

To install these, open your command prompt or terminal and type:

    pip install pandas scikit-learn

## About the Training Data

The program learns from a file called "sentiment_dataset.csv". This file should be like a spreadsheet with two columns:
1. A column called "text" with example messages
2. A column called "label" that says if each message is positive or negative

## How to Use the Program

1. First, make sure you have installed everything needed
2. Put the "sentiment_dataset.csv" file in the same folder as the program
3. Open your command prompt or terminal
4. Go to the folder containing the program
5. Type: python text_classification.py
6. The program will start and ask you to type a message
7. Type any message you want to analyze
8. To stop the program, just type "exit" or "quit"

## Example of Using the Program

When you run the program, it works like this:

    Program: "Enter a sentence to analyze sentiment:"
    You type: "I really enjoyed this movie"
    Program tells you: "Predicted sentiment: positive"

    Program: "Enter a sentence to analyze sentiment:"
    You type: "This was a terrible experience"
    Program tells you: "Predicted sentiment: negative"

## What You Can Learn From This

This project helps you understand:
1. How to prepare text for a computer to understand it
2. How computers can learn from examples
3. How to make predictions using what the computer learned
4. How to create a simple program that users can interact with

## Room for Improvement

This is a basic version meant for learning. If you want to make it better, you could:
1. Add more training examples
2. Use more advanced text processing
3. Add ways to check how accurate the program is
4. Try different types of learning models
5. Make the program handle more complex sentences 
