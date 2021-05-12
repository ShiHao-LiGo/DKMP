from django.conf.urls import url
from django.urls import path

from . import QA_view,entity_view,up_views,index_view,relation_view,annotation,over_view,ner_view,login_view
from .login_view import user
from .views import *
app_name = 'demo'
urlpatterns = [
    # path('',base),
    path('',over_view.over_view),
    path('login/',login_view.login, name="Login"),
    path('up/',annotation.local_a),
    path('shibie/',index_view.index),
    path('logout/',login_view.logout,name='Logout'),
    path('register/',login_view.register,name="register"),
    path('users/', user),
    path('overview/',over_view.over_view),
    path('q_a/',QA_view.q_a),
    path('annotating/',annotation.to_fileupload),
    path('local/',annotation.local,name='local'),
    path('relation/',entity_view.search_relation),
    path('test/',relation_view.relation),
    path('search_entity/',entity_view.entity),
    path('ER-post/',ner_view.ner_post),
    path('test_QA/',QA_view.QA1),
    path('testtupu/',relation_view.testtupu)
]


