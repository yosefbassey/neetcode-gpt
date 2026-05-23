import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        z = z - np.max(z)
        exp_logits = np.exp(z)
        sumexp_logits = np.sum(exp_logits)
        sft_max = exp_logits / sumexp_logits
        return np.round(sft_max, 4)
