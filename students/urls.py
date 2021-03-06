from django.conf.urls import url
from students import views

app_name = 'students'


urlpatterns =[
    url(r'^$',views.StudentsListView.as_view(),name='student_list'),
    url(r'^student/new/$', views.StudentsCreateView.as_view(), name='student_new'),
    url(r'^(?P<pk>\d+)/$',views.StudentsDetailView.as_view(),name='detail'),
    url(r'^student/(?P<pk>\d+)/edit/$', views.StudentsUpdateView.as_view(), name='student_edit'),
]
