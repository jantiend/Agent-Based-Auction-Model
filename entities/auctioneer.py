from .buyer import Buyer
from .seller import Seller
from typing import List
from operator import attrgetter
from collections import namedtuple
from statistics import median


class Auctioneer(object):

    def __init__(self, buyers: List[Buyer], sellers: List[Seller]):
        self.buyers = buyers
        self.sellers = sellers

    def auction(self):
        """
        Auctions with the buyers and sellers provided to this Auctioneer.
        """

        # Get Qs and Median Ps:
        total_q_s = 0
        auction_items = []

        for m in sellers:
            total_q_s += m[1]
            for i in range(m[1]):
                auction_items.append(m[2])

        median_p_s = median(sorted(auction_items))

        # Get Qb and Median Pb:
        total_q_b = 0
        auction_items_b = []

        for n in buyers:
            total_q_b += n[1]
            for j in range(n[1]):
                auction_items_b.append(n[2])

        auction_items_b = sorted(auction_items_b, reverse=True)
        median_p_b = median(auction_items_b[0:total_q_s])

        # Determine auction price:
        price = (median_p_s + median_p_b) / 2

        print("There are %s items for sale." % total_q_s)
        print("Total demand is %s" % total_q_b)
        print("Median seller price: %s" % median_p_s)
        print("Median buyer price: %s" % median_p_b)
        print("Final auction price: %s" % price)

        # (5) Distribution of the auction items:
        """
        To distribute to the buyers with the highest bids, I had to sort the list. However, this returns the index
        of the sorted list, not the original index. Haven't fixed this yet, first wanted to discuss solution.
        """
        buyers = sorted(buyers, key=attrgetter('item_price'), reverse=True)
        for n in buyers:
            buyer_quantity = n[1]

            buyer_code = buyers.index(n)
            if total_q_s >= buyer_quantity:
                print("Buyer %s gets %s units." % (buyer_code, buyer_quantity))
                total_q_s -= buyer_quantity
            elif total_q_s > 0:
                print("Buyer %s gets %s units." % (buyer_code, total_q_s))
                total_q_s = 0
            else:
                print("Buyer %s gets nothing." % buyer_code)

    def _broker_bids(self):
        """
        Helper function to broker the bids into a fair redistribution, according
        to some algorithm.
        """
        pass  # TODO
