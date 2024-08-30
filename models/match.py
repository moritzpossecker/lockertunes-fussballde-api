"""Match model"""


class Match:
    def __init__(self, match_day: int,
                 team: str, team_logo_src: str,
                 opponent: str, opponent_logo_src: str,
                 home_game: bool, AwayHome: str):
        self.match_day = match_day
        self.team = team
        self.team_logo_src = team_logo_src
        self.opponent = opponent
        self.opponent_logo_src = opponent_logo_src
        self.home_game = home_game
        self.AwayHome = AwayHome

    def to_dict(self):
        return {
            "match_day": self.match_day,
            "team": self.team,
            "team_logo_src": self.team_logo_src,
            "opponent": self.opponent,
            "opponent_logo_src": self.opponent_logo_src,
            "home_game": self.home_game,
            "AwayHome": self.AwayHome
        }

    def __repr__(self):
        return (f'{self.match_day}.\t{self.team}\t-\t{self.opponent}\n'
                f'{self.team_logo_src}\n{self.opponent_logo_src}')
