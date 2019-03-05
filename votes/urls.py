from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'votes'
urlpatterns = [
    path('', views.index, name='index'),
    path('partylist/', views.party_list, name='partylist_list'),
    path('partylist/<int:partylist_id>/', views.det_partylist,
        name='detail_partylist'),    
    path('partylist/create/', views.cre_partylist, name='create_partylist'),
    path('partylist/update/<int:partylist_id>/', views.upd_partylist,
        name='update_partylist'),
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
    path('vote/', views.vote_view, name='vote_page'),
    path('vote/<int:position_id>/', views.vote_candidate,
        name='vote_candidates_pos'), 
    path('register/', views.registration, name='registration'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
