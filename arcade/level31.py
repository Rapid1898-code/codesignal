def depositProfit(deposit, rate, threshold):
    actDeposit = deposit
    count = 0
    while actDeposit < threshold:
        count += 1
        actDeposit += actDeposit * rate / 100
    return count
        