

# Hyperparameter tuning:
# - Computationally extensive,
# - sometimes leads to very slight improvement,
# weight the impact of tuning on the whole project.

# Basic imports 
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error as MSE
from sklearn.model_selection import GridSearchCV

# Set seed for reproductibility
SEED = 1

# Define the DataFrames
X = pd.DataFrame()
y = pd.DataFrame()

# Split dataset into 70% train and 30% test
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,
    random_state=SEED)

# Instantiate a random forest regressor 'rf'
rf = RandomForestRegressor(random_state=SEED)

# Inspect rf' s hyperparameters
rf.get_params()

# Define a grid of hyperparameters 'params_rf'
params_df = {
    'n_estimators': [300, 400, 500],
    'max_depth': [4, 6, 8],
    'min_samples_leaf': [0.1, 0.2],
    'max_features': ['log2', 'sqrt']
    }

# Instantiate 'grid_rf'
grid_rf = GridSearchCV(
    estimator=rf,
    param_grid=params_df,
    cv=3,
    scoring='neg_mean_squared_error',
    verbose=1,
    n_jobs=-1
    )

# Searching for the best Hyperparameters
# Fit 'grid_rf' to the training set
grid_rf.fit(X_train, y_train)

# Extract the best hyperparameters from 'grid_rf'
best_hyperparams = grid_rf.best_params_

# Evaluating the best model performance
# Extract the best model from 'grid_rf'
best_model = grid_rf.best_estimator_

# Predict the test set labels
y_pred = best_model.predict(X_test)

# Evaluate the test set RMSE
rmse_test = MSE(y_test, y_pred)**(1/2)