"""kozhikode URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from city import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('form/', views.form),
    path('table/', views.table),
    path('admin_menu/', views.admin_menu),
    path('adminhome/', views.adminhome),
    path('restauranthome/', views.restauranthome),
    path('lodgehome/', views.lodgehome),
    path('travelhome/', views.travelhome),
    path('lodge_registration/', views.lodge_registration),



    #admin
    path('hospitaladd/',views.hospitaladd),
    path('hospitaladd_data/',views.hospitaladd_data),
    path('hospitalremove/',views.hospitalremove),
    path('remove_hospitaldata/<str:s1>',views.remove_hospitaldata),

    path('restaurantadd/',views.restaurantadd),
    path('restaurantadd_data/',views.restaurantadd_data),
    path('restaurantremove/',views.restaurantremove),
    path('restaurantremove_data/<str:s2>',views.restaurantremove_data),

    path('workshopadd/',views.workshopadd),
    path('workshopadd_data/',views.workshopadd_data),
    path('workshopremove/',views.workshopremove),
    path('workshopremove_data/<str:s2>',views.workshopremove_data),

    path('add_event/', views.add_event),
    path('add_eventdata/', views.add_eventdata),
    path('remove_event/', views.remove_event),
    path('remove_eventdata/<str:s1>', views.remove_eventdata),
    path('update_eventdata/<str:s1>', views.update_eventdata),
    path('updateevent1/<str:s1>', views.updateevent1),

    path('restaurant_registration/', views.restaurant_registration),
    path('restaurant_registrationdata/', views.restaurant_registrationdata),
    path('verify_restaurant/', views.verify_restaurant),
    path('accept_restaurant/<str:s2>', views.accept_restaurant),
    path('reject_restaurant/<str:s2>', views.reject_restaurant),

    path('login/', views.loginview),
    path('loadlogin/',views.loadlogin),
    path('viewmenu/<str:id>',views.viewmenu),
    path('events/',views.events),

    # restaurant
    path('edit_profile/', views.edit_profile),
    path('edit_profiledata/<str:s2>', views.edit_profiledata),
    path('add_menumanagement/', views.add_menumanagement),
    path('add_menudata/', views.add_menudata),
    path('remove_menumanagement/', views.remove_menumanagement),
    path('remove_menudata/<str:s2>', views.remove_menudata),
    path('update_menumanagement/', views.update_menumanagement),
    path('update_menu/<str:s2>', views.update_menu),
    path('update_menudata/<str:s2>', views.update_menudata),
    path('restaurant_logout/', views.restaurant_logout),

    #admin
    path('addfood_management/', views.addfood_management),
    path('addfood_managementdata/', views.addfood_managementdata),
    path('removefood_management/', views.removefood_management),
    path('removefood_managementdata/<str:s2>', views.removefood_managementdata),
    path('approvefood_management/', views.approvefood_management),
    path('accept_foodmanagementdata/<str:s2>', views.accept_foodmanagementdata),
    path('reject_foodmanagementdata/<str:s2>', views.reject_foodmanagementdata),

    path('addlocation/', views.addlocation),
    path('addlocation_data/', views.addlocation_data),
    path('removelocation/', views.removelocation),
    path('removelocation_data/<str:s2>', views.removelocation_data),

    path('add_petrolpump/', views.add_petrolpump),
    path('add_petrolpumpdata/', views.add_petrolpumpdata),

    path('add_taxistand/', views.add_taxistand),
    path('add_taxistanddata/', views.add_taxistanddata),

    path('add_busstand/', views.add_busstand),
    path('add_busstanddata/', views.add_busstanddata),

    path('addlodge/', views.addlodge),
    path('add_lodgedata/', views.add_lodgedata),  
    path('removelodge/', views.removelodge),
    path('remove_lodgedata/<str:s2>', views.remove_lodgedata), 
    path('admin_logout/', views.admin_logout),

    #lodgehome
    path('editprofile_lodge/', views.editprofile_lodge), 
    path('editprofile_lodgedata/<str:s2>', views.editprofile_lodgedata),

    path('addroom/', views.addroom),
    path('addroom_data/', views.addroom_data),
    path('removeroom/', views.removeroom),
    path('remove_roomdata/<str:s2>', views.remove_roomdata),
    path('updateroom/', views.updateroom),
    path('update_room/<str:s2>', views.update_room),
    path('update_roomdata/<str:s2>', views.update_roomdata),
    path('lodge_logout/', views.lodge_logout),

    #public
    path('traveller_registration/', views.traveller_registration),
    path('traveller_registrationdata/', views.traveller_registrationdata),
    path('view_hospital/', views.view_hospital),
    path('view_workshop/', views.view_workshop),
    path('upload_foodlocation/', views.upload_foodlocation),
    path('upload_foodlocationdata/', views.upload_foodlocationdata),

    path('view_restaurant/', views.view_restaurant),
    path('view_location/', views.view_location),
    path('view_publicfoodlocation/', views.view_publicfoodlocation),
    path('view_petrolpump/', views.view_petrolpump),
    path('view_busstand/', views.view_busstand),
    path('view_taxistand/', views.view_taxistand),
    path('view_lodge/', views.view_lodge),

    #travelhome
    path('insert_foodlocation/', views.insert_foodlocation),
    path('insert_foodlocationdata/', views.insert_foodlocationdata),

    path('insert_location/', views.insert_location),
    path('insert_locationdata/', views.insert_locationdata),

    path('insert_workshop/', views.insert_workshop),
    path('insert_workshopdata/', views.insert_workshopdata),
    path('add_review/', views.add_review),
    path('add_reviewdata/', views.add_reviewdata),
    path('traveller_logout/', views.traveller_logout),



]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
