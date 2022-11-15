# Sample Digital Ocean Deployment for Streamlit

## What you need to change
1. Edit ```./do/app.yaml```
2. Edit ```./do/deploy.template.yaml```
3. Edit/Replace ```app.py``` to your application
4. Replace ```requirements.txt``` with your own

## Local development
```sh
# build image
docker build . -t streamlit_app

# start container
docker run -p 8501:8501 streamlit_app
```
You can now visit http://localhost:8501 in your browser.

## Digital Ocean App Platform
Under App platform, go to Create App and select your repository. The app platform should build and deploy successfully. 

## References
https://docs.digitalocean.com/products/app-platform/reference/app-spec/

https://www.digitalocean.com/community/questions/how-to-deploy-docker-container-using-do-deploy-template-yaml

https://docs.streamlit.io/knowledge-base/tutorials/deploy/docker