from typing import List, Tuple


def program4B(n: int, k: int, values: List[int]) -> Tuple[int, List[int]]:
    """
    Solution to Program 4B
    
    Parameters:
    n (int): number of vaults
    k (int): no two chosen vaults are within k positions of each other
    values (List[int]): the values of the vaults

    Returns:
    int:  maximal total value
    List[int]: the indices of the chosen vaults(1-indexed)
    """
    # initialize the OPT array and first element 
    OPT = [0] * (n+1)
    OPT[0] = 0
    vaults = []

    # fill the OPT array
    for i in range(1, n + 1):
        include_value = values[i - 1]
        if i - k - 1 > 0:
            include_value += OPT[i - k - 1]
        last_value = OPT[i - 1]
        if include_value > last_value:
            OPT[i] = include_value
        else:
            OPT[i] = last_value

    # backtrack to find which vaults were chosen
    i = n
    while i > 0:
        if OPT[i] != OPT[i - 1]:
            vaults.append(i)
            i -= k + 1
        else:
            i -= 1
    
    return OPT[n], vaults[::-1]


if __name__ == '__main__':
    n, k = map(int, input().split())
    values = list(map(int, input().split()))

    m, indices = program4B(n, k, values)

    print(m)
    for i in indices:
        print(i)