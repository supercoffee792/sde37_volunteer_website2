from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # user login
    path('login', login, name="login"),
    path('signup', signup, name="signup"),
    path("logout/", VolunteerLogout.as_view(), name="volunteer_logout"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("volunteer_info/", VolunteerTokenInfo.as_view(), name="volunteer_token_info"),

    # volunteers
    path("volunteers/", get_volunteers, name="get_volunteers"),
    path("volunteers/create", create_volunteer, name="create_volunteers"),
    path("volunteers/<int:pk>", manage_volunteer, name="manage_volunteers"),
    path("volunteers/<int:pk>/notifications/", get_notifications, name="get_notifications"),
    
    # events
    path("events/", get_events, name="get_events"),
    path("events/create", create_event, name="create_events"),
    path("events/<int:pk>", manage_event, name="manage_event"),
    path("events/<int:pk>/signup/", event_signup, name="event_signup"),
    path("events/one/<int:pk>", get_one_event, name="get_one_event"),

    # report modules
    path('pdf/', generate_pdf, name='generate_pdf')
]