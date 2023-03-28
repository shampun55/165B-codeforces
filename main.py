def good(n, v, k):
	counter = v
	power = 1
    while v // (k ** power) > 0:
	    counter += v // (k ** power)
	    power += 1
	return counter >= n


def main():
    n, k = map(int, input().split())
    l, r = -1, 10**9
    while l+1 < r:
        mid = (l+r) // 2
        if good(n, mid, k):
            r = mid
        else:
            l = mid
    print(r)

if __name__ == '__main__':
    main()