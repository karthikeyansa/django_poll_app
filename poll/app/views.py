from django.shortcuts import render,redirect
from .models import Question
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create(request):
    if request.method == 'POST':
        question = request.POST['question']
        choice1 = request.POST['choice1']
        choice2 = request.POST['choice2']
        newquestion = Question(question = question,choice1=choice1,choice2=choice2)
        newquestion.save()
        return redirect(home)
    else:
        return render(request,'polls/create.html')
@csrf_exempt
def vote(request,id):
    question = Question.objects.get(pk=id)
    if request.method == 'POST':
        selected = request.POST['choice']
        if selected == question.choice1:
            question.choice1_count += 1
            question.save()
        elif selected == question.choice2:
            question.choice2_count += 1
            question.save()
        else:
            return render(request,'polls/view.html')
        return redirect(home)
    else:
        return render(request,'polls/view.html')
@csrf_exempt
def home(request):
    polls = Question.objects.all().order_by('-id')
    return render(request,'polls/home.html',{'polls':polls})
@csrf_exempt
def view(request,id):
    poll = Question.objects.get(pk = id)
    context = {'poll':poll}
    return render(request,'polls/view.html',context)
@csrf_exempt
def delete(request,id):
    question = Question.objects.filter(pk = id).delete()
    return redirect(home)