from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('message.urls')),
    path('blog/', include('blog.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Login - Logout
    path('accounts/', include('accounts.urls')),  # SignUp
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
