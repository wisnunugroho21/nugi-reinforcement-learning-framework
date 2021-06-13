import torch

class OffPolicyLoss():
    def compute_loss(self, predicted_q_value1, predicted_q_value2):
        policy_loss = torch.min(predicted_q_value1, predicted_q_value2).mean() * -1
        return policy_loss