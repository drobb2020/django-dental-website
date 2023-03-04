from django.core.mail import send_mail
from django.shortcuts import render


def index(request):
    context = {}
    return render(request, "core/index.html", context)


def about(request):
    context = {}
    return render(request, "core/about.html", context)


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        # phone = request.POST["phone"]
        message = request.POST["message"]
        # send email
        send_mail(
            name,
            message,
            email,
            ['drobb2011@gmail.com'],
            fail_silently=False,
        )
        context = {'name': name}
        return render(request, "core/contact.html", context)
    else:
        context = {}
        return render(request, "core/contact.html", context)


def test(request):
    context = {}
    return render(request, "core/test.html", context)
