from sklearn.metrics.pairwise import cosine_similarity
from encode_features import features_df, df

similarity_matrix = cosine_similarity(features_df)

def get_similar_tracks(track_name, top_n=3):
    track_index = df[df["name"] == track_name].index[0]
    similarity_scores = list(enumerate(similarity_matrix[track_index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    similar_tracks = []
    for index, score in similarity_scores:
        if index != track_index:
            similar_tracks.append((df.iloc[index]["name"], df.iloc[index]["artist"], score))
        if len(similar_tracks) == top_n:
            break
    return similar_tracks

compare_to = input("Name of song you want to compare to:  ")
try:
    results = get_similar_tracks(compare_to)
except IndexError:
    print(f"Error: song '{compare_to}' is not in your top tracks")

else:
    for name, artist, score in results:
        print(f"{name} by {artist} ---- similarity: {score:.2f}")
