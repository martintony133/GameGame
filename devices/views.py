from django.shortcuts import render, get_object_or_404
from .models import Device
from django.core.paginator import Paginator
from games.cart import Cart
# Create your views here.
def device(request):
        device_list = Device.objects.order_by('id')
        paginator = Paginator(device_list, 6)
        page_number = request.GET.get('page',1)
        devices_page = paginator.get_page(page_number)
        context = {
                'devices' : devices_page, 
                'cart' : Cart(request),
                }
        return render(request,'devices/home.html', context)

def product(request, product_id):
        single_device = get_object_or_404(Device, pk=product_id)
        previous_device = Device.objects.filter(id__lt=single_device.id).order_by('-id').first()
        next_device = Device.objects.filter(id__gt=single_device.id).order_by('id').first()
        device_list = Device.objects.exclude(id=product_id).order_by('?')[:4]
        context = {
                'item': single_device,
                'previous_device' : previous_device,
                'next_device' : next_device,
                'cart' : Cart(request), 
                'devices' : device_list
                }
        return render(request,'devices/product.html', context)