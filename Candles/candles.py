def solution(candlesNumber, makeNew):
    leftovers=0
    burn=0
    
    while candlesNumber > 0 or leftovers>=makeNew:
        # burn the candles
        burn+=candlesNumber
        
        # left overs from candles burnt
        leftovers+=candlesNumber
        
        # get how many new candles
        candlesNumber=leftovers//makeNew
        leftovers=leftovers%makeNew
        
    return burn
    
if __name__ == "__main__":
    print(solution(5,2))