import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
from pprint import pprint

from wavenet_nn import WaveNetNN

wn_model = WaveNetNN(layers=10,
                     blocks=4,
                     dilation_channels=32,
                     residual_channels=32,
                     skip_channels=256,
                     end_channels=256,
                     classes=1,
                     #                     input_channels=256,
                     #                     output_channels=256,
                     output_length=32,
                     kernel_size=2)


print(f'rfs: {wn_model.receptive_field}')
x = torch.randn(1, 256, 4093)


wn_model.eval()

#y = wn_model(x)
#y = wn_model.wavenet(x, dilation_func=wn_model.queue_dilate)

s = torch.randn(5)

x_hat = wn_model.generate_fast(num_samples=5,
                               first_samples=s)
