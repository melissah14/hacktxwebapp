import web 
from web import form
render = web.template.render('templates/')

#db = web.database(dbn='mysql', user='username', pw='password', db='userAut')

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
