class Survey:
    @staticmethod
    def show_submit(result):
        return '{"status": "ok"}' if result else '{"status": "error"}'
