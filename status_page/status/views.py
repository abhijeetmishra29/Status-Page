from django.shortcuts import render
from .models import ServiceStatus
from status.models import ServiceStatus  # Import your model
from django.db.models import Count
from django.db.models.functions import TruncDate
from django.db.models import Q # Import Q

def status_page(request):
    services = ServiceStatus.objects.select_related("service").all()
    
    # Debugging print statement
    print("Retrieved Services:", services)

    return render(request, "status/status_page.html", {"services": services})

def system_status(request):
    services = ServiceStatus.objects.all()  # Fetch all system statuses
    return render(request, "status/system_status.html", {"services": services})


def uptime_report(request):
    # Calculate daily uptime/downtime
    daily_stats = ServiceStatus.objects.annotate(date=TruncDate('updated_at')).values('date', 'service__name').annotate(
        operational_count=Count('id', filter=Q(status='operational')), # Use Q for filtering
        downtime_count=Count('id', filter=Q(status='down')) # Use Q for filtering
    ).order_by('date', 'service__name')

    report_data = {}
    for item in daily_stats:
        if item['date'] not in report_data:
            report_data[item['date']] = {}
        report_data[item['date']][item['service__name']] = {
            'operational': item['operational_count'],
            'downtime': item['downtime_count'],
        }

    return render(request, 'status/uptime_report.html', {'report_data': report_data})
