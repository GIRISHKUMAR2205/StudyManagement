from django.urls import include,path
from . import views


urlpatterns=[
    path('',views.studylist,name='study_list'),
    path('form/<int:id>',views.studyform,name='study_update'),
    path('form/',views.studyform,name='study_form'),
    path('delete/',views.studydelete,name='study_delete'),
    path('<int:id>/',views.studyview,name='study_view'),
]