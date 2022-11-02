import torch
from kornia.geometry.transform import rotate

class Rotate():
    def __init__(self, n_trans, group_size=360):
        self.n_trans, self.group_size = n_trans, group_size
    def apply(self, data):
        if self.group_size == 360:
            theta = torch.arange(0, 360)[1:][torch.randperm(359)]
            theta = theta[:self.n_trans].type_as(data)
        else:
            theta = torch.arange(0, 360, int(360 / (self.group_size+1)))[1:]
            theta = theta[torch.randperm(self.group_size)][:self.n_trans].type_as(data)
        return torch.cat([rotate(data, _theta) for _theta in theta])