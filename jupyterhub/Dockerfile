FROM jupyterhub/jupyterhub
COPY jupyterhub_config.py . 
RUN pip install \
 dockerspawner \
 jupyterhub-firstuseauthenticator \
 jupyterhub-idle-culler