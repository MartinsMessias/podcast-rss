from podgen import Episode, Media, Podcast, Person, htmlencode
from datetime import datetime
import pytz

# Create the Podcast
podcast = Podcast(
    name="William Shakespeare Podcast",
    website="https://www.pensador.com/autor/william_shakespeare/",
    explicit=False,
    image="https://image.flaticon.com/icons/png/512/1312/1312585.png",
)

podcast.description = "William Shakespeare fala sobre a vida."
podcast.feed_url = "https://storage.googleapis.com/martins_lab1/rss.xml"
podcast.authors.append(Person("Eddie Giovanne", "eddie@uos.de"))
podcast.authors.append(Person("Messias Martins", "messias@uos.de"))

# Add some episodes
podcast.episodes += [
    Episode(
        title="Episódio 1 - Dúvidas",
        publication_date=datetime(2021, 4, 21, 13, 37, 10, tzinfo=pytz.utc),
        media=Media(
            "https://storage.googleapis.com/martins_lab1/podcast.mp3", size=359280
        ),
        summary="Nossas dúvidas são traidoras e nos fazem perder o que, com frequência, poderíamos ganhar, por simples medo de arriscar.",
    ),
]

# Generate the RSS Feed
rss = podcast.rss_file(filename="ws_rss.xml")