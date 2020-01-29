"""this entire filed needed to be added, all it seems to do is
allow views to be assined from urls to templates.

So in order to access the stuff in your data base, you need to import the model, the tutorail
does not indicate the path and shows that it can not find it unless its there.

Once you have it imported, assigne it to a varaibal i.e. data then assigne that to a dictionary
name in the function's return value.
[]
"""




import random

from django.shortcuts import render
from question.models import Question
from question.forms import QuestionSelectForm

def homePage(request):



    try:
        selectedQuestion = request.GET ['selectedValue'];
    except:
        selectedQuestion = "L-1-1"


    optionBank = []; #empty array to establsih option bank.



    form = QuestionSelectForm(request.POST)
    data = Question.objects;
    entry = Question.objects.get(QuestionReferenceCode = selectedQuestion)

    optionBank.append((entry.answer,entry.answerDetails, True, 'Button1','selector1','descriptor1')) ## this appends the correct answer as the first item in the list.

    optionBank.append((entry.herring1,entry.herringDetails1, False, 'Button2','selector2','descriptor2'))
    optionBank.append((entry.herring2,entry.herringDetails2, False, 'Button3','selector3','descriptor3'))
    optionBank.append((entry.herring3,entry.herringDetails3, False, 'Button4','selector4','descriptor4'))
    optionBank.append((entry.herring4,entry.herringDetails4, False, 'Button5','selector5','descriptor5'))

    random.shuffle(optionBank);



    return render(request, 'home.html', {'optionBank': optionBank, 'testvariable': 'this Works', 'entry': entry, 'data':data, 'form':form, 'Qselect':selectedQuestion})
