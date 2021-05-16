from django.conf.urls import url
from django.urls import path

from . import QA_view,entity_view,index_view,relation_view,up_load,over_view,ner_view,login_view
from .login_view import user
from .views import *
app_name = 'demo'
urlpatterns = [
    # path('',base),
    path('',over_view.over_view),
    path('login/',login_view.login, name="Login"),
    path('up/', up_load.local),
    path('shibie/',index_view.index),
    path('logout/',login_view.logout,name='Logout'),
    path('register/',login_view.register,name="register"),
    path('users/', user),
    path('overview/',over_view.over_view),
    path('q_a/',QA_view.q_a),
    path('annotating/', up_load.to_fileupload),
    path('local/', up_load.local, name='local'),
    path('relation/',entity_view.search_relation),
    path('test/',relation_view.relation),
    path('search_entity/',entity_view.entity),
    path('ER-post/',ner_view.ner_post),
    path('test_QA/',QA_view.QA1),
    path('testtupu/',relation_view.testtupu)
]


