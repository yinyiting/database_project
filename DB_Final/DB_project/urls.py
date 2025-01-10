from django.contrib import admin

from django.urls import path
from myapp.views import index, search_order
from myapp.views import movie_page
from myapp import views
from myapp.views import (
    index,
    search_order,
    get_branches_by_movie,
    get_showtimes_by_movie_and_branch,
    get_seats_for_show,
    check_phone
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # 修改：將 "/" 根路徑指向 home 視圖
    path('search_order/', search_order, name='search_order'),
    path('api/branches/<int:movie_id>/', get_branches_by_movie, name='get_branches_by_movie'),
    path('api/showtimes/<int:movie_id>/<str:branch>/', get_showtimes_by_movie_and_branch, name='get_showtimes_by_movie_and_branch'),
    path('api/seats/<int:show_id>/', get_seats_for_show, name='get_seats_for_show'),
    path('api/submit_ticket/', views.submit_ticket, name='submit_ticket'),
    path('quick_order/', views.quick_order, name='quick_order'),
    path('api/check_phone/', check_phone, name='check_phone'),
    path('movies/', movie_page, name='movie_page'),
    path('cancel_order/', views.cancel_order, name='cancel_order')
]
