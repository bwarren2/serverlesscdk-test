
# Note

This is a python implementation of the tutorial project [here](https://docs.aws.amazon.com/cdk/latest/guide/serverless_example.html).  Currently it is broken; I need to fix the non-base-GET handlers.

Things learned:

Adding the local env installs for autocompletes: very important.  Looks like
```
    "python.autoComplete.extraPaths": [
        "${workspaceFolder}/.env/lib/python3.7/site-packages"
    ]
```
in `.vscode`.

A new cloudwatch group is spawned per deployment, ie you need to cycle through groups to keep up with changes.  You do get print debugging that way, though.

Wish I knew of a better way to test; might just need to declare some mock objects.  It feels like there should be a library for this?


# Welcome to your CDK Python project!

This is a blank project for Python development with CDK.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the .env
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .env
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .env/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .env\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
