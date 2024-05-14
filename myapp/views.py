import logging
#from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Index page accessed')
    return HttpResponse("Hello World")


def about(request):
    try:
        # some code that might raise an exception
        result = 1 / 0
    except Exception as e:
        logger.exception(f'Error in about page: {e}')
        return HttpResponse("Ooops, somethong went wrong.")
    else:
        logger.debug('About page accessed')
        return HttpResponse('This is about page.')