from django.urls import path
from votes import views

app_name = 'votes'
urlpatterns = [
    path('', views.index, name='index'),
    path('candidate/', views.cand_list, name='candidates_list'),
    path('candidate/<int:candidate_id>/', views.det_candidate,
        name='detail_candidate'),
    path('candidate/create/', views.cre_candidate, name='create_candidate'),
    path('candidate/update/<int:candidate_id>/', views.upd_candidate,
        name='update_candidate'),
    path('position/', views.det_position, name='detail_position'),
    path('position/create/', views.create_position, name='create_position'),
    path('position/update/<int:position_id>/', views.upd_position,
        name='update_position'),
    path('candidate/<int:candidate_id>/vote', views.vote, name='vote'),
    path('register/', views.registration, name='registration'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout')
]