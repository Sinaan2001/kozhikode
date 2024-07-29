from django.shortcuts import render,redirect,HttpResponse
from city.models import tbl_hospital, tbl_restaurant, tbl_workshop, id_gen, tbl_event, login, tbl_menu, tbl_food, tbl_location
from city.models import tbl_petrolpump, tbl_taxistand, tbl_busstand, tbl_lodge, tbl_room, tbl_traveller, tbl_review
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail


# Create your views here.

def index(request):
    return render(request, "index.html")

def form(request):
    return render(request, "form.html")

def table(request):
    return render(request, "table.html")

def lodge_registration(request):
    return render(request, "lodge_registration.html")


def admin_menu(request):
    return render(request, "adminmenubar.html")

def adminhome(request):
    if 'uid' not in request.session:
        return render(request, "index.html")
    else:
        return render(request, "adminhome.html")



# Admin

def hospitaladd(request):

    if 'uid' not in request.session:
        return render(request, "index.html")
    else:
        data = id_gen.objects.get(id=1)
        s1 = data.Hospital_id
        s1 = int(s1)+1
        Hospital_id = "HOS_00"+str(s1)
        request.session['s'] = s1
        return render(request,"hospitaladd.html",{'hid':Hospital_id})

def hospitaladd_data(request):
    if request.method == 'POST':
        hospital = tbl_hospital()
        hospital.Hospital_id = request.POST.get('hospital_id')
        hospital.Name = request.POST.get('name')
        hospital.Location = request.POST.get('location')
        hospital.District = request.POST.get('district')
        hospital.Pincode = request.POST.get('pincode')
        hospital.Phone = request.POST.get('phone')
        hospital.Email = request.POST.get('email')
        hospital.Status = "Active"
        hospital.save()


        data = id_gen.objects.get(id=1)
        hid = request.session['s']
        data.Hospital_id = hid
        data.save()

    

        return redirect('/hospitaladd')
    else:
        return HttpResponse("Invalid")

def hospitalremove(request):

    if 'uid' not in request.session:
        return render(request, "index.html")
    else:
        data=tbl_hospital.objects.all()
        return render(request,'hospitalremove.html',{'data1':data})

def remove_hospitaldata(request,s1):
    data=tbl_hospital.objects.get(Hospital_id=s1)
    data.delete()
    return redirect('/hospitalremove')

#restaurant

def restaurantadd(request):

    if 'uid' not in request.session:
        return render(request, "index.html")
    else:
        data = id_gen.objects.get(id=1)
        s1 = data.Restaurant_id
        s1 = int(s1)+1
        Restaurant_id="RES_00"+str(s1)
        request.session['s'] =s1
        return render(request,'restaurantadd.html',{'rid':Restaurant_id})

def restaurantadd_data(request):
    if request.method == 'POST':

        restaurant=tbl_restaurant()
        restaurant.Restaurant_id=request.POST.get('restaurant_id')
        restaurant.Name=request.POST.get('name')

        Photo = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(Photo.name, Photo) 
        uploaded_file_url = fs.url(filename)
        restaurant.Photo = uploaded_file_url
        
        restaurant.Description=request.POST.get('description')
        restaurant.Phone=request.POST.get('phone')
        restaurant.Email=request.POST.get('email')
        restaurant.Website=request.POST.get('website')
        restaurant.Status = "Verified"
        restaurant.save()

        data= id_gen.objects.get(id=1)
        rid=request.session['s']
        data.Restaurant_id = rid
        data.save()

        data1 = login()
        data1.Username = request.POST.get('restaurant_id')
        data1.Password = request.POST.get('phone')
        data1.Category = "Restaurant"
        data1.save()

        #send an mail
        #send_mail('jjjjjjjj', 'username:'+data1.Username, 'Password:'+data1.Password, '',[])




        return redirect('/restaurantadd') 
    else:
        return HttpResponse("Invalid")

def restaurantremove(request):
    if 'uid' not in request.session:
        return render(request, "index.html")
    else:
        data=tbl_restaurant.objects.all()
        return render(request,'restaurantremove.html',{'data1':data})

def restaurantremove_data(request,s2):
    data=tbl_restaurant.objects.get(Restaurant_id=s2)
    data.delete()

    data2 = login.objects.get(Username=s2)
    data2.delete()
    return redirect('/restaurantremove')

# workshop

