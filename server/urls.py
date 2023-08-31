







from django.urls import path
from .           import views


urlpatterns = [

    path('hello/',      views.hello_world, name='hello_world'  ),
    path('getFlicks/',  views.getFlicks,   name='getFlicks'    ),
    path('getPoster/',  views.getPoster,   name='getPoster'    ),
    path('getPosters/', views.getPoster,   name='getPosters'   ),
]