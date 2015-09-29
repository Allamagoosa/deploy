from fabric.api import env, cd, sudo, get, put, local, hosts, roles

env.roledefs['app'] = ['10.20.0.22']
env.roledefs['static'] = ['10.20.0.33']

def app_env():
    env.user = 'vagrant'
    env.key_filename = 'D:/vagrant2/.vagrant/machines/default/virtualbox/private_key'

def static_env():
    env.user = 'vagrant'
    env.key_filename = 'D:/vagrant3/.vagrant/machines/default/virtualbox/private_key'

# Default role: env.roles = ['one_node']

@roles('app')
def get_static():
    app_env()
    get('/var/www/nginx/static/', './')

@roles('static')
def put_static():
    static_env()
    with cd('/var/'):
        sudo('mkdir -p /var/www/nginx/static')
        put('./static/', '/var/www/nginx/', use_sudo=True)

