from AI_Tree_Structure import Branch, Leaf


class CPUPlayer:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def build_decision_tree(self):
        tree = Branch(
            Branch_q=self.has_wild_draw_four,  # Branch question: Do we have a Wild Draw Four?
            child_1=Leaf("Play Wild Draw Four"),  # Child 1: Yes, play it.
            child_2=Branch(  # Child 2: No, check the next question.
                Branch_q=self.has_skip_card,  # Do we have a card matching current color or number?
                child_1=Leaf("Play Skip card"),  # Yes, play it.
                child_2=Branch(  # No, check the next question: skip card, wild card, +2 card, reverse card, etc.
                    Branch_q=self.has_matching_card(),  # Do we have a Skip card?
                    child_1=Leaf("Play matching card"),  # Yes, play it.
                    child_2=Branch(  # No, check for a Wild card.
                        Branch_q=self.has_wild_card,  # Do we have a Wild card?
                        child_1=Leaf("Play Wild card"),  # Yes, play it.
                        child_2=Branch(  # No, check for a +2 card.
                            Branch_q=self.has_plus_two_card,  # Do we have a +2 card?
                            child_1=Leaf("Play +2 card"),  # Yes, play it.
                            child_2=Branch(  # No, check for a Reverse card.
                                Branch_q=self.has_reverse_card,  # Do we have a Reverse card?
                                child_1=Leaf("Play Reverse card"),  # Yes, play it.
                                child_2=Leaf("Draw card")  # No specific cards to play, draw a card.
                            )
                        )
                    )
                )
            )
        )
        return tree

    # Functions to check card availability can be implemented here.

    def has_wild_draw_four(self, player_hand):
        for card in player_hand:
            if "Wild Draw Four" in card:
                return True
        return False

    def has_matching_card(self, player_hand, current_color, card_value):
        for card in player_hand:
            card_parts = card.split()
            if "Wild" in card or (
                    len(card_parts) == 2 and (current_color == card_parts[0] or card_value == card_parts[1])):
                return True
        return False

    def has_skip_card(self, player_hand):
        for card in player_hand:
            if "Skip" in card:
                return True
        return False

    def has_wild_card(self, player_hand):
        for card in player_hand:
            if "Wild" in card and "Wild Draw Four" not in card:
                return True
        return False

    def has_plus_two_card(self, player_hand):
        for card in player_hand:
            if "Draw Two" in card:
                return True
        return False

    def has_reverse_card(self, player_hand):
        for card in player_hand:
            if "Reverse" in card:
                return True
        return False
