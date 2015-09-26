from gamr.exception.invalid_survey_type import InvalidSurveyTypeException
from gamr.exception.survey_not_initialized import SurveyNotInitializedException
import json

class Survey:
    survey_titles = ['identity',
                     'consent',
                     'brain type',
                     'personality',
                     'gamer type',
                     ]
    surveys = None
    
    def init_responses(self, surveys, force=False):
        if not self.surveys or force:
            self.surveys = json.loads(surveys)

    def save_identity(self, identity_responses):
        return True

    def save_consent(self, consent_responses):
        return True

    def save_brain_type(self, brain_type_responses):
        return True

    def save_personality(self, personality_responses):
        return True

    def save_gamer_type(self, gamer_type_responses):
        return True

    def save(self):
        if not self.surveys:
            raise SurveyNotInitializedException('You need to initialize the survey before calling save')
        for survey in self.surveys:
            survey_title = survey['title'].lower()
            if survey_title not in self.survey_titles:
                raise InvalidSurveyTypeException('Invalid survey title: {}'.format(survey_title))
            if survey_title == 'identity':
                self.save_identity(survey['form'])
            elif survey_title == 'consent':
                self.save_consent(survey['form'])
            elif survey_title == 'brain type':
                self.save_brain_type(survey['statements'])
            elif survey_title == 'personality':
                self.save_personality(survey['statements'])
            else:
                self.save_gamer_type(survey['statements'])

        return True
