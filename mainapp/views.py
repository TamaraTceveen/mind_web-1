from django.shortcuts import render


def index(request):
    """
    main page
    """
    title = 'главная'
    content = {
        "title": title,
    }
    return render(request, 'mainapp/index.html', context=content)


def service(request):
    """
    service page
    """
    title = 'MindWeb - услуги'
    content = {
        "title": title,
    }
    return render(request, 'mainapp/service.html', context=content)


def team(request):
    """
    team page
    """
    title = 'MindWeb - команда'
    content = {
        "title": title,
    }
    return render(request, 'mainapp/team.html', context=content)


def order(request):
    # print(request.method)
    if request.method == 'POST':
        form_data = request.data
        print(form_data)
    return render(request, 'mainapp/team.html')