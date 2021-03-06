from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers

from league import views

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'matches', views.MatchViewSet)
router.register(r'players', views.PlayerViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'kicker_league.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include([
        url(r'^$', views.IndexView.as_view(), name='index'),
        url(r'^set_mode$', views.set_mode, name='set_mode'),
        url(r'^players$', views.PlayerView.as_view(), name='players'),
        url(r'^players/top$', views.PlayerTop.as_view(), name='players_top'),
        url(r'^players/(?P<pk>\d+)$', views.PlayerDetailView.as_view(),
            name='player_detail'),
        url(r'^matches$', views.MatchView.as_view(), name='matches'),
        url(r'^matches/enter$', views.MatchCreate.as_view(),
            name='matches_enter'),
        url(r'^about$', views.about, name='about'),
        ], namespace='league')),
    url(r'api/', include(router.urls)),
]
