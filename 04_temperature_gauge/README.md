# README

Demonstrates a temperature gauge running on a RPI with UnicornHat.  

TODO:

* Build an app, reads temperature, posts it to the gateway.  
* Create a grafana dashboard  
* Dockerise it  
* Mermaid Diagram  

## Prepare the device

```sh
# install the libs on the device.
curl https://get.pimoroni.com/rainbowhat | bash
Note: Rainbow HAT requires SPI communication
Note: Rainbow HAT requires I2C communication
```

## Start the services

To start up Prometheus and Grafana

```sh
# start the server
docker compose -f ./docker-compose.yaml -f ./docker-compose.mitmreverseproxy.yaml up -d --build --force-recreate
```

```sh
# Check scrape configuration 
open http://localhost:8081
```

```sh
# Check scrape configuration 
xdg-open http://localhost:9090
```

```sh
# load some metrcis into prometheus
./load_metrics.sh
# load through mitm proxy
./load_metrics.sh 8080

# check mitm logs
docker compose logs mitmproxy
```

```sh
# Check pushgateway configuration 
open http://localhost:9091
# check metrics appear
open http://localhost:9091/metrics
```

## PromQL

```js
// list all the metrics
{__name__!=""}

// graph the metric
{__name__="some_metric"}
```

## Grafana

```sh
open http://localhost:3000
```

## Cleanup

```sh
# stop the server
docker compose -f ./docker-compose.yaml -f ./docker-compose.mitmreverseproxy.yaml down --volumes
```

## Resources

* Pushgateway docs [here](https://github.com/prometheus/pushgateway/blob/master/README.md)  
* Pushgateway repo [here](https://github.com/prometheus/pushgateway)
* Pushgateway dockerhub [here](https://hub.docker.com/r/prom/pushgateway)

* Provision Grafana [here](https://grafana.com/docs/grafana/latest/administration/provisioning/)

* Getting Started with Rainbow HAT [here](https://learn.pimoroni.com/article/getting-started-with-rainbow-hat-in-python)
