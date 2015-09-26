from gamr.model.user import User as UserModel
from gamr.view.user import User as UserView 

class User:
    def __init__(self):
        self.model = UserModel()

    def get(self, wow_name, wow_world, wow_region,
            bfhl_name, bfhl_platform, bf4_name,
            bf4_platform, lol_name, lol_region,
            birth_year, birth_month, country,
            english_level, gender):
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
        self.model.save_personal_info(birth_year,
                                      birth_month,
                                      country,
                                      english_level,
                                      gender,
                                      )
        return UserView.format_get(statuses)