def workshopadd(request):

    if 'uid' not in request.session:
        return render(request, "index.html")
    else:
        data=id_gen.objects.get(id=1)
        s1 = data.Workshop_id
        s1 = int(s1+1)
        Workshop_id="WORK_00"+str(s1)
        request.session['s'] =s1
        return render (request,'workshopadd.html',{'wid':Workshop_id})

def workshopadd_data(request):
    if request.method == 'POST':
        workshop=tbl_workshop()
        workshop.Workshop_id=request.POST.get('workshop_id')
        workshop.Name=request.POST.get('name')
        workshop.Category=request.POST.get('category')
        workshop.Description=request.POST.get('description')
        workshop.Phone=request.POST.get('phone')
        workshop.Email=request.POST.get('email')
        workshop.Status="Active"
        workshop.save()

        data= id_gen.objects.get(id=1)
        wid=request.session['s']
        data.Workshop_id = wid
        data.save()

        return redirect('/workshopadd')
    else:
        return HttpResponse("Invalid")

def workshopremove(request):

    if 'uid' not in request.session:
        return render(request, "index.html")
    else:
        data=tbl_workshop.objects.all()
        return render(request,'workshopremove.html',{'data1':data})

def workshopremove_data(request,s2):
    data=tbl_workshop.objects.get(Workshop_id=s2)
    data.delete()
    return redirect('/workshopremove')

# event

def add_event(request):

    if 'uid' not in request.session:
        return render(request, "index.html")
    else:
        data = id_gen.objects.get(id = 1)
        s1 = data.Event_id
        s1 = int(s1)+1
        Event_id = "EVT_00"+ str(s1)
        request.session['s'] = s1
        return render(request, "add_event.html", {'evid':Event_id})

def add_eventdata(request):
    if request.method == 'POST':
        Event = tbl_event()
        Event.Event_id = request.POST.get('eventid')
        Event.Name = request.POST.get('name')
        Event.Description = request.POST.get('description')

        Photo = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(Photo.name, Photo) 
        uploaded_file_url = fs.url(filename)
        Event.Photo = uploaded_file_url

        Event.Date = request.POST.get('date')
        Event.Status = "Active"  
        Event.save()

        data = id_gen.objects.get(id = 1)
        evid = request.session['s']
        data.Event_id = evid
        data.save()

        return redirect('/add_event')
    else:
        return HttpResponse("Invalid") 

def remove_event(request):

    if 'uid' not in request.session:
        return render(request, "index.html")
    else:
        data = tbl_event.objects.all()
        return render(request, "remove_eventtable.html" , {'data':data}) 
def events(request):
    data = tbl_event.objects.all()
    return render(request, "events.html" , {'data':data})         

def remove_eventdata(request,s1):
    data = tbl_event.objects.get(Event_id = s1)
    data.delete()
    return redirect('/remove_event') 
def update_eventdata(request,s1):
    data = tbl_event.objects.get(Event_id = s1)
    return render(request,"updatedata.html",{'data':data})
def updateevent1(request,s1):
    if request.method == 'POST':
        data=tbl_event.objects.get(Event_id=s1)
        
        data.Name = request.POST.get('name')
        data.Description = request.POST.get('description')

        

        data.Date = request.POST.get('date')
        data.save()
        return redirect('/remove_event')
    else:
        return HttpResponse("Invalid")     
#restaurant registration in public

def restaurant_registration(request):

    data = id_gen.objects.get(id=1)
    s1 = data.Restaurant_id
    s1 = int(s1)+1
    Restaurant_id="RES_00"+str(s1)
    request.session['s'] =s1

    return render(request, "restaurant_registration.html", {'rid':Restaurant_id})

def restaurant_registrationdata(request):
        if request.method == 'POST':

            restaurant = tbl_restaurant()
            restaurant.Restaurant_id=request.POST.get('restaurant_id')
            restaurant.Name=request.POST.get('name')

            Photo = request.FILES['photo']
            fs = FileSystemStorage()
            filename = fs.save(Photo.name, Photo) 
            uploaded_file_url = fs.url(filename)
            restaurant.Photo = uploaded_file_url
            
            restaurant.Description=request.POST.get('description')
            restaurant.Phone=request.POST.get('phone')
            restaurant.Email=request.POST.get('email')
            restaurant.Website=request.POST.get('website')
            restaurant.Status = "Not verified"
            restaurant.save()

            data= id_gen.objects.get(id=1)
            rid=request.session['s']
            data.Restaurant_id = rid
            data.save()

            return redirect('/restaurant_registration') 
        else:
            return HttpResponse("Invalid")

