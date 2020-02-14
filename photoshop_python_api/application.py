# -*- coding: utf-8 -*-
"""
module author: Long Hao <hoolongvfx@gmail.com>
"""
import os
import time

# Import local modules
from photoshop_python_api._core import Photoshop
# Import built-in modules
from photoshop_python_api.active_document import ActiveDocument
from photoshop_python_api.document import Document
from photoshop_python_api.documents import Documents
from photoshop_python_api.solid_color import SolidColor


class Application(Photoshop):
    object_name = 'Application'

    def __init__(self, version=None):
        super(Application, self).__init__(version)

    @property
    def document(self):
        return Document()

    @property
    def activeDocument(self):
        return ActiveDocument()

    @property
    def backgroundColor(self):
        return SolidColor

    @property
    def build(self):
        return self.app.build

    @property
    def colorSettings(self):
        return self.app.colorSettings

    @property
    def currentTool(self):
        return self.app.currentTool

    @property
    def displayDialogs(self):
        return self.app.displayDialogs

    @property
    def documents(self):
        return Documents()

    # TODO:
    @property
    def fonts(self):
        return self.app.fonts

    @property
    def foregroundColor(self):
        """The default foreground color (used to paint, fill,
        and stroke selections)."""
        return self.app.foregroundColor

    @property
    def freeMemory(self):
        """The amount of unused memory available to Photoshop."""
        return self.app.freeMemory

    @property
    def locale(self):
        """The language locale of the application."""
        return self.app.locale

    @property
    def macintoshFileTypes(self):
        """A list of the image file types Photoshop can open."""
        return self.app.macintoshFileTypes

    @property
    def measurementLog(self):
        """The log of measurements taken."""
        return self.app.measurementLog

    @property
    def name(self):
        return self.app.name

    @property
    def notifiers(self):
        """The notifiers currently configured (in the Scripts Events Manager menu in the application)."""
        return self.app.notifiers

    @property
    def notifiersEnabled(self):
        """If true, notifiers are enabled."""
        return self.app.notifiersEnabled

    @property
    def parent(self):
        """The object’s container."""
        return self.app.parent

    @property
    def path(self):
        return self.app.path

    @property
    def playbackDisplayDialogs(self):
        return self.app.playbackDisplayDialogs

    @property
    def playbackParameters(self):
        return self.app.playbackParameters

    @property
    def preferences(self):
        return self.app.preferences

    @property
    def preferencesFolder(self):
        return self.app.preferencesFolder

    @property
    def recentFiles(self):
        return self.app.recentFiles

    @property
    def scriptingBuildDate(self):
        return self.app.scriptingBuildDate

    @property
    def scriptingVersion(self):
        return self.app.scriptingVersion

    @property
    def systemInformation(self):
        return self.app.systemInformation

    @property
    def typename(self):
        return self.app.typename

    @property
    def version(self):
        return self.app.version

    @property
    def windowsFileTypes(self):
        return self.app.windowsFileTypes

    # Methods.

    def batch(self):
        pass

    def beep(self):
        """Alerts the user."""
        pass

    def bringToFront(self):
        return self.eval_javascript("app.bringToFront();")

    def changeProgressText(self, text):
        """Changes the text that appears in the progress window."""
        self.eval_javascript("app.changeProgressText('{}');".format(text))

    def doAction(self, action, action_from):
        """Plays the specified action from the Actions palette."""
        return self.app.doAction(action, action_from)

    def doForcedProgress(self, title, javascript):
        script = "app.doForcedProgress('{}', '{}')".format(title,
                                                           javascript)
        self.eval_javascript(script)
        # Ensure the script execute success.
        time.sleep(1)

    def doProgress(self, title, javascript):
        """Performs a task with a progress bar. Other progress APIs must be
        called periodically to update the progress bar and allow cancelling.

        Args:
            title (str): String to show in the progress window.
            javascript (str): JavaScriptString to execute.

        """
        script = "app.doProgress('{}', '{}')".format(title,
                                                     javascript)
        self.eval_javascript(script)
        # Ensure the script execute success.
        time.sleep(1)

    def doProgressSegmentTask(self, segmentLength, done, total, javascript):
        script = "app.doProgressSegmentTask({}, {}, {}, '{}');".format(
            segmentLength, done, total, javascript)
        self.eval_javascript(script)
        # Ensure the script execute success.
        time.sleep(1)

    def doProgressSubTask(self, index, limit, javascript):
        script = "app.doProgressSubTask({}, {}, '{}');".format(
            index, limit, javascript)
        self.eval_javascript(script)
        # Ensure the script execute success.
        time.sleep(1)

    def doProgressTask(self, index, javascript):
        """Sections off a portion of the unused progress bar for execution of
        a subtask. Returns false on cancel.

        """
        script = "app.doProgressTask({}, '{}');".format(index, javascript)
        self.eval_javascript(script)
        # Ensure the script execute success.
        time.sleep(1)

    def eraseCustomOptions(self):
        pass

    def executeAction(self, eventID, descriptor, displayDialogs):
        return self.app.executeAction(eventID, descriptor, displayDialogs)

    @property
    def active_layer(self):
        return self.app.ArtLayer

    def active_layer_set(self):
        return self.app.LayerSets

    @property
    def preferences(self):
        return self.app.Preferences

    def open(self, *args, **kwargs):
        self.app.Open(*args, **kwargs)

    def doJavaScript(self, javascript, Arguments, ExecutionMode):
        self.app.doJavaScript(javascript, Arguments, ExecutionMode)

    def isQuicktimeAvailable(self):
        return self.adobe.IsQuicktimeAvailable()

    def purge(self, index):
        """

        Args:
            index:
                .e.g:
                    0: Clears all caches.
                    1: Clears the clipboard.
                    2: Deletes all history states from the History palette.
                    3: Clears the undo cache.

        Returns:

        """
        self.app.purge(index)

    def refreshFonts(self):
        """Force the font list to get refreshed."""
        return self.eval_javascript("app.refreshFonts();")

    def showColorPicker(self):
        return self.eval_javascript("app.showColorPicker();")

    @staticmethod
    def system(command):
        os.system(command)

    def typeIDToStringID(self, typeID):
        return self.app.typeIDToStringID(typeID)

    def typeIDToCharID(self, typeID):
        return self.app.typeIDToCharID(typeID)

    def updateProgress(self, done, total):
        self.eval_javascript("app.updateProgress({}, {})".format(done, total))
