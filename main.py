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
    # this underline prevents a bug in the json api also the 49 line
    player = roster[0]
    players_dict = player['players']
    # the keys for player is '1610616833', '1610616834' that one is empty dont know why..
    pl = players_dict['1610616833']
    """every object in the pl list will be a player and have those keys 'firstName', 'lastName', 
    'personId', 'teamAbbrev', 'teamCity', 'teamName', 'teamConf', 'teamId', 'jersey', 'positionFull', 'positionShort',
     'starter', 'reserve', 'injured', 'playerConf', 'firstTime', 'captain', 'allStarTeamId', 'nugget', 'stats"""
    for i in pl:
    	firstName = i['firstName']
    	lastName = i['lastName']
    	teamName = i['teamName']
    	positionFull = i['positionFull']
    	jersey = i['jersey']
    	starter = i['starter']

    	print(f"Name: {firstName} {lastName} \nTeam: {teamName}\nPosition: {positionFull}\nJersey: {jersey}\nStarter: {starter}")
    	print("=" * 20)
    


get_all_star()
