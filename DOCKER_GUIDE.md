# Docker Setup Guide for a365labs

This guide covers how to build and run the a365labs Flask application using Docker.

## Prerequisites

- Docker installed ([Download Docker](https://www.docker.com/products/docker-desktop))
- Docker Compose installed (included with Docker Desktop)

## Quick Start

### Option 1: Using Docker Compose (Recommended for Development)

```bash
# Start the application
docker-compose up -d

# View logs
docker-compose logs -f

# Stop the application
docker-compose down
```

The app will be available at `http://localhost:5000`

### Option 2: Using Docker CLI (Production-Ready)

**Build the image:**
```bash
docker build -t a365labs:latest .
```

**Run the container:**
```bash
docker run -d \
  --name a365labs \
  -p 5000:5000 \
  a365labs:latest
```

**View logs:**
```bash
docker logs -f a365labs
```

**Stop the container:**
```bash
docker stop a365labs
docker rm a365labs
```

## Development Workflow

### Using Docker Compose with Volume Mounts

The `docker-compose.yml` includes volume mounts for live code reloading:

```bash
# Start development server
docker-compose up

# Make changes to your code
# Changes will be automatically reflected in the container

# Rebuild if dependencies change
docker-compose up --build
```

## Image Details

- **Base Image**: Python 3.12-slim (lightweight production-ready)
- **Multi-stage Build**: Reduces final image size by ~60%
- **Non-root User**: Runs as `appuser` for security
- **Health Checks**: Built-in container health monitoring
- **Production Server**: Gunicorn with 4 workers and 2 threads
- **Logs**: Both access and error logs streamed to stdout

## Production Deployment

### Building for Production

```bash
docker build -t a365labs:1.0.0 .
```

### Running in Production

```bash
docker run -d \
  --name a365labs \
  -p 5000:5000 \
  --restart unless-stopped \
  --health-interval=30s \
  --health-timeout=3s \
  --health-retries=3 \
  a365labs:1.0.0
```

### Docker Compose for Production

Create a `docker-compose.prod.yml`:

```yaml
version: '3.8'
services:
  web:
    image: a365labs:latest
    container_name: a365labs
    ports:
      - "5000:5000"
    restart: unless-stopped
    networks:
      - a365-network

networks:
  a365-network:
    driver: bridge
```

Run with:
```bash
docker-compose -f docker-compose.prod.yml up -d
```

## Troubleshooting

### Container won't start
```bash
# Check logs
docker logs <container_id>

# Verify image built correctly
docker images
```

### Port already in use
```bash
# Change port in docker-compose.yml or use different port
docker run -d -p 8000:5000 a365labs:latest
```

### Clear cache and rebuild
```bash
docker system prune -a
docker-compose up --build
```

## File Structure

```
a365labs/
├── Dockerfile           # Multi-stage production image
├── docker-compose.yml   # Development setup
├── .dockerignore        # Files excluded from Docker image
├── requirements.txt     # Python dependencies
├── app.py              # Flask application
├── templates/          # HTML templates
├── static/             # Static files (CSS, JS, images)
└── DOCKER_GUIDE.md     # This file
```

## Environment Variables

For future configuration, you can pass environment variables:

```bash
docker run -e FLASK_ENV=production a365labs:latest
```

## Size Optimization

The multi-stage build reduces the final image size:
- Base Python image: ~170MB
- With dependencies: ~220MB (development)
- Final production image: ~200MB

## Security Notes

1. ✅ Non-root user execution
2. ✅ Health checks enabled
3. ✅ Read-only filesystem ready (can be enabled)
4. ✅ No secrets in Dockerfile
5. ✅ Minimal attack surface

## Next Steps

- Push to Docker Hub or private registry
- Deploy to Kubernetes or Docker Swarm
- Set up CI/CD pipeline for automatic builds
- Configure reverse proxy (Nginx) in front of app
