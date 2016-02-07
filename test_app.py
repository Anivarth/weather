from bottle import run, route, template, debug

@route('/<name>/<job>')
def index(name,job):
	return template('index.tpl',name=name, job=job)

@route('/<name>/')
@route('/<name>')
def only_name(name):
	return "Hello!"
debug(True)
run(reloader=True)