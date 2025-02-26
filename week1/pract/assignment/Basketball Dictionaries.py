# Challenge 1: Update the Constructor
class Player:
    def __init__(self, player_dict):
        self.name = player_dict["name"]
        self.age = player_dict["age"]
        self.position = player_dict["position"]
        self.team = player_dict["team"]

    # Ninja Bonus: Add a class method to create a list of Player objects
    @classmethod
    def get_team(cls, team_list):
        return [cls(player) for player in team_list]

    # Optional: Add a __repr__ method to make it easier to print Player objects
    def __repr__(self):
        return f"Player(name={self.name}, age={self.age}, position={self.position}, team={self.team})"


# Challenge 2: Create instances using individual player dictionaries
kevin = {
    "name": "Kevin Durant", 
    "age": 34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}

jason = {
    "name": "Jason Tatum", 
    "age": 24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}

kyrie = {
    "name": "Kyrie Irving", 
    "age": 32, 
    "position": "Point Guard", 
    "team": "Brooklyn Nets"
}

# Create Player instances
player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

# Print instances to verify
print(player_kevin)
print(player_jason)
print(player_kyrie)


# Challenge 3: Populate a list of Player instances from a list of dictionaries
players = [
    {
        "name": "Kevin Durant", 
        "age": 34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age": 24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age": 32, 
        "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age": 33, 
        "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age": 32, 
        "position": "Power Forward", 
        "team": "Philadelphia 76ers"
    },
    {
        "name": "", 
        "age": 16, 
        "position": "P", 
        "team": "en"
    }
]

# Create a new list of Player instances
new_team = []
for player_dict in players:
    player = Player(player_dict)
    new_team.append(player)

# Print the new_team list to verify
print(new_team)


# Ninja Bonus: Use the class method to create a list of Player objects
team_list = [
    {
        "name": "Kevin Durant", 
        "age": 34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age": 24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    }
]

# Use the class method to create Player objects
team_players = Player.get_team(team_list)

# Print the team_players list to verify
print(team_players)