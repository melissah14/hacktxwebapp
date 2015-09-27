<<<<<<< HEAD
import web
import sys
sys.path.append('/usr/local/mysql/lib') 
#import mySql
=======
import web 
from web import form
>>>>>>> 30cdfcda538a4bc0a1dc0f2c4759ed856dfa2699
render = web.template.render('templates/')

db = web.database(dbn='mysql', user='username', pw='password', db='userAut')

urls = (
  '/print/(.*)', 'index',
  '/loginuser/(.*)/(.*)', 'login',
  '/login/', 'login',
  '/registration/', 'registration'
)

myform = form.Form( 
    form.Textbox('Username', description="Username"),
    form.Password('Password', description="Password"),
)

newUser = form.Form(
    form.Textbox('First name: ', description="enter your first name"),
    form.Textbox('Last name: ', description="enter your last name"),
    form.Dropdown('personid',[('Tutor','tutor'),('Student','student')]),
    form.Password('Enter your password', description="enter a password")
)

class index:
    def GET(self):
        auths = db.select('userAut');
        return render.index(auths);


class login:
	def GET(self):
		f=myform()
		return render.formtest(f)
class registration:
    def GET(self):
        f=newUser()
        return render.regForm(f)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
