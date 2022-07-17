# README

Demonstrates a temperature gauge.  

TODO:

* Build an app, reads temperature, posts it to the gateway.
* Create a grafana dashboard 
* 
* Dockerise it
* Mermaid Diagram 

## Prepare the device

```sh
# install the libs on the device.
curl https://get.pimoroni.com/rainbowhat | bash
```

## Start the services

To start up Prometheus and Grafana

```sh
# start the server
docker compose --profile prometheus up -d
```

```sh
# Check scrape configuration 
xdg-open http://localhost:9090
```

```sh
# load some metrcis into prometheus
./load_metrics.sh
```

```sh
# Check pushgateway configuration 
open http://localhost:9091
```

## PromQL   

```js
// list all the metrics
{__name__!=""}

// graph the metric
{__name__="some_metric"}
```

## Cleanup

```sh
# stop the server
docker compose --profile prometheus down --volumes
```


## Resources

* Pushgateway docs [here](https://github.com/prometheus/pushgateway/blob/master/README.md)  
* Pushgateway repo [here](https://github.com/prometheus/pushgateway)
* Pushgateway dockerhub [here](https://hub.docker.com/r/prom/pushgateway)


https://learn.pimoroni.com/article/getting-started-with-rainbow-hat-in-python



Note: Rainbow HAT requires SPI communication
Note: Rainbow HAT requires I2C communication