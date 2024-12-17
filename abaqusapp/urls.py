from django.urls import path
from .views import PortfolioListView, PortfolioDetailView, PortfolioDataView, ExcelUploadView, index

urlpatterns = [
    path('', index, name='index'),
    path('portfolios/', PortfolioListView.as_view(), name='portfolio_list'),
    path('portfolios/<int:pk>/', PortfolioDetailView.as_view(), name='portfolio_detail'),
    path('api/portfolio-data/', PortfolioDataView.as_view(), name='portfolio_data'),
    path('upload/', ExcelUploadView.as_view(), name='excel_upload'),
]