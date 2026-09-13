# Fantasy Football Championship Prediction Model

## Goal
Build a reproducible model that ranks fantasy teams using production, consistency, depth, and high-end weekly scoring.

## Why this project?
Fantasy football provides a useful sports-analytics problem because season-long success depends on both **ceiling and consistency**. The project demonstrates feature engineering and predictive modeling while keeping assumptions transparent.

## Method
The included script creates a reproducible synthetic league dataset for demonstration and:
1. Calculates team-level production features.
2. Engineers consistency, depth, and ceiling metrics.
3. Defines a transparent championship-contender outcome.
4. Trains a Random Forest classifier.
5. Evaluates the model using a holdout set.
6. Produces contender rankings and visualizations.

**Important:** The included data is synthetic and clearly labeled. It is not presented as historical NFL league results.

## Results
The generated run reports the model's holdout accuracy/AUC and ranks the strongest contender profiles. Because the dataset is synthetic, these results demonstrate the workflow rather than claims about real NFL outcomes.

## Files
- `fantasy_championship_model.py` — complete analysis
- `synthetic_fantasy_teams.csv` — reproducible demonstration data
- `contender_rankings.csv` — model output
- `contender_scores.png` — visualization
- `requirements.txt` — Python dependencies
