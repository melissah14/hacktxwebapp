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
    form.Textbox('Username', description="username"),
    form.Password('Password', description="password"),
    form.Button('Login', description="login"),
    form.Button('New User?', description="new user", id="newuser")
)

newUser = form.Form(
    form.Textbox('First name: ', description="First Name"),
    form.Textbox('Last name: ', description="Last Name"),
    form.Dropdown('Account Type',[('Tutor','Tutor'),('Student','Student')]),
    form.Password('Enter your password', description="Password")
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
