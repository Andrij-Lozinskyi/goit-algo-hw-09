import timeit

class CoinFinder:
    def find_coins_greedy(self, amount, coins=[50, 25, 10, 5, 2, 1]):
        coin_count = {}
        for coin in coins:
            count = amount // coin
            if count > 0:
                coin_count[coin] = count
                amount -= coin * count
        return coin_count

    def find_min_coins(self, amount, coins=[50, 25, 10, 5, 2, 1]):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        prev_coin = [0] * (amount + 1)

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0 and dp[i - coin] + 1 < dp[i]:
                    dp[i] = dp[i - coin] + 1
                    prev_coin[i] = coin

        if dp[amount] == float('inf'):
            return {}

        coin_count = {}
        while amount > 0:
            coin = prev_coin[amount]
            if coin in coin_count:
                coin_count[coin] += 1
            else:
                coin_count[coin] = 1
            amount -= coin

        return coin_count

coin_finder = CoinFinder()

def run_greedy():
    return coin_finder.find_coins_greedy(113)

def run_dp():
    return coin_finder.find_min_coins(113)

if __name__ == "__main__":
    greedy_time = timeit.timeit(run_greedy, number=1000)
    dp_time = timeit.timeit(run_dp, number=1000)

    print(f"Жадібний алгоритм (1000 ітерацій): {greedy_time} секунд")
    print(f"Динамічне програмування (1000 ітерацій): {dp_time} секунд")
