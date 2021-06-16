from django.urls import path
from . import views

urlpatterns = [
    path('register.html', views.registerPage, name='register'),
    path('login.html', views.loginPage, name='login'),
    path('logout', views.logoutPage, name='logout'),
    path('', views.homePage, name='index'),
    path('homepage.html', views.homePage, name='index'),
    path('question.html', views.newQuestionPage, name='new-question'),
    path('question/<int:id>', views.questionPage, name='question'),
    path('reply', views.replyPage, name='reply'),
    path('body/<int:id>', views.questionPage, name='question'),
    path('notice.html/', views.notice, name='notice')
]
