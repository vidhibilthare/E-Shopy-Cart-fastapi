from tortoise.models import Model
from tortoise import Tortoise,fields


class Userr(Model):
    id=fields.IntField(pk=True)
    name=fields.CharField(100)
    email=fields.CharField(100)
    phone=fields.CharField(10)
    password=fields.CharField(100)
    shopname=fields.CharField(50)
    gst=fields.IntField()
    is_active = fields.BooleanField(default=True)
    last_login = fields.DatetimeField(auto_now_add=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

class Category(Model):
    id=fields.IntField(pk=True)
    name=fields.CharField(200,unique=True)
    slug=fields.CharField(200)
    category_image=fields.TextField()
    description=fields.TextField()
    is_active = fields.BooleanField(default=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)


    
