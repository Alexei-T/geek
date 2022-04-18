FROM python:3.7
RUN pip install --no-cache-dir click==7.1.2 Flask==1.1.2 itsdangerous==1.1.0 && \
pip install --no-cache-dir Jinja2==2.11.2 MarkupSafe==1.1.1 Werkzeug==1.0.1
COPY ./app.py .
EXPOSE 8080
ENTRYPOINT python app.py
