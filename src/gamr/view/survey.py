class Survey:
    @staticmethod
    def show_submit(result):
        template = '{\'status\': \'{}\'}'
        return template.format('ok') if result else template.format('error')
