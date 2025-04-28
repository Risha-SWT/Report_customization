# carbone_app/models.py
from django.db import models

class CarboneRender(models.Model):
    template_file = models.FileField(upload_to='templates/')
    json_file = models.FileField(upload_to='json/')
    pdf_file = models.FileField(upload_to='pdf/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Render {self.id} - {self.created_at}"