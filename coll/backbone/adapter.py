#!/usr/bin/env python
#
# Copyright the CoLL team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
# Intro: adapter structure for task-incremental learning
# Author: Tongtong Wu
# Time: Aug 4, 2021
"""
import torch
import torch.nn as nn

__all__ = ['BaseAdapter', 'AdapterFusion']


class BaseAdapter(nn.Module):
    """
    the base adapter structure and functions.
    """
    def __init__(self):
        super(BaseAdapter, self).__init__()
        pass
    
    def forward(self, x):
        pass
    
    def add_adapter(self, model: nn.Module):
        pass
    
    def init_parameter(self):
        pass


class AdapterFusion(nn.Module):
    def __init__(self):
        super(AdapterFusion, self).__init__()
        pass
