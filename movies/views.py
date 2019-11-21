from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Review, Genre
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

def movielist(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies':movies})


def moviedetail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    form = ReviewForm()
    context = {'movie': movie, 'form': form}
    return render(request, 'movies/detail.html', context)


@login_required
def reviews_create(request, movie_pk):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.movie_id = movie_pk
            review.save()
            return redirect('movies:moviedetail', movie_pk)
    else:
        form = ReviewForm()
    return redirect('movies:moviedetail', movie_pk)


@login_required
def reviews_delete(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if review.user == request.user:
        review.delete()
    return redirect('movies:moviedetail', movie_pk)


@login_required
def like(request, movie_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    if user in movie.liked_users.all():
        movie.liked_users.remove(user)
    else:
        movie.liked_users.add(user)
    return redirect('movies:moviedetail', movie_pk)
