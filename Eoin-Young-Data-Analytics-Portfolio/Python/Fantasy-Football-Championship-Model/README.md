# Fantasy Football WR Production Model — 2024

## Why this project is different from a fantasy ranking

Fantasy rankings are useful, but they can hide *why* a player scored well.

I wanted to build a small explanatory model around one question:

> **How much of a WR's weekly PPR production can be explained by volume, efficiency and scoring opportunity?**

This project uses real 2024 NFL WR data and a Ridge regression model.

## Inputs

The model uses:

- Targets
- Catch rate
- Yards per target
- Receiving touchdowns
- Games played

The target variable is:

- PPR fantasy points per game

The model standardizes the inputs and uses Ridge regression to reduce the impact of correlated variables.

## Why Ridge?

Targets, receptions, yards and fantasy points are naturally related. A normal linear regression can become unstable when predictors overlap.

Ridge regression adds regularization, which makes the coefficients more stable in a small exploratory dataset.

## What I am actually using this for

I am not presenting this as a “draft the players the model says” algorithm.

The useful part is the **residual**:

`actual production - model estimate`

A positive residual means the player produced more fantasy points per game than the model expected from the selected inputs.

A negative residual means the player produced less.

Those outliers are where I would start asking better football questions.

For example:

- Was touchdown production unusually high?
- Was the player especially efficient after the catch?
- Did injuries reduce the sample?
- Was the quarterback/offense unusual?
- Did a player have a role change?

## Results

The model does a reasonable job describing broad production differences, but the residuals show that basic box-score features still miss important context.

That is the main takeaway: **simple models can organize the problem, but they should create better questions rather than pretend to explain everything.**

## Validation note

Because this is a one-season exploratory project with a relatively small sample, I am deliberately not calling this a production forecasting system.

A stronger next version would train on 2020–2024 data and evaluate 2025 production using a true out-of-sample split.

## Charts

- `actual_vs_predicted.png`
- `model_coefficients.png`
- `largest_residuals.png`

## Sources

- FantasyPros 2024 WR stats: https://www.fantasypros.com/nfl/stats/wr.php?year=2024
- Pro-Football-Reference 2024 receiving: https://www.pro-football-reference.com/years/2024/receiving.htm

The statistics are public third-party data. The model, feature engineering and analysis are my own.
