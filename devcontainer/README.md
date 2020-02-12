# vscode-devcontainer template

A Dockerfile template that extends images to allow adding a non-root user in [vscode-devcontainer](https://code.visualstudio.com/docs/remote/containers-advanced#_adding-a-nonroot-user-to-your-dev-containerr).

## How to use it?

```bash
docker build . --build-arg BASE_IMAGE=<base-image> -t <base-image>_dev
```
