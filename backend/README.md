# Backend part
## Requirements
- poetry
- Docker

## Deploying
Build docker container
```
$ docker build -t [app_name] [path_to_dockerfile]
```
and run them
```
$ docker run -p [ports]
```
For now you can only try the root point. The rest will come later :)


## JWT RS256

You must create certs dir and private and public keys for creating JWT.

1. Create directory
   ```
   mkdir certs
   ```
2. Generate private key
   ```
   $ openssl genrsa -out jwt-private.pem 2048
   ```
3. Generate public key
   ```
   $ openssl rsa -in jwt-private.pem -outform PEM -pubout -out jwt-public.pem
   ```
4. Add path to keys in app.core.settings
   ```python
    PRIVATE_KEY: Path = BACKEND_BASE_DIR / "certs" / "jwt-private.pem"
    PUBLIC_KEY: Path = BACKEND_BASE_DIR / "certs" / "jwt-public.pem"
   ```

### If you wanna use algorithm HS256
1. Change Algorithm in app.core.settings
   ```python
    ALGORITHM: str = "HS256"
   ```
2. In app.core.security add method for create jwt with HS256. For secret key use
```python
    app.settings.SECRET_KEY
```
