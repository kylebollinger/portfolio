<div align="center">
<h1 align="center">
<img src="https://kboll.s3.amazonaws.com/projects/portfolio/terminal-icon-gradient.svg" width="100" />
<br>kboll portfolio</h1>
<h3>Official portfolio website for Kyle Bollinger<br /><a href="https://kylebollinger.dev" target="_blank">kylebollinger.dev</a></h3>
<h3>Developed with the software and tools below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/SVG-FFB13B.svg?style&logo=SVG&logoColor=black" alt="SVG" />
<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style&logo=JavaScript&logoColor=black" alt="JavaScript" />
<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style&logo=HTML5&logoColor=white" alt="HTML5" />
<img src="https://img.shields.io/badge/Autoprefixer-DD3735.svg?style&logo=Autoprefixer&logoColor=white" alt="Autoprefixer" />
<img src="https://img.shields.io/badge/Sass-CC6699.svg?style&logo=Sass&logoColor=white" alt="Sass" />
<img src="https://img.shields.io/badge/Webpack-8DD6F9.svg?style&logo=Webpack&logoColor=black" alt="Webpack" />

<img src="https://img.shields.io/badge/Bootstrap-7952B3.svg?style&logo=Bootstrap&logoColor=white" alt="Bootstrap" />
<img src="https://img.shields.io/badge/Gunicorn-499848.svg?style&logo=Gunicorn&logoColor=white" alt="Gunicorn" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/Buffer-231F20.svg?style&logo=Buffer&logoColor=white" alt="Buffer" />
<img src="https://img.shields.io/badge/Django-092E20.svg?style&logo=Django&logoColor=white" alt="Django" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style&logo=JSON&logoColor=white" alt="JSON" />
</p>
<img src="https://img.shields.io/github/last-commit/kylebollinger/portfolio?style&color=5D6D7E" alt="git-last-commit" />
<img src="https://img.shields.io/github/commit-activity/m/kylebollinger/portfolio?style&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/languages/top/kylebollinger/portfolio?style&color=5D6D7E" alt="GitHub top language" />
</div>

---

## 📖 Table of Contents
- [📖 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [🚀 Getting Started](#-getting-started)
    - [🔧 Installation](#-installation)
    - [🤖 Running portfolio](#-running-portfolio)
- [🛣 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)

---


## 📍 Overview

This repo houses the full Django application running my personal portfolio website. The backend is setup to add new projects, galleries and tags at anytime. 

![ERD diagrom of the backend design for the library](https://kboll.s3.amazonaws.com/projects/portfolio/db-diagram@1x.webp)
ERD diagrom of the backend design logic running the main models: projects, galleries, and tags

---

## 📦 Features

The app consists of 3 primary pages here:

1. **Homepage -** lists the top 3 projects and an about me section.
2. **Projects Index Page** - list of all the projects. 
3. **Project Details Page** - the full writeup about the project including videos, screenshots, and links to source code and live website.

---


## 📂 Repository Structure

```sh
└── portfolio/
    ├── core/
    │   ├── settings.py
    │   ├── urls.py
    ├── main/
    │   ├── static/
    │   ├── templates/
    │   ├── urls.py
    │   └── views.py
    ├── projects/
    │   ├── migrations/
    │   ├── models.py
    │   ├── templates/
    │   ├── urls.py
    │   └── views.py
    ├── src/
    │   ├── js/
    │   └── scss/
    ├── templates/
    │   ├── app.html
    │   ├── includes/
    │   └── layout/
    ├── Procfile    
    ├── manage.py
    ├── package-lock.json
    ├── package.json
    ├── requirements.txt
    └── webpack.config.js
```

---

## 🚀 Getting Started

***Dependencies***

Please ensure you have the following dependencies installed on your system:

`- ℹ️ Python >= 3.11`

`- ℹ️ Node/NPM`


### 🔧 Installation

1. Clone the portfolio repository:
```sh
git clone https://github.com/kylebollinger/portfolio
```

2. Change to the project directory:
```sh
cd portfolio
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

4. Install the node packages:
```sh
npm install
```

5. Config .env file from example:
```sh
mv .env.example .env
```


### 🤖 Running portfolio


1. Start web dev server
```sh
npm run watch
```

2. Start local web server
```sh
python manage.py runserver
```

---


## 🛣 Roadmap

> - [ ] `ℹ️  Create project types to display different kinds of work`
> - [ ] `ℹ️  Filter & sort projects by tags, type, date in ASC/DESC`
> - [ ] `ℹ️  Add an About page`


---

## 🤝 Contributing

Contributions are always welcome! Please follow these steps:
1. Fork the project repository. This creates a copy of the project on your account that you can modify without affecting the original project.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive name (e.g., `new-feature-branch` or `bugfix-issue-123`).
```sh
git checkout -b new-feature-branch
```
4. Make changes to the project's codebase.
5. Commit your changes to your local branch with a clear commit message that explains the changes you've made.
```sh
git commit -m 'Implemented new feature.'
```
6. Push your changes to your forked repository on GitHub using the following command
```sh
git push origin new-feature-branch
```
7. Create a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
The project maintainers will review your changes and provide feedback or merge them into the main branch.