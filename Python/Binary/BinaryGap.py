def Binary_Gap(n):
    # limit the range of numbers
    if n <= 1 :
      return 0
    # search 1
    while n > 0 and n & 1 == 0 :
        n >>= 1
    max_gap = current_gap = 0
    # calculate number of '0'
    while n :
        if n & 1 :
            max_gap = max(max_gap, current_gap)
            current_gap = 0
        else :
            current_gap += 1
    return max_gap
