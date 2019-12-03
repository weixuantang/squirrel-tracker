from django.core.management.base import BaseCommand, CommandError
from tracker.models import Squirrel
import datetime

class Command(BaseCommand):
    help = 'Import squirrel data from specified path'

    def add_arguments(self, parser):
        parser.add_argument('path', nargs='+', type=str)
        
    
    def handle(self, *args, **options):
        import csv
        path = options['path'][0]
        f = open(path)
        lines = csv.reader(f)
        next(lines)
        num = 0
        
        def str2bool(string):
            if string == 'true':
                return True
            elif string == 'false':
                return False
            else:
                return None

        for line in lines:
            squirrel, boolean = Squirrel.objects.get_or_create(
                    x = float(line[0]),
                    y = float(line[1]),
                    unique_squirrel_id = line[2],
                    hectare = line[3],
                    shift = line[4],
                    date = datetime.datetime.strptime(line[5],'%m%d%Y'),
                    hectare_squirrel_number = int(line[6]),
                    age = line[7],
                    primary_fur_color = line[8],
                    highlight_fur_color = line[9],
                    combination_of_primary_and = line[10],
                    color_notes = line[11],
                    location = line[12],
                    above_ground_sighter = line[13],
                    specific_location = line[14],
                    running = str2bool(line[15]),
                    chasing = str2bool(line[16]),
                    climbing = str2bool(line[17]),
                    eating = str2bool(line[18]),
                    foraging = str2bool(line[19]),
                    other_activities = line[20],
                    kuks = str2bool(line[21]),
                    quaas = str2bool(line[22]),
                    moans = str2bool(line[23]),
                    tail_flags = str2bool(line[24]),
                    tail_twitches = str2bool(line[25]),
                    approaches = str2bool(line[26]),
                    indifferent = str2bool(line[27]),
                    runs_from = str2bool(line[28]),
                    other_interactions = line[29]
            )
            if boolean:
                num += 1

        self.stdout.write(self.style.SUCCESS('Successfully import %d squirrel data.' % num))
