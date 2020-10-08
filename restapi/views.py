from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.

def home(request):
    return HttpResponse('hello django')

def taskstring(request):
    result = 'Rest API string'
    return HttpResponse(result,content_type='text/plain')

def taskxml(request):
    result = '''
            <employees>
                <employee>
                    <firstname>John</firstname>
                    <lastname>Doe</lastname>
                </employee>
                <employee>
                    <firstname>Anna</firstname>
                    <lastname>Smith</lastname>
                </employee>
            </employees>
    '''
    return HttpResponse(result,content_type='text/xml')

def taskjson(request):
    result = {
                'employees':[
                    {'firstname':'John','lastname':'Doe'},
                    {'firstname':'Anna','lastname':'Smith'},
                    {'firstname':'Peter','lastname':'Jones'}
                ]
    }

    return JsonResponse(result)


