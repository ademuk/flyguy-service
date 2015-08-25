from django.conf.urls import url, include
from rest_framework import routers
import views

router = routers.DefaultRouter()
router.register(r'flights', views.FlightViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'', include(router.urls)),
    url(r'^users/$', views.UserCreateView.as_view()),
    url(r'^token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^email-confirmation/', include('email_confirm_la.urls')),
]
