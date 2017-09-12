from videos.models import Video
from playlists.models import Playlist
from categories.models import Category
from datetime import date, timedelta

def private_data(request):
    # all categories
    categories = Category.objects.all()
    # all playlists
    playlists = Playlist.objects.all()
    # 7 days ago
    d = date.today()-timedelta(days=7)
    # all videos posted 7 days ago
    latests = Video.objects.filter(date_added__gte=d).order_by('-date_added')[:10]
    return {
        'categories': categories,
        'playlists': playlists,
        'latests': latests
    }