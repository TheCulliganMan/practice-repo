# pull from the python 3.7 image (based on debian)
FROM python:3.7  
# Create folder recursive 
CMD mkdir -p /usr/src/app  
# Set current working directory to the working dir
WORKDIR /usr/src/app
# Copy requirements.txt from host to container
COPY requirements.txt .
# Run a single command that will not serve as the containers entrypoint
RUN pip install -r requirements.txt
# Copy all items (not in .dockerignore) into the folder
COPY . .
# write the image entrypoint.  This command will run on container start.
# bind port 8000, 4 workers, 2 second timeout
CMD ["gunicorn", "application:app", "-b", "8000:8000", "-w", "4", "--timeout", "2"]
