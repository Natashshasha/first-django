from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm


def reviews_page(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews')
    else:
        form = ReviewForm()

    reviews = Review.objects.filter(is_checked=True)

    return render(request, 'reviews/reviews.html', {
        'form': form,
        'reviews': reviews,
    })