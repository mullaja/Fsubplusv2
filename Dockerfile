# SET BASE IMAGE OS
FROM python:3.9-alpine

# WORKDIR
WORKDIR /home/fsub

# CLONE REPOSITORY
COPY . ./

RUN apk add git

# IGNORE PIP WARNING 
ENV PIP_ROOT_USER_ACTION=ignore

# UPDATE PIP
RUN pip install -U pip

# INSTALL REQUIREMENTS
RUN pip install -U \
                --no-cache-dir \
                -r requirements.txt

# COMMAND TO RUN
CMD ["python", "-m", "fsub"]
