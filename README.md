# Hi!

It has been my dream for some time to be able to get an internship in spotify.

Because of this, I am making some projects to learn new things, put on my resume, and hopefully
land it!

This first project will be a spotify song recommendation algorithm, in which I am striving to 
improve on spotify's idea of DJ and general recommendation feature. 

## Note on data sources

Originally I was going to use Spotify's endpoint on audio information such as tempo, energy, valence, other tags
for similarity scoring when recommending tracks. However, that endpoint was deprecated for new developer apps as of 
November 2024, and in February 2026 they restricted several other endpoints like looking up artists in bulk. Because
of this, I am pivoting to manually curating genre tags for a small data set I am using and comparing it to other 
tracks using what is still available like duration, release date, and if it is explicit.
