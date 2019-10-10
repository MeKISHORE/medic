from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import reg, patient_data


# Create your views here.
def index(request):
    return render(request,'hospital/index.html')

def HospitalReg(request):
    return render(request,'hospital/HospitalReg.html')


def Hospital_login(request):
    return render(request,'hospital/Hospital_login.html')

def RegisterHospital(request):
    if request.method=='POST':
        id=request.POST['hid']
        hname=request.POST['hname']
        mail=request.POST['mail']
        beds=request.POST['beds']
        psw=request.POST['psw']
        data=reg(
            Hopital_id=id,
            hospital_name=hname,
            hospital_mail=mail,
            Hopital_t_beds=beds,
            Hospital_pass=psw,
        )
        data.save()
        return redirect('index')
    else:
        return redirect('index')


def Hospital_page(request):
    # return HttpResponse('hello')
    try:
        hospital_mail = request.POST['Hospital_Email']
        Hospital_pass = request.POST['Hospital_Pass']
        if request.method == 'POST':
            # print('2')
            obj = reg.objects.get(Q(hospital_mail=hospital_mail))
            if obj.Hospital_pass == Hospital_pass:
                # print('3')
                data=patient_data.objects.filter(hospital_id=obj.Hopital_id)
                pend=data.filter(process='pending')
                appr=data.filter(process='approved')
                return render(request, 'hospital/Hospital_page.html', {'obj': obj,'pend': pend,'appr':appr})
        else:
            # print('4')
            # return redirect('Hospital_login')
            return redirect('index')

    except:
        # print('6')
        # return redirect('Hospital_login')
        return redirect('index')

# update section-------------------------------------------------------------------------------------------------
def updatehospital(request):
    try:
        hospital_mail = request.POST['hmail']
        Hopital_id = request.POST['hid']
        beds = request.POST['beds']
        abeds = request.POST['abeds']
        passw = request.POST['pass']
        if request.method == 'POST':
            print('2')
            obj = reg.objects.get(Q(hospital_mail=hospital_mail))
            if obj.Hopital_id == Hopital_id:
                obj.Hopital_t_beds = beds
                obj.Hopital_v_beds = abeds
                obj.Hospital_pass = passw
                obj.save()
                print(obj.Hopital_v_beds)
                obj = reg.objects.get(Q(hospital_mail=hospital_mail))
                data = patient_data.objects.filter(hospital_id=obj.Hopital_id)
                pend = data.filter(process='pending')
                appr = data.filter(process='approved')
                return render(request, 'hospital/Hospital_page.html', {'obj': obj, 'pend': pend, 'appr': appr})
        else:
            print('4')
            # return redirect('Hospital_login')
            return redirect('index')
    except:
        return redirect('index')

#

# update section-------------------------------------------------------------------------------------------------

def maps(request):
    return render(request,'hospital/maps.html')


def new(request):
    return render(request,'hospital/newindex.html')


def User_form(request):
    if request.method=='POST':
        hospital_name = request.POST['hospital_name']
        obj=reg.objects.get(Q(hospital_name=hospital_name))
        return render(request, 'hospital/User_form.html', {'obj': obj})
    else:
        return render(request, 'hospital/maps.html')

def emergency(request):
    try:
        if request.method=='POST':
            p_hospital = request.POST['hname']
            h_id = request.POST['hid']
            P_name = request.POST['pname']
            A_name = request.POST['aname']
            Mobile = request.POST['amobile']
            P_address = request.POST['address']

            print(P_name)
            print(p_hospital)
            print(h_id)
            print(Mobile)
            obj=patient_data(
                hospital_name = p_hospital,
                hospital_id = h_id,
                P_name = P_name,
                A_name = A_name,
                Mobile = Mobile,
                P_address = P_address
            )
            obj.save()
            return redirect('index')
    except:
        return redirect('maps')

#
# def updatehospital(request):
#     Hopital_id = request.POST['hid']
#     hmail = request.POST['hmail']
#     obj = reg.objects.get(Q(hospital_mail=hmail))
#     # print(Hopital_id)
#     # print(hmail)
#     obj.Hopital_v_beds
#     return HttpResponse("hello")


def approve(request):
     try:
        pname = request.POST['approve']
        print(pname)
        if request.method=='POST':
            data = patient_data.objects.get(Q(P_name = pname))
            print(data.hospital_id)
            data.process='approved'
            data.save()

            obj = reg.objects.get(Q(hospital_id=data.hospital_id))
            data = patient_data.objects.filter(hospital_id=obj.Hopital_id)
            pend = data.filter(process='pending')
            appr = data.filter(process='approved')
            return render(request, 'hospital/Hospital_page.html', {'obj': obj, 'pend': pend, 'appr': appr})

        else:
            # print('4')
            # return redirect('Hospital_login')
            return redirect('index')

     except:
        # print('6')
        # return redirect('Hospital_login')
        return redirect('index')







