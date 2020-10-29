#!/usr/bin/env python3

from aws_cdk import core

from serverlesscdk.serverlesscdk_stack import ServerlesscdkStack


app = core.App()
ServerlesscdkStack(app, "serverlesscdk")

app.synth()
