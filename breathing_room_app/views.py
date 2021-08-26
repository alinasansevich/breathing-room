from django.shortcuts import render

def index(request):
    """The home page for Breathing Room."""
    return render(request, 'breathing_room_app/index.html')


def exercises(request):
    """Breathing exercises instructions for Breathing Room users."""
    return render(request, 'breathing_room_app/exercises.html')