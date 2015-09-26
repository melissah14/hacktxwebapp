import web 
render = web.template.render('templates/')

urls = (
  '/print/(.*)', 'index',
  '/loginuser/(.*)/(.*)', 'login'
)

class index:
    def GET(self, name):
        return render.index(name)


class login:
    def GET(self, user, pw):
        print user
        print pw
        return


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
