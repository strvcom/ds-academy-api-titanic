## :rocket: ds-academy-api-titanic

Titanic survival model API.
Written in [FastAPI](https://fastapi.tiangolo.com/).
Deployed on [Heroku](https://www.heroku.com/).

## :pencil: Authors

- [Jaroslav Bezdek](https://www.github.com/jardabezdek)
- [Jan Maly](https://github.com/honzaMaly)

## :construction_worker_man: Setup

### Local development

1. Intall requirements from `requirements-dev.txt`.

> The only difference between `requirements-dev.txt` and `requirements.txt` is
that in `requirements-dev.txt` there are two extra dependencies: `notebook`,
and `streamlit`.

### Docker for Heroku deployment

> Prerequisite for the following steps is to have
[Docker Desktop](https://www.docker.com/products/docker-desktop/) installed
on our system.

1. In project root directory, build the docker image
`docker build -t ds-academy-api-titanic:latest .`
1. Run the docker container with web server running inside:
`docker run -i -e "PORT=8000" -p 8000:8000 ds-academy-api-titanic:latest`
1. In logs, you should see a local URL address with running API.

### Deployment to Heroku

The repository is ready to be deployed to Heroku without any extra hassle.
For deployment, follow these steps.

1. Review the `heroku.yml` file to see configuration for Heroku.
1. Create your user profile on [Heroku](https://www.heroku.com).
1. [Install Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) and
log in to your Heroku account: `heroku login`.
1. [Create the app on Heroku](https://devcenter.heroku.com/articles/creating-apps).
1. Set stack for the project to container: `heroku stack:set container -a=<name of the app>`.
1. [Integrate the app with GitHub for auto-deployments](https://devcenter.heroku.com/articles/github-integration).
