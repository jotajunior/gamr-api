from gamr.model.survey import Survey as SurveyModel
from gamr.view.survey import Survey as SurveyView

class Survey:
    def __init__(self):
        self.model = SurveyModel()

    def submit(self, surveys):
        self.model.init_responses(surveys)
        result = self.model.save()
        return SurveyView.show_submit(result)
