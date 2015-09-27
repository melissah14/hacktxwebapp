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
