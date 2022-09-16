
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from home import views
from django.conf import settings
from django.conf.urls.static import static
import home
from django.conf.urls import handler404, handler500
from django.views.generic.base import TemplateView

admin.site.site_header = 'Sociio Ichor'
admin.site_site_title = 'Sociio Ichor'
admin.site.index_title = 'Sociio Ichor Administration'

urlpatterns = [
    path('editor/', include ('django_summernote.urls')),
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('team.urls')),
    path('', include('blog.urls')),
    path('', include('newsletter.urls')),

    path("robots.txt",TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),  #add the robots.txt file

    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
     
handler404 = home.views.error_404
handler500 = home.views.error_500