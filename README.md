# django-devops-2026
Master Django DevOps with Infrastructure as Code. Automate deployments using Terraform, Render, Docker and CI/CD



# Docker

docker build -t django-devops .
docker run -d -p 8000:8000 django-devops

## Delete all
docker system prune -a --volumes -f

# Django server

python3 manage.py runserver

# Test Token
<github-container-registry-pat>

# Docker image build (imgname: <repo>)
docker build -t ghcr.io/<github-username>/django-devops-2026 .
docker build --no-cache -t ghcr.io/<github-username>/django-devops:latest . 

# Github Container Registry (PAT: Personal access token)
docker login ghcr.io --username <github-username> --password PAT
echo "PAT" | docker login ghcr.io -u <github-username> --password-stdin
docker logout ghcr.io

# Push docker image to ghcr
docker push ghcr.io/<github-username>/django-devops-2026:latest

# Link ghcr img to a specific repo (Dockerfile)
LABEL org.opencontainers.image.source="https://github.com/<github-username>/<repo>"