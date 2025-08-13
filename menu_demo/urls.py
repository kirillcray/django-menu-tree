import debug_toolbar
from django.contrib import admin
from django.urls import include, path, re_path
from treemenu import views

# Create your views here.
urlpatterns = [
    path("__debug__/", include(debug_toolbar.urls)),
    path("admin/", admin.site.urls),
    re_path(r"^.*$", views.make_tree_menu, name="index"),
]
