from django.contrib.auth.forms import UserCreationForm, forms
from django import forms as forms2
from django.contrib.auth.models import User
from User.models import Userinfo, Courseinfo, Paymentinfo

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=15)
    last_name = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ['username',
                  'email',
                  'first_name',
                  'last_name',
                  'password1',
                  'password2'
                  ]

class UserInfoForm(forms2.ModelForm):

    class Meta:
        model = Userinfo
        exclude = ["user",
                   'user_firstname',
                   'user_lastname',
                   ]
        fields = ['user_id',
                  'user_semester',
                  ]

class UserDeleteForm(forms2.ModelForm):

    class Meta:
        model = Userinfo
        fields = ['user_id',
                  ]

class CourseInfoForm(forms2.ModelForm):

    class Meta:
        model = Courseinfo
        fields = ['course_userid',
                  'course_semester',
                  'course_id',
                  'course_title',
                  ]

class CourseDeleteForm(forms2.ModelForm):

    class Meta:
        model = Courseinfo
        fields = ['course_id',
                  ]

class PaymentInfoForm(forms2.ModelForm):

    class Meta:
        model = Paymentinfo
        exclude = ["payment_installment",
                   'payment_due',
                   'payment_paid',
                   'payment_status',
                   ]
        fields = ['payment_userid',
                  'payment_semester',
                  ]

class PaymentDeleteForm(forms2.ModelForm):

    class Meta:
        model = Paymentinfo
        fields = ['payment_userid',
                  'payment_semester',
                  ]

class MakePaymentForm(forms2.ModelForm):

    class Meta:
        model = Paymentinfo
        fields = ['payment_userid',
                  'payment_semester',
                  'payment_paid',
                  ]