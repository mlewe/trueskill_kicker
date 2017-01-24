from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import render
from league.models import Player, Match


class MatchAdmin(admin.ModelAdmin):
    change_list_template = 'admin/league/match_list.html'

    list_display = ('score', 'team1_player1', 'team1_player2', 'team2_player1',
            'team2_player2', 'timestamp')
    list_filter = ('timestamp',)

    def get_urls(self):
        urls = super(MatchAdmin, self).get_urls()
        new_urls = [
            url(r'^reorder/$', self.admin_site.admin_view(self.reorder),
                name='league_match_reorder')
        ]
        return new_urls + urls

    def reorder(self, request):
        from league.helper import reorder_scores
        reorder_scores()
        context = {
            'opts': self.model._meta,
            'title': 'Reordering scores has been successful!',
        }
        return render(request, 'admin/league/refresh.html', context)


class PlayerAdmin(admin.ModelAdmin):
    change_list_template = 'admin/league/player_list.html'

    list_display = ('name', 'rank', 'attacker_rank', 'defender_rank')

    def get_urls(self):
        urls = super(PlayerAdmin, self).get_urls()
        new_urls = [
            url(r'^refresh/$', self.admin_site.admin_view(self.refresh),
                name='league_player_refresh')
        ]
        return new_urls + urls

    def refresh(self, request):
        from league.helper import refresh_scores
        refresh_scores()
        context = {
            'opts': self.model._meta,
            'title': 'Refreshing scores has been successful!',
        }
        return render(request, 'admin/league/refresh.html', context)

admin.site.register(Player, PlayerAdmin)
admin.site.register(Match, MatchAdmin)
