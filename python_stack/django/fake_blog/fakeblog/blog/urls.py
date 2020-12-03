from django.urls import path
from . import views	# the . indicates that the views file can be found in the same directory as this file
                    
urlpatterns = [
    path('', views.root_method),
    path('blogs/', views.index),
    path('blogs/new/', views.new),
    path('create/', views.create),
    path('blogs/<int:my_val>', views.blog_num), 
    path('edit/<int:my_val>', views.edit),
    path('delete/', views.delete),
    path('jsonrep/', views.json_rep),

]