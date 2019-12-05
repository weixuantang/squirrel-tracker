from django.forms import ModelForm
from .models import Squirrel

class AddForm(ModelForm):
    class Meta:
        model = Squirrel
        fields = [
            'x',
            'y',
            'unique_squirrel_id',
            'shift',
            'date',
            'age',
            'primary_fur_color',
            'location',
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
            'runs_from'
        ]
        labels = {
            'x':'Longitude',
            'y':'Latitude'
        }

class SquirrelForm(ModelForm):
    class Meta:
        model = Squirrel
        fields = [
            'x',
            'y', 
            'unique_squirrel_id',
            'hectare',
            'shift',
            'date',
            'hectare_squirrel_number',
            'age',
            'primary_fur_color',
            'highlight_fur_color',
            'combination_of_primary_and',
            'color_notes',
            'location',
            'above_ground_sighter',
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
            'other_interactions'    
        ]
        labels = {
            'x':'Longitude',
            'y':'Latitude'
        }
