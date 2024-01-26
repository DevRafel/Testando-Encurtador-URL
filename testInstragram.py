import instaloader


L = instaloader.Instaloader()

username = 'instagram'

profile = instaloader.Profile.from_username(L.context, username)

L.download_profilepic(profile)
