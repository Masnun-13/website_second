from django.shortcuts import render
from .form import UserRegistrationForm, UserInfoForm, UserDeleteForm, CourseInfoForm, CourseDeleteForm, PaymentInfoForm, MakePaymentForm, PaymentDeleteForm
from .models import Userinfo, Courseinfo, Paymentinfo
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "User/home.html")

def register(request):
    if(request.method == "POST"):
        form = UserRegistrationForm(request.POST)
        if(form.is_valid()):
            form.save()
            return render(request, "User/home.html")
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, "User/register.html", context)

def login(request):
    return render(request, "User/login.html")

@login_required
def logout(request):
    return render(request, "User/logout.html")

@login_required
def profile(request):
    context = {
        'fname': request.user.first_name,
        'lname': request.user.last_name,
        'email': request.user.email,
    }
    return render(request, "User/profile.html", context)

@login_required
def userinfo(request):
    uinfo = Userinfo.objects.all().order_by('user_id', '-user_semester')
    context = {'uinfo': uinfo}
    return render(request, "User/userinfo.html", context)

@login_required()
def enteruserinfo(request):
    if(request.method == "POST"):
        form = UserInfoForm(request.POST)
        if(form.is_valid()):
            this_user= form.save(commit=False)
            this_user.user=request.user.username
            this_user.user_firstname=request.user.first_name
            this_user.user_lastname = request.user.last_name
            this_user.save()
            uinfo = Userinfo.objects.all().order_by('user_id', '-user_semester')
            context = {'uinfo': uinfo}
            return render(request, "User/userinfo.html", context)
    else:
        form = UserInfoForm()
    context = {'form': form}
    return render(request, "User/enteruserinfo.html", context)

@login_required()
def deleteuser(request, user_id):
    user = Userinfo.objects.get(user_id=user_id)
    form = UserDeleteForm(request.POST)
    if request.method == "POST":
        user.delete()
        uinfo = Userinfo.objects.all().order_by('user_id', '-user_semester')
        context = {'uinfo': uinfo}
        return render(request, "User/userinfo.html", context)

    context = {'form': form}
    return render(request, "User/delete.html", context)

@login_required()
def updateuser(request, user_id):
    user = Userinfo.objects.get(user_id=user_id)
    form = UserInfoForm(request.POST)
    if request.method == 'POST':
        form = UserInfoForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            uinfo = Userinfo.objects.all().order_by('user_id', '-user_semester')
            context = {'uinfo': uinfo}
            return render(request, "User/userinfo.html", context)
    form = UserInfoForm(initial=user.__dict__)
    context = {'form': form, 'user' : user}
    return render(request, "User/update.html", context)

@login_required
def courseinfo(request):
    cinfo = Courseinfo.objects.all().order_by('course_userid', '-course_semester')
    context = {'cinfo': cinfo}
    return render(request, "User/courseinfo.html", context)

@login_required()
def entercourseinfo(request):
    if(request.method == "POST"):
        form = CourseInfoForm(request.POST)
        if(form.is_valid()):
            form.save()
            cinfo = Courseinfo.objects.all().order_by('course_userid', '-course_semester')
            context = {'cinfo': cinfo}
            return render(request, "User/courseinfo.html", context)
    else:
        form = CourseInfoForm()
    context = {'form': form}
    return render(request, "User/entercourseinfo.html", context)

@login_required()
def deletecourse(request, course_id):
    course = Courseinfo.objects.get(course_id=course_id)
    form = CourseDeleteForm(request.POST)
    if request.method == "POST":
        course.delete()
        cinfo = Courseinfo.objects.all().order_by('course_userid', '-course_semester')
        context = {'cinfo': cinfo}
        return render(request, "User/courseinfo.html", context)

    context = {'form': form}
    return render(request, "User/deletecourse.html", context)

