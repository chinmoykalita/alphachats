from django.db import models

# Create your models here.
class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_name = models.CharField(max_length=30)
    room_link = models.URLField()
    ip_address = models.GenericIPAddressField(default="", protocol="both", unpack_ipv4=False)
    time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.room_name
        
class Chat(models.Model):
    chat_id = models.AutoField(primary_key=True)
    room_name = models.ForeignKey(Room, on_delete=models.CASCADE)
    message = models.TextField()
    person = models.CharField(max_length=30)
    ip_address = models.GenericIPAddressField(default="", protocol="both", unpack_ipv4=False)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        a = f'{self.room_name}-{self.message}'
        return a