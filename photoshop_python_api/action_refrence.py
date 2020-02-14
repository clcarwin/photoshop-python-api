"""ActionDescriptor of photoshop scripting.

A record of key-value pairs for actions, such as those included on the
Adobe Photoshop Actions menu. The ActionDescriptor class is part of the Action
Manager functionality. For more details on the Action Manager,
see the Photoshop Scripting Guide.

"""
from photoshop_python_api._core import Photoshop


class ActionReference(Photoshop):
    object_name = "ActionReference"

    def __init__(self):
        super(ActionReference, self).__init__()
