import web 
from web import form
render = web.template.render('templates/')

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
    def GET(self, name):
        return render.index(name)


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
