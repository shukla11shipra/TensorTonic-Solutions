import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    ypred = np.array(y_pred);
    ytrue = np.array(y_true);

    mse = np.mean((ypred-ytrue)**2)
    return mse;