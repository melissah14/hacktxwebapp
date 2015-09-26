import web 
from web import form
render = web.template.render('templates/')

myform = form.Form( 
    form.Textbox("boe"), 
    form.Textbox("bax", 
        form.notnull,
        form.regexp('\d+', 'Must be a digit'),
        form.Validator('Must be more than 5', lambda x:int(x)>5)),
    form.Textarea('moe'),
    form.Checkbox('curly'), 
    form.Dropdown('french', ['mustard', 'fries', 'wine'])) 

urls = (
  '/print/(.*)', 'index',
  '/loginuser/(.*)/(.*)', 'login',
  '/form/', 'formtest'
)
class index:
    def GET(self, name):
        return render.index(name)


class login:
    def GET(self, user, pw):
        print user
        print pw
        return
class formtest:
	def GET(self):
		form=myform()
		return render.formtest(form)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
