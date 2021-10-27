from django.shortcuts import render

# Create your views here.
from celery.result import AsyncResult

from fastapp.tasks import add,text_input
from django_celery_results.models import TaskResult

def celery_test(request):
    if 'add_button' in request.POST:
        x = int(request.POST['input_a'])
        y = int(request.POST["input_b"])
        task_id = add.delay(x,y)

    result = list(TaskResult.objects.all().values_list("result",flat=True))
    if len(result) == 0:
        result[0] = 0
    context = {'result': result[0]}

    print(context)

    return render(request, 'testApp/celery_test.html', context)

def AI_chatBot(request):
    if 'sub_button' in request.POST:
        textA = str(request.POST['input_textA'])
        ANS_text = str(request.POST["input_ANS_text"])
        task_id = text_input.delay(textA,ANS_text)


    result = list(TaskResult.objects.all().values_list("result",flat=True))
        # print(result)
        # print("test")
    if len(result) == 0:
        result[0] = 0
    context = {'result': result[0]}
    # print(context)

    return render(request,"testApp/ai_bot_chat.html",context)



    

