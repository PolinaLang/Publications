from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime
from mysite import settings
from web.models import Publication


def index(request):
    return render(request, 'index.html')


def status(request):
    return render(request, 'status.html')


def publication(request, number):
    pubs = Publication.objects.filter(id=number)

    if len(pubs) == 1:
        pub = model_to_dict(pubs[0])
        return render(request, 'publication.html', pub)
    else:
        return redirect('/')


def publications(request):
    return render(request, 'publications.html', {
        'publications': Publication.objects.all()
    })


def publish(request):
    if request.method == 'GET':
        return render(request, 'publish.html')
    else:
        name = request.POST['name']
        password = request.POST['password']
        text = request.POST['text']

        if password != settings.SECRET_KEY:
            return render(request, 'publish.html', {
                'error': 'Incorrect password'
            })
        if len(name) == 0 or len(text) == 0:
            return render(request, 'publish.html', {
                'error': 'Null data'
            })

        Publication(
            name=name,
            date=datetime.now(),
            text=text.replace('\n', '<br>')
        ).save()
        return redirect('/publications')


