from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.io import show, output_file
from pprintpp import pprint


current_movies = [
    {'imdbid': 'tt0099878', 'title': 'Jetsons: The Movie', 'genre': 'Animation, Comedy, Family', 'released': '07/06/1990', 'imdbrating': 5.4, 'imdbvotes': 2731, 'country': 'USA', 'numericrating': 4.3, 'usermeter': 46},
    {'imdbid': 'tt0099892', 'title': 'Joe Versus the Volcano', 'genre': 'Comedy, Romance', 'released': '03/09/1990', 'imdbrating': 5.6, 'imdbvotes': 23680, 'country': 'USA', 'numericrating': 5.2, 'usermeter': 54},
    {'imdbid': 'tt0099938', 'title': 'Kindergarten Cop', 'genre': 'Action, Comedy, Crime', 'released': '12/21/1990', 'imdbrating': 5.9, 'imdbvotes': 83461, 'country': 'USA', 'numericrating': 5.1, 'usermeter': 51},
    {'imdbid': 'tt0099939', 'title': 'King of New York', 'genre': 'Crime, Thriller', 'released': '09/28/1990', 'imdbrating': 7, 'imdbvotes': 19031, 'country': 'Italy, USA, UK', 'numericrating': 6.1, 'usermeter': 79},
    {'imdbid': 'tt0099951', 'title': 'The Krays', 'genre': 'Biography, Crime, Drama', 'released': '11/09/1990', 'imdbrating': 6.7, 'imdbvotes': 4247, 'country': 'UK', 'numericrating': 6.4, 'usermeter': 82}
]


source = ColumnDataSource({
    'movies': [movie['title'] for movie in current_movies],
    'imdb_ratings': [movie['imdbrating'] for movie in current_movies],
    'rt_ratings': [movie['usermeter'] for movie in current_movies],
    'colors': ['#008000' if 'USA' in movie['country'] else '#FF9900' for movie in current_movies],
    'countries': [movie['country'] for movie in current_movies]
})

plot = figure(tooltips=[('Movie', '@movies'), ('Country', '@countries')])
plot.circle(x='imdb_ratings', y='rt_ratings', color='colors', source=source)
plot.xaxis.axis_label = 'IMDB Rating'
plot.yaxis.axis_label = 'Rotten Tomatoes Rating'

print(source.data['colors'])
output_file('movies_ratings.html')
show(plot)
