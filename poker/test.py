from cards import Card, Hand
cards1 = [Card("heart", i) for i in range(1, 6)]
hand1 = Hand(*cards1)
cards2 = [Card("spade", i) for i in range(1, 6)]
hand2 = Hand(*cards2)

assert (hand1 == hand2)
assert not (hand1 != hand2)
assert (hand1 <= hand2)
assert not (hand1 < hand2)
assert (hand1 >= hand2)
assert not (hand1 > hand2)
