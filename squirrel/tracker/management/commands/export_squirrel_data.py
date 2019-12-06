from django.core.management.base import BaseCommand, CommandError
from tracker.models import Squirrel
import datetime
import csv


class Command(BaseCommand):
    help = 'Import squirrel data from specified path'

    def add_arguments(self, parser):
        parser.add_argument('path')


    def handle(self, *args, **options):
        with open(options['path'],'w',) as fp:
            fieldnames = [
                'x',
                'y',
                'unique_squirrel_id',
#                'hectare',
                'shift',
                'date',
#                'hectare_squirrel_number',
                'age',
                'primary_fur_color',
#                'highlight_fur_color',
#                'combination_of_primary_and',
#                'color_notes',
                'location',
#                'above_ground_sighter',
                'specific_location',
                'running',
                'chasing',
                'climbing',
                'eating',
                'foraging',
                'other_activities',
                'kuks',
                'quaas',
                'moans',
                'tail_flags',
                'tail_twitches',
                'approaches',
                'indifferent',
                'runs_from',
#                'other_interactions'    
            ]
            writer = csv.DictWriter(fp, fieldnames=fieldnames)
            writer.writeheader()
            num = 0
            for squirrel in Squirrel.objects.all():
                writer.writerow({
                    'x': squirrel.longitude,
                    'y': squirrel.latitude,
                    'unique_squirrel_id': squirrel.unique_squirrel_id,
#                    'hectare': squirrel.hectare,
                    'shift': squirrel.shift,
                    'date': squirrel.date.strftime('%m%d%Y'),
#                    'hectare_squirrel_number': squirrel.hectare_squirrel_number,
                    'age': squirrel.age,
                    'primary_fur_color': squirrel.primary_fur_color,
#                    'highlight_fur_color': squirrel.highlight_fur_color,
#                    'combination_of_primary_and': squirrel.combination_of_primary_and,
#                    'color_notes': squirrel.color_notes,
                    'location': squirrel.location,
#                    'above_ground_sighter': squirrel.above_ground_sighter,
                    'specific_location': squirrel.specific_location,
                    'running': squirrel.running,
                    'chasing': squirrel.chasing,
                    'climbing': squirrel.climbing,
                    'eating': squirrel.eating,
                    'foraging': squirrel.foraging,
                    'other_activities': squirrel.other_activities,
                    'kuks': squirrel.kuks,
                    'quaas': squirrel.quaas,
                    'moans': squirrel.moans,
                    'tail_flags': squirrel.tail_flags,
                    'tail_twitches': squirrel.tail_twitches,
                    'approaches': squirrel.approaches,
                    'indifferent': squirrel.indifferent,
                    'runs_from': squirrel.runs_from,
#                    'other_interactions': squirrel.other_interactions = float(item['x']),
                })
                num += 1

        self.stdout.write(self.style.SUCCESS('Successfully exported %d squirrel data.' % num))

