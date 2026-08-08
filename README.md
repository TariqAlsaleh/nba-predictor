# NBA Game Outcome Predictor

Predicts the winner of an NBA matchup using a machine learning model trained on
historical game data, and generates a written explanation of the prediction
using the Claude API.

## Approach

**Prediction model** — a scikit-learn classifier (logistic regression /
Random Forest) trained on 4 seasons of NBA game logs. Features are built only
from information available *before* each game (recent form, win streaks,
head-to-head record, rest days, home court advantage), and evaluated against
a simple baseline ("home team always wins").

**Claude API** — used for two things: extracting structured injury
information from report text as a model feature, and generating a
plain-English explanation of each prediction that is grounded in the model's
actual output.

## Status

In progress.

- [x] Data pipeline — `fetch_data.py` pulls 4 seasons of game logs via `nba_api`
- [ ] Feature engineering
- [ ] Model training and evaluation
- [ ] Claude API: injury report parsing
- [ ] Claude API: prediction explanations
- [ ] CLI prediction script

Usage instructions will be added once the prediction script is complete.
