"""Card Games

https://exercism.org/tracks/python/exercises/card-games

"""
from typing import List


def get_rounds(number: int) -> List[int]:
    """

     :param number: int - current round number.
     :return: list - current round and the two that follow.
    """

    return list(range(number, number + 3))


def concatenate_rounds(rounds_1: List[int], rounds_2: List[int]) -> List[int]:
    """

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds: List[int], number: int) -> bool:
    """

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    """

    return number in rounds


def card_average(hand: List[int]) -> float:
    """

    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    """

    return sum(hand) / len(hand)


def approx_average_is_average(hand: List[int]) -> bool:
    """

    :param hand: list - cards in hand.
    :return: bool - if approximate average equals to the `true average`.
    """

    ave = card_average(hand)
    hand.sort()
    approx_ave = (hand[0] + hand[-1]) / 2
    hand_len = len(hand)
    if hand_len % 2 == 1:
        med = hand[(hand_len - 1) // 2]
    else:
        med = (hand[hand_len // 2 - 1] + hand[hand_len // 2]) / 2

    return ave in (approx_ave, med)


def average_even_is_average_odd(hand: List[int]) -> bool:
    """

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    hand_len = len(hand)
    if hand_len == 0:
        return True
    if hand_len == 1:
        return False

    odds = hand[0::2]
    evens = hand[1::2]
    return card_average(odds) == card_average(evens)


def maybe_double_last(hand: List[int]) -> List[int]:
    """

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if hand[-1] == 11:
        hand[-1] *= 2
    return hand