def verify_restaurant(request):

    if 'uid' not in request.session:
        return render(request, "]index.html")
    else:
        data = tbl_restaurant.objects.all()
        return render(request, "verify_restauranttable.html", {'data':data})

def accept_restaurant(request,s2):
    data = tbl_restaurant.objects.get(Restaurant_id=s2)
    data.Status = "Verified"
    data.save()

    data1 = login()
    data1.Username = data.Restaurant_id
    data1.Password = data.Phone
    data1.Category = "Restaurant"
    data1.save()

    return redirect('/verify_restaurant')

def reject_restaurant(request,s2): 

    data = tbl_restaurant.objects.get(Restaurant_id=s2)
    data.Status = "Rejected"
    data.save()
    return redirect('/verify_restaurant')



def loginview(request):
    return render(request, "login1.html")

def loadlogin(request):
    if request.method =='POST':
        dataa = login.objects.all()
        un = request.POST.get('username')
        pwd = request.POST.get('password')

        flag = 0

        for x in dataa:
            if un == x.Username and pwd == x.Password:
                type = x.Category

                flag = 1

                if type == "admin":
                    request.session['uid'] = un
                    return redirect('/adminhome')
                elif type == "Restaurant":
                    request.session['rid'] = un
                    return redirect('/restauranthome')
                elif type == "Lodge":
                    request.session['lid'] = un
                    return redirect('/lodgehome')
                elif type == "Traveller":
                    request.session['tid'] = un
                    return redirect('/travelhome')
                else:
                    return HttpResponse("Invalid acct type")
        if flag==0:
            return HttpResponse("Invalid user")



def restauranthome(request):
    if 'rid' not in request.session:
        return render(request, "index.html")
    else:
        return render(request, "restauranthome.html")


#restaurant home

def edit_profile(request):
    if 'rid' not in request.session:
        return render(request, "index.html")
    else:
        data = tbl_restaurant.objects.get(Restaurant_id= request.session['rid'])
        return render(request, "edit_profile.html", {'data':data})

def edit_profiledata(request,s2):
    if request.method == 'POST':
            restaurant = tbl_restaurant.objects.get(Restaurant_id=s2)
            if 'photo' not in request.FILES:
                restaurant.Name=request.POST.get('name')            
                restaurant.Description=request.POST.get('description')
                restaurant.Phone=request.POST.get('phone')
                restaurant.Email=request.POST.get('email')
                restaurant.save()
            else:
                restaurant.Name=request.POST.get('name')            
                restaurant.Description=request.POST.get('description')
                restaurant.Phone=request.POST.get('phone')
                restaurant.Email=request.POST.get('email')
                Photo = request.FILES['photo']
                fs = FileSystemStorage()
                filename = fs.save(Photo.name, Photo) 
                uploaded_file_url = fs.url(filename)
                restaurant.Photo = uploaded_file_url

                restaurant.save()
            return redirect('/restauranthome')
    else:
        return HttpResponse("Invalid")

def add_menumanagement(request):

    if 'rid' not in request.session:
        return render(request, "index.html")
    else:

        data = id_gen.objects.get(id=1)
        s1 = data.Menu_id
        s1 = int(s1)+1
        Menu_id="MENU_00"+str(s1)
        request.session['s'] =s1

        data1 = tbl_restaurant.objects.get(Restaurant_id= request.session['rid'])
        return render(request, "add_menumanagement.html", {'mid':Menu_id,'data1':data1})

def add_menudata(request):
    if request.method == 'POST':
        Menu= tbl_menu()
        Menu.Menu_id=request.POST.get('menuid')
        Menu.Restaurant_id_id=request.POST.get('restaurantid')
        
        Menu.Menu_name=request.POST.get('name')
        Menu.Description=request.POST.get('description')

        Photo = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(Photo.name, Photo) 
        uploaded_file_url = fs.url(filename)
        Menu.Photo = uploaded_file_url

        Menu.Quantity=request.POST.get('quantity')
        Menu.Price =request.POST.get('price')
        Menu.Status = "Active"
        Menu.save()

        data= id_gen.objects.get(id=1)
        mid=request.session['s']
        data.Menu_id = mid
        data.save()

        return redirect('/add_menumanagement')
    else:
        return HttpResponse("Invalid")

def remove_menumanagement(request):

    if 'rid' not in request.session:
        return render(request, "index.html")
    else:
        data = tbl_menu.objects.all()
        return render(request, "remove_menumanagement_table.html", {'data':data})
def viewmenu(request,id):
    data = tbl_menu.objects.filter(Restaurant_id=id)
    return render(request, "viewmenu.html", {'data':data})
def remove_menudata(request,s2):

    data = tbl_menu.objects.get(Menu_id = s2)
    data.delete()
    return redirect('/remove_menumanagement')

def update_menumanagement(request):

    if 'rid' not in request.session:
        return render(request, "index.html")
    else:
        data = tbl_menu.objects.all()
        return render(request, "update_menumanagement_table.html", {'data':data})

def update_menu(request, s2):

    if 'rid' not in request.session:
        return render(request, "index.html")
    else:
        data = tbl_menu.objects.get(Menu_id= s2)
        return render(request, "update_menu.html", {'data':data})

def update_menudata(request, s2):

    if request.method == 'POST':
        Menu = tbl_menu.objects.get(Menu_id=s2)
        if 'photo' not in request.FILES:
            Menu.Quantity=request.POST.get('quantity')            
            Menu.Price=request.POST.get('price')
            Menu.save()
        else:
            Menu.Quantity=request.POST.get('quantity')            
            Menu.Price=request.POST.get('price')

            Photo = request.FILES['photo']
            fs = FileSystemStorage()
            filename = fs.save(Photo.name, Photo) 
            uploaded_file_url = fs.url(filename)
            Menu.Photo = uploaded_file_url

            Menu.save()

        return redirect('/update_menumanagement')
    else:
        return HttpResponse("Invalid")

#restaurant logout

def restaurant_logout(request):
    del request.session['rid']
    return render(request, "index.html")


#Admin

def addfood_management(request):
    if 'uid' not in request.session:
        return render(request, "index.html")
    else:

        data = id_gen.objects.get(id = 1)
        s1 = data.Food_id
        s1 = int(s1)+1
        Food_id = "FD_00" + str(s1)
        request.session['s'] = s1 
        

        data1 = tbl_restaurant.objects.all()
        return render(request, "addfood_management.html", {'data1':data1, 'fid':Food_id})

def addfood_managementdata(request):

    if request.method == "POST":
        foodmanagement = tbl_food()
        foodmanagement.Food_id = request.POST.get('foodid')
        foodmanagement.Restaurant_name = request.POST.get('restaurantname')
        foodmanagement.Speciality = request.POST.get('speciality')
        foodmanagement.Location = request.POST.get('location')
        foodmanagement.Status = "Verified"        

        Photo = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(Photo.name, Photo) 
        uploaded_file_url = fs.url(filename)
        foodmanagement.Photo = uploaded_file_url

        foodmanagement.save()

        data= id_gen.objects.get(id=1)
        fid=request.session['s']
        data.Food_id = fid
        data.save()

        return redirect('/addfood_management')
    else:
        return HttpResponse("Invalid")


def removefood_management(request):
    if 'uid' not in request.session:
        return render(request, "index.html")
    else:

        data = tbl_food.objects.filter(Status="Verified")
        return render(request, "removefood_management.html", {'data':data})

def removefood_managementdata(request, s2):
    data = tbl_food.objects.get(Food_id = s2)
    data.delete()
    return redirect('/removefood_management')

def approvefood_management(request):

    if 'uid' not in request.session:
        return render(request, "index.html")
    else:
        data = tbl_food.objects.all()
        return render(request, "approve_foodmanagement.html", {'data':data})

def accept_foodmanagementdata(request,s2):
    data = tbl_food.objects.get(Food_id=s2)
    data.Status = "Verified"
    data.save()

    return redirect('/approvefood_management')

def reject_foodmanagementdata(request,s2):
    data = tbl_food.objects.get(Food_id=s2)
    data.Status = "Rejected"
    data.save()

    return redirect('/approvefood_management')


def addlocation(request):

    if 'uid' not in request.session:
        return render(request, "index.html")
    else:
        data = id_gen.objects.get(id = 1)
        s1 = data.Location_id
        s1 = int(s1)+1
        Location_id = "LCN_00" + str(s1)
        request.session['s'] = s1 
        
        return render(request, "addlocation.html", {'lid':Location_id})



