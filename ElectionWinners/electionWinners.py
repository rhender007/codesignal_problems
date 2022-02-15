def solution(votes, k):
    # winner needs more votes than anyone else ie difference less than k means candidate can still win
    max_votes=max(votes) # 5
    min_votes_can_still_win=max_votes-k+1
    
    # adding this to handle the case where if we have k=0 and tie
    if k==0 and votes.count(max_votes)>1:
        # set min votes to win to higher than the max vote
        min_votes_can_still_win=max_votes+1
    
    if k==0 and votes.count(max_votes)==1:
        # win is the max here
        min_votes_can_still_win=max_votes
    return sum(1 for i in votes if i >= min_votes_can_still_win)
    
if __name__ == "__main__":
    print(solution(votes=[2, 3, 5, 2],k=3))
