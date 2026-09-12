import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
from build_features import build_feature_dataframe

df = build_feature_dataframe()

mlb = MultiLabelBinarizer()
genre_encoded = mlb.fit_transform(df["genres"])
genre_df = pd.DataFrame(genre_encoded, columns=mlb.classes_)

features_df = pd.concat([
    df[["duration_ms"]].reset_index(drop=True),
    df["explicit"].astype(int).reset_index(drop=True),
    genre_df.reset_index(drop=True)
], axis=1)

print(features_df)