def addlocation_data(request):

    if request.method == "POST":
        Location = tbl_location()
        Location.Location_id = request.POST.get('locationid')
        Location.Location_name = request.POST.get('locationname')
        Location.Speciality = request.POST.get('speciality')
        Location.Transportation = request.POST.get('transportation')
        Location.Route = request.POST.get('route')
        Location.Time_taken = request.POST.get('timetaken')

        Photo = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(Photo.name, Photo) 
        uploaded_file_url = fs.url(filename)
        Location.Photo = uploaded_file_url

        Location.save()

        data= id_gen.objects.get(id=1)
        lid=request.session['s']
        data.Location_id = lid
        data.save()

        return redirect('/addlocation')
    else:
        return HttpResponse("Invalid")

def removelocation(request):

    if 'uid' not in request.session:
        return render(request, "index.html")
    else:
        data = tbl_location.objects.all()
        return render(request, "removelocation.html", {'data':data})

def removelocation_data(request, s2):
    data = tbl_location.objects.get(Location_id = s2)
    data.delete()
    return redirect('/removelocation')


def add_petrolpump(request):

    if 'uid' not in request.session:
        return render(request, "index.html")
    else:
        data = id_gen.objects.get(id = 1)
        s1 = data.Pump_id
        s1 = int(s1)+1
        Pump_id = "PUMP_00" +str(s1)
        request.session['s'] = s1

        return render(request, "add_petrolpump.html", {'pid':Pump_id})

def add_petrolpumpdata(request):
    if request.method == 'POST':
        Petrolpump = tbl_petrolpump()
        Petrolpump.Pump_id = request.POST.get('pumpid')
        Petrolpump.Pump_name = request.POST.get('pumpname')
        Petrolpump.Location = request.POST.get('location')
        Petrolpump.Phone = request.POST.get('phone')
        Petrolpump.Details = request.POST.get('details')
        Petrolpump.save()

        data = id_gen.objects.get(id=1)
        pid = request.session['s']
        data.Pump_id = pid
        data.save()

        return redirect('/add_petrolpump')

    else:
        return HttpResponse("Invalid")

def add_taxistand(request):

    if 'uid' not in request.session:
        return render(request, "index.html")
    else:

        data = id_gen.objects.get(id =1)
        s1 = data.Taxistand_id
        s1 = int(s1)+1
        Taxistand_id = "TS_00"+ str(s1)
        request.session['s'] = s1

        return render(request, "add_taxistand.html", {'tsid':Taxistand_id})

def add_taxistanddata(request):
    if request.method == 'POST':
        Taxistand = tbl_taxistand()
        Taxistand.Taxistand_id = request.POST.get('taxistandid')
        Taxistand.Name = request.POST.get('taxistandname')
        Taxistand.Location = request.POST.get('location')
        Taxistand.save()

        data = id_gen.objects.get(id=1)
        tsid = request.session['s']
        data.Taxistand_id = tsid
        data.save()

        return redirect('/add_taxistand')

    else:
        return HttpResponse("Invalid")

def add_busstand(request):

    if 'uid' not in request.session:
        return render(request, "index.html")
    else:
        data = id_gen.objects.get(id=1)
        s1 = data.Busstand_id
        s1 = int(s1)+1
        Busstand_id = "BS_00"+ str(s1)
        request.session['s']= s1

        return render(request, "add_busstand.html", {'bsid':Busstand_id})

def add_busstanddata(request):
    if request.method == 'POST':
        Busstand = tbl_busstand()
        Busstand.Busstand_id = request.POST.get('busstandid')
        Busstand.Name = request.POST.get('busstandname')
        Busstand.Location = request.POST.get('location')
        Busstand.Category = request.POST.get('category')
        Busstand.save()

        data = id_gen.objects.get(id=1)
        bsid = request.session['s']
        data.Busstand_id = bsid
        data.save()

        return redirect('/add_busstand')

    else:
        return HttpResponse("Invalid")


def addlodge(request):

    if 'uid' not in request.session:
        return render(request, "index.html")
    else:
        data = id_gen.objects.get(id=1)
        s1 = data.Lodge_id
        s1 = int(s1)+1
        Lodge_id = "LOG_00"+str(s1)
        request.session['s']= s1

        return render(request, "add_lodge.html", {'lgid':Lodge_id})

