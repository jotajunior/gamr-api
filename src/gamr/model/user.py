from gamr.scraper import bfhl, wow, riot
from gamr.exception.invalid_game_exception import InvalidGameException

class User:
    games = ['bfhl',
            'wow',
            'bf4',
            'lol',
            ]

    def exists_wow(self, name, world, region):
        if not name or not world or not region:
            return None
        wow_obj = wow.Wow(region)
        return wow_obj.user_exists(name, world)

    def exists_bfhl(self, name, platform):
        if not name or not platform:
            return None
        bfhl_obj = bfhl.BFHL()
        return bfhl_obj.user_exists(name, platform)

    def exists_bf4(self, name, platform):
        if not name or not platform:
            return None
        bf4_obj = bfhl.BF4(platform)
        return bf4_obj.user_exists(name)

    def exists_lol(self, name, region):
        if not name or not region:
            return None
        lol_obj = riot.Riot(region)
        return lol_obj.user_exists_by_name(name)

    def exists(self, game, **kwargs):
        if game not in self.games:
            raise InvalidGameException('Game {} does not exist'.format(game))

        if game == 'wow':
            return self.exists_wow(kwargs['name'],
                                   kwargs['world'],
                                   )
        elif game == 'bfhl':
            return self.exists_bfhl(kwargs['name'],
                                    kwargs['platform'],
                                    )
        elif game == 'bf4':
            return self.exists_bf4(kwargs['name'],
                                   kwargs['platform'],
                                   )
        elif game == 'lol':
            return self.exists_lol(kwargs['name'],
                                   kwargs['region'],
                                   )
    def exists_all(self, wow_name, wow_world, wow_region,
                   bfhl_name, bfhl_platform,
                   bf4_name, bf4_platform,
                   lol_name, lol_region,
                   ):
        result = {}
        result['wow'] = self.exists_wow(wow_name, wow_world, wow_region)
        result['bfhl'] = self.exists_bfhl(bfhl_name, bfhl_platform)
        result['bf4'] = self.exists_bf4(bf4_name, bf4_platform)
        result['lol'] = self.exists_lol(lol_name, lol_region)

        return result

    def is_registered_all(self, wow_name, wow_world, wow_region,
                          bfhl_name, bfhl_platform,
                          bf4_name, bf4_platform,
                          lol_name, lol_region,
                          ):
        result = {}
        result['wow'] = True
        result['bfhl'] = True
        result['bf4'] = True
        result['lol'] = True

        return result

    def get_status_all(self, wow_name, wow_world, wow_region,
                       bfhl_name, bfhl_platform,
                       bf4_name, bf4_platform,
                       lol_name, lol_region,
                       ):

        result_exists = self.exists_all(wow_name,
                                        wow_world,
                                        wow_region,
                                        bfhl_name,
                                        bfhl_platform,
                                        bf4_name,
                                        bf4_platform,
                                        lol_name,
                                        lol_region,
                                        )

        result_registered = self.is_registered_all(wow_name,
                                                   wow_world,
                                                   wow_region,
                                                   bfhl_name,
                                                   bfhl_platform,
                                                   bf4_name,
                                                   bf4_platform,
                                                   lol_name,
                                                   lol_region,
                                                   )
        result = {}

        names = {}
        names['wow'] = wow_name
        names['bfhl'] = bfhl_name
        names['bf4'] = bf4_name
        names['lol'] = lol_name

        for game in self.games:
            if game not in result:
                result[game] = {}
            result[game]['status'] = 'invalid'
            if result_exists.get(game, False):
                result[game]['status'] = 'good'
            if result_registered.get(game, False):
                result[game]['status'] = 'taken'
            result[game]['name'] = names[game]
        
        return result


    def save_personal_info(self, birth_year, birth_month,
                           country, english_level, gender):
        return True

if __name__ == '__main__':
    a = User()
    print(a.get_status_all('quelthalas', 'amanthul', 'us',
                            'xtreme', 'pc',
                            'xdfjkghdgf', 'pc',
                            'quelthalas', 'na'))
