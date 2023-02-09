from django.shortcuts import render

# Create your views here.
def firstPage(r):
    c=''
    try:
       if r.method=="POST":
        n1=eval(r.POST.get('num1'))
        n2=eval(r.POST.get('num2'))
        opr=r.POST.get('opr')
        if opr=="+":
            c=n1+n2;
        elif opr=="-":
            c=n1-n2;
        elif opr=="*":
            c=n1*n2;
        elif opr=="/":
            c=n1/n2;
    except:
        c="Invalid..."
    print(c)
    return render(r,'firstPage.html',{'c':c})

def even_odd(r):
    c=''
    try:
        if r.method=="POST":
            n=eval(r.POST.get('num1'))
            if n%2==0:
                c="Even Number";
            else :
                c="Odd Number";
    except:
        pass
    print(c)
    return render(r,'even_odd.html',{'c':c})

def result(r):
           if r.method=="POST":
             hindi=eval(r.POST.get('hindi'))
             sanskrit=eval(r.POST.get('sanskrit'))
             science=eval(r.POST.get('science'))
             social_science=eval(r.POST.get('social_science'))
             math=eval(r.POST.get('math'))

             total_marks=hindi+sanskrit+science+social_science+math
             percentage=total_marks*100/500
             if percentage>=30:
                div="3rd Div"
             elif percentage>=45:
                div="2nd DIV"
             elif percentage>=60:
                div="1st DIV"
             else:
                div="FAIL"
             data={
                'total_marks':total_marks,
                'percentage':percentage,
                'div':div
             }
             return render(r,'result.html',data)
           return render(r,'result.html')