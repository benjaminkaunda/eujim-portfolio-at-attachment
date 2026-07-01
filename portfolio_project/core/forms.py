from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 dark:border-gray-600 bg-gray-50 dark:bg-slate-700 focus:ring-2 focus:ring-primary focus:border-transparent outline-none transition',
            'placeholder': 'Your full name'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 dark:border-gray-600 bg-gray-50 dark:bg-slate-700 focus:ring-2 focus:ring-primary focus:border-transparent outline-none transition',
            'placeholder': 'your.email@example.com'
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 dark:border-gray-600 bg-gray-50 dark:bg-slate-700 focus:ring-2 focus:ring-primary focus:border-transparent outline-none transition',
            'rows': 5,
            'placeholder': 'Your message...'
        })
    )