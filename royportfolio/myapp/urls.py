from django.contrib import admin
from django.urls import path , include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('',views.home, name="home"),
    path('aboutme',views.aboutme, name="aboutme"),
    path('contactme/',views.contactme, name="contactme"),

    path('allblog',views.allblog, name="allblog"),
    path('blogdetails/<slug:post_slug>',views.blogdetails, name="blogdetails"),
#     path('blog/<slug:post_slug>', views.blogdetails , name='blogdetails'),

    path('allproject',views.allproject, name="allproject"),
    path('projectdemo/<slug:post_slug>',views.projectdemo, name="projectdemo"),

    path('register',views.register, name="register"),
    path('login_view/',views.login_view, name="login_view"),
    path('logout/',views.logout_view, name='logout'),
    # path('signup',views.signup, name="signup"),
    # path('login',views.login, name="login"),
    # path('logout',views.logout, name="logout"),
]
# ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
