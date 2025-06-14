.
├── k8s
│   ├── db
│   │   ├── postgres-deployment.yaml
│   │   ├── postgres-pvc.yaml
│   │   └── postgres-service.yaml
│   ├── elk
│   │   ├── elasticsearch
│   │   │   ├── deployment.yaml
│   │   │   ├── pvc.yaml
│   │   │   └── service.yaml
│   │   ├── kibana
│   │   │   ├── deployment.yaml
│   │   │   ├── pvc.yaml
│   │   │   └── service.yaml
│   │   └── logstash
│   │       ├── deployment.yaml
│   │       ├── pvc.yaml
│   │       └── service.yaml
│   ├── nginx
│   │   ├── deployment.yaml
│   │   ├── nginx.conf
│   │   └── service.yaml
│   └── wagtail
│       ├── deployment.yaml
│       ├── ingress.yaml
│       └── service.yaml
├── README.md
├── requirements.txt
├── tree.txt
└── wagtail-src
    ├── blog
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-311.pyc
    │   │   ├── __init__.cpython-312.pyc
    │   │   ├── urls.cpython-312.pyc
    │   │   └── wsgi.cpython-312.pyc
    │   ├── settings
    │   │   ├── base.py
    │   │   ├── dev.py
    │   │   ├── __init__.py
    │   │   ├── production.py
    │   │   └── __pycache__
    │   │       ├── base.cpython-311.pyc
    │   │       ├── base.cpython-312.pyc
    │   │       ├── dev.cpython-311.pyc
    │   │       ├── dev.cpython-312.pyc
    │   │       ├── __init__.cpython-311.pyc
    │   │       └── __init__.cpython-312.pyc
    │   ├── static
    │   │   ├── css
    │   │   │   └── blog.css
    │   │   └── js
    │   │       └── blog.js
    │   ├── templates
    │   │   ├── 404.html
    │   │   ├── 500.html
    │   │   └── base.html
    │   ├── urls.py
    │   └── wsgi.py
    ├── Dockerfile
    ├── home
    │   ├── apps.py
    │   ├── __init__.py
    │   ├── migrations
    │   │   ├── 0001_initial.py
    │   │   ├── 0002_create_homepage.py
    │   │   ├── 0003_homepage_intro.py
    │   │   ├── __init__.py
    │   │   └── __pycache__
    │   │       ├── 0001_initial.cpython-312.pyc
    │   │       ├── 0002_create_homepage.cpython-312.pyc
    │   │       ├── 0003_homepage_intro.cpython-312.pyc
    │   │       └── __init__.cpython-312.pyc
    │   ├── models.py
    │   ├── __pycache__
    │   │   ├── apps.cpython-312.pyc
    │   │   ├── __init__.cpython-312.pyc
    │   │   └── models.cpython-312.pyc
    │   ├── static
    │   │   └── css
    │   │       └── welcome_page.css
    │   └── templates
    │       └── home
    │           ├── home_page.html
    │           └── welcome_page.html
    ├── manage.py
    ├── requirements.txt
    └── search
        ├── __init__.py
        ├── __pycache__
        │   ├── __init__.cpython-312.pyc
        │   └── views.cpython-312.pyc
        ├── templates
        │   └── search
        │       └── search.html
        └── views.py
