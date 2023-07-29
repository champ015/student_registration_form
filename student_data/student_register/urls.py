from django.urls import path,include
from .import views 
urlpatterns=[
    path('',views.studform,name='insert'),

    path('<int:id>/',views.studform,name='updatedata'),

    path('Kanha/',views.studlist,name='data'),
    
    path('delete<int:id>/',views.deletedata,name='delete'),
] 