"""this entire filed needed to be added, all it seems to do is
allow views to be assined from urls to templates.

So in order to access the stuff in your data base, you need to import the model, the tutorail
does not indicate the path and shows that it can not find it unless its there.

Once you have it imported, assigne it to a varaibal i.e. data then assigne that to a dictionary
name in the function's return value.
[]
"""






from django.shortcuts import render
from question.models import Question
from question.forms import QuestionSelectForm

def homePage(request):

    selectedQuestion = request.GET ['selectedValue'];
    print(selectedQuestion);

    form = QuestionSelectForm(request.POST)
    data = Question.objects;
    entry = Question.objects.get(QuestionReferenceCode = selectedQuestion)

    return render(request, 'home.html', {'testvariable': 'this Works', 'entry': entry, 'data':data, 'form':form, 'Qselect':selectedQuestion})
