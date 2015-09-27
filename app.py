import web
import sys
sys.path.append('/usr/local/mysql/lib') 
#import mySql
render = web.template.render('templates/')

db = web.database(dbn='mysql', user='username', pw='password', db='userAut')

urls = (
  '/', 'index',
  '/loginuser/(.*)/(.*)', 'login'
)

class index:
    def GET(self):
        auths = db.select('userAut');
        return render.index(auths);


class login:
    def GET(self, user, pw):
        print user
        print pw
        return


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
