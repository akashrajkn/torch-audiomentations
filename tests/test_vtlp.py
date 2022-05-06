import numpy as np
import torch

from torch_audiomentations import VTLP


class TestVTLP:
    def test_vtlp(self):
        samples = torch.randn(3, 1, 32000)
        sample_rate = 16000

        augment = VTLP(p=1.0, sample_rate=sample_rate, output_type="dict")
        processed_samples = augment(
            samples=samples, sample_rate=sample_rate
        ).samples.numpy()

        assert processed_samples.shape == samples.shape
        assert processed_samples.dtype == np.float32