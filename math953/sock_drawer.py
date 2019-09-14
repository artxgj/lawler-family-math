from scipy.special import binom

def sock_drawer(black_limit):
   """
      r - red socks
      b - black socks

      When two socks are drawn at random, the probability that both
      are red is 1/2.

      Binomial(r, 2) / Binomial(r+b, 2) = 1/2
   """
   prev_black_sol = 0
   for r in range(1, int(2.5*black_limit) + 1):
       for b in range(prev_black_sol+1, black_limit+1):
           ratio = binom(r, 2)/binom(r+b, 2)

           if ratio == 0.5:
               print(f"black={b}, red={r}")
               prev_black_sol = b
               break

           if ratio < 0.5:
               break


if __name__ == '__main__':
    sock_drawer(8000)
