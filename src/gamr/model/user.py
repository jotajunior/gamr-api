from gamr.scrapers import bfhl, wow, riot
from gamr.exception import InvalidGameException

class User:
    games = ['bfhl',
            'wow',
            'bf4',
            'lol',
            ]

    def exists_wow(self, name, world):
        wow_obj = wow.Wow()
        return wow_obj.user_exists(name, world)

    def exists_bfhl(self, name, platform):
        bfhl_obj = bfhl.BFHL()
        return bfhl_obj.user_exists(name, platform)

    def exists_bf4(self, name, platform):
        bf4_obj = bfhl.BF4(platform)
        return bf4_obj.user_exists(name)

    def exists_lol(self, name, region):
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
    def exists_all(self, wow_name, wow_world,
                   bfhl_name, bfhl_platform,
                   bf4_name, bf4_platform,
                   lol_name, lol_platform,
                   ):
        result = {}
        result['wow'] = self.exists_wow(wow_name, wow_world)
        result['bfhl'] = self.exists_bfhl(bfhl_name, bfhl_platform)
        result['bf4'] = self.exists_bf4(bf4_name, bf4_platform)
        result['lol'] = self.exists_lol(lol_name, lol_region)

        return result

    def is_registered_all(self, wow_name, wow_world,
                          bfhl_name, bfhl_platform,
                          bf4_name, bf4_platform,
                          lol_name, lol_platform,
                          ):
        result = {}
        result['wow'] = True
        result['bfhl'] = True
        result['bf4'] = True
        result['lol'] = True

        return result

