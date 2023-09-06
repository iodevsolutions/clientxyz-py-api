# Python Flask API Project

## Prerequisites for local container or Virtual Environment testing:
<ul>
  <li>Python v3.9 or higher</li>
  <li>Docker v23.x or higher</li>
</ul>
<br>

## Build and Deploy to Kubernetes Cluster
### Set up to following GitHub Actions secrets (SSH_HOST, SSH_PRIVATE_KEY and SSH_USER) which will allow GitHub Actions to deploy this application to the remote Kubernetes cluster

```
Name = SSH_HOST, Secret = "SSH Hostname or IP Address"
Name = SSH_PRIVATE_KEY, Secret ="SSH Private Key to access SSH_HOST"
Name = SSH_USER, Secret = "Username associate with SSH_PRIVATE_KEY to access SSH_HOST" 

```
<br>

## Build and test using local Docker container

### Change directory to the container build location:
*DEV*
```
cd container
```

### Execute the build image bash script and check for errors:
```
. ./build_local_image.sh
```

### Execute the run container bash script and check for errors:
```
. ./run_local_container.sh
```

### Test via browser or curl:
```
curl http://127.0.0.1:7080/api 
```
