from django.db import models

QUESTION_TYPES = (
    ('text', 'Text'),
    ('radio', 'Radio'),
    ('mcq', 'Multi Choice'),
    ('yesno', 'Yes/No'),
    ('rating', 'Rating'),
    ('file', 'File Upload'),
)

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)


    def __str__(self):
        return self.name

class Question(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='questions')
    text = models.CharField(max_length=500)
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES)
    options = models.TextField(
        help_text="Comma separated options if applicable", blank=True, null=True
    )

    def get_options_list(self):
        if self.options:
            return [option.strip() for option in self.options.split(',')]
        return []

    def __str__(self):
        return f"{self.text} ({self.get_question_type_display()})"

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='reviews')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.product.name} on {self.submitted_at.strftime('%Y-%m-%d')}"

class Answer(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE,
                               related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return f"Answer to: {self.question.text}"
