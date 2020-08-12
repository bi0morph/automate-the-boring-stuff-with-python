#! /usr/bin/env python
# randomQuizGenerator.py -Creates quizzes with questions and answers in
# random order, along with the answer key

import random, os

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau',
            "Arizona": 'Phoenix', 'Colorado': 'Denver',
            'Arkansas': 'Little Rock', 'California': 'Sacramento',
            'Connecticut': 'Hartford', 'Delaware': 'Dover',
            'Florida': 'Tallahassee', 'Idaho': 'Boise',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu',
            'Illinois': 'Springfield', 'Indiana': 'Indianapolis',
            'Iowa': 'Des Moines', 'Louisiana': 'Baton Rouge',
            'Kansas': 'Topeka', 'Kentucky': 'Frankfort',
            'Maine': 'Augusta', 'Maryland': 'Annapolis',
            'Massachusetts': 'Boston', 'Mississippi': 'Jackson',
            'Michigan': 'Lansing', 'Minnesota': 'Saint Paul',
            'Missouri': 'Jefferson City', 'Montana': 'Helena',
            'Nebraska': 'Lincoln', 'New Jersey': 'Trenton',
            'Nevada': 'Carson City', 'New Hampshire': 'Concord',
            'New Mexico': 'Santa Fe', 'New York': 'Albany',
            'North Carolina': 'Raleigh', 'Oklahoma': 'Oklahoma City',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg',
            'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
            'South Dakota': 'Pierre', 'Tennessee': 'Nashville',
            'Texas': 'Austin', 'Utah': 'Salt Lake City',
            'Vermont': 'Montpelier', 'West Virginia': 'Charleston',
            'Virginia': 'Richmond', 'Washington': 'Olympia',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quizNum in range(35):
    quizFile = open(os.path.join('capitalquiz', 'quiz%s.txt' % (quizNum + 1)), 'w')
    answerKeyFile = open(os.path.join('capitalquiz', 'answers%s.txt' % (quizNum + 1)), 'w')

    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write(' ' * 20 + 'State Capitals Quiz (Form %s' % (quizNum + 1))
    quizFile.write('\n\n')

    states = list(capitals.keys())
    random.shuffle(states)

    for questionNum in range(len(states)):

        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)

        answersOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answersOptions)

        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))
        for i in range(4):
            quizFile.write('    %s. %s\n' % ('ABCD'[i], answersOptions[i]))

        quizFile.write('\n')

        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answersOptions.index(correctAnswer)]))

    quizFile.close()
    answerKeyFile.close()
