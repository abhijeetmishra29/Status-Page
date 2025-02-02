from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class ServiceStatus(models.Model):
    STATUS_CHOICES = [
        ("Operational", "Operational"),
        ("Down", "Down"),
        ("Under Maintenance", "Under Maintenance"),
    ]

    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Operational")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.service.name} - {self.status}"


class ServiceStatusHistory(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    old_status = models.CharField(max_length=20, choices=ServiceStatus.STATUS_CHOICES)
    new_status = models.CharField(max_length=20, choices=ServiceStatus.STATUS_CHOICES)
    changed_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return f"{self.service.name}: {self.old_status} → {self.new_status} at {self.changed_at}"