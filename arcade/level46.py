def electionsWinners(votes, k):
    countPossible = 0
    maxVotes = max(votes)
    if k == 0:
        if votes.count(maxVotes) == 1:
            return 1
        else:
            return 0
    for e in votes:
        if e + k > maxVotes:
            countPossible += 1
    return(countPossible)