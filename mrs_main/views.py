from .mrs_script import recommend, search, find_movie, random_movies
import html
from django.shortcuts import render, redirect

def index(request):
    search_query = request.POST.get('my_input')
    if request.method == 'POST':

        if search_query == '' or search_query == None or search_query == "None":
            r_movies = random_movies()
            context = {'search_term': search_query, 'random_movies': r_movies}
        else:
            results = search(search_query)
            context = {'results': results, 'search_term': search_query}
    else:
        r_movies = random_movies()
        context = {'result': None, 'search_term': search_query, 'random_movies': r_movies}

    return render(request, 'index.html', context)


def movie(request):
    if request.method == 'POST':
        search_query = request.POST.get('my_input')
        movie_title = html.escape(request.POST.get('movie_recommend'))
        movie_id = int(request.POST.get('movieId'))

        if movie_title == '' or movie_id == '':
            return redirect('/')
        else:
            results = find_movie(movie_id)
            recommendations = recommend(movie_title)
            context = {'movie': results, 'recommendations': recommendations, 'search_term': search_query}
    else:
        return redirect('/')

    return render(request, 'movie.html', context)
