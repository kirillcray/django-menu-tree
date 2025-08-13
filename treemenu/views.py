from django.shortcuts import render


def make_tree_menu(request):
    template = "index.html"
    return render(request, template)
