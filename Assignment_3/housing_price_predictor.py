import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def load_data(file_path):
    """Load and return the housing dataset using pandas."""
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("Error: Dataset file not found!")
        return None
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        return None

def explore_data(data):
    """Display basic statistics about the dataset using pandas."""
    if data is None:
        return
    
    print("\nDataset Statistics:")
    print("------------------")
    print(data.describe())
    print("\nFirst few rows of data:")
    print(data.head())

def visualize_data(data):
    """Create scatter plot of house sizes vs prices using matplotlib."""
    if data is None:
        return
    
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Size'], data['Price'], color='blue', alpha=0.5)
    plt.title('House Size vs Price')
    plt.xlabel('Size (sq ft)')
    plt.ylabel('Price ($)')
    plt.grid(True)
    plt.show()

def train_model(data):
    """Train linear regression model using scikit-learn."""
    if data is None:
        return None, None, None
    
    X = data['Size'].values.reshape(-1, 1)
    y = data['Price'].values
    
    model = LinearRegression()
    model.fit(X, y)
    
    # Calculate R² score
    y_pred = model.predict(X)
    r2 = r2_score(y, y_pred)
    
    return model, model.coef_[0], model.intercept_, r2

def visualize_model(data, model):
    """Plot data points and regression line using matplotlib."""
    if data is None or model is None:
        return
    
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Size'], data['Price'], color='blue', alpha=0.5, label='Data points')
    
    # Plot regression line
    X = data['Size'].values.reshape(-1, 1)
    y_pred = model.predict(X)
    plt.plot(data['Size'], y_pred, color='red', label='Regression line')
    
    plt.title('House Size vs Price with Regression Line')
    plt.xlabel('Size (sq ft)')
    plt.ylabel('Price ($)')
    plt.legend()
    plt.grid(True)
    plt.show()

def predict_price(model, size):
    """Predict house price for given size."""
    if model is None:
        return None
    
    try:
        size = float(size)
        if size <= 0:
            print("Error: Size must be positive!")
            return None
        
        prediction = model.predict([[size]])[0]
        return prediction
    except ValueError:
        print("Error: Please enter a valid number!")
        return None

def main():
    # Load data
    data = load_data('housing_data.csv')
    if data is None:
        return
    
    # Explore data
    explore_data(data)
    
    # Visualize data
    visualize_data(data)
    
    # Train model
    model, slope, intercept, r2 = train_model(data)
    if model is not None:
        print("\nModel Statistics:")
        print(f"Slope (Price per sq ft): ${slope:.2f}")
        print(f"Intercept: ${intercept:.2f}")
        print(f"R² Score: {r2:.4f}")
        
        # Visualize model
        visualize_model(data, model)
        
        # Interactive prediction
        while True:
            print("\nEnter house size in square feet (or 'q' to quit):")
            user_input = input("> ")
            
            if user_input.lower() == 'q':
                break
            
            prediction = predict_price(model, user_input)
            if prediction is not None:
                print(f"Predicted price: ${prediction:,.2f}")

if __name__ == "__main__":
    main() 