# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 17:13:20 2021

@author: chris
"""
STARTING_MARGIN = 0.2
MARGIN_INCREMENT = 0.01


class Strategy:
    # todo rethink slots as they may scale better
    # __slots__ = ['num_pools', 'pledges', 'margins', 'owned_pools', 'stake_allocations']

    def __init__(self, pledges=None, margins=None, stake_allocations=None,
                 owned_pools=None, num_pools=0):
        if pledges is None:
            pledges = []
        if margins is None:
            margins = []
        if owned_pools is None:
            owned_pools = dict()
        if stake_allocations is None:
            stake_allocations = dict()
        self.stake_allocations = stake_allocations
        self.owned_pools = owned_pools
        # todo remove the following as redundant
        self.num_pools = num_pools
        self.pledges = pledges
        self.margins = margins

