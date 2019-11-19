from django import forms


class QueryForm(forms.Form):
    TYPE_SELECTION = (
        ("ブログの感想","ブログの感想"),
        ("サイトへの要望","サイトへの要望"),
        ("仕事の依頼","仕事の依頼")
    )
    username = forms.CharField(max_length=31,empty_value="名無しさん",required=False)
    email = forms.EmailField()
    query_type = forms.ChoiceField(choices=TYPE_SELECTION)
    content = forms.TextInput()


