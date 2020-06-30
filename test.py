from plexapi.server import PlexServer
baseurl = 'http://192.168.1.99:32400'
token = 'cf7x1RsehzRbnvzRTqJn'
plex = PlexServer(baseurl, token)

# movies = plex.library.section('Movies')
# for video in movies.search(unwatched=True):
#     print(video.title)
    
    
# from plexapi.audio import Track
# for track in Track:
#     print(track.userRating)
    
# podcasts = plex.library.section('Podcasts')
# for podcast in podcasts.search(sort="addedAt:asc",maxresults=100,libtype="track",unwatched=True):

music = plex.library.section('Music')
tracks = music.searchTracks()
trackNum = len(tracks)
print("Number of tracks: ", trackNum)

for track in tracks:
    if track.userRating > 0:
        print(track.title, ": ", track.userRating)
