valknode/
├── k8s/
│   ├── wagtail/
│   │   ├── deployment.yaml
│   │   ├── service.yaml
│   │   └── ingress.yaml
│   ├── db/
│   │   ├── postgres-deployment.yaml
│   │   ├── postgres-service.yaml
│   ├── nginx/
│   │   ├── deployment.yaml
│   │   └── service.yaml
│   └── elk/
│       ├── elasticsearch/
│       │   ├── deployment.yaml
│       │   ├── service.yaml
│       │   └── pvc.yaml
│       ├── kibana/
│       │   ├── deployment.yaml
│       │   ├── service.yaml
│       │   └── ingress.yaml
│       └── logstash/ (optional)
│           ├── deployment.yaml
│           └── configmap.yaml
├── wagtail-src/
│   ├── manage.py
│   └── blog/
├── Dockerfile
├── requirements.txt
└── README.md
