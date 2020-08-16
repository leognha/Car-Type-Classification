import torch
import torch.nn as nn
from dataset import IMAGE_Dataset
from torch.autograd import Variable
from torch.utils.data import DataLoader
from torchvision import transforms
from pathlib import Path
import copy
import torchvision.models as models

##REPRODUCIBILITY
torch.manual_seed(123)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False

CUDA_DEVICES = 1
DATASET_ROOT = r'D:\users\leognha\Desktop\607410158ML2\crop_train'

def train():
	data_transform = transforms.Compose([
		transforms.Resize((224,224)),
		transforms.ToTensor(),
		transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
	])
	#print(DATASET_ROOT)
	train_set = IMAGE_Dataset(Path(DATASET_ROOT), data_transform)
	data_loader = DataLoader(dataset=train_set, batch_size=32, shuffle=True, num_workers=1)
	#print(train_set.num_classes)

	resnet101 = models.resnet101(pretrained=False) #esnet101
	fc_features = resnet101.fc.in_features
	resnet101.fc = nn.Linear(fc_features, 196)
	model = resnet101.cuda(CUDA_DEVICES)
	model.train()

	best_model_params = copy.deepcopy(model.state_dict())
	best_acc = 0.0
	num_epochs =10
	criterion = nn.CrossEntropyLoss()
	optimizer = torch.optim.SGD(params=model.parameters(), lr=0.01, momentum=0.9)

	file = open("acc_output.txt", mode='w')
	file = open("loss_output.txt", mode='w')

	for epoch in range(num_epochs):
		print(f'Epoch: {epoch + 1}/{num_epochs}')
		print('-' * len(f'Epoch: {epoch + 1}/{num_epochs}'))

		training_loss = 0.0
		training_corrects = 0

		for i, (inputs, labels) in enumerate(data_loader):
			inputs = Variable(inputs.cuda(CUDA_DEVICES))
			labels = Variable(labels.cuda(CUDA_DEVICES))			

			optimizer.zero_grad()

			outputs = model(inputs)
			_, preds = torch.max(outputs.data, 1)
			loss = criterion(outputs, labels)

			loss.backward()
			optimizer.step()

			training_loss += loss.item() * inputs.size(0)
			#revise loss.data[0]-->loss.item()
			training_corrects += torch.sum(preds == labels.data)
			#print(f'training_corrects: {training_corrects}')

		training_loss = training_loss / len(train_set)
		training_acc = training_corrects.double() / len(train_set)
		# print(training_acc.type())
		# print(f'training_corrects: {training_corrects}\tlen(train_set):{len(train_set)}\n')
		print(f'Training loss: {training_loss:.4f}\taccuracy: {training_acc:.4f}\n')

		if training_acc > best_acc:
			best_acc = training_acc
			best_model_params = copy.deepcopy(model.state_dict())

		file = open("acc_output.txt", mode='a')
		file.write('%s ,' %training_acc)

		file = open("loss_output.txt", mode='a')
		file.write('%s ,' %training_loss)

		if ((epoch + 1) % 1 == 0):
			model.load_state_dict(best_model_params)
			torch.save(model, f'model-{training_acc:.04f}-{epoch + 1:2d}.pth')

	file.close()
	file.close()

if __name__ == '__main__':
	train()
