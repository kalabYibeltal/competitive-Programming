class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        array = [[alice+bob,alice,bob] for alice, bob in zip(aliceValues, bobValues)]
        array = sorted(array, key=lambda items: items[0], reverse=True)
        al = b = 0
        turn = 0 
        for tot, A, B in array:
            al += (1-turn) *  A
            b += (turn) * B
            turn = 1 - turn 
        
        if al == b: return 0
        if al > b: return 1
        return -1