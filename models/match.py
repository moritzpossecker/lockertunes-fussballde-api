"""Match model"""


class Match:
    def __init__(self, match_day: int, home_team: str, away_team: str,):
        self.match_day = match_day
        self.home_team = home_team
        self.away_team = away_team

    def __repr__(self):
        return f'{self.match_day}.\t{self.home_team}\t-\t{self.away_team}'
