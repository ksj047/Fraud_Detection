import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load your DataFrames
data = pd.read_pickle('/content/2018-09-01.pkl')


print("DataFrame loaded successfully!")
print(data.head())
print(data.info())
print(data.describe())

# Convert columns to integer type if necessary
data['TERMINAL_ID'] = data['TERMINAL_ID'].astype(int)
data['CUSTOMER_ID'] = data['CUSTOMER_ID'].astype(int)

# Define features and target variable
X = data[['TX_AMOUNT', 'TERMINAL_ID', 'CUSTOMER_ID']]
y = data['TX_FRAUD']

# Visualize the data
plt.scatter(data['TX_AMOUNT'], data['TERMINAL_ID'], alpha=0.2, c=y, cmap='viridis')
plt.xlabel('Transaction Amount')
plt.ylabel('Terminal ID')
plt.title('Scatter plot of Transaction Amount vs Terminal ID')
plt.colorbar(label='Fraud (0 = No, 1 = Yes)')
plt.show()

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize and fit the logistic regression model
model = LogisticRegression(max_iter=1000)  # Increase max_iter if convergence warning occurs
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

