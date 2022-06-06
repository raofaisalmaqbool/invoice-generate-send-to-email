from django.shortcuts import redirect, render
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from  . models import producat,seller,buyer
import datetime
from email_invoice import settings

# Create your views here.
def index(request):
    pro = producat.objects.all()
    slr = seller.objects.all()
    return render(request,'index.html',{'products':pro,'seller':slr})

def buy(request,pk):
    # print(pk)
    pro = producat.objects.get(pk=pk)

    if request.method == "POST":
        name = request.POST['name']
        address = request.POST['address']
        phone = request.POST['phone']
        email = request.POST['email']
        quantity = int(request.POST['quantity'])
        
        by = buyer(name=name,address=address,phone=phone, email=email)
        by.save()
        id = by.pk
        purchase_date = by.purchase_date
        # id = by.objects.get(id)
        # purchase_date = by.objects.get(purchase_date)
        amount = float(pro.price)
        pn = pro.name
        dis = pro.dis
        price = amount
        pro_quantity =quantity
        pro_total = amount*quantity         
        slr = seller.objects.all()
        data = {'id':id, 'purchase_date':purchase_date, 'p_name':pn,'p_price':price, 'email':email, 'b_name':name,'b_address':address,'b_phone':phone,'p_dis':dis,'p_quantity':pro_quantity, 'p_total':pro_total}
        
        html_content = render_to_string("detail.html", {'data': data, 'seller': slr} )
        text_content = strip_tags(html_content)
 
        email = EmailMultiAlternatives(subject='Product Invoice', from_email=settings.EMAIL_HOST_USER,
                             to=[email], body=text_content)
        email.attach_alternative(html_content, "text/html")
        email.send()
        msg = "Send Successfully"
        return render(request, 'detail.html', {'data': data, 'seller': slr, 'msg':msg})

    return render(request, 'buy.html')

