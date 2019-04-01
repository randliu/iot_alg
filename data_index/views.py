from django.shortcuts import render,HttpResponse
import datetime
# Create your views here.
import logging

def current_datetime(request):
    now = datetime.datetime.now()
    logging.getLogger('run').info("now is :%s"%str(now))
    html = "<html><title>frequency domain </title><body>data index！<br>It is now %s.</body></html>" % now
    test_logger = logging.getLogger("test_logger")
    test_logger.info("bye")
    return HttpResponse(html)
