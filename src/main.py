import yt_dlp as yt

yt.YoutubeDL({'format': 'best', 'outtmpl': '%(title)s.%(ext)s'}).download(['https://youtube.com/shorts/kQ1QMl6tCZQ?si=-pFljHaY17IZ2FSY'])