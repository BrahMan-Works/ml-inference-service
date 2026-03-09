import torch
import torchvision.models as models

# this is a simple feed forward model
#class SimpleModel(nn.Module):
#    def __init__(self):
#        super().__init__()
#        self.net = nn.Sequential(
#            nn.Linear(50, 256),
#            nn.ReLU(),
#            nn.Linear(256, 128),
#            nn.ReLU(),
#            nn.Linear(128, 1)
#        )

#    def forward(self, x):
#        return self.net(x)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)

model.eval()
model.to(device)

with torch.no_grad():
    dummy = torch.randn(1, 3, 224, 224).to(device)
    model(dummy)

def predict(features):
    with torch.no_grad():
        tensor = torch.tensor(features, dtype=torch.float32).to(device)
        output = model(tensor)
        
    return output.cpu().numpy()

