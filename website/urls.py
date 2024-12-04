from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # pages for all users
    path('', views.login, name='login'),
    path('home', views.home, name='home'),
    path('books/', views.books, name='books'),
    path('lectures/', views.lectures, name='lectures'),  # No subject_id
    path('lectures/<int:subject_id>/', views.lectures, name='lectures'),
    
    # pages for admins
    path('upload/', views.upload_page, name='upload'),
    path('upload/book/', views.upload_book, name='upload_book'),
    path('upload/lecture/', views.upload_lecture, name='upload_lecture'),
    path('logout/', views.logout_view, name='logout'),  # This is the logout URL
    path('delete/<str:item_type>/<int:item_id>/', views.delete_item, name='delete_item'),
    path('edit/<str:item_type>/<int:item_id>/', views.edit_item, name='edit_item'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)