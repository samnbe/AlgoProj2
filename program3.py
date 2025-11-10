from typing import List, Tuple


def program3(n: int, k: int, values: List[int]) -> Tuple[int, List[int]]:
    """
    Solution to Program 3
    
    Parameters:
    n (int): number of vaults
    k (int): no two chosen vaults are within k positions of each other
    values (List[int]): the values of the vaults

    Returns:
    int:  maximal total value
    List[int]: the indices of the chosen vaults(1-indexed)
    """
    # initialize the OPT array
    OPT = [-1] * (n + 1)
    vaults = []

    # fill the OPT array
    def compute_OPT(i: int) -> int:
        if i <= 0:
            return 0

        include_value = values[i - 1] + compute_OPT(i - k - 1)
        exclude_value = compute_OPT(i - 1)

        OPT[i] = max(include_value, exclude_value)
        return max(include_value, exclude_value)
    
    ans = compute_OPT(n)

    # backtrack to find which vaults were chosen
    i = n
    while i > 0:
        if OPT[i] != OPT[i - 1]:
            vaults.append(i)
            i -= k + 1
        else:
            i -= 1

    return ans, vaults[::-1] 


if __name__ == '__main__':
    n, k = map(int, input().split())
    values = list(map(int, input().split()))

    m, indices = program3(n, k, values)

    print(m)
    for i in indices:
        print(i)