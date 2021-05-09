## PyAPI

### Docker

#### Generate Configuration

**Prereqs for setup before building the container**:

#### Build Container:

Build and run PyAPI container:

```
cd docker
docker build -t test:pyapi pyapi
```

#### Run Container:

```
docker run -it -p 5000:5000 --mount src=$(pwd),target=/var/www/test,type=bind test:pyapi
```