def add_lodgedata(request):
    if request.method =='POST':
        Lodge =tbl_lodge()
        Lodge.Lodge_id = request.POST.get('lodgeid')
        Lodge.Name = request.POST.get('name')
        Lodge.Location = request.POST.get('location')
        Lodge.Description = request.POST.get('description')
        Lodge.Phone= request.POST.get('phone')
        Lodge.Email = request.POST.get('email')
        Lodge.Status = "Active"


        Photo = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(Photo.name, Photo) 
        uploaded_file_url = fs.url(filename)
        Lodge.Photo = uploaded_file_url

        Lodge.save()

        data = id_gen.objects.get(id=1)
        lgid = request.session['s']
        data.Lodge_id = lgid
        data.save()

        data1 = login()
        data1.Username = request.POST.get('lodgeid')
        data1.Password = request.POST.get('phone')
        data1.Category = "Lodge"
        data1.save()

        return redirect('/addlodge')

    else:
        return HttpResponse("Invalid")

def removelodge(request):

    if 'uid' not in request.session:
        return render(request, "index.html")
    else:
        data = tbl_lodge.objects.all()
        return render(request, "removelodge.html", {'data':data})

def remove_lodgedata(request,s2):
    data = tbl_lodge.objects.get(Lodge_id=s2)
    data.delete()

    data2 = login.objects.get(Username=s2)
    data2.delete()
    return redirect('/removelodge')

def admin_logout(request):
    del request.session['uid']
    return render(request, "index.html")

# Lodge

def lodgehome(request):
    if 'lid' not in request.session:
        return render(request, "index.html")
    else:
        return render(request, "lodgehome.html")

def editprofile_lodge(request):
    if 'lid' not in request.session:
        return render(request, "index.html")
    else:
        data = tbl_lodge.objects.get(Lodge_id = request.session['lid'])
        return render(request, "editprofile_lodge.html", {'data':data})


def editprofile_lodgedata(request, s2):

    if request.method == 'POST':
        Lodge = tbl_lodge.objects.get(Lodge_id=s2)
        if 'photo' not in request.FILES:
            Lodge.Name = request.POST.get('name')
            Lodge.Location = request.POST.get('location')
            Lodge.Description = request.POST.get('description')
            Lodge.Phone = request.POST.get('phone')
            Lodge.Email = request.POST.get('email')
            Lodge.save()
        else:
            Lodge.Name = request.POST.get('name')
            Lodge.Location = request.POST.get('location')
            Lodge.Description = request.POST.get('description')
            Lodge.Phone = request.POST.get('phone')
            Lodge.Email = request.POST.get('email')
            Photo = request.FILES['photo']
            fs = FileSystemStorage()
            filename = fs.save(Photo.name, Photo)
            uploaded_file_url = fs.url(filename)
            Lodge.Photo = uploaded_file_url
            Lodge.save()

        return redirect('/lodgehome')
    else:
        return HttpResponse("Invalid")

def addroom(request):

    if 'lid' not in request.session:
        return render(request, "index.html")
    else:
        data = id_gen.objects.get(id =1)
        s1 = data.Room_id
        s1 = int(s1)+1
        Room_id = "RM_00"+str(s1)
        request.session['s'] = s1

        data1 = tbl_lodge.objects.get(Lodge_id = request.session['lid'])
        return render(request, "addroom.html", {'rmid':Room_id, 'data1':data1})

def addroom_data(request):
    if request.method == 'POST':
        Room = tbl_room()
        Room.Room_id = request.POST.get('roomid')
        Room.Lodge_id_id = request.POST.get('lodgeid')
        Room.Room_type = request.POST.get('roomtype')
        Room.Rate = request.POST.get('rate')
        Room.Status = "Active"
        Room.save()

        data = id_gen.objects.get(id=1)
        rmid = request.session['s']
        data.Room_id = rmid
        data.save()
        return redirect('/addroom')

    else:
        return HttpResponse("Invalid")

def removeroom(request):

    if 'lid' not in request.session:
        return render(request, "index.html")
    else:
        data = tbl_room.objects.filter(Lodge_id = request.session['lid'])
        return render(request, "removeroom.html",{'data':data})

def remove_roomdata(request,s2):
    data = tbl_room.objects.get(Room_id=s2)
    data.delete()
    return redirect('/removeroom')

def updateroom(request):

    if 'lid' not in request.session:
        return render(request, "index.html")
    else:
        data = tbl_room.objects.filter(Lodge_id = request.session['lid'])
        return render(request, "updateroom_table.html", {'data':data})

def update_room(request,s2):

    if 'lid' not in request.session:
        return render(request, "index.html")
    else:
        data = tbl_room.objects.get(Room_id=s2)
        return render(request, "update_room.html", {'data':data})

def update_roomdata(request,s2):
    if request.method == 'POST':
        Room = tbl_room.objects.get(Room_id=s2)
        Room.Room_type = request.POST.get('roomtype')
        Room.Rate = request.POST.get('rate')
        Room.save()
        return redirect('/updateroom')
    else:
        return HttpResponse("Invalid")

# Lodge logout

def lodge_logout(request):
    del request.session['lid']
    return render(request, "index.html")


#public

def traveller_registration(request):

    data = id_gen.objects.get(id = 1)
    s1 = data.Traveller_id
    s1 = int(s1)+1
    Traveller_id = "TRL_00"+str(s1)
    request.session['s'] = s1

    return render(request, "traveller_registration.html", {'tvid':Traveller_id})

def traveller_registrationdata(request):
    if request.method == 'POST':
        Traveller = tbl_traveller()
        Traveller.Traveller_id = request.POST.get('travellerid')
        Traveller.Name = request.POST.get('name')
        Traveller.Address = request.POST.get('address')
        Traveller.Phone = request.POST.get('phone')
        Traveller.Email = request.POST.get('email')
        Traveller.save()

        data = id_gen.objects.get(id = 1)
        tvid = request.session['s']
        data.Traveller_id = tvid
        data.save()

        data1 = login()
        data1.Username = request.POST.get('travellerid')
        data1.Password = request.POST.get('phone')
        data1.Category = "Traveller"
        data1.save()

        return redirect('/traveller_registration')
    else:
        return HttpResponse("Invalid")

def view_hospital(request):
    data = tbl_hospital.objects.all()
    return render(request, "view_hospital.html", {'data':data})

def view_workshop(request):
    data = tbl_workshop.objects.all()
    return render(request, "view_workshop.html", {'data':data})

def upload_foodlocation(request):

    data = id_gen.objects.get(id = 1)
    s1 = data.Food_id
    s1 = int(s1)+1
    Food_id = "FD_00"+str(s1)
    request.session['s'] = s1

    data1 = tbl_restaurant.objects.all()
    return render(request, "upload_foodlocation.html", {"fid":Food_id,  'data1':data1})

def upload_foodlocationdata(request):
    if request.method == "POST":
        foodmanagement = tbl_food()
        foodmanagement.Food_id = request.POST.get('foodid')
        foodmanagement.Restaurant_name = request.POST.get('restaurantname')
        foodmanagement.Speciality = request.POST.get('speciality')
        foodmanagement.Location = request.POST.get('location')
        foodmanagement.Status = "Not verified"      

        Photo = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(Photo.name, Photo) 
        uploaded_file_url = fs.url(filename)
        foodmanagement.Photo = uploaded_file_url

        foodmanagement.save()

        data= id_gen.objects.get(id=1)
        fid=request.session['s']
        data.Food_id = fid
        data.save()

        return redirect('/upload_foodlocation')
    else:
        return HttpResponse("Invalid")

def view_restaurant(request):
    data = tbl_restaurant.objects.all()
    return render(request, "view_restaurant.html", {'data':data})

def view_location(request):
    data = tbl_location.objects.all()
    return render(request, "view_location.html", {'data':data})

def view_publicfoodlocation(request):
    data = tbl_food.objects.filter(Status="Verified")
    return render(request, "view_publicfood_location.html", {'data':data})

def view_petrolpump(request):
    data = tbl_petrolpump.objects.all()
    return render(request, "view_petrolpump.html", {'data':data})

def view_busstand(request):
    data = tbl_busstand.objects.all()
    return render(request, "view_busstand.html",{'data':data})

def view_taxistand(request):
    data = tbl_taxistand.objects.all()
    return render(request, "view_taxistand.html", {'data':data})

def view_lodge(request):
    data = tbl_lodge.objects.all()
    return render(request, "view_lodge.html", {'data':data})

#Travelhome


def travelhome(request):

    if 'tid' not in request.session:
        return render(request, "index.html")
    else:
        return render(request, "travelhome.html")

