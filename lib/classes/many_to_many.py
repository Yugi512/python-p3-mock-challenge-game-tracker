class Game:

    def __init__(self, title):
        self.title = title

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        is_false = hasattr(self,"title")

        if isinstance(title, str) and len(title) > 0 and is_false == False:
            self._title = title
        else:
            raise Exception("not a string")
        

    def results(self):
        ind_game_list = []
        results_list = Result.all
        for result in results_list:
            if result.game == self:
                ind_game_list.append(result)
        return ind_game_list


    def players(self):
        ind_player_list = []
        results_list = Result.all
        for result in results_list:
            if result.game == self and result.player not in ind_player_list:
                ind_player_list.append(result.player)
        return ind_player_list

    def average_score(self, player):
        count = 0
        count_list = []
        results_list = Result.all
        for result in results_list: 
            if result.player == player:
                count_list.append(result.score)
                count += result.score
        return count/len(count_list)

class Player:

    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self,username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username
        else:
            raise Exception("not a string")

    def results(self):
        ind_player_list = []
        results_list = Result.all
        for result in results_list:
            if result.player == self:
                ind_player_list.append(result)
        return ind_player_list
        

    def games_played(self):
        games_list = []
        results_list = Result.all
        for result in results_list:
            if result.game not in games_list and self == result.player:
                games_list.append(result.game)
        return games_list

    def played_game(self, game):
        if game in self.games_played():
            return True
        else:
            return False 

    def num_times_played(self, game):
        dicts = {}
        results_list = Result.all
        if game.title not in dicts:
            dicts[game.title] = 0
        for result in results_list:
            print(dicts)
            if self == result.player and result.game.title in dicts:
                dicts[result.game.title] += 1
        return dicts.get(game.title)

class Result:
    all= []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        self.all.append(self)
    
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,score):
        is_false = hasattr(self,"score")
        if isinstance(score, int) and is_false == False  and 1 <= score <= 5000:
            self._score = score
        else:
            raise Exception("not a int")
        
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        is_false = hasattr(self,"player")
        if isinstance(player, Player) and is_false == False:
            self._player = player
        else:
            raise Exception("not the same")
        
    @property
    def game(self):
        return self._game

    @game.setter
    def game(self,game):
        is_false = hasattr(self,"game")
        if isinstance(game, Game) and is_false == False:
            self._game = game
        else:
            raise Exception("not the same")