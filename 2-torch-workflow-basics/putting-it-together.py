import torch
import torch.nn as nn
# import matplotlib.pyplot as plt

print(torch.__version__)

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# Create weight and bias
weight = 0.7
bias = 0.3

# Create range values
start = 0
end = 1
step = 0.02

# Create X and y (features and labels)
X = torch.arange(start, end, step).unsqueeze(dim=1) 
y = weight * X + bias 
print(X[:10], y[:10])

# Split data
train_split = int(0.8 * len(X))
X_train, y_train = X[:train_split], y[:train_split]
X_test, y_test = X[train_split:], y[train_split:]

print(len(X_train), len(y_train), len(X_test), len(y_test))

# def plot_predictions(train_data=X_train, 
#                      train_labels=y_train, 
#                      test_data=X_test, 
#                      test_labels=y_test, 
#                      predictions=None):
#   """
#   Plots training data, test data and compares predictions.
#   """
#   plt.figure(figsize=(10, 7))
#   plt.scatter(train_data, train_labels, c="b", s=4, label="Training data")
  
#   # Plot test data in green
#   plt.scatter(test_data, test_labels, c="g", s=4, label="Testing data")

#   if predictions is not None:
#     # Plot the predictions in red (predictions were made on the test data)
#     plt.scatter(test_data, predictions, c="r", s=4, label="Predictions")

#   # Show the legend
#   plt.legend(prop={"size": 14});

# plot_predictions(X_train, y_train, X_test, y_test)

class LinearRegressionModelV2(nn.Module):
    # define init
    def __init__(self):
        super().__init__()
        self.linear_layer = nn.Linear(
            in_features = 1,
            out_features = 1,
            bias = True # default is true
        )
    
    # forward pass 
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.linear_layer(x)

torch.manual_seed(741)
model_1 = LinearRegressionModelV2()
print(f"\nModel:\n{model_1}\n\nModel state dict:\n{model_1.state_dict()}\n")

model_1.to(device)
print(next(model_1.parameters()).device)

# ============================= Training

# loss function
loss_fn = nn.L1Loss()

# optimizer
optimizer = torch.optim.SGD(model_1.parameters(), 0.01)

# training loop
torch.manual_seed(741)

epochs = 1000

for epoch in range(epochs):
    # forward pass
    model_1.train()
    y_pred = model_1(X_train)

    # calculate loss
    loss = loss_fn(y_pred, y_train)

    # zero grad
    optimizer.zero_grad()

    # backward
    loss.backward()

    # optimizer step
    optimizer.step()

    # testing
    model_1.eval()
    with torch.inference_mode():
        test_pred = model_1(X_test)
        test_loss = loss_fn(test_pred, y_test)
    
    if epoch % 10 == 0:
        print(f"Epoch: {epoch} | Train loss: {loss} | Test loss: {test_loss}")


from pprint import pprint
print("\nThe model learned the following values for weights and bias:")
pprint(model_1.state_dict())
print("\nAnd the original values for weights and bias are:")
print(f"weights: {weight}, bias: {bias}\n")

# ======================= Making predictions on test data
print("======================= Making predictions on test data")
# Turn model into evaluation mode
model_1.eval()

# Make predictions on the test data
with torch.inference_mode():
    y_preds = model_1(X_test)
print(f"\ny_preds gives us:\n{y_preds}\n")