from django.shortcuts import render


rooms = [
    {'id': 1, 'name': "Let's learn Python"},
    {'id': 2, 'name': "Learn Vue.js"},
    {'id': 3, 'name': "Build with Django"}
]


def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
            break

    context = {'room': room}

    return render(request, 'base/room.html', context)
