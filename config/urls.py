from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

urlpatterns = [
                  path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
                  path(
                      "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
                  ),
                  # Django Admin, use {% url 'admin:index' %}
                  path(settings.ADMIN_URL, admin.site.urls),
                  # User management
                  path("users/", include("itembase.users.urls", namespace="users")),
                  path("accounts/", include("allauth.urls")),
                  # Your stuff: custom urls includes go here
                  path("api/v1/", include('core.urls.api_urls')),
                  path("client/", include('core.urls.client_urls')),
                  # path("clist/", include('core.urls.checklist_urls')),
                  # path("csys/", include('core.urls.client_system_urls')),
                  path("contact/", include('core.urls.contact_urls')),
                  path("loc/", include('core.urls.location_urls')),
                  path("vendors/", include('core.urls.vendor_urls')),
                  path("items/", include('core.urls.vendor_item_urls')),
                  # path("proj/", include('core.urls.project_urls')),
                  path("staff/", include('core.urls.staffing_urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
