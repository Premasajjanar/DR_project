import torch
from torch import nn
from torchvision import models
from PIL import Image
import torchvision.transforms as transforms

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def get_model():
    model = models.resnet152(pretrained=True)
    num_ftrs = model.fc.in_features
    out_ftrs = 5
    model.fc = nn.Sequential(
        nn.Linear(num_ftrs, 512),
        nn.ReLU(),
        nn.Linear(512, out_ftrs),
        nn.LogSoftmax(dim=1)
    )

    for name, child in model.named_children():
        if name in ['layer2', 'layer3', 'layer4', 'fc']:
            for param in child.parameters():
                param.requires_grad = True
        else:
            for param in child.parameters():
                param.requires_grad = False

    model.to(device)
    return model

def load_model(path=r'G:\My Drive\DR_Project\models\new_classifier.pt'):
    model = get_model()
    checkpoint = torch.load(path, map_location=device)
    model.load_state_dict(checkpoint['model_state_dict'])
    model.eval()
    return model

def inference(model, file, transform, classes):
    image = Image.open(file).convert('RGB')
    img_t = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        output = model(img_t)
        ps = torch.exp(output)
        top_p, top_class = ps.topk(1, dim=1)
        idx = top_class.item()
        return idx, classes[idx]

test_transforms = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=(0.485, 0.456, 0.406),
                         std=(0.229, 0.224, 0.225))
])

classes = ['No DR', 'Mild', 'Moderate', 'Severe', 'Proliferative DR']
