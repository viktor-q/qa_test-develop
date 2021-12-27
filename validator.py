#!/usr/bin/python


from zero_cm import ZCM, LogFile, LogEvent
import sys, os


blddir = os.path.dirname(os.path.realpath(__file__)) + "/../../build/examples/examples/"
sys.path.insert(0, blddir + "types/")

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/zcm_types/py/")


from zcm_types.py.ZcmOrientusAccuracy import ZcmOrientusAccuracy
from zcm_types.py.ZcmOrientusFilterStatus import ZcmOrientusFilterStatus
from zcm_types.py.ZcmOrientusNavGw import ZcmOrientusNavGw
from zcm_types.py.ZcmOrientusOrientation import ZcmOrientusOrientation
from zcm_types.py.ZcmOrientusSystemStatus import ZcmOrientusSystemStatus
from zcm_types.py.ZcmOrientusVelocity import ZcmOrientusVelocity
from zcm_types.py.ZcmService import ZcmService


log = LogFile("imu_orientus.zcm", "r")

system_status = {"False": 0, "True": 0}
filter_status = {"False": 0, "True": 0}
accuracy_status = {"BAD": 0, "OK": 0}
orient_status = {"BAD": 0, "OK": 0}
velocity_status = {"BAD": 0, "OK": 0}

while True:
    evt = log.readNextEvent()
    if not evt:
        print("log was ended")
        break
    decoded = ZcmOrientusNavGw().decode(evt.getData())

    # check orientus system status
    checklist_system_status = [
        decoded.orientusSystemStatus.systemFailure,
        decoded.orientusSystemStatus.accelerometerSensorFailure,
        decoded.orientusSystemStatus.gyroscopeSensorFailure,
        decoded.orientusSystemStatus.magnetometerSensorFailure,
        decoded.orientusSystemStatus.accelerometerOverRange,
        decoded.orientusSystemStatus.gyroscopeOverRange,
        decoded.orientusSystemStatus.magnetometerOverRange,
        decoded.orientusSystemStatus.minimumTemperatureAlarm,
        decoded.orientusSystemStatus.maximumTemperatureAlarm,
        decoded.orientusSystemStatus.lowVoltageAlarm,
        decoded.orientusSystemStatus.highVoltageAlarm,
        decoded.orientusSystemStatus.dataOutputOverflowAlarm,
    ]
    for slot in checklist_system_status:
        zcm_system_status = checklist_system_status[slot]
        if zcm_system_status == False:
            system_status["False"] += 1
        if zcm_system_status == True:
            system_status["True"] += 1

    # check orientus velocity
    orient_x = decoded.orientusVelocity.acceleration_X
    orient_y = decoded.orientusVelocity.acceleration_Y
    orient_z = decoded.orientusVelocity.acceleration_Z
    velocity = abs(orient_x + orient_y + orient_z)

    # check orientus filter status
    checklist_filter_status = [
        decoded.orientusFilterStatus.orientationFilterInitialised,
        decoded.orientusFilterStatus.headingInitialised,
        decoded.orientusFilterStatus.magnetometersEnabled,
        decoded.orientusFilterStatus.velocityHeadingEnabled,
        decoded.orientusFilterStatus.externalPositionActive,
        decoded.orientusFilterStatus.externalVelocityActive,
        decoded.orientusFilterStatus.externalHeadingActive,
    ]
    for slots in checklist_filter_status:
        zcm_filter_status = checklist_filter_status[slots]
        if zcm_filter_status == False:
            filter_status["False"] += 1
        if zcm_filter_status == True:
            filter_status["True"] += 1

    # check orientus accuracy
    rph = [
        decoded.orientusAccuracy.stdRoll,
        decoded.orientusAccuracy.stdPitch,
        decoded.orientusAccuracy.stdHeading,
    ]
    for elem in range(3):
        checklist_accuracy_rph = rph[elem]
        if checklist_accuracy_rph <= 3.1415926:
            accuracy_status["OK"] += 1
        else:
            accuracy_status["BAD"] += 1

    stdqx = [
        decoded.orientusAccuracy.stdQ0,
        decoded.orientusAccuracy.stdQ1,
        decoded.orientusAccuracy.stdQ2,
        decoded.orientusAccuracy.stdQ3,
    ]
    for std in range(4):
        checklist_accuracy_stdQ0 = stdqx[std]
        if checklist_accuracy_stdQ0 <= 1:
            accuracy_status["OK"] += 1
        else:
            accuracy_status["BAD"] += 1

    # check orientus orientation
    rph_orient = [
        decoded.orientusOrientation.roll,
        decoded.orientusOrientation.pitch,
        decoded.orientusOrientation.heading,
    ]
    for elem_orient in range(3):
        checklist_orient_rph = rph_orient[elem_orient]
        if checklist_orient_rph <= 3.1415926:
            orient_status["OK"] += 1
        else:
            orient_status["BAD"] += 1

    qx = [
        decoded.orientusOrientation.q0,
        decoded.orientusOrientation.q1,
        decoded.orientusOrientation.q2,
        decoded.orientusOrientation.q3,
    ]
    for param_q in range(4):
        checklist_orientation_q = qx[param_q]
        if checklist_orientation_q <= 1:
            orient_status["OK"] += 1
        else:
            orient_status["BAD"] += 1

    # check orientus velocity
    velo = [
        decoded.orientusVelocity.angularVelocity_X,
        decoded.orientusVelocity.angularVelocity_Y,
        decoded.orientusVelocity.angularVelocity_Z,
        decoded.orientusVelocity.acceleration_X,
        decoded.orientusVelocity.acceleration_Y,
        decoded.orientusVelocity.angularAcceleration_X,
        decoded.orientusVelocity.angularAcceleration_Y,
        decoded.orientusVelocity.angularAcceleration_Z,
    ]
    for velo_x in range(8):
        checklist_velocity = velo[velo_x]
        if checklist_velocity < abs(1):
            velocity_status["OK"] += 1
        else:
            velocity_status["BAD"] += 1

    velo_accel_z = decoded.orientusVelocity.acceleration_Z
    if velo_accel_z > -9.82 and velo_accel_z < -9.80:
        velocity_status["OK"] += 1
    else:
        velocity_status["BAD"] += 1

# results all tests
print("System status", system_status)
if system_status["True"] == 0:
    print("System status OK")
if system_status["True"] != 0:
    print("System status BAD")

print("Velocity value is", velocity)
if velocity <= 10:
    print("velocity acceleration is OK")
if velocity > 10:
    print("velocity acceleration is BAD")

print("Filter status", filter_status)
if filter_status["False"] != 0:
    print("Filter status BAD")
if filter_status["False"] == 0:
    print("Filter status OK")

print("Accuracy status", accuracy_status)
if accuracy_status["BAD"] != 0:
    print("Accuracy status id BAD")
if accuracy_status["BAD"] == 0:
    print("Accuracy status is OK")

print("Orientation status", orient_status)
if orient_status["BAD"] != 0:
    print("Orientation status id BAD")
if orient_status["BAD"] == 0:
    print("Orientation status is OK")

print("Velocity status", velocity_status)
if velocity_status["BAD"] != 0:
    print("Orientation status id BAD")
if velocity_status["BAD"] == 0:
    print("Orientation status is OK")
