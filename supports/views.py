from django.shortcuts import render, redirect
from django.contrib import messages
from .models import SupportTicket

def support_create_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message_content = request.POST.get('message')
        
        # 📌 使用 getlist 獲取使用者上傳的所有照片列表
        # 請確保你 HTML <input type="file" name="photo" multiple> 的 name 是叫 'photo'
        photos = request.FILES.getlist('photo')
        
        # 先抓取第一張作為主要照片，若沒上傳則為 None
        photo_main = photos[0] if len(photos) > 0 else None
        
        # 依序抓取後續的照片 (1 到 6)
        photo_1 = photos[1] if len(photos) > 1 else None
        photo_2 = photos[2] if len(photos) > 2 else None
        photo_3 = photos[3] if len(photos) > 3 else None
        photo_4 = photos[4] if len(photos) > 4 else None
        photo_5 = photos[5] if len(photos) > 5 else None
        photo_6 = photos[6] if len(photos) > 6 else None
        
        # 建立資料並正確對應到模型的所有圖片欄位
        ticket = SupportTicket.objects.create(
            user=request.user if request.user.is_authenticated else None,
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message_content,
            photo_main=photo_main,
            photo_1=photo_1,
            photo_2=photo_2,
            photo_3=photo_3,
            photo_4=photo_4,
            photo_5=photo_5,
            photo_6=photo_6,
        )
        
        # 提示訊息並重導向
        messages.success(request, "Your issue has been successfully submitted. We will contact you as soon as possible!")
        return redirect('pages:index')
        
    return render(request, 'supports/support_create.html')