def insert_foodlocation(request):
    if 'tid' not in request.session:
        return render(request, "index.html")
    else:
        
        data = id_gen.objects.get(id=1)
        s1 = data.Food_id
        s1 = int(s1)+1
        Food_id = "FD_00"+str(s1)
        request.session['s']=s1

        data1 = tbl_restaurant.objects.all()
        return render(request, "insert_foodlocation.html",{'fid':Food_id, 'data1':data1})

def insert_foodlocationdata(request):

    if request.method == 'POST':
        Foodlocation = tbl_food()
        Foodlocation.Food_id = request.POST.get('foodid')
        Foodlocation.Restaurant_name = request.POST.get('restaurantname')       
        Foodlocation.Speciality = request.POST.get('speciality')
        Foodlocation.Location = request.POST.get('location')
        Foodlocation.Status= "Not verified"     

        Photo = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(Photo.name, Photo)
        uploaded_file_url = fs.url(filename)
        Foodlocation.Photo = uploaded_file_url
        Foodlocation.save()


        data = id_gen.objects.get(id=1)
        fid = request.session['s']
        data.Food_id=fid
        data.save()


        return redirect('/insert_foodlocation')

    else:
        return HttpResponse("Invalid")

def insert_location(request):

    if 'tid' not in request.session:
        return render(request, "index.html")
    else:

        data = id_gen.objects.get(id = 1)
        s1 = data.Location_id
        s1 = int(s1)+1
        Location_id = "LCN_00"+str(s1)
        request.session['s'] = s1
        return render(request, "insert_location.html" ,{'lid':Location_id})

def insert_locationdata(request):

    if request.method == 'POST':
        Location = tbl_location()
        Location.Location_id = request.POST.get('locationid')
        Location.Location_name = request.POST.get('locationname')        
        Location.Speciality = request.POST.get('speciality')
        Location.Transportation = request.POST.get('transportation')
        Location.Route = request.POST.get('route')
        Location.Time_taken = request.POST.get('timetaken')

        Photo = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(Photo.name, Photo)
        uploaded_file_url = fs.url(filename)
        Location.Photo = uploaded_file_url

        Location.save()

        data = id_gen.objects.get(id = 1)
        lid = request.session['s']
        data.Location_id = lid
        data.save()

        return redirect('/insert_location')

    else:
        return HttpResponse("Invalid")

def insert_workshop(request):

    if 'tid' not in request.session:
        return render(request, "index.html")
    else:

        data = id_gen.objects.get(id =1)
        s1 = data.Workshop_id
        s1 = int(s1)+1
        Workshop_id = "WORK_00"+str(s1)
        request.session['s'] = s1

        return render(request, "insert_workshop.html", {'wid':Workshop_id})

def insert_workshopdata(request):

    if request.method == 'POST':
        workshop=tbl_workshop()
        workshop.Workshop_id=request.POST.get('workshop_id')
        workshop.Name=request.POST.get('name')
        workshop.Category=request.POST.get('category')
        workshop.Description=request.POST.get('description')
        workshop.Phone=request.POST.get('phone')
        workshop.Email=request.POST.get('email')
        workshop.Status="Active"
        workshop.save()

        data= id_gen.objects.get(id=1)
        wid=request.session['s']
        data.Workshop_id = wid
        data.save()

        return redirect('/insert_workshop')
    else:
        return HttpResponse("Invalid")

def add_review(request):

    if 'tid' not in request.session:
        return render(request, "index.html")
    else:

        data = id_gen.objects.get(id =1)
        s1 = data.Review_id
        s1 = int(s1)+1
        Review_id = "REV_00"+str(s1)
        request.session['s'] = s1

        data1 = tbl_traveller.objects.get(Traveller_id=request.session['tid'])
        return render(request,"add_review.html", {'rvid':Review_id, 'data1':data1})

def add_reviewdata(request):

    if request.method == "POST":
        Review = tbl_review()
        Review.Review_id = request.POST.get('reviewid')
        Review.Traveller_id_id = request.POST.get('travellerid')
        Review.Review = request.POST.get('review')
        Review.Review_date = request.POST.get('reviewdate')

        Photo = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(Photo.name, Photo)
        uploaded_file_url = fs.url(filename)
        Review.Photo = uploaded_file_url

        Review.save()

        data = id_gen.objects.get(id =1)
        rvid = request.session['s']
        data.Review_id = rvid
        data.save()
        return redirect('/add_review')

    else:
        return HttpResponse("Invalid")

def traveller_logout(request):
    del request.session['tid']
    return render(request, "index.html")







