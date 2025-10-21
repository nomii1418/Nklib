# Deployment Guide

## Prerequisites

- Server with Ubuntu 20.04+ or similar
- Domain name (optional but recommended)
- SSL certificate (Let's Encrypt recommended)
- MongoDB 5.0+
- Python 3.9+
- Node.js 18+
- Nginx (for reverse proxy)
- Telegram Bot Token

## Production Deployment

### 1. Server Setup

\`\`\`bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install dependencies
sudo apt install -y python3-pip python3-venv nodejs npm mongodb nginx certbot python3-certbot-nginx

# Install PM2 for process management
sudo npm install -g pm2
\`\`\`

### 2. Clone and Setup

\`\`\`bash
# Clone repository
git clone https://github.com/yourusername/mechanical-library.git
cd mechanical-library

# Setup backend
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd ..

# Setup frontend
cd frontend
npm install
npm run build
cd ..
\`\`\`

### 3. Configure Environment

\`\`\`bash
# Edit backend/.env
MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=mechanical_library
SECRET_KEY=$(openssl rand -hex 32)
TELEGRAM_BOT_TOKEN=your_production_bot_token
ADMIN_USERNAME=nk28
ADMIN_PASSWORD=your_secure_password
FRONTEND_URL=https://yourdomain.com
BACKEND_URL=https://api.yourdomain.com
\`\`\`

### 4. Setup Nginx

\`\`\`nginx
# /etc/nginx/sites-available/mechanical-library

# Backend API
server {
    listen 80;
    server_name api.yourdomain.com;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /uploads {
        proxy_pass http://localhost:8000/uploads;
        proxy_set_header Host $host;
    }
}

# Frontend
server {
    listen 80;
    server_name yourdomain.com;

    root /path/to/mechanical-library/frontend/dist;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }

    location /api {
        proxy_pass http://localhost:8000/api;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
\`\`\`

\`\`\`bash
# Enable site
sudo ln -s /etc/nginx/sites-available/mechanical-library /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
\`\`\`

### 5. Setup SSL

\`\`\`bash
# Get SSL certificates
sudo certbot --nginx -d yourdomain.com -d api.yourdomain.com
\`\`\`

### 6. Start Services with PM2

\`\`\`bash
# Start backend
cd backend
pm2 start "uvicorn app.main:app --host 0.0.0.0 --port 8000" --name mechanical-backend

# Start bot
cd ../bot
pm2 start telegram_bot.py --name mechanical-bot --interpreter python3

# Save PM2 configuration
pm2 save
pm2 startup
\`\`\`

### 7. Setup MongoDB

\`\`\`bash
# Enable authentication
sudo mongo
> use admin
> db.createUser({user: "admin", pwd: "your_password", roles: ["root"]})
> exit

# Edit MongoDB config
sudo nano /etc/mongod.conf
# Add:
security:
  authorization: enabled

# Restart MongoDB
sudo systemctl restart mongod

# Update backend/.env with authentication
MONGODB_URL=mongodb://admin:your_password@localhost:27017
\`\`\`

## Docker Deployment

### 1. Build and Run

\`\`\`bash
# Set environment variable
export TELEGRAM_BOT_TOKEN=your_token

# Start all services
docker-compose up -d

# Check logs
docker-compose logs -f
\`\`\`

### 2. Setup Nginx for Docker

\`\`\`nginx
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://localhost:3000;
        proxy_set_header Host $host;
    }

    location /api {
        proxy_pass http://localhost:8000/api;
        proxy_set_header Host $host;
    }
}
\`\`\`

## Cloud Deployment

### AWS EC2

1. **Launch EC2 Instance:**
   - Ubuntu 20.04
   - t3.medium or larger
   - Open ports: 80, 443, 22

2. **Setup:**
   \`\`\`bash
   ssh -i your-key.pem ubuntu@your-ip
   # Follow Server Setup steps above
   \`\`\`

3. **RDS for MongoDB:**
   - Use MongoDB Atlas instead
   - Update MONGODB_URL in .env

### DigitalOcean

1. **Create Droplet:**
   - Ubuntu 20.04
   - 2GB RAM minimum
   - Add SSH key

2. **Setup:**
   \`\`\`bash
   ssh root@your-ip
   # Follow Server Setup steps above
   \`\`\`

### Heroku

1. **Backend:**
   \`\`\`bash
   cd backend
   heroku create mechanical-library-api
   heroku addons:create mongolab
   git push heroku main
   \`\`\`

2. **Frontend:**
   \`\`\`bash
   cd frontend
   heroku create mechanical-library-web
   git push heroku main
   \`\`\`

## Monitoring

### Setup PM2 Monitoring

\`\`\`bash
pm2 install pm2-logrotate
pm2 set pm2-logrotate:max_size 10M
pm2 set pm2-logrotate:retain 7
\`\`\`

### Setup Application Monitoring

\`\`\`bash
# Install monitoring tools
pip install prometheus-client
npm install prom-client

# Configure alerts
pm2 install pm2-slack
pm2 set pm2-slack:slack_url https://hooks.slack.com/services/YOUR/SLACK/WEBHOOK
\`\`\`

## Backup Strategy

### Database Backup

\`\`\`bash
# Create backup script
cat > /usr/local/bin/backup-mongodb.sh << 'EOF'
#!/bin/bash
DATE=$(date +%Y%m%d_%H%M%S)
mongodump --out /backups/mongodb_$DATE
# Upload to S3 or similar
aws s3 cp /backups/mongodb_$DATE s3://your-bucket/backups/
EOF

chmod +x /usr/local/bin/backup-mongodb.sh

# Add to crontab (daily at 2 AM)
crontab -e
0 2 * * * /usr/local/bin/backup-mongodb.sh
\`\`\`

### File Backup

\`\`\`bash
# Backup uploads directory
rsync -avz uploads/ backup-server:/backups/uploads/
\`\`\`

## Scaling

### Horizontal Scaling

1. **Multiple Backend Instances:**
   \`\`\`bash
   pm2 start app.main:app -i max
   \`\`\`

2. **Load Balancer:**
   \`\`\`nginx
   upstream backend {
       server localhost:8000;
       server localhost:8001;
       server localhost:8002;
   }
   \`\`\`

### Vertical Scaling

- Upgrade server resources
- Increase MongoDB memory
- Optimize queries

## Security Checklist

- [ ] Change default admin password
- [ ] Enable MongoDB authentication
- [ ] Setup SSL/TLS
- [ ] Configure firewall
- [ ] Setup fail2ban
- [ ] Regular security updates
- [ ] Backup encryption
- [ ] API rate limiting
- [ ] Input validation
- [ ] CORS configuration

## Maintenance

### Update Application

\`\`\`bash
# Pull latest code
git pull origin main

# Update backend
cd backend
source venv/bin/activate
pip install -r requirements.txt
pm2 restart mechanical-backend

# Update frontend
cd frontend
npm install
npm run build

# Update bot
pm2 restart mechanical-bot
\`\`\`

### Database Maintenance

\`\`\`bash
# Compact database
mongo mechanical_library --eval "db.runCommand({ compact: 'subjects' })"

# Rebuild indexes
mongo mechanical_library --eval "db.subjects.reIndex()"
\`\`\`

## Troubleshooting

### Check Logs

\`\`\`bash
# PM2 logs
pm2 logs mechanical-backend
pm2 logs mechanical-bot

# Nginx logs
sudo tail -f /var/log/nginx/error.log

# MongoDB logs
sudo tail -f /var/log/mongodb/mongod.log
\`\`\`

### Restart Services

\`\`\`bash
pm2 restart all
sudo systemctl restart nginx
sudo systemctl restart mongod
\`\`\`

## Performance Optimization

1. **Enable Compression:**
   \`\`\`nginx
   gzip on;
   gzip_types text/plain text/css application/json application/javascript;
   \`\`\`

2. **Cache Static Files:**
   \`\`\`nginx
   location ~* \.(jpg|jpeg|png|gif|ico|css|js)$ {
       expires 1y;
       add_header Cache-Control "public, immutable";
   }
   \`\`\`

3. **Database Indexing:**
   - Already configured in database.py
   - Monitor slow queries
   - Add indexes as needed

## Support

For deployment issues:
1. Check service logs
2. Verify configuration
3. Test connectivity
4. Review security settings
5. Contact support team
