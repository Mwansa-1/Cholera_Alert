from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Listing
    #-----------
    path("submitted_results_view/", views.Submitted_ResultsList.as_view(), name="submitted_result-view"),
    path("device_results_view/", views.Device_ResultsList.as_view(), name="device_results-view"),
    path("blog_view/", views.BlogList.as_view(), name="blog-view"),
    path("provinces_view/", views.ProvincesList.as_view(), name="provinces-view"),
    path("previous_tests_view/", views.Previous_TestList.as_view(), name="previous_tests-view"),
    path("alert_view/", views.AlertList.as_view(), name="alert-view"),



    # Creating
    #-----------
    path("submitted_results/", views.Submitted_ResultsListCreate.as_view(), name="submitted_result-view-create"),
    path("device_results/", views.Device_ResultsListCreate.as_view(), name="device_results-view-create"),
    path("blog/", views.BlogListCreate.as_view(), name="blog-view-create"),
    path("provinces/", views.ProvincesListCreate.as_view(), name="provinces-view-create"),
    path("previous_tests/", views.Previous_TestListCreate.as_view(), name="previous_tests-view-create"),
    path("alert/", views.AlertListCreate.as_view(), name="alert-view-create"),

    # Updating or Deleting
    #-----------
    path("submitted_results/<int:pk>", views.Submitted_ResultsUpdateDestroy.as_view(), name="submitted_result-view-update"),
    path("device_results/<int:pk>", views.Device_ResultsUpdateDestroy.as_view(), name="device_results-view-update"),
    path("blog/<int:pk>", views.BlogUpdateDestroy.as_view(), name="blog-view-update"),
    path("provinces/<int:pk>", views.ProvincesUpdateDestroy.as_view(), name="provinces-view-update"),
    path("previous_tests/<int:pk>", views.Previous_TestUpdateDestroy.as_view(), name="previous_tests-view-update"),
    path("alert/<int:pk>", views.AlertUpdateDestroy.as_view(), name="alert-view-update"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)