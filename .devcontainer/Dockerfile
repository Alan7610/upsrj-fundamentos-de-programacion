FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    build-essential \
    gdb \
    make \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Crear usuario no-root para VS Code
RUN useradd -ms /bin/bash vscode
USER vscode

WORKDIR /workspace