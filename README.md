# DevOps Interview Lab (Docker, Ansible, CI, Logs)

This mini-lab lets you practice the exact items you asked for: 
- Dockerfile optimization
- Ansible playbook basics
- GitHub Actions CI pipeline
- Bash & Python log parsing

## 1) Dockerfile Optimization
Build both images and compare sizes:
```bash
docker build -t lab-unopt -f Dockerfile.unoptimized .
docker build -t lab-opt -f Dockerfile.optimized .
docker images | grep lab-
```

Run the optimized image:
```bash
docker run -d -p 8000:8000 --name lab lab-opt
curl -s http://localhost:8000/health
docker rm -f lab
```

## 2) Ansible Playbook (localhost & safe)
Install prerequisites (on Ubuntu/Debian-like):
```bash
python3 -m pip install --user ansible ansible-lint
```

Run and lint:
```bash
ansible-playbook -i ansible/inventory.ini ansible/site.yml
ansible-lint ansible/site.yml
cat /tmp/lab/app.conf
```

## 3) GitHub Actions (locally just review; run in GitHub)
- Push this repo to GitHub and the workflow runs automatically on push/PR: `.github/workflows/ci.yml`  
- Locally, you can emulate steps:
```bash
python -m pip install flake8 ansible ansible-lint
flake8 app
ansible-lint ansible/site.yml
docker build -t lab-app -f Dockerfile.optimized .
docker run -d -p 8000:8000 --name lab-app lab-app
sleep 2 && curl -sSf http://localhost:8000/health
docker rm -f lab-app
```

## 4) Log Parsing (Bash & Python)
```bash
bash scripts/parse_logs.sh logs/sample.log
python3 scripts/parse_logs.py logs/sample.log
```

## Cleanup
```bash
docker rm -f lab lab-app 2>/dev/null || true
docker rmi lab-unopt lab-opt lab-app 2>/dev/null || true
rm -rf /tmp/lab
```
