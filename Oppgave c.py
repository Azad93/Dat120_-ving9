# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 22:24:09 2021

@author: Azat Kaplan
"""

# DAT120 øving 8: Dictionaries, klasser og objekter

# Oppgave c)

class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     "What color are apples?\n(a) Red/Green\n(b)Orange: ",
     "What color are bananas?\n(a) Red/Green\n(b)Yellow: ",
]

questions = [
     Question(question_prompts[0], "a"),
     Question(question_prompts[1], "b"),
]

def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
     print("you got", score, "out of", len(questions))

run_quiz(questions)


