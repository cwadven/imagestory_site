from django.shortcuts import render

# Create your views here.
def tutorial_list(request):
    return render(request, "tutorial.html", {})

def board_info(request):
    return render(request, "board_info.html", {})

def board_write(request):
    return render(request, "board_write.html", {})

def board_modify(request):
    return render(request, "board_modify.html", {})

def board_delete(request):
    return render(request, "board_delete.html", {})

def area_write(request):
    return render(request, "area_write.html", {})

def area_layer(request):
    return render(request, "area_layer.html", {})

def area_modify(request):
    return render(request, "area_modify.html", {})

def area_delete(request):
    return render(request, "area_delete.html", {})

def alert(request):
    return render(request, "alert.html", {})

def mypage(request):
    return render(request, "mypage.html", {})