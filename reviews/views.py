from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Question, Review, Answer
from .forms import ReviewForm
from django.db.models import Count
from django.db.models.functions import TruncDate
import json

def product_list(request):
    products = Product.objects.all()
    return render(request, "reviews/product_list.html", {"products": products})

def product_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    questions = product.questions.all()

    if request.method == "POST":
        form = ReviewForm(request.POST, questions=questions)
        if form.is_valid():
            review = Review.objects.create(product=product)
            for question in questions:
                field_name = f"question_{question.id}"
                answer_data = form.cleaned_data.get(field_name)
                if isinstance(answer_data, list):
                    # Save list answers as comma separated
                    answer_str = ", ".join(answer_data)
                    Answer.objects.create(
                        review=review, question=question, answer=answer_str
                    )
                else:
                    Answer.objects.create(
                        review=review, question=question, answer=answer_data
                    )
            return redirect("review_thanks")
    else:
        form = ReviewForm(questions=questions)

    context = {
        "product": product,
        "form": form,
    }
    return render(request, "reviews/product_review.html", context)

def review_thanks(request):
    return render(request, "reviews/thanks.html")

def review_analytics(request):
    # Rating distribution
    rating_data = Answer.objects.filter(
        question__question_type='rating'
    ).values('answer').annotate(
        count=Count('id')
    ).order_by('answer')
    
    rating_counts = [0] * 5
    for item in rating_data:
        try:
            index = int(item['answer']) - 1
            rating_counts[index] = item['count']
        except (ValueError, IndexError):
            continue
    rating_labels = ['1', '2', '3', '4', '5']

    # Yes/No responses - fixed with proper ordering
    yes_no_data = Answer.objects.filter(
        question__question_type='yesno'
    ).values('answer').annotate(
        count=Count('id')
    ).order_by('answer')  # Add ordering
    
    yes_no_counts = [0, 0]  # Default [Yes, No] counts
    yes_no_labels = ['Yes', 'No']
    
    for item in yes_no_data:
        if item['answer'] == 'Yes':
            yes_no_counts[0] = item['count']
        elif item['answer'] == 'No':
            yes_no_counts[1] = item['count']

    # MCQ responses
    mcq_data = Answer.objects.filter(
        question__question_type='mcq'
    ).values('answer').annotate(
        count=Count('id')
    ).order_by('-count')
    
    mcq_labels = [item['answer'] for item in mcq_data]
    mcq_counts = [item['count'] for item in mcq_data]

    # Timeline data
    timeline_data = Review.objects.annotate(
        date=TruncDate('submitted_at')
    ).values('date').annotate(
        count=Count('id')
    ).order_by('date')
    
    timeline_labels = [item['date'].strftime('%Y-%m-%d') for item in timeline_data]
    timeline_counts = [item['count'] for item in timeline_data]

    context = {
        'rating_labels': json.dumps(rating_labels),
        'rating_data': json.dumps(rating_counts),
        'yes_no_labels': json.dumps(yes_no_labels),
        'yes_no_data': json.dumps(yes_no_counts),
        'mcq_labels': json.dumps(mcq_labels),
        'mcq_data': json.dumps(mcq_counts),
        'timeline_labels': json.dumps(timeline_labels),
        'timeline_data': json.dumps(timeline_counts),
    }
    
    return render(request, "reviews/analytics.html", context)

def add_product(request):
    # Your view logic here
    return render(request, 'add_product.html')