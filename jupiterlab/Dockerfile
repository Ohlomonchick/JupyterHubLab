FROM jupyter/scipy-notebook:ed2908bbb62e
RUN conda install --quiet --yes \
 'r-base' \
 'r-irkernel' && \
 conda clean -tipy && \
 fix-permissions $CONDA_DIR
ARG NOTEBOOKS_FROM
ARG HUB_PATH
USER root
# remove pre-created image folders
RUN rm -r /home/jovyan
RUN pip install \
 sas7bdat && \
 fix-permissions $CONDA_DIR
ADD $NOTEBOOKS_FROM $HUB_PATH