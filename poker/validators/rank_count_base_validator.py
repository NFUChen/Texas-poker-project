class RankCountValidator:
    def _ranks_with_target_count(self, target_count: int) -> dict:
        '''
        coupled with _card_rank_counts() method
        '''
        return {
            rank: rank_count
            for rank, rank_count in self._card_rank_counts.items()
            if rank_count == target_count
        }

    @property
    def _card_rank_counts(self) -> dict:
        '''
        coupled with _ranks_with_target_count() method
        '''

        card_rank_count = {}
        for card in self._cards:
            # if the key already exists, do nothing
            card_rank_count.setdefault(card.rank, 0)
            card_rank_count[card.rank] += 1

        return card_rank_count