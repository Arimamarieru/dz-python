from django.shortcuts import render

from .models import UserName


def home(request):
    greeting = ""
    error = ""

    if request.method == "POST":
        name = request.POST.get("name", "").strip()

        if name:
            UserName.objects.create(name=name)
            greeting = f"Привет, {name}!"
        else:
            error = "Введите имя."

    return render(
        request,
        "greetings/index.html",
        {"greeting": greeting, "error": error},
    )
