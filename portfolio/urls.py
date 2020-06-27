
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static  # sirve para el manejo de imagenes
import jobs.views   #importa las views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',jobs.views.home, name='home'),
    path('blog/', include('blog.urls')),#ir a la app 'blogs',dentro ir al archivo 'views', y dentro del archivo a la funcion 'home'
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
