from recommendation.models import Industry, Sector
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Populate db with sectors and industries'

    def handle(self, *args, **options):
        INDUSTRY_CHOICES = (
            ('Communication Services', (
                ('Diversified Telecommunication Services', 'Diversified Telecommunication Services'),
                ('Entertainment','Entertainment'),
                ('Interactive Media & Services','Interactive Media & Services'),
                ('Media','Media'),
                ('Wireless Telecommunication Services','Wireless Telecommunication Services'))),
            ('Consumer Discretionary', (
                ('Auto Components', 'Auto Components'),
                ('Automobiles', 'Automobiles'),
                ('Distributors', 'Distributors'),
                ('Diversified Consumer Services', 'Diversified Consumer Services'),
                ('Hotels, Restaurants & Leisure', 'Hotels, Restaurants & Leisure'),
                ('Household Durables', 'Household Durables'),
                ('Internet & Direct Marketing Retail', 'Internet & Direct Marketing Retail'),
                ('Leisure Products', 'Leisure Products'),
                ('Multiline Retail', 'Multiline Retail'),
                ('Specialty Retail', 'Specialty Retail'),
                ('Textiles, Apparel & Luxury Goods', 'Textiles, Apparel & Luxury Goods'))),
            ('Consumer Staples', (
                ('Beverages', 'Beverages'),
                ('Food & Staples Retailing', 'Food & Staples Retailing'),
                ('Food Products', 'Food Products'),
                ('Household Products', 'Household Products'),
                ('Personal Products', 'Personal Products'),
                ('Tobacco', 'Tobacco'))),
            ('Energy',(
                ('Energy Equipment & Services', 'Energy Equipment & Services'),
                ('Oil, Gas & Consumable Fuels', 'Oil, Gas & Consumable Fuels'))),
            ('Financials',(
                ('Banks', 'Banks'),
                ('Capital Markets', 'Capital Markets'),
                ('Consumer Finance', 'Consumer Finance'),
                ('Diversified Financial Services', 'Diversified Financial Services'),
                ('Insurance', 'Insurance'))),
            ('Health Care',(
                ('Biotechnology', 'Biotechnology'),
                ('Health Care Equipment & Supplies', 'Health Care Equipment & Supplies'),
                ('Health Care Providers & Services', 'Health Care Providers & Services'),
                ('Health Care Technology', 'Health Care Technology'),
                ('Life Sciences Tools & Services', 'Life Sciences Tools & Services'),
                ('Pharmaceuticals', 'Pharmaceuticals'))),
            ('Industrials',(
                ('Aerospace & Defense', 'Aerospace & Defense'),
                ('Air Freight & Logistics', 'Air Freight & Logistics'),
                ('Airlines', 'Airlines'),
                ('Building Products', 'Building Products'),
                ('Commercial Services & Supplies', 'Commercial Services & Supplies'),
                ('Construction & Engineering', 'Construction & Engineering'),
                ('Electrical Equipment', 'Electrical Equipment'),
                ('Industrial Conglomerates', 'Industrial Conglomerates'),
                ('Machinery', 'Machinery'),
                ('Professional Services', 'Professional Services'),
                ('Road & Rail', 'Road & Rail'),
                ('Trading Companies & Distributors', 'Trading Companies & Distributors'))),
            ('Information Technology',(
                ('Communications Equipment', 'Communications Equipment'),
                ('Electronic Equipment, Instruments & Components', 'Electronic Equipment, Instruments & Components'),
                ('IT Services', 'IT Services'),
                ('Semiconductors & Semiconductor Equipment', 'Semiconductors & Semiconductor Equipment'),
                ('Software', 'Software'),
                ('Technology Hardware, Storage & Peripherals', 'Technology Hardware, Storage & Peripherals'))),
            ('Materials',(
                ('Chemicals', 'Chemicals'),
                ('Construction Materials', 'Construction Materials'),
                ('Containers & Packaging', 'Containers & Packaging'),
                ('Metals & Mining', 'Metals & Mining'))),
            ('Real Estate',(
                ('Equity Real Estate Investment Trusts (REITs)', 'Equity Real Estate Investment Trusts (REITs)'),
                ('Real Estate Management & Development', 'Real Estate Management & Development'))),
            ('Utilities',(
                ('Electric Utilities', 'Electric Utilities'),
                ('Gas Utilities', 'Gas Utilities'),
                ('Independent Power and Renewable Electricity Producers',
                'Independent Power and Renewable Electricity Producers'),
                ('Multi-Utilities', 'Multi-Utilities'),
                ('Water Utilities', 'Water Utilities')))
                )

        for (sector_name, industries) in INDUSTRY_CHOICES:
            sector, created = Sector.objects.get_or_create(name=sector_name)
            self.stdout.write(sector.name + ' created: ' + str(created))
            for industry_name in industries:
                industry, created = Industry.objects.get_or_create(name=industry_name[0], sector=sector)
                self.stdout.write(industry.name + ' created: ' + str(created))
