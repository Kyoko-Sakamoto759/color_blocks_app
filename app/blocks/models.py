from django.db import models
import uuid

# Userモデルを定義
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'Users'
        verbose_name = 'ユーザー'
        verbose_name_plural = 'ユーザー'
    
    def __str__(self):
        return f"{self.username}"
    
# Boardsモデルを定義
class Board(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='boards')
    title = models.CharField(max_length=30)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'Boards'
        verbose_name = 'ボード'
        verbose_name_plural = 'ボード'
    
    def __str__(self):
        return f"{self.title}"

# Colorsモデルを定義
class Block_Color(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True) 
    
    class Meta:
        db_table = 'Colors'
        verbose_name = 'カラー'
        verbose_name_plural = 'カラー'
    
    def __str__(self):
        return f"{self.name} ({self.name})"
    
# Blocksモデルを定義
class Block(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='blocks')
    color = models.ForeignKey(Block_Color, on_delete=models.CASCADE, related_name='blocks_color')
    culumn = models.IntegerField()
    row = models.IntegerField()
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True) 
    
    class Meta:
        db_table = 'Blocks'
        verbose_name = 'ブロック'
        verbose_name_plural = 'ブロック'
    
    def __str__(self):
        return f"{self.color}-({self.culumn}, {self.row})"  
    
