# Spotify Recommendation Engine

It has been my dream for some time to be able to get an internship in spotify.

Because of this, I am making some projects to learn new things, put on my resume,
and hopefully land it!

This project will be a spotify song recommendation engine, in which I am striving
to emulate spotify's idea of DJ and general recommendation feature.

## How it works

- authentication with Spotify through OAuth using refresh token flow
- using the spotify api, find your personal top tracks
- attach genre information and track meta data to songs (see design decisions)
- encode information into binary feature vectors and weighted values for duration
- compute cosine similarity between all tracks and find closest matches

## Setup

- Clone the repo and create a virtual environment using:

``````zshrc
python3 -m venv venv
source venv/bin/activate
pip install requests python-dotenv pandas scikit-learn
``````

- register an app at [developer.spotify.com](https://developer.spotify.com)
and select Web API
- create an `.env` file with:

```python-dotenv
CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
REFRESH_TOKEN=your_refresh_token
```

- Run `python3 similarity.py`

## Design decisions

### Note 1

Originally I was going to use Spotify's `/audio-features` endpoint using
tempo, energy, valence, other tags for similarity scoring when recommending
tracks. However, that endpoint was deprecated for new developer apps as of
[November 2024](https://developer.spotify.com/blog/2024-11-27-changes-to-the-web-api)
, and in [February 2026](https://developer.spotify.com/documentation/web-api/references/changes/february-2026)
they restricted several other endpoints like looking up artists in bulk.

Because of this, I am pivoting to manually curating genre tags for a small data
set I am using and comparing it to other tracks using what is still available
like duration, release date, and if it is explicit.

Although the functionality has been gutted, I hope to be able to pivot towards other
features and uses in the future, like a small app that just gives you your top tracks
without having to wait for the spotify wrapped.

### Note 2

"Popularity" has also been removed as information that can be pulled from the
track along with the other changes to track information

## Limitations

- Genre tags will be manually curated for this dataset and won't scale to a larger
catalog automatically
- If you have an artist with multiple appearances like a song and a version with
a feature (ex. Dracula ~ Tame Impala and Dracula ft JENNIE by Tame Impala) it
can dominate your results
- No multi user deployment available, it is designed for personal use with your
spotify credentials

## License

MIT
