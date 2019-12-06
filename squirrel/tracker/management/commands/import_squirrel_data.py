from django.core.management.base import BaseCommand, CommandError
from tracker.models import Squirrel
import datetime
import csv


class Command(BaseCommand):
    help = 'Import squirrel data from specified path'

    def add_arguments(self, parser):
        parser.add_argument('path')
        
    
    def handle(self, *args, **options):
        with open(options['path']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)

        def str2bool(string):
            if string in ['true','True','TRUE']:
                return True
            elif string in['false','False','TRUE']:
                return False
            else:
                return None
        
        num = 0
        for item in data:
            squirrel = Squirrel(
                longitude = float(item['x']),
                latitude = float(item['y']),
                unique_squirrel_id = item['unique_squirrel_id'],
#                hectare = item['hectare'],
                shift = item['shift'],
                date = datetime.datetime.strptime(item['date'],'%m%d%Y'),
#                hectare_squirrel_number = int(item['hectare_squirrel_number']),
                age = item['age'],
                primary_fur_color = item['primary_fur_color'],
#                highlight_fur_color = item['highlight_fur_color'],
#                combination_of_primary_and = item['combination_of_primary_and'],
#                color_notes = item['color_notes'],
                location = item['location'],
#                above_ground_sighter = item['above_ground_sighter'],
                specific_location = item['specific_location'],
                running = str2bool(item['running']),
                chasing = str2bool(item['chasing']),
                climbing = str2bool(item['climbing']),
                eating = str2bool(item['eating']),
                foraging = str2bool(item['foraging']),
                other_activities = item['other_activities'],
                kuks = str2bool(item['kuks']),
                quaas = str2bool(item['quaas']),
                moans = str2bool(item['moans']),
                tail_flags = str2bool(item['tail_flags']),
                tail_twitches = str2bool(item['tail_twitches']),
                approaches = str2bool(item['approaches']),
                indifferent = str2bool(item['indifferent']),
                runs_from = str2bool(item['runs_from']),
#                other_interactions = item['other_interactions']
            )
            squirrel.save()
            num += 1

        self.stdout.write(self.style.SUCCESS('Successfully imported %d squirrel data.' % num))
