from django.urls import path, include
from . import views
from rest_framework import routers


app_name = 'app'

router = routers.DefaultRouter()
router.register('app', views.text_restful)

urlpatterns = [
    #path('', views.main, name='main'),
    path('text_insert', views.text_insert, name='text_insert'),
    path('text_delete/<int:pk_id>', views.text_delete, name='text_delete'),
    path('text_update/<int:pk_id>', views.text_update, name='text_update'),
    path('api', include((router.urls, 'app'), namespace='api')),
]