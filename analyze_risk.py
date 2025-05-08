import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

df = pd.read_csv("financial_data.csv")


df.columns = df.columns.str.strip()


print(df.head())


X = df.drop("risk", axis=1)  # Features
y = df["risk"]  # Target


categorical_features = ["employment_status"]  # Categorical column
numerical_features = X.select_dtypes(include=["float64", "int64"]).columns.tolist()
numerical_features = [col for col in numerical_features if col != "risk"]  # Remove the target variable


numeric_transformer = StandardScaler()
categorical_transformer = Pipeline(steps=[
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])


preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numerical_features),
        ("cat", categorical_transformer, categorical_features)
    ]
)


pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier())
])


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


pipeline.fit(X_train, y_train)


y_pred = pipeline.predict(X_test)


print(classification_report(y_test, y_pred))
