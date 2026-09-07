from django.urls import path

from core.page_views import (
    InicioPageView,
)

from .views import (
    LoginView,
    LogoutView,
    PerfilView,
    RegisterView,
)


urlpatterns = [

    # ==========================================
    # INICIO
    # ==========================================

    path(
        "",
        InicioPageView.as_view(),
        name="inicio"
    ),


    # ==========================================
    # LOGIN
    # ==========================================

    path(
        "login/",
        LoginView.as_view(),
        name="login"
    ),


    # ==========================================
    # REGISTRO
    # ==========================================

    path(
        "register/",
        RegisterView.as_view(),
        name="register"
    ),


    # ==========================================
    # LOGOUT
    # ==========================================

    path(
        "logout/",
        LogoutView.as_view(),
        name="logout"
    ),


    # ==========================================
    # PERFIL
    # ==========================================

    path(
        "perfil/<int:id_usuario>/",
        PerfilView.as_view(),
        name="perfil"
    ),
]