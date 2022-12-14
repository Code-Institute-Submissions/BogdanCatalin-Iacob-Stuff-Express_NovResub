from django import forms
from .models import Product, Category, Review


# from code institute
class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for friendly_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border border-black rounded-lg'


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = (
            'review_text',
            'star_rating',
        )
