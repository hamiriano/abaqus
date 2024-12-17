# management/commands/load_portfolio_data.py
from django.core.management.base import BaseCommand
from ...utils import load_data_from_excel, calculate_initial_quantities

class Command(BaseCommand):
    help = 'Loads portfolio data from Excel and calculates initial quantities'

    def handle(self, *args, **options):
        load_data_from_excel()
        calculate_initial_quantities()
        self.stdout.write(self.style.SUCCESS('Portfolio data loaded and initial quantities calculated.'))