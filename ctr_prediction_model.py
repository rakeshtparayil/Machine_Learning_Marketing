import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load and prepare the data
def prepare_data(df):
    # CTR is already calculated in the data as 'CTR (all)'
    
    # Select features for the model
    features = [
        'Impressions',
        'Frequency',
        'Amount spent',
        'CPC (all)',
        'CPM (cost per 1,000 impressions)',
        'Views'
    ]
    
    # Remove rows with missing values or infinite values
    df = df.replace([np.inf, -np.inf], np.nan)
    df = df.dropna(subset=features + ['CTR (all)'])
    
    return df[features], df['CTR (all)']

def train_model():
    # Read the CSV data
    df = pd.read_csv('meta.csv')
    
    # Prepare features and target
    X, y = prepare_data(df)
    
    # Print basic statistics about the data
    print("\nDataset Statistics:")
    print(f"Number of samples: {len(X)}")
    print("\nFeature Statistics:")
    print(X.describe())
    print("\nTarget (CTR) Statistics:")
    print(y.describe())
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Scale the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train Random Forest model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test_scaled)
    
    # Calculate metrics
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    
    print("\nModel Performance Metrics:")
    print(f"Mean Squared Error: {mse:.4f}")
    print(f"Root Mean Squared Error: {rmse:.4f}")
    print(f"R² Score: {r2:.4f}")
    
    # Feature importance
    feature_importance = pd.DataFrame({
        'feature': X.columns,
        'importance': model.feature_importances_
    }).sort_values('importance', ascending=False)
    
    print("\nFeature Importance:")
    print(feature_importance)
    
    # Plot feature importance
    plt.figure(figsize=(10, 6))
    plt.bar(feature_importance['feature'], feature_importance['importance'])
    plt.xticks(rotation=45)
    plt.title('Feature Importance for CTR Prediction')
    plt.tight_layout()
    plt.savefig('feature_importance.png')
    
    return model, scaler

if __name__ == "__main__":
    model, scaler = train_model() 