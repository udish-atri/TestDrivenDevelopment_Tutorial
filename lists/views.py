from django.shortcuts import render


def home_page(request):
    # if request.method == "POST":
    #     return HttpResponse("You submitted: " + request.POST["item_text"])
    # # return HttpResponse("<html><title>To-Do lists</title></html>")
    # return render(request, "home.html")
    return render(
        request, "home.html", {"new_item_text": request.POST.get("item_text", "")}
    )
