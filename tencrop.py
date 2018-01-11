#in this file  introduced the use of tencrop method


# the process of trainloader is as follows:
trainLoader = torch.utils.data.DataLoader(
            torchvision.datasets.ImageFolder(traindir, torchvision.transforms.Compose([
            torchvision.transforms.CenterCrop(224),
            torchvision.transforms.RandomHorizontalFlip(),
            torchvision.transforms.Lambda(lambda crops: torch.stack([torchvision.transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)) (torchvision.transforms.ToTensor()(crop)) for crop in crops])),
           
        ])),
'''
other process code 
'''
#training process

    for i, (input, target) in enumerate(train_loader):
    	# the input is 5-d tensor, so obtain the size
        bs, ncrops, c, h, w = input.size()

        # move the target and input_var to gpu\
        #resize the view to 4-d tensor
        input_var = torch.autograd.Variable(input.view(-1, c, h, w)).cuda(gpu)
        input_var = torch.autograd.Variable(input.cuda(gpu))
        target = target.cuda(gpu,async=True)
        target_var = torch.autograd.Variable(target)

        # compute output
        output_all= model(input_var)
        #because the size of targe  is not equivalent to the size of input
        #resize  output_all and get the mean value 
        output=output_all.view(bs, ncrops, -1).mean(1)

#       compute the loss 
        loss = criterion(output, target_var)

'''
	other training code
'''
