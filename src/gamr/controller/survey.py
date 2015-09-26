from gamr import model
from gamr import view

class Survey:
    def __init__(self):
        self.model = model.Survey()

    def submit(self, surveys):
        self.model.init_responses(surveys)
        result = self.model.save()
        return view.Survey.show_submit(result)
