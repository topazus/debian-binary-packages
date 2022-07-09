FROM debian:11

WORKDIR /home

RUN apt update && \
    apt install -y gcc g++ python3 python3-virtualenv git passwd nano sudo curl wget

# gh cli
RUN bash setup.sh



RUN addgroup wheel && useradd -m -G wheel ruby

# locale
RUN apt update && apt install -y locales && rm -rf /var/lib/apt/lists/* \
    && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8