from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import ServiceStatus, ServiceStatusHistory

@receiver(pre_save, sender=ServiceStatus)
def log_status_change(sender, instance, **kwargs):
    """
    Logs a status change in ServiceStatusHistory before saving.
    """
    if instance.pk:  # Check if the object already exists (not a new entry)
        previous_status = ServiceStatus.objects.get(pk=instance.pk)
        if previous_status.status != instance.status:
            # Only log if the status has actually changed
            ServiceStatusHistory.objects.create(
                service=instance.service,
                old_status=previous_status.status,
                new_status=instance.status
            )
