################################################################################
#
# iannix.py     Version 1.0     20-June-2016    Seth Stoudenmier and Bill Manaris
#
################################################################################
#
# DESCRIPTION:
#
# Inherits OSC.py and works as the inbetween for jythonMusic and Iannix. Allows
# for messages to be received from and sent to Iannix through Open Sound Control.
#
################################################################################
#
# REVISIONS:
#
#   1.0     (ss, bm) Initial planning and implementation.
#
################################################################################

from osc import *


# IannixIn(port) - waits for incoming messages on this port from one (or more) Iannix installation.
#
# Once an IannixIn object has been created, e.g.,
#
# iannixIn = IannixIn(57110)
#

class IannixIn(OscIn):

    def __init__(self, port=57110):
        # initialize the OscIn port that is used by IannixIn
        OscIn.__init__(self, port)
        # dictionaries that will contain the functions that are passed value whenever
        # the corresponding OscIn address comes from Iannix
        self.transportFunctions = {"play":[], "stop":[], "fastrewind":[]}
        self.cursorFunctions = {}
        self.triggerFunctions = {}
        # functions that take in the osc messages are declared in the constructor because
        # they are only able to received one parameter, the message from the OscIn.onInput(),
        # however they need to be able to see the dictionaries that contain the functions
        # declared by the onTrigger, onCursor, and onTransport methods
        def handleTransportMessage(message):
            args = message.getArguments()
            # values taken from the OscIn "/transport" address from Iannix
            state = args[0]
            timeStamp = float(args[1])
            # calling functions depending on which state is sent
            for function in self.transportFunctions[state]:
                function(timeStamp)

        def handleCursorMessage(message):
            args = message.getArguments()
            # values taken from OscIn "/cursor" address from Iannix
            cursorID = args[0]
            x = args[5]
            y = args[6]
            z = args[7]
            # calling functions depending on which cursor id is sent
            for function in self.cursorFunctions[cursorID]:
                function(x, y, z)

        def handleTriggerMessage(message):
            args = message.getArguments()
            # values taken from OscIn "/trigger" address from Iannix
            triggerID = args[0]
            x = args[5]
            y = args[6]
            z = args[7]
            # calling functions depending on which trigger id is sent
            for function in self.triggerFunctions[triggerID]:
                function(x, y, z)
        # OscIn addresses from Iannix that are listened for
        self.onInput("/transport", handleTransportMessage)
        self.onInput("/cursor", handleCursorMessage)
        self.onInput("/trigger", handleTriggerMessage)

    '''
    Adds the provided function to a list of functions that are called when the correct
    message is received from Iannix.
    @param: triggerID - trigger ID that is being listened for
             function - function that receives the arguments passed by the trigger;
                         should expect 3 arguments (x, y, z)
    '''
    def onTrigger(self, triggerID, function):
        if triggerID in self.triggerFunctions.keys():
            self.triggerFunctions[triggerID].append(function)
        else:
            self.triggerFunctions[triggerID] = [function]

    '''
    Adds the provided function to a list of functions that are called when the correct
    message is received from Iannix.
    @param: cursorID - cursor ID that is being listened for
            function - function that receives the arguments passed by the cursor;
                        should expect 3 arguments (x, y, z)
    '''
    def onCursor(self, cursorID, function):
        if cursorID in self.cursorFunctions.keys():
            self.cursorFunctions[cursorID].append(function)
        else:
            self.cursorFunctions[cursorID] = [function]

    '''
    Adds the provided function to a list of functions that are called when the correct
    message is received from Iannix.
    @param: function - function that receives the argument passed by the play button;
                        should expect one argument, an int representing the current
                        time (e.g. 1 min, 12 sec, and 813 ms = 72.813)
    '''
    def onPlay(self, function):
        self.transportFunctions["play"].append(function)

    '''
    Adds the provided function to a list of functions that are called when the correct
    message is received from Iannix.
    @param: function - function that receives the argument passed by the stop button;
                        should expect one argument, an int representing the current
                        time (e.g. 1 min, 12 sec, and 813 ms = 72.813)
    '''
    def onStop(self, function):
        self.transportFunctions["stop"].append(function)

    '''
    Adds the provided function to a list of functions that are called when the correct
    message is received from Iannix.
    @param: function - function that receives the argument passed by the fast rewind button;
                        should expect one argument, an int representing the current
                        time (e.g. 1 min, 12 sec, and 813 ms = 72.813)
    '''
    def onFastRewind(self, function):
        self.transportFunctions["fastrewind"].append(function)


# IannixOut(IPaddress, port) - send out messages to a particular Iannix installation.
# NOTE:  There can be several IannixOut objects, if you wish to communicate with several Iannix installations.
#
# Once an IannixOut object has been created, e.g.,
#
# iannixOut = IannixOut(“xxx.xxx.xxx.xxx”, 57111)
#
class IannixOut(OscOut):

    def __init__(self, ipAddress=127.0.0.1, port=57111):

        # initialize the OscOut IP Address and Port used by Iannix
        OscOut.__init__(self, ipAddress, port)
        # dictionary to keep count of what the next point ID should be;
        # <curveID> : <pointIDCounter>
        self.curvePointsID = {}
        # dictionary to keep track of what ids are in use and what each id is;
        # <objectID> : <type of object (e.g. "curve", "trigger", "cursor")
        self.objectIDs = {}

    '''
    Adds a point to the Iannix score at the provided coordinates. The Bezier points are used
    to create a quadratic Bezier curve between itself and the previous point on the curve.
    @param:       curveID - the Iannix object ID for a curve that the point should be
                             added to
                  x, y, z - coordinates of the point in 3D space
            cx1, cy1, cz1 - coordinates for the first quadratic Bezier point
            cx2, cy2, cz2 - coordinates for the second quadratic Bezier point
    '''
    def addPointToCurve(self, curveID, x, y, z, cx1=0, cy1=0, cz1=0, cx2=0, cy2=0, cz2=0):
        # makes sure that the curve id exists
        if curveID not in self.objectIDs:
            raise ValueError("ID value", curveID, "does not exist.")
        # OSC messages to add a point to the curve
        self.sendMessage("/iannix/setPointAt", curveID, self.curvePointsID[curveID], x, y, z,
                        c1x, c1y, c1z, c2x, c2y, c2z)
        # increment the point id counter used for the curve
        self.curvePointsID[curveID]+= 1


    '''
    Adds a list of points to a curve in the Iannix score. List of points are in the format
    such that [(x1, y1, z1), (x2, y2, z2), ..., (xn, yn, zn)]. This is also true for the control
    points. (Note: Length of listControlPoints1 and 2 should either be equal to the length of
    listPoints or they should be equal to None.)
    @param:            curveID - the Iannix ojbect ID for a curve that the point should be
                                  added to
                    listPoints - list of (x, y, z) ordered pairs that will make up
                                  multiple points to be added to the curve
            listControlPoints1 - list of (cx1, cy1, cz1) ordered pairs that will make up
                                  multiple control points to be added to the curve
            listControlPoints2 - list of (cx2, cy2, cz2) ordered pairs that will make up
                                  multiple control points to be added to the curve
    '''
    def addPointListToCurve(self, curveID, listPoints, listControlPoints1=None, listControlPoints2=None):
        # makes sure that the curve id exists
        if curveID not in self.objectIDs:
            raise ValueError("ID value", curveID, "does not exist.")
        # creates lists of 0s if the listControlPoints are not used
        if listControlPoints1 == None and listControlPoints2 == None:
            listControlPoints1 = [(0, 0, 0)] * len(listPoints)
            listControlPoints2 = [(0, 0, 0)] * len(listPoints)
        # make sure that all of the lists are the same Length
        if len(listPoints) != len(listControl1Points) != len(listControl2Points):
            raise ValueError("List lengths do no match.")
        # OSC messages in a for loop that add multiple points to a curve
        for i in len(listPoints):
            x, y, z = point[0], point[1], point[2]
            c1x, c1y, c1z = listControlPoints1[0], listControlPoints1[1], listControlPoints1[2]
            c2x, c2y, c2z = listControlPoints2[0], listControlPoints2[1], listControlPoints2[2]
            self.sendMessage("/iannix/setPointAt", curveID, self.curvePointsID[curveID], x, y, z,
                            c1x, c1y, c1z, c2x, c2y, c2z)
            # increment the point id counter used for the curve
            self.curvePointsID[curveID]+= 1

    '''
    Adds a curve to the provided coordiantes. A curve is created without any points and
    any points will need to be declared.
    @param: curveID - object ID used to define the curve in Iannix
            x, y, z - coordinates where the curve will be added
    '''
    def addCurve(self, curveID, x, y, z):
        # makes sure that the curve id does not already exist
        if curveID in self.objectIDs:
            raise ValueError("ID value", curveID, "is currently taken.")
        # OSC messages needed to create a curve
        self.sendMessage("/iannix/add", "curve", curveID)
        self.sendMessage("/iannix/setpos", curveID, x, y, z)
        self.curvePointsID[curveID] = 0
        self.objectIDs[curveID] = "curve"

    '''
    Removes a curve with the provided curve ID.
    @param: curveID - object ID of an Iannix curve that will be removed
    '''
    def removeCurve(self, curveID):
        # make sure the ID exists
        if curveID not in self.objectIDs:
            raise ValueError("ID value", curveID, "does not exist.")
        # make sure that the ID is for a curve
        if self.objectIDs[curveID] != "curve":
            raise ValueError("ID value", curveID, "is not the ID of a curve.")
        # remove the curve
        self.sendMessage("/iannix/remove", curveID)
        # remove the curve from the list of object IDs in use
        del self.objectIDs[curveID]
        # remove the curve from the list of curve : point ids in use
        del self.curvePointsID[curveID]

    '''
    Adds a trigger to the provided coordinates.
    @param: triggerID - object ID used to define the trigger in Iannix
              x, y, z - coordinates where the trigger will be added
    '''
    def addTrigger(self, triggerID, x, y, z):
        # makes sure that the trigger id does not already exist
        if triggerID in self.objectIDs:
            raise ValueError("ID value", triggerID, "is currently taken.")
        # OSC messages needed to create a trigger
        self.sendMessage("/iannix/add", "trigger", triggerID)
        self.sendMessage("/iannix/setpos", triggerID, x, y, z)
        # adds the trigger to the dictionary of object ids
        self.objectIDs[triggerID] = "trigger"

    '''
    Removes a trigger with the provided trigger ID
    @param: triggerID - object ID of an Iannix trigger that will be removed
    '''
    def removeTrigger(self, triggerID):
        # make sure the ID exists
        if triggerID not in self.objectIDs:
            raise ValueError("ID value", triggerID, "does not exist.")
        # make sure that the ID is for a trigger
        if self.objectIDs[triggerID] != "trigger":
            raise ValueError("ID value", triggerID, "is not the ID of a trigger.")
        # remove the trigger
        self.sendMessage("/iannix/remove", triggerID)
        # remove the trigger from the list of object IDs in use
        del self.objectIDs[triggerID]

    '''
    Adds a cursor to a particular curve with a given offset. The offset is how many
    seconds from the start of the curve that the cursor should be placed.
    @param:  curveID - curve that the cursor should be placed on
            cursorID - Iannix object ID for a cursor
              offset - seconds from the beginning of a curve that the cursor should
                        be placed
    '''
    def addCursor(self, curveID, cursorID, offset=0):
        # make sure that the cursorID provided does not exist already
        if cursorID in self.objectIDs:
            raise ValueError("ID value", cursorID, "is currently taken.")
        # make sure that the curveID provided exists
        if curveID not in self.objectIDs:
            raise ValueError("ID value", curveID, "does not exist.")
        # make sure that the curveID provided is for a curve
        if self.objectIDs[curveID] != "curve":
            raise ValueError("ID value", curveID, "is not the ID of a curve.")
        # adds a cursor to a curve
        self.sendMessage("/iannix/add", "cursor", cursorID)
        self.sendMessage("/iannix/setcurve", cursorID, curveID)

    '''
    Removes a cursor with the provided cursor ID.
    @param: cursorID - object ID of an Iannix cursor that will be removed
    '''
    def removeCursor(self, cursorID):
        # make sure the ID exists
        if cursorID not in self.objectIDs:
            raise ValueError("ID value", cursorID, "is not a valid ID.")
        # make sure that the ID is for a cursor
        if self.objectIDs[cursorID] != "cursor":
            raise ValueError("ID value", cursorID, "is not the ID of a cursor.")
        # remove the cursor
        self.sendMessage("/iannix/remove", cursorID)
        # remove the cursor from the list of object IDs in use
        del self.objectIDs[cursorID]

    '''
    Clears all objects from the Iannix score.
    '''
    def clear(self):
        self.sendMessage("/iannix/clear")
        self.curvePointsID.clear()
        self.objectIDs.clear()

    '''
    Plays the Iannix score.
    '''
    def play(self):
        self.sendMessage("/iannix/play")

    '''
    Stops the Iannix score.
    '''
    def stop(self):
        self.sendMessage("/iannix/stop")

    '''
    Fast Rewinds the Iannix score.
    '''
    def fastRewind(self):
        self.sendMessage("/iannix/fastrewind")


################################################################################
# Unit Tests
################################################################################
if __name__ == '__main__':

    ############################################################################
    ### IannixIn Unit Tests ####################################################
    ############################################################################

    # define IannixIn object and variables that hold test IDs
    iannixIn = IannixIn(57110)
    triggerID = 3
    cursorID = 2

    ### test for onTrigger functionality #######################################
    def printOnTrigger(x, y, z):
        print("On Trigger Results", x, y, z)

    iannixIn.onTrigger(triggerID, printOnTrigger)

    ### test for onTrigger functionality #######################################
    def printOnCursor(x, y, z):
        print("On Cursor Results", x, y, z)

    iannixIn.onCursor(cursorID, printOnCursor)

    ### test for onPlay functionality ##########################################
    def printOnPlay(time):
        print("On Play Results:", time)

    iannixIn.onPlay(printOnPlay)

    ### test for onStop functionality ##########################################
    def printOnStop(time):
        print("On Stop Results:", time)

    iannixIn.onStop(printOnStop)

    ### test for onFastRewind functionality ####################################
    def printOnFastRewind(time):
        print("On FastRewind Results:", time)

    iannixIn.onFastRewind(printOnFastRewind)