@login_required()
def updatecourse(request, course_id):
    course = Courseinfo.objects.get(course_id=course_id)
    if request.method == 'POST':
        form = CourseInfoForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            cinfo = Courseinfo.objects.all().order_by('course_userid', '-course_semester')
            context = {'cinfo': cinfo}
            return render(request, "User/courseinfo.html", context)
    form = CourseInfoForm(initial=course.__dict__)
    context = {'form': form, 'course' : course}
    return render(request, "User/updatecourse.html", context)

@login_required
def paymentinfo(request):
    for r in Paymentinfo.objects.all():
        if(r.payment_paid>=r.payment_due):
            r.payment_status="Paid"
            r.save()
        elif(r.payment_paid>0):
            r.payment_status = "Partially Paid"
            r.save()
    pinfo = Paymentinfo.objects.all().order_by('payment_userid', 'payment_semester', 'payment_installment')
    context = {'pinfo': pinfo}
    return render(request, "User/paymentinfo.html", context)

@login_required()
def enterpaymentinfo(request):
    if(request.method == "POST"):
        form = PaymentInfoForm(request.POST)
        if(form.is_valid()):
            a = form.instance.payment_userid
            b = form.instance.payment_semester
            for t in range (1, 6):
                r = Paymentinfo(payment_userid=a, payment_semester=b,
                                payment_installment=t, payment_due=14850,
                                payment_paid=0, payment_status="Unpaid")
                r.save()
            for r in Paymentinfo.objects.all():
                if (r.payment_paid >= r.payment_due):
                    r.payment_status = "Paid"
                    r.save()
                elif(r.payment_paid > 0):
                    r.payment_status = "Partially Paid"
                    r.save()
            pinfo = Paymentinfo.objects.all().order_by('payment_userid', 'payment_semester', 'payment_installment')
            context = {'pinfo': pinfo}
            return render(request, "User/paymentinfo.html", context)
    else:
        form = PaymentInfoForm()
    context = {'form': form}
    return render(request, "User/enterpaymentinfo.html", context)

def deletepaymentinfo(request):
    if(request.method == "POST"):
        form = PaymentDeleteForm(request.POST)
        if(form.is_valid()):
            a = form.instance.payment_userid
            b = form.instance.payment_semester
            for r in Paymentinfo.objects.all():
                if(r.payment_userid==a and r.payment_semester==b):
                    r.delete()
            for r in Paymentinfo.objects.all():
                if (r.payment_paid >= r.payment_due):
                    r.payment_status = "Paid"
                    r.save()
                elif (r.payment_paid > 0):
                    r.payment_status = "Partially Paid"
                    r.save()
            pinfo = Paymentinfo.objects.all().order_by('payment_userid', 'payment_semester', 'payment_installment')
            context = {'pinfo': pinfo}
            return render(request, "User/paymentinfo.html", context)
    else:
        form = PaymentDeleteForm()
    context = {'form': form}
    return render(request, "User/deletepayment.html", context)

def makepayment(request):
    if(request.method == "POST"):
        form = MakePaymentForm(request.POST)
        if(form.is_valid()):
            a = form.instance.payment_userid
            s = form.instance.payment_semester
            b = form.instance.payment_paid
            for t in range (1,6):
                r = Paymentinfo.objects.get(payment_userid=a, payment_semester=s, payment_installment=t)
                if(b<=(r.payment_due-r.payment_paid)):
                    r.payment_paid+=b
                    b=0;
                else:
                    b-=(r.payment_due-r.payment_paid)
                    r.payment_paid=r.payment_due
                r.save()
            for r in Paymentinfo.objects.all():
                if (r.payment_paid >= r.payment_due):
                    r.payment_status = "Paid"
                    r.save()
                elif(r.payment_paid > 0):
                    r.payment_status = "Partially Paid"
                    r.save()
            pinfo = Paymentinfo.objects.all().order_by('payment_userid', 'payment_semester', 'payment_installment')
            context = {'pinfo': pinfo}
            return render(request, "User/paymentinfo.html", context)
    else:
        form = MakePaymentForm()
    context = {'form': form}
    return render(request, "User/makepayment.html", context)