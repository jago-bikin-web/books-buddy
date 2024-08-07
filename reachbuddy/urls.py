from django.urls import path
from reachbuddy.views import *

app_name = 'reachbuddy'

urlpatterns = [
    path('', show_reachbuddy, name='show_reachbuddy'),
    path('create-thread', create_thread, name='create_thread'),
    path('json/', show_json, name='show_json'), 
    path('json_book/', show_json_book, name='show_json_book'), 
    path('json_user/', show_json_user, name='show_json_user'), 
    path('json_user_id/<int:id>/', show_json_user_id, name='show_json_user_id'),
    path('trash_thread/<int:id>', trash_thread, name='trash_thread'),
    path('get-books/', get_books_json, name='get_books_json'),
    path('get-threads/', get_threads_json, name='get_threads_json'),
    path('get_book_json_id/<int:id>/', get_book_json_id, name='get_book_json_id'),
    path('get_profile_json_id/<int:id>/', get_profile_json_id, name='get_profile_json_id'),
    path('create_thread_ajax/<int:id>/', create_thread_ajax, name='create_thread_ajax'),
    path('thread_like/<int:id>/', thread_like, name='thread_like'),
    path('delete_thread_ajax/<int:id>/', delete_thread_ajax, name='delete_thread_ajax'),
    path('get-threads-flutter/', get_threads_flutter, name='get_threads_flutter'),
    path('get-thread-detail-flutter/<int:id>/', get_thread_detail_flutter, name='get_thread_detail_flutter'),
    path('create-thread-flutter/', create_thread_flutter, name='create_thread_flutter'),
    path('get-book-json-id-flutter/<int:id>/', get_book_json_id_flutter, name='get_book_json_id_flutter'),
]
