from typing import Callable
import argparse
import random

def jury_correct(pr_twojurors):
    pr_flippant_juror = 0.5

    correct_decision = 0

    rndval1 = random.random()
    rndval2 = random.random()
    rndval3 = random.random()

    if rndval1 < pr_twojurors:
        correct_decision += 1

    if rndval2 < pr_twojurors:
        correct_decision += 1

    if rndval3 < pr_flippant_juror:
        correct_decision += 1

    return correct_decision > 1  # did majority make a correct decision?


def correct_decision_simulations(trials, pr_twojurors):
    correct = 0
    for _ in range(trials):
        if jury_correct(pr_twojurors):
            correct += 1

    return correct/trials

def is_valid_probabity(prob):
    return 0.0 <= prob < 1.0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--probability_twojurors", help="the probability p of making the correct decision", type=float)
    parser.add_argument("-t", "--trials", help="the number of trials for the simulation", type=int, default=100)
    args = parser.parse_args()

    if not args.probability_twojurors:
        raise ValueError("Missing probability value for the jurors")

    if not is_valid_probabity(args.probability_twojurors):
        raise ValueError("probability_twojurors is not in the range of [0.0, 1.0).")


    if args.trials < 1:
        raise ValueError("trials must be > 0.")

    pr_correct = correct_decision_simulations(args.trials, args.probability_twojurors)
    print(f"The jury's probability of making the correct correct_decision_simulations ({args.trials} trials): {pr_correct}")
