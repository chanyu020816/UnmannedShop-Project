FROM ubuntu:20.04
LABEL authors="Chan-Yu"

ENV TZ=America/Los_Angeles
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY source /source
WORKDIR /source/

## install Python3.8, pip and wget
RUN apt-get update && apt-get install -y \
    python3.8 \
    python3-pip \
    wget

## upgrade pip3
RUN pip3 install --upgrade setuptools && pip3 install --upgrade pip
## install Python packages (listed in pkg.txt file)
RUN pip3 install -r pkgs.txt
RUN apt install python3-tk -y
RUN pip3 install --upgrade google-cloud-bigquery


# ENTRYPOINT ["top", "-b"]

CMD ["/bin/bash"]