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

# Github Container Registry
docker login ghcr.io --username <github-username> --password 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
echo "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" | docker login ghcr.io -u <github-username> --password-stdin

# Push docker image to ghcr
docker push ghcr.io/<github-username>/django-devops-2026:latest

# Link ghcr img to a specific repo (Dockerfile)
LABEL org.opencontainers.image.source="https://github.com/<github-username>/<repo>"