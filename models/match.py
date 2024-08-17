"""Match model"""


class Match:
    def __init__(self, match_day: int,
                 home_team: str, home_team_logo_src: str,
                 away_team: str, away_team_logo_src: str):
        self.match_day = match_day
        self.home_team = home_team
        self.home_team_logo_src = home_team_logo_src
        self.away_team = away_team
        self.away_team_logo_src = away_team_logo_src

    def __repr__(self):
        return (f'{self.match_day}.\t{self.home_team}\t-\t{self.away_team}\n'
                f'{self.home_team_logo_src}\n{self.away_team_logo_src}')
