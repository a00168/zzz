import route

@route.route('/greeting/(.*)')
class greeting:
    def GET(self, greetings):
        return 'new greeting: ' + greetings
