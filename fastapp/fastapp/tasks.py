from __future__ import absolute_import, unicode_literals
from celery import shared_task
import time

@shared_task
def add(x1, x2):
    print('処理開始')
    time.sleep(10)
    y = x1 + x2
    print('処理完了 ANS: '+str(y))
    return y


@shared_task
def text_input(x1,x2):
    print("処理開始")
    time.sleep(10)
    
    print('処理完了 ANS: '+ str(x2))
    return x2
