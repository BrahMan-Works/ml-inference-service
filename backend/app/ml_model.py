import torch
import torch.nn as nn

# this is a simple feed forward model
class SimpleModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(50, 256),
            nn.ReLU(),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Linear(128, 1)
        )

    def forward(self, x):
        return self.net(x)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = SimpleModel().to(device)
model.eval()

with torch.no_grad():
    dummy = torch.randn(1, 50).to(device)
    model(dummy)

def predict(features):
    with torch.no_grad():
        tensor = torch.tensor(features, dtype=torch.float32).to(device)
        output = model(tensor)
        return output.cpu().numpy()

