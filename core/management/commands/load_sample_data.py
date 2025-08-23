from django.core.management.base import BaseCommand
from core.models import Service, Project, Testimonial, CompanyInfo

class Command(BaseCommand):
    help = 'Load sample data for PrimeHomes Constructions'

    def handle(self, *args, **options):
        self.stdout.write('Loading sample data...')

        # Create Company Info if it doesn't exist
        if not CompanyInfo.objects.exists():
            CompanyInfo.objects.create(
                name="PrimeHomes Constructions",
                tagline="Building Your Dreams Into Reality",
                description="With over 15 years of experience in the construction industry, PrimeHomes Constructions has established itself as a trusted name in building excellence. We specialize in residential, commercial, and industrial construction projects.",
                address="123 Construction Ave, Building City, BC 12345",
                phone="(555) 123-4567",
                email="info@primehomes.com",
                facebook="https://facebook.com/primehomes",
                twitter="https://twitter.com/primehomes",
                linkedin="https://linkedin.com/company/primehomes",
                instagram="https://instagram.com/primehomes",
                projects_completed=500,
                years_experience=15,
                client_satisfaction=100
            )
            self.stdout.write(self.style.SUCCESS('Company info created'))

        # Create Services if they don't exist
        if not Service.objects.exists():
            services_data = [
                {
                    'title': 'Residential Construction',
                    'description': 'Custom home building and residential renovations with attention to detail and quality craftsmanship.',
                    'icon': 'fas fa-home',
                    'color': '#0d6efd'
                },
                {
                    'title': 'Commercial Construction',
                    'description': 'Office buildings, retail spaces, and commercial facilities built to meet your business needs.',
                    'icon': 'fas fa-building',
                    'color': '#198754'
                },
                {
                    'title': 'Industrial Construction',
                    'description': 'Warehouses, factories, and industrial facilities designed for efficiency and durability.',
                    'icon': 'fas fa-industry',
                    'color': '#fd7e14'
                },
                {
                    'title': 'Renovation & Remodeling',
                    'description': 'Transform your existing space with our renovation and remodeling services.',
                    'icon': 'fas fa-tools',
                    'color': '#6f42c1'
                },
                {
                    'title': 'Project Management',
                    'description': 'Comprehensive project management services to ensure your project stays on time and budget.',
                    'icon': 'fas fa-tasks',
                    'color': '#dc3545'
                },
                {
                    'title': 'Interior Design',
                    'description': 'Professional interior design services to create beautiful and functional spaces.',
                    'icon': 'fas fa-paint-brush',
                    'color': '#20c997'
                }
            ]

            for service_data in services_data:
                Service.objects.create(**service_data)
            
            self.stdout.write(self.style.SUCCESS('Services created'))

        # Create Projects if they don't exist
        if not Project.objects.exists():
            projects_data = [
                {
                    'title': 'Modern Office Complex',
                    'description': 'A state-of-the-art office complex featuring sustainable design and modern amenities.',
                    'category': 'Commercial',
                    'status': 'Completed'
                },
                {
                    'title': 'Luxury Residential Villa',
                    'description': 'Custom luxury villa with premium finishes and smart home technology.',
                    'category': 'Residential',
                    'status': 'Completed'
                },
                {
                    'title': 'Industrial Warehouse',
                    'description': 'Large-scale warehouse facility with advanced logistics infrastructure.',
                    'category': 'Industrial',
                    'status': 'In Progress'
                },
                {
                    'title': 'Shopping Center Renovation',
                    'description': 'Complete renovation of a shopping center with modern retail spaces.',
                    'category': 'Commercial',
                    'status': 'Completed'
                },
                {
                    'title': 'Eco-Friendly Home',
                    'description': 'Sustainable residential home with green building practices and renewable energy.',
                    'category': 'Residential',
                    'status': 'In Progress'
                },
                {
                    'title': 'Restaurant Interior Design',
                    'description': 'Complete interior design and renovation of a fine dining restaurant.',
                    'category': 'Interior Design',
                    'status': 'Completed'
                }
            ]

            for project_data in projects_data:
                Project.objects.create(**project_data)
            
            self.stdout.write(self.style.SUCCESS('Projects created'))

        # Create Testimonials if they don't exist
        if not Testimonial.objects.exists():
            testimonials_data = [
                {
                    'name': 'John Smith',
                    'rating': 5,
                    'comment': 'PrimeHomes Constructions exceeded our expectations. They delivered our dream home on time and within budget. Highly recommended!'
                },
                {
                    'name': 'Sarah Johnson',
                    'rating': 5,
                    'comment': 'Professional team, excellent workmanship, and outstanding customer service. Our office renovation was completed perfectly.'
                },
                {
                    'name': 'Mike Davis',
                    'rating': 5,
                    'comment': 'The best construction company we\'ve worked with. They transformed our warehouse into a modern facility that improved our operations significantly.'
                },
                {
                    'name': 'Emily Wilson',
                    'rating': 5,
                    'comment': 'Outstanding quality and attention to detail. Our restaurant renovation was completed beautifully and on schedule.'
                },
                {
                    'name': 'David Brown',
                    'rating': 5,
                    'comment': 'PrimeHomes delivered exceptional results for our commercial project. Their expertise and professionalism are unmatched.'
                }
            ]

            for testimonial_data in testimonials_data:
                Testimonial.objects.create(**testimonial_data)
            
            self.stdout.write(self.style.SUCCESS('Testimonials created'))

        self.stdout.write(self.style.SUCCESS('Sample data loaded successfully!')) 