# accessories/views.py
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Accessory

def accessory(request):
        """
        View to list all accessories with pagination.
        Prefetches 'colors' to optimize database hits.
        """
        # 1. Fetch all accessories, ordered by ID, and optimize with prefetch_related
        accessory_list = Accessory.objects.prefetch_related('colors').order_by('id')

        # 2. Paginate: Show 6 accessories per page
        paginator = Paginator(accessory_list, 6)
        page_number = request.GET.get('page', 1)
        accessories_page = paginator.get_page(page_number)

        context = {
        'accessories': accessories_page,
        }
        # Renders your accessories homepage template
        return render(request, 'Accessories/home.html', context)


def product(request, product_id):
        """
        View to display a single accessory and its available colors.
        """
        # 1. Fetch single accessory using the ID from URLs, or return 404 if not found
        single_accessory = get_object_or_404(
        Accessory.objects.prefetch_related('colors'), 
        pk=product_id
        )

        context = {
        'accessory': single_accessory,
        }
        # Renders your accessory detail page template
        return render(request, 'Accessories/single.html', context)
