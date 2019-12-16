class PlayerAdmission:
    def __init__(self, player_type, initial_cash):
        self._player_type = player_type
        self._initial_cash = initial_cash

    def admit(self):
        return self._player_type(self._initial_cash)


class MartingaleGambler:
    def __init__(self, cash):
        self._cash = cash
        self._bet_round = 0

    @property
    def wager(self) -> int:
        bet = self._cash
        self._cash = 0
        return bet

    @property
    def play(self) -> int:
        return self._bet_round

    def wins(self, money: int) -> None:
        self._cash = money
        self._bet_round += 1    # advance to next round

    @property
    def cash(self):
        return self._cash


class MartingaleGameConfiguration:
    def __init__(self, s: str, alphabet: str):
        self._s = s
        self._absorbent_state = len(s)
        self._alphabet = alphabet
        self._alphabet_size = len(alphabet)

    def win_value(self, bet):
        return bet * self._alphabet_size

    def _state_is_valid(self, state):
        if state < 0 or state > self._absorbent_state:
            raise ValueError(f"state is out of bounds; valid values are [0={self._alphabet_size-1}")

    def get_state(self, state: int) -> str:
        self._state_is_valid(state)
        return self._s[state]

    def is_absorbent_state(self, state):
        self._state_is_valid(state)
        return state == self._absorbent_state


class MartingaleGame:
    def __init__(self, player_admission: PlayerAdmission, game_config: MartingaleGameConfiguration):
        self._admission = player_admission
        self._game_config = game_config

    def run(self):
        round = 0
        gamblers = set()

        while not self._game_config.is_absorbent_state(round):
            gamblers.add(self._admission.admit())
            losers = set()

            for gambler in gamblers:
                bet_amount = gambler.wager

                if self._game_config.get_state(gambler.play) == self._game_config.get_state(round):
                    gambler.wins(self._game_config.win_value(bet_amount))
                else:
                    losers.add(gambler)

            gamblers = gamblers.difference(losers)
            round += 1

        return gamblers

