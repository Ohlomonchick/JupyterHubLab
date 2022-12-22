import os
import sys
from firstuseauthenticator import FirstUseAuthenticator 

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'

# environment configuration
c.DockerSpawner.image = os.environ['DOCKER_JUPYTER_IMAGE']
c.DockerSpawner.network_name = os.environ['DOCKER_NETWORK_NAME']
c.JupyterHub.hub_ip = os.environ['HUB_IP']

c.JupyterHub.services = [ 
    { 
        'name': 'idle-culler', 
        'admin': True, 
        'command': [ 
        sys.executable, 
        '-m', 'jupyterhub_idle_culler', 
        '--timeout=600',
        '--cull-users=True',
        '--cull-admin-users=true',
        '--remove-named-servers=true'
        ], 
    } 
] 


# simle authentication
# c.JupyterHub.authenticator_class = 'firstuseauthenticator.FirstUseAuthenticator'
c.Authenticator.admin_users = {'admin'}
c.JupyterHub.admin_access = True
# c.FirstUseAuthenticator.create_users = False


# storage configuration for single-users
notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan'
c.DockerSpawner.notebook_dir = notebook_dir 
c.DockerSpawner.volumes = { 
    'jupyterhub-user-{username}': notebook_dir, 
    'jupyterhub-shared': '/home/jovyan/shared'
}

# user environment limits
c.Spawner.default_url = '/lab' 
c.Spawner.cpu_limit = 1
c.Spawner.mem_limit = '2G'

