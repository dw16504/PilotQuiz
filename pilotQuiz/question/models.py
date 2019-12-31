## recovered

from django.db import models

class Question(models.Model):
    QUESTION_TYPE = (
        ('M', 'Multiple Choice'),
        ('F', 'Fill in the Blank'),
        ('O', 'Options'),
    )

    TOPIC_OPTIONS = (
        ('L', 'Limitations'),
        ('S', 'Systems'),
        ('O', 'Operations & OPV'),
    )

    LEVEL_OPTIONS = (
        ('1', 'Required Knowlege'),
        ('2', '80 Percent Item'),
        ('3', 'probable Understanding'),
        ('4', 'Indicates good understanding'),
        ('5', 'Indicates material mastery'),
        ('6', 'Stump the Chump'),

    )

    questionType = models.CharField(max_length = 2, null = True, choices =QUESTION_TYPE);
    topic = models.CharField(max_length=15, null = True, choices = TOPIC_OPTIONS);
    level = models.CharField(max_length=3, null = True, choices = LEVEL_OPTIONS);
    QuestionReferenceCode = models.CharField(max_length=5, null = True)


    questionText = models.CharField(max_length=200, null = True)

    answer = models.CharField(max_length = 150, null = True)
    answerDetails = models.CharField(max_length = 200, null = True)





    herring1 = models.CharField(max_length = 150, null = True)
    herringDetails1 = models.CharField(max_length = 200, null = True)
    herring2 = models.CharField(max_length = 150, null = True)
    herringDetails2 = models.CharField(max_length = 200, null = True)
    herring3 = models.CharField(max_length = 150, null = True)
    herringDetails3 = models.CharField(max_length = 200, null = True)
    herring4 = models.CharField(max_length = 150, null = True)
    herringDetails4 = models.CharField(max_length = 200, null = True)

    reference = models.CharField(max_length = 30, null = True)
    explanation = models.CharField(max_length = 350, null = True)
