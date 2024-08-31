from django.urls import path
from . import views

app_name = "blogs"
urlpatterns = [
    path("categories/",views.CategoryList.as_view(),name="CategoriesList"),
    path("categories/<int:pk>/", views.CategoryDetail.as_view(),name = "CategoriesDetail"),
    path("register/",views.RegisterUser.as_view(), name = "RegisterUser"),
    path("login/",views.LoginUser.as_view(), name = "LoginUser")

]