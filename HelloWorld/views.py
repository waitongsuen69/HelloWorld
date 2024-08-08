from django.http import HttpResponse
from django.shortcuts import render
 
def hello(request):
    return HttpResponse("Hello world !")

# def runoob(request):
#     context = {}
#     context['hello'] = 'halo chica!'
#     # return render(request, 'runoob.html', context)
    
def runoob(request):
    new_var = "mis amigos "
    my_list = ["my_list_0","my_list_1","my_list_2","my_list_3"]
    return render(request, "runoob.html", {"var":new_var, "list":my_list})