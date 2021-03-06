import torch
import numpy as np

def set_device(use_gpu = True):
    if use_gpu:
        if torch.cuda.is_available():
            return torch.device('cuda:0')
        else:
            return torch.device('cpu')
    else:
        return torch.device('cpu')

def to_list(datas, use_gpu = True):
    if use_gpu:
        if torch.cuda.is_available():
            return datas.detach().cpu().tolist()
        else:
            return datas.detach().tolist()
    else:
        return datas.detach().tolist()

def to_tensor(datas, use_gpu = True, first_unsqueeze = False, last_unsqueeze = False, detach = False):
    if isinstance(datas, tuple):
        datas = list(datas)
        for i, data in enumerate(datas):
            data    = torch.FloatTensor(data).to(set_device(use_gpu))
            if first_unsqueeze: 
                data    = data.unsqueeze(0)
            if last_unsqueeze:
                data    = data.unsqueeze(-1) if data.shape[-1] != 1 else data
            if detach:
                data    = data.detach()
            datas[i] = data
        datas = tuple(datas)

    elif isinstance(datas, list):
        for i, data in enumerate(datas):
            data    = torch.FloatTensor(data).to(set_device(use_gpu))
            if first_unsqueeze: 
                data    = data.unsqueeze(0)
            if last_unsqueeze:
                data    = data.unsqueeze(-1) if data.shape[-1] != 1 else data
            if detach:
                data    = data.detach()
            datas[i] = data
        datas = tuple(datas)

    else:
        datas   = torch.FloatTensor(datas).to(set_device(use_gpu))
        if first_unsqueeze: 
            datas   = datas.unsqueeze(0)
        if last_unsqueeze:
            datas   = datas.unsqueeze(-1) if datas.shape[-1] != 1 else datas
        if detach:
            datas   = datas.detach()
    
    return datas

def copy_parameters(source_model, target_model, tau = 0.95):
    for target_param, param in zip(target_model.parameters(), source_model.parameters()):
        target_param.data.copy_(target_param.data * tau + param.data * (1.0 - tau))

    return target_model
