# Use a base image
FROM debian:bullseye
# Set environment variables
ENV GRAFANA_VERSION=7.5.11
ENV GRAFANA_HOME=/opt/grafana

# Install dependencies
RUN apt-get update && mkdir -p ${GRAFANA_VERSION} && \
    apt-get install -y wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Download and extract Grafana
RUN wget https://dl.grafana.com/oss/release/grafana-${GRAFANA_VERSION}.linux-amd64.tar.gz && \
    tar -zxvf grafana-${GRAFANA_VERSION}.linux-amd64.tar.gz && \
    rm grafana-${GRAFANA_VERSION}.linux-amd64.tar.gz && \
    mv grafana-${GRAFANA_VERSION} /opt/grafana

# Expose Grafana port
EXPOSE 3000

# Start Grafana
CMD ["/opt/grafana/bin/grafana-server", "-homepath", "/opt/grafana"]
