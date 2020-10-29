from aws_cdk import core
from . import widget_service


class ServerlesscdkStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        widget_service.WidgetService(self, "Widgets")
