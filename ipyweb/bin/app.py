import web

urls =(
    '/hello', 'Index'
)

app = web.application(urls, globals())
render = web.template.render('templates/', base='layout')

class Index(object):
    def GET(self):
        #return render.foo(words = words)
        return render.hello_form()

    def POST(self):
        form = web.input(name="Nobody", password="Null")
        return render.index(username=form.name, password=form.password)

if __name__ == '__main__':
    app.run()

