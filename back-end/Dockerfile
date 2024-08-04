FROM debian:buster-slim

# 必要なパッケージをインストールする
RUN apt-get update && apt-get install -y \
    wget \
    build-essential \
    tcl \
    libssl-dev \
    zlib1g-dev \
    libncurses5-dev \
    libncursesw5-dev \
    libreadline-dev \
    libsqlite3-dev \
    libgdbm-dev \
    libdb5.3-dev \
    libbz2-dev \
    libexpat1-dev \
    liblzma-dev \
    llvm \
    xz-utils \
    tk-dev \
    libffi-dev \
    python-openssl \
    git \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Download and install Python with the latest SQLite
WORKDIR /usr/src
RUN wget https://www.sqlite.org/2024/sqlite-autoconf-3460000.tar.gz \
    && tar xvfz sqlite-autoconf-3460000.tar.gz \
    && cd sqlite-autoconf-3460000 \
    && ./configure --prefix=/usr && make && make install

ENV LD_LIBRARY_PATH="/usr/local/lib:/usr/lib"
ENV LDFLAGS="-L/usr/local/lib"
ENV CPPFLAGS="-I/usr/local/include -I/usr/local/include/sqlite3"

WORKDIR /usr/src
RUN wget https://www.python.org/ftp/python/3.12.4/Python-3.12.4.tgz \
    && tar xvfz Python-3.12.4.tgz \
    && cd Python-3.12.4 \
    && ./configure --enable-loadable-sqlite-extensions --prefix=/usr \
    && make && make install

RUN rm -rf /usr/src


# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . .

# Install production dependencies.
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "80"]
