from requests import get
from pprint import PrettyPrinter

# Public API
BASE_URL = "https://data.nba.net"
ALL_JSON = "/prod/v1/today.json"
TEAM_ROSTER = "/prod/v1/2022/teams/roster.json"
TEAMS = "/prod/v2/2022/teams.json"
printer = PrettyPrinter()


# vars
def get_links():
    data = get(BASE_URL + ALL_JSON).json()
    links = data['links']
    #printer.pprint(links)
    return links


def get_calendar():
    calendar = get_links()['calendar']
    data = get(BASE_URL + calendar).json()
    return data


def get_teams():
    teams = get_links()['teams']
    data = get(BASE_URL + teams).json()
    league = data['league']
    standard = league['standard']
    print("STANDARD LEAGUE")
    for team in standard:
        fullname = team['fullName']
        nickname = team['nickname']
        print(f"{fullname} /nickname/ --> {nickname}")
        print("=" * 20)


def get_all_star():
    all_star = get_links()['allstarRoster']
    data = get(BASE_URL + all_star).json()
    content = data['sportsContent']
    roster = content['roster']
    # this underline prevents a bug in the json api
    player = roster[0]
    players_dict = player['players']
    # the keys for player is '1610616833', '1610616834' that one is empty dont know why...
    players = players_dict['']
    return players
    """for i in players:
        first_name = players['firstName']
        jersey = players['jersey']
        teamName = players['teamName']
        positionFull = players['positionFull']
        print(f'{first_name} is an allstar, plays for the{teamName} as a {positionFull} and wear the {jersey} jersey')"""

a = get_all_star()
printer.pprint(a)
