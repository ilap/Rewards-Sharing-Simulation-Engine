# Empirical Modelling

The aim of this model is to compare the behavior of the Cardano blockchain's (chain or system) states from the initial Shelley era, by applying a very similar initial condition and parameters from historical data.

If the model describes or has some relationships to the real-life observations of the Cardano blockchain, then we could assume that any changes on the reward schemes and/or system's parameters could predict/describe, in some degree, the Cardano blockhain future state.

## Initial conditions

The initial condition of the model (model parameters) is defined by the system's (internal) state, parameters and settings at the transition epoch from Byron to Shelley era.

## Historical State changes

The model tries to simulate the state changes over time (by epoch) of the chain. The states of the system, and therefore the model, are impacted by `external` inputs (such us change in the nr. of stakeholders, their behavioral profile or protocol parameter changes) and the used Reward Sharing Scheme (RSS).

External inputs are (semi)independent of the system's internal state and are mainly driven by the perceptions of the Cardano in the real world.

## Model Parameters

Model parameter describes the initial state, the change of the states and the constraints of the states.

### Maximum nr. of pools (NEW)

### Minimum pledge per pools (NEW)


### Number of Agents (n)

The number of agent represents all stakeholders of the system and it depends
on the popularity of the system (Cardano blockhain)

It has grown from ~17K to 1.3m from epoch 208 to 375.
The number of pools created, has a logarythmic relationship to the number of agents (accounts/wallets) 
joining to the system.


### Optimal number or pools (k)

Initially it was 150 and changed to 500 at epoch 240. It's observed
that before the change in `k` caused a small increase on creating staking pools.

### Influence factor (a0)

This system's parameter is set to `0.3`

### Stake Distributions (stake_distr_source)

Based on the historical data, the initial stake distribution at epoch 208 has
a relationship to some distribution which is slowly skews to the left by each epoch as more
ppl is joining (and therefore distribution of the wealth is spreading to more by the time)


### Stakeholders behaviour (agent_profile_distr)

RSS's equilibirium predicts a `k` number of pools, therefore we can assume that the delegators of the first
`k` pools are `non-myopic` i.e, rational and therefore, the rest are irrational (`myopic`).  
The 3rd type of stakeholders are the `abstainers`. Abstainers can be thought as stakeholders that are not participating staking.

Initially, they were (`delegator_with_stake/account_with_amount`)  around 38% of the Shelley accounts which has grown to around 60% by epoch `370`.
Their growth (in the number of accounts/entities and in percentages) has some logaritmic relationships.

### Delegated vs. Total  Stake Fraction (inactive_stake_fraction)

In other words, total ADA staked.
The initial 19.1% delegated stake at epoch, has grown to around 73% and its growth has a very strong logarythmic correlation.

### (inactive_stake_fraction_known)

The absolute utility threshold for accepting new moves (relates to inertia i.e., resistance to change). 
If an agent develops a new strategy whose utility does not exceed that of its current one by at least this threshold, then the
new strategy is rejected. The default value is 10-9, but any non-negative real number is accepted.

### (absolute_utility_threshold)

**absolute_utility_threshold**: The absolute utility threshold for accepting new moves (relates to inertia). 
If an 
agent develops a new strategy whose utility does not exceed that of its current one by at least this threshold, then the 
new strategy is rejected. The default value is 10<sup>-9</sup>, but any non-negative real number is accepted.

### (relative_utility_threshold)

**relative_utility_threshold**: The relative utility threshold for accepting new moves (relates to inertia). 

If an 
agent develops a new strategy whose utility does not exceed that of its current one by at least this fraction, then the 
new strategy is rejected. 

The default value is 0, i.e. no relative utility threshold exists, but any non-negative real 
number is accepted. For example, if this threshold is 0.1 then it means that a new move has to yield utility at least 
10% higher than that of the current move in order to be selected.

### (cost_min)
### (cost_max)
### (extra_pool_cost_fraction)

## Stakeholders

Stakeholders are the main drivers of Cardano blockchain. 
They're driven by different external (economical and psychological) and internal (by RSS) incentives.
The game theory assumes them as `rational` players, though real life observations do not match with the assumption.

Stakeholders assumed to be entities (individuals, group of ppl., organizations etc.).
Initial stakeholders were the Byron genesis' vending machine (AVVM) users. Though, different entities could buy multiple
AVVM certificates we can assume that initial wealth distriburtion was fair and honest.

The Cardano protocol has a (saturation) capped reward scheme tight to the `k` (`nOpt`nr. of optimal number of pools).

Stakeholders can have more or less stake than the saturation level above.

Stakeholder can decide whether they want to be pool operators, delegators or abstainers.

Abstainers (accounts) are those delegators who do not want to participate in delegations for different reasons.
