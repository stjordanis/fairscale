# Copyright (c) Facebook, Inc. and its affiliates. All rights reserved.

from ...optim import Optimizer
from ... import device, Tensor
from typing import Dict, Any, Optional

class GradScaler(object):
    _scale: Optional[Tensor]
    _grows_tracker: Optional[Tensor]
    _per_optimizer_states: Dict[int, Dict[str, Any]]

    def __init__(self, init_scale: float, growth_factor: float, backoff_factor: float, growth_interval: int, enabled: bool): ...
    def _unscale_grads_(self, optimizer: Optimizer, inv_scale: Tensor, found_inf: Tensor, allow_fp16: bool) -> Dict[device, Tensor]: ...
    def step(self, optimizer: Optimizer, *args: Any, **kwargs: Any): ...	
    def update(self, new_scale: Optional[float]=None): ...
    def unscale_(self, optimizer: Optimizer) -> None: ...
