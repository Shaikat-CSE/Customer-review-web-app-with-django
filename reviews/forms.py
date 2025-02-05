from django import forms
from .models import Review, Answer, Question

class ReviewForm(forms.Form):
    """
    Dynamically builds a form based on a product's questions.
    """

    def __init__(self, *args, **kwargs):
        questions = kwargs.pop("questions", [])
        super().__init__(*args, **kwargs)

        for question in questions:
            field_name = f"question_{question.id}"
            if question.question_type == "text":
                self.fields[field_name] = forms.CharField(
                    label=question.text, widget=forms.Textarea, required=True
                )
            elif question.question_type == "radio":
                choices = [(opt, opt) for opt in question.get_options_list()]
                self.fields[field_name] = forms.ChoiceField(
                    label=question.text, widget=forms.RadioSelect, choices=choices
                )
            elif question.question_type == "mcq":
                choices = [(opt, opt) for opt in question.get_options_list()]
                self.fields[field_name] = forms.MultipleChoiceField(
                    label=question.text, widget=forms.CheckboxSelectMultiple,
                    choices=choices
                )
            elif question.question_type == "yesno":
                self.fields[field_name] = forms.ChoiceField(
                    label=question.text,
                    choices=[("Yes", "Yes"), ("No", "No")],
                    widget=forms.RadioSelect,
                )
            elif question.question_type == "rating":
                # rating between 1 and 5
                choices = [(str(num), str(num)) for num in range(1, 6)]
                self.fields[field_name] = forms.ChoiceField(
                    label=question.text, widget=forms.RadioSelect,
                    choices=choices
                )
            elif question.question_type == "file":
                self.fields[field_name] = forms.FileField(
                    label=question.text, required=False
                )
            else:
                self.fields[field_name] = forms.CharField(
                    label=question.text, required=True
                )
