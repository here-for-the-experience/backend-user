# Github Actions Workflow

### GitHub Actions Workflow for Pull Requests to Develop

+ This GitHub Actions workflow is used to build, test, and deploy the backend-user branch when a pull request is made to the develop branch. The workflow is triggered when a pull request is opened or updated.
The workflow first checks if there were any changes to the alembic directory. If there were, the workflow runs alembic upgrade head to upgrade the database schema to the latest version.
+ Next, the workflow builds and runs the Python application in a Docker container. The application is configured to use the DEV_DB_URL and DEV_SECRET_TOKEN secrets from GitHub Secrets.
+ Finally, the workflow runs the pytest test suite. If the tests pass, the workflow sends a message to Slack. If the tests fail, the workflow rolls back the database schema to the previous version.

Sends notification to Slack in both cases the tests pass or fail.
<img width="1440" alt="image" src="https://github.com/here-for-the-experience/backend-vaccine/assets/77661612/eed10b8f-6e4a-4e92-bae5-4fff888f2ab8">

##### The workflow is configured to run on Ubuntu-latest. The Python version is set to 3.9.





#### The workflow uses the following GitHub Secrets:
```
DEV_DB_URL: The URL of the development database.
DEV_SECRET_TOKEN: The secret token for the development database.
SLACK_WEBHOOK_URL: The URL of the Slack webhook.
```

#### Here are some additional details about the workflow:

+ The **changed-files-alembic** step uses the **tj-actions/changed-files** action to check if there were any changes to the alembic directory.
+ The **alembic-upgrade** step uses the alembic command-line tool to upgrade the database schema to the latest version.
+ The **pytest** step uses the pytest command-line tool to run the Python test suite.
+ The **slack** step uses the **slackapi/slack-github-action** action to send a message to Slack.

### GitHub Actions Workflow to Build and Deploy to DockerHub and Update to Deployment Repository
+ This GitHub Actions workflow is used to build, deploy, and update to deployment of the backend-vaccine branch when a push is made to the develop branch. The workflow is triggered when a push is made to the develop branch.
+ The workflow first builds the Docker image for the Python application. The image is tagged with the **github.run_number** variable, which is a unique identifier for the current run.
+ Next, the workflow pushes the Docker image to Docker Hub.
+ Finally, the workflow checkouts the deployment repository and modifies the deployment file to update the Docker image tag. The workflow then pushes the changes to the deployment repository.

##### The workflow is configured to run on Ubuntu-latest. The Python version is set to 3.9.

#### The workflow uses the following GitHub Secrets:
```
DOCKERHUB_USERNAME: The username for Docker Hub.
DOCKERHUB_TOKEN: The secret token for Docker Hub.
PAT_TOKEN: The personal access token for GitHub.
SLACK_WEBHOOK_URL: The URL of the Slack webhook.
```
#### Here are some additional details about the workflow:

+ The **build-and-push** step uses the docker/build-push-action@v4 action to build and push the Docker image to Docker Hub.
+ The **checkout-deployment-repo** step uses the **actions/checkout@v3** action to checkout the deployment repository.
+ The **modify-deployment-file** step uses the **sed** command-line tool to update the deployment file to update the Docker image tag.
+ The **push-changes-of-deployment** step uses the git command-line tool to push the changes to the deployment repository.
+ The **slack** step uses the **slackapi/slack-github-action@v1.24.0** action to send a message to Slack.


### GitHub Actions Workflow for Pushing to The Main Branch
+ This GitHub Actions workflow is used to build, deploy, and update the deployment of a Python application when a push is made to the main branch. The workflow is triggered when a push is made to the main branch.
+ The workflow first builds the Docker image for the Python application and The image is tagged with the github.run_number variable, which is a unique identifier for the current run.
+ Next, the workflow pushes the Docker image to Docker Hub.
+ Finally, the workflow checkouts the deployment repository and modifies the deployment file to update the Docker image tag. The workflow then pushes the changes to the deployment repository.

###### The workflow is configured to run on Ubuntu-latest. The Python version is set to 3.9.

##### The workflow uses the following GitHub Secrets:
```
DOCKERHUB_USERNAME: The username for Docker Hub.
DOCKERHUB_TOKEN: The token for Docker Hub.
PAT_TOKEN: The personal access token for GitHub.
SLACK_WEBHOOK_URL: The URL of the Slack webhook.
```

#### Here are some additional details about the workflow:

+ The **build-and-push** step uses the **docker/build-push-action@v4** action to build and push the Docker image to Docker Hub.
+ The **checkout-deployment-repo** step uses the **actions/checkout@v3** action to checkout the deployment repository.
+ The **modify-deployment-file** step uses the **sed** command-line tool to update the deployment file to update the Docker image tag.
+ The **push-changes-of-deployment** step uses the git command-line tool to push the changes to the deployment repository.
+ The **slack** step uses the slackapi/slack-github-action@v1.24.0 action to send a message to Slack.

##Reporting Problems 
  You can send us a mail at :
+ iam.reduan@gmail.com
+ Raufun.nazin13@gmail.com
+ shakil.csedu@gmail.com

## Contributors 
+ Alve Reduan
+ Fahim Shakil
