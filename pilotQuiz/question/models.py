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


    questionText = models.CharField(max_length=200, null = True, blank = True)

    answer = models.CharField(max_length = 150, null = True, blank = True)
    answerDetails = models.CharField(max_length = 200, null = True, blank = True)





    herring1 = models.CharField(max_length = 150, null = True, blank = True)
    herringDetails1 = models.CharField(max_length = 200, null = True, blank = True)
    herring2 = models.CharField(max_length = 150, null = True, blank = True)
    herringDetails2 = models.CharField(max_length = 200, null = True, blank = True)
    herring3 = models.CharField(max_length = 150, null = True, blank = True)
    herringDetails3 = models.CharField(max_length = 200, null = True, blank = True)
    herring4 = models.CharField(max_length = 150, null = True, blank = True)
    herringDetails4 = models.CharField(max_length = 200, null = True, blank = True)

    reference = models.CharField(max_length = 30, null = True, blank = True)
    explanation = models.CharField(max_length = 350, null = True, blank = True)

    image  = models.ImageField(upload_to = 'images/', null = True, blank = True)
