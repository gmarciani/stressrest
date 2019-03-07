# StressREST
Stress tests for REST APIs.


## Requirements

### Locust
[Locust](https://locust.io/) is an open source load testing tool.
Define user behaviour with Python code, and swarm your system with millions of simultaneous users.

```
pip install locustio
```

## Usage
If you want to run the stress test defined in `${FILE}`:

```
locust --locustfile ${FILE} --host ${HOST}
```

If you want to run the stress test defined in `${FILE}` against the host `${HOST}:${PORT}`:

```
locust --locustfile ${FILE} --host=${HOST}:${PORT}
```



## Authors
Giacomo Marciani, [gmarciani@acm.org](mailto:gmarciani@acm.org)


## License
The project is released under the [MIT License](https://opensource.org/licenses/MIT).
