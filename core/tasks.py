import django_rq

from .utils import update_fib_number_assinc


def fib_assinc(fib_number):
    queue = django_rq.get_queue()
    queue.enqueue(update_fib_number_assinc, fib_number)
