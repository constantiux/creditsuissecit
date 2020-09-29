# it's CodeIT Suisse 2020!

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/grrlic/creditsuissecit) or test it on [Glitch](http://codeitsuisse.glitch.me/)

## Introduction

As someone who just began doing competitive programming questions, this 24H challenge is disturbingly a great cause to make you an insane person for one whole day pun intended. Unlike **Codeforces** and **Codechef**, you are not only have to figure out the more efficient algorithms for each respective problems, but you have setup and deploy your code (in my case it's _python_ and wrap it with _flask_ and _gunicorn_) to _Heroku_ and at the least had to make sure you are treating the corrent input (JSON or text) and lastly _jsonify_ the **return** value.

Too bad but not too bad, I managed to fight up the ladder and ended up at the _11th pos_ of the individual Hong Kong leaderboard. For you who are in the penultimate year and below, this challenge is definitely a _yes yes_.

![](res/leaderboard.jpg)

## Afterwards..

(*) **_Disclaimer_**: After a while since the competition ended, I decided to do a full documentation out of my interest to complete the questions that I unable to finish. If any of from the Credit Suisse organizer express concerns regarding copyright issues, please let me know.

**Credits**:
To make it quick, I decided to source from other participants' solutions, so kudos to:
- [jiayushe](https://github.com/jiayushe/codeit-suisse-2020)
- [alex-hjk](https://github.com/alex-hjk/CodeItSuisse-2020)
- [certifiedjoon](https://github.com/CertifiedJoon/CodeSuisse2020)
- [csjlimo](https://github.com/CSJLIMO/credit-suisse-python-demo)

(*) _The accuracy of each solution might not be hundred-percent correct, since there are hidden testcases untested._

## Example Usage

These instruction are to help you solve a test challenge "Calculate Square". Instruction to this test challenge can be found at https://calculate-square.herokuapp.com/instructions

### Step by step

As per the instruction you have to implement a post endpoint /square

- Go to `square.py` under `codeitsuisse/routes` folder in this template and you will find a post method with name  `/square` 
- write your implementation in this method. This method will be the entry point when you submit your solution for evaluation
- Note the __init__.py file in each folder. This file makes python treat directories containing it to be loaded in a module
- Follow similar approach to implement actual challenges during the event

### List of endpoints

Besides `/square` there are 20 others respective to each problem statements. They are:

- `/bored-scribe`
- `/bucket-fill`
- `/clean_floor`
- `/cluster`
- `/contact_trace`
- `/encryption`
- `/fruitbasket`
- `/intelligent-farming`
- `/olympiad-of-babylon`
- `/optimizedportfolio`
- `/pre-tick`
- `/revisitgeometry`
- `/salad-spree`
- `/slsm`
- `/social_distancing`
- `/supermarket`
- `/swaphedge`
- `/yin-yang`
