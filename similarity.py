from sklearn.metrics.pairwise import cosine_similarity
from encode_features import features_df, df

similarity_matrix = cosine_similarity(features_df)

print(similarity_matrix)
