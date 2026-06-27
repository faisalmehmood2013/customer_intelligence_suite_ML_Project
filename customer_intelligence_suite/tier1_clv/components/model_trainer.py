"""
model_trainer.py  (tier1_clv)
----------------------------
Yahan MULTIPLE algorithms train hote hain aur GridSearchCV se best
hyperparameters dhunde jate hain.

Algorithms to try: Linear, Ridge, Lasso, ElasticNet, SVR, Decision Tree Regressor, Random Forest Regressor

Yahan banayenge:
    def train_models(X_train, y_train):
        # Har algorithm ke liye GridSearchCV/RandomizedSearchCV
        # Best model + best params return karo (sab algorithms ka
        # comparison bhi yahan ho sakta hai)
"""
