FROM debian:11

WORKDIR /home

RUN apt-get update && \
    apt-get install -y gcc g++ python3 git


RUN addgroup wheel && useradd -m -G wheel ruby
# Change to non-root privilege
USER ruby

# locale
RUN apt-get update && apt-get install -y locales && rm -rf /var/lib/apt/lists/* \
	&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8