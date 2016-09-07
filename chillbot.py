from errbot import BotPlugin, botcmd, arg_botcmd
import random

movies = {"action": {"Spectre": ['punny', 'silly'], "Inception": ['thought-provoking', 'sad', 'creepy'],
                     "Fight Club": ['thought-provoking', 'sad', 'uplifting', 'romantic']},
          "thriller": {"V for Vendetta": ['thought-provoking', 'uplifting'],
                       "Donnie Darko": ['creepy', 'thought-provoking', 'sad'],
                       "Seven": ['thought-provoking', 'sad', 'creepy']},
          "comedy": {"Deadpool": ['silly', 'punny'], "Ferris Bueller's Day Off": ['silly', 'romantic', 'uplifting'],
                     "The Breakfast Club": ['silly', 'romantic', 'thought-provoking', 'uplifting'],
                     "Shirely Valentine": ['life affirming', 'need a good cry and laugh']},
          "drama": {"The Cook, The Thief, His Wife & Her Lover": ['crying', 'emotionally drained', 'enraged', 'awe'],
                    "Shirely Valentine": ['life affirming', 'need a good cry and laugh']}}

genres = ['action', 'comedy', 'thriller', 'drama']

moods = ['creepy', 'thought-provoking', 'uplifting', 'silly', 'romantic', 'crying', 'emotionally drained', 'enraged',
         'awe', 'life affirming', 'need a good cry and laugh']


class Chillbot(BotPlugin):
    """
    Used to pick random movies to watch for Netflix and chill.
    """

    @botcmd
    def moods(self, message, args):
        return ', '.join(moods).title()

    @botcmd
    def genres(self, message, args):
        return ', '.join(genres).title()

    @arg_botcmd('genre', type=str)
    @arg_botcmd('--mood', dest='mood', type=str)
    def letschill(self, genre=None, mood=None):
        movie_list = []
        if not mood:
            mood = random.choice(moods)
        elif mood.lower() not in moods:
            return "Please use the moods command to get list of available moods."
        if genre.lower() not in genres:
            return "Please use the genres command to get list of available genres."
        for k,v in movies[genre.lower()].items():
            if mood.lower() in v:
                movie_list.append(k)
        return "You should watch {}".format(random.choice(movie_list))
