from gamr import model
from gamr import view 

class User:
    def __init__(self):
        self.model = model.User()

    def get(self, wow_name, wow_world, wow_region,
            bfhl_name, bfhl_platform, bf4_name,
            bf4_platform, lol_name, lol_region,
            ):
        statuses = self.model.get_status_all(wow_name,
                                             wow_world,
                                             wow_region,
                                             bfhl_name,
                                             bfhl_platform,
                                             bf4_name,
                                             bf4_platform,
                                             lol_name,
                                             lol_region,
                                             )
        return view.User.format_get(statuses)
