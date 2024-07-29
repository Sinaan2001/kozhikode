from django.db import models

# Create your models here.
class tbl_hospital(models.Model):
    Hospital_id = models.CharField(primary_key=True, max_length=30)
    Name = models.CharField(max_length=30)
    Location = models.CharField(max_length=90)
    District = models.CharField(max_length=90)
    Pincode = models.CharField(max_length=90)
    Phone = models.IntegerField()
    Email = models.CharField(max_length=90)
    Status = models.CharField(max_length=90)
    
    
    class Meta:
        db_table = "tbl_hospital"

class tbl_restaurant(models.Model):
    Restaurant_id = models.CharField(primary_key=True, max_length=30)
    Name = models.CharField(max_length=30)
    Photo = models.CharField(max_length=225) 
    Description = models.CharField(max_length=90)
    Phone = models.IntegerField()
    Email = models.CharField(max_length=90)
    Status = models.CharField(max_length=90)
    Website = models.CharField(max_length=100)
    
    
    class Meta:
        db_table = "tbl_restaurant"

class id_gen(models.Model):
    Hospital_id= models.IntegerField()
    Restaurant_id=models.IntegerField()
    Workshop_id=models.IntegerField()
    Event_id = models.IntegerField()
    Menu_id = models.IntegerField()
    Food_id = models.IntegerField()
    Location_id = models.IntegerField()
    Pump_id = models.IntegerField()
    Taxistand_id = models.IntegerField()
    Busstand_id = models.IntegerField()
    Lodge_id = models.IntegerField()
    Room_id = models.IntegerField()
    Traveller_id = models.IntegerField()
    Review_id = models.IntegerField()

    class Meta:
        db_table= "id_gen"

class tbl_workshop(models.Model):
    Workshop_id =models.CharField(primary_key=True, max_length=30)
    Name = models.CharField(max_length=30)
    Category = models.CharField(max_length=225) 
    Description = models.CharField(max_length=90)
    Phone = models.CharField(max_length=90)
    Email = models.CharField(max_length=90)
    Status = models.CharField(max_length=90)
    
    
    class Meta:
        db_table = "tbl_workshop"

class tbl_event(models.Model):
    Event_id = models.CharField(primary_key=True, max_length=30)
    Name = models.CharField(max_length=90)
    Description = models.CharField(max_length= 100)
    Photo = models.CharField(max_length = 90)
    Date = models.CharField(max_length = 50)
    Status = models.CharField(max_length=90)

    class Meta:
        db_table = "tbl_event"

class login(models.Model):
    Username = models.CharField(primary_key=True,max_length=90)
    Password = models.CharField(max_length=30)
    Category  = models.CharField(max_length=30)

    class Meta:
        db_table = "login"

class tbl_menu(models.Model):
    Menu_id = models.CharField(primary_key=True, max_length=30)
    Restaurant_id = models.ForeignKey(tbl_restaurant, on_delete = models.CASCADE)
    Menu_name = models.CharField(max_length=90)
    Description = models.CharField(max_length= 100)
    Photo = models.CharField(max_length = 90)
    Quantity = models.CharField(max_length = 50)
    Price = models.CharField(max_length = 50)
    Status = models.CharField(max_length=90)

    class Meta:
        db_table = "tbl_menu"

class tbl_food(models.Model):
    Food_id = models.CharField(primary_key=True, max_length=30)
    Restaurant_name = models.CharField(max_length= 100)
    Speciality = models.CharField(max_length= 100)
    Photo = models.CharField(max_length = 90)
    Location = models.CharField(max_length=90)
    Status = models.CharField(max_length=90)

    class Meta:
        db_table = "tbl_food"


class tbl_location(models.Model):
    Location_id = models.CharField(primary_key=True, max_length=30)
    Location_name = models.CharField(max_length=90)
    Photo = models.CharField(max_length = 90)
    Speciality = models.CharField(max_length=90)
    Transportation = models.CharField(max_length = 100)
    Route = models.CharField(max_length = 90)
    Time_taken = models.CharField(max_length=90)

    class Meta:
        db_table = "tbl_location"


class tbl_petrolpump(models.Model):
    Pump_id = models.CharField(primary_key=True, max_length=50)
    Pump_name = models.CharField(max_length=100)
    Location = models.CharField(max_length=90)
    Phone = models.CharField(max_length=50)
    Details = models.CharField(max_length= 100)

    class Meta:
        db_table = "tbl_petrolpump"

class tbl_taxistand(models.Model):
    Taxistand_id = models.CharField(primary_key = True, max_length = 50)
    Name = models.CharField(max_length=100)
    Location = models.CharField(max_length= 90)

    class Meta:
        db_table = "tbl_taxistand"

class tbl_busstand(models.Model):
    Busstand_id = models.CharField(primary_key = True, max_length = 50)
    Name = models.CharField(max_length=100)
    Location = models.CharField(max_length= 90)
    Category = models.CharField(max_length = 90)

    class Meta:
        db_table = "tbl_busstand"

class tbl_lodge(models.Model):
    Lodge_id = models.CharField(primary_key=True, max_length=50)
    Name = models.CharField(max_length=100)
    Photo = models.CharField(max_length=50)
    Location = models.CharField(max_length=50)
    Description = models.CharField(max_length=100)
    Phone = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Status= models.CharField(max_length=50)

    class Meta:
        db_table = "tbl_lodge"

class tbl_room(models.Model):
    Room_id = models.CharField(primary_key=True, max_length=50)
    Lodge_id = models.ForeignKey(tbl_lodge, on_delete=models.CASCADE)
    Room_type = models.CharField(max_length=50)
    Rate = models.CharField(max_length=50)
    Status = models.CharField(max_length=90)

    class Meta:
        db_table = "tbl_room"

class tbl_traveller(models.Model):
    Traveller_id = models.CharField(primary_key=True, max_length=50)
    Name = models.CharField(max_length=90)
    Address = models.CharField(max_length = 100)
    Phone = models.CharField(max_length = 30)
    Email = models.CharField(max_length=30)

    class Meta:
        db_table = "tbl_traveller"

class tbl_review(models.Model):
    Review_id = models.CharField(primary_key=True, max_length=50)
    Traveller_id = models.ForeignKey(tbl_traveller, on_delete=models.CASCADE)
    Review = models.CharField(max_length=90)
    Photo = models.CharField(max_length=80)
    Review_date = models.CharField(max_length=50)

    class Meta:
        db_table = "tbl_review"