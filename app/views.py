from django.http import HttpResponse


# Create your tests here.
def test(request):
    return HttpResponse('blabla')
