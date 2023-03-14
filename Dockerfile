# Workaround for arm64 wheels are not available, so rust must be installed
# https://github.com/openai/tiktoken/issues/23#issuecomment-1437463984
FROM python:3.11-slim-bullseye as builder

# Tiktoken requires Rust toolchain, so build it in a separate stage
RUN apt-get update && apt-get install -y gcc curl
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y && apt-get install --reinstall libc6-dev -y
ENV PATH="/root/.cargo/bin:${PATH}"
RUN pip install --upgrade pip && pip install tiktoken==0.1.2 #<-- Shall be same version as in requirements.txt

#-----------------------------------------------------------------------
FROM python:3.11-slim-bullseye

RUN apt-get update && apt-get install -y gcc curl procps

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Copy pre-built packages from builder stage
COPY --from=builder /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/

# building some packages was giving a setuptools error. 
# This fixex the issue
RUN pip install --upgrade pip && pip install setuptools && pip install --upgrade setuptools

# Regular requirements install
RUN pip install --upgrade pip && pip install -r requirements.txt

# Set the OPENAI_API environment variable
ENV OPENAI_API_KEY="your_api_key_here"

# Expose port 8000 for the Flask application to run on
EXPOSE 80

# Create a volume for Gunicorn logs
VOLUME /var/log/

# Run the Flask app with Gunicorn
CMD ["gunicorn", "--config", "gunicorn_config_docker.py", "web:app"]






