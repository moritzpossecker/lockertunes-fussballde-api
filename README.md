# lockertunes-fussballde-api

Get data about your team from [fussball.de](https://www.fussball.de).

## How to use

This API contains following endpoints:

- /get-teams/`league_url: string`
- /get-matches/`team_name: string`/`league_url: string`/`game_span: int`

### Formatting

- Url's should be sent without `https://www.fussball.de/`
- Slashes should be replaced with `SHLASH`
- Spaces should be replaced with `SPACE`