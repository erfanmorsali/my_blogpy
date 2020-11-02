from django.urls import path

from .views import login_page, log_out, user_home,sidebar_render_partial

urlpatterns = [
    path('accounts/', user_home, name='user_profile'),
    path('accounts/login/', login_page, name='login_page'),
    path('accounts/logout/', log_out, name='logout'),
    path('side_bar_render_partial', sidebar_render_partial, name='side_bar_render_partial'),
]
