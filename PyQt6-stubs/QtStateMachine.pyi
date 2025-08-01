# The PEP 484 type hints stub file for the QtStateMachine module.
#
# Generated by SIP 6.12.0
#
# Copyright (c) 2025 Riverbank Computing Limited <info@riverbankcomputing.com>
#
# This file is part of PyQt6.
#
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
#
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# info@riverbankcomputing.com.
#
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.

import collections
import collections.abc
import enum
import typing
from typing import Any

from PyQt6 import QtCore, QtGui
from PyQt6.QtCore import pyqtBoundSignal

# Support for QDate, QDateTime and QTime.

# Convenient type aliases.
type PYQT_SIGNAL = QtCore.pyqtSignal | QtCore.pyqtBoundSignal
type PYQT_SLOT = collections.abc.Callable[..., Any] | QtCore.pyqtBoundSignal

class QAbstractState(QtCore.QObject):
    def __init__(self, parent: QState | None = ...) -> None: ...
    def event(self, e: QtCore.QEvent | None) -> bool: ...
    def onExit(self, event: QtCore.QEvent | None) -> None: ...
    def onEntry(self, event: QtCore.QEvent | None) -> None: ...
    exited: typing.ClassVar[QtCore.pyqtSignal]
    entered: typing.ClassVar[QtCore.pyqtSignal]
    activeChanged: typing.ClassVar[QtCore.pyqtSignal]
    def active(self) -> bool: ...
    def machine(self) -> QStateMachine | None: ...
    def parentState(self) -> QState | None: ...

class QAbstractTransition(QtCore.QObject):
    class TransitionType(enum.Enum):
        ExternalTransition = ...
        InternalTransition = ...

    def __init__(self, sourceState: QState | None = ...) -> None: ...
    def event(self, e: QtCore.QEvent | None) -> bool: ...
    def onTransition(self, event: QtCore.QEvent | None) -> None: ...
    def eventTest(self, event: QtCore.QEvent | None) -> bool: ...
    targetStatesChanged: typing.ClassVar[QtCore.pyqtSignal]
    targetStateChanged: typing.ClassVar[QtCore.pyqtSignal]
    triggered: typing.ClassVar[QtCore.pyqtSignal]
    def animations(self) -> list[QtCore.QAbstractAnimation]: ...
    def removeAnimation(
        self, animation: QtCore.QAbstractAnimation | None
    ) -> None: ...
    def addAnimation(
        self, animation: QtCore.QAbstractAnimation | None
    ) -> None: ...
    def machine(self) -> QStateMachine | None: ...
    def setTransitionType(
        self, type: QAbstractTransition.TransitionType
    ) -> None: ...
    def transitionType(self) -> QAbstractTransition.TransitionType: ...
    def setTargetStates(
        self, targets: collections.abc.Iterable[QAbstractState]
    ) -> None: ...
    def targetStates(self) -> list[QAbstractState]: ...
    def setTargetState(self, target: QAbstractState | None) -> None: ...
    def targetState(self) -> QAbstractState | None: ...
    def sourceState(self) -> QState | None: ...

class QEventTransition(QAbstractTransition):
    @typing.overload
    def __init__(self, sourceState: QState | None = ...) -> None: ...
    @typing.overload
    def __init__(
        self,
        object: QtCore.QObject | None,
        type: QtCore.QEvent.Type,
        sourceState: QState | None = ...,
    ) -> None: ...
    def event(self, e: QtCore.QEvent | None) -> bool: ...
    def onTransition(self, event: QtCore.QEvent | None) -> None: ...
    def eventTest(self, event: QtCore.QEvent | None) -> bool: ...
    def setEventType(self, type: QtCore.QEvent.Type) -> None: ...
    def eventType(self) -> QtCore.QEvent.Type: ...
    def setEventSource(self, object: QtCore.QObject | None) -> None: ...
    def eventSource(self) -> QtCore.QObject | None: ...

class QFinalState(QAbstractState):
    def __init__(self, parent: QState | None = ...) -> None: ...
    def event(self, e: QtCore.QEvent | None) -> bool: ...
    def onExit(self, event: QtCore.QEvent | None) -> None: ...
    def onEntry(self, event: QtCore.QEvent | None) -> None: ...

class QHistoryState(QAbstractState):
    class HistoryType(enum.Enum):
        ShallowHistory = ...
        DeepHistory = ...

    @typing.overload
    def __init__(self, parent: QState | None = ...) -> None: ...
    @typing.overload
    def __init__(
        self, type: QHistoryState.HistoryType, parent: QState | None = ...
    ) -> None: ...
    def event(self, e: QtCore.QEvent | None) -> bool: ...
    def onExit(self, event: QtCore.QEvent | None) -> None: ...
    def onEntry(self, event: QtCore.QEvent | None) -> None: ...
    historyTypeChanged: typing.ClassVar[QtCore.pyqtSignal]
    defaultStateChanged: typing.ClassVar[QtCore.pyqtSignal]
    defaultTransitionChanged: typing.ClassVar[QtCore.pyqtSignal]
    def setHistoryType(self, type: QHistoryState.HistoryType) -> None: ...
    def historyType(self) -> QHistoryState.HistoryType: ...
    def setDefaultState(self, state: QAbstractState | None) -> None: ...
    def defaultState(self) -> QAbstractState | None: ...
    def setDefaultTransition(
        self, transition: QAbstractTransition | None
    ) -> None: ...
    def defaultTransition(self) -> QAbstractTransition | None: ...

class QKeyEventTransition(QEventTransition):
    @typing.overload
    def __init__(self, sourceState: QState | None = ...) -> None: ...
    @typing.overload
    def __init__(
        self,
        object: QtCore.QObject | None,
        type: QtCore.QEvent.Type,
        key: int,
        sourceState: QState | None = ...,
    ) -> None: ...
    def eventTest(self, event: QtCore.QEvent | None) -> bool: ...
    def onTransition(self, event: QtCore.QEvent | None) -> None: ...
    def setModifierMask(
        self, modifiers: QtCore.Qt.KeyboardModifier
    ) -> None: ...
    def modifierMask(self) -> QtCore.Qt.KeyboardModifier: ...
    def setKey(self, key: int) -> None: ...
    def key(self) -> int: ...

class QMouseEventTransition(QEventTransition):
    @typing.overload
    def __init__(self, sourceState: QState | None = ...) -> None: ...
    @typing.overload
    def __init__(
        self,
        object: QtCore.QObject | None,
        type: QtCore.QEvent.Type,
        button: QtCore.Qt.MouseButton,
        sourceState: QState | None = ...,
    ) -> None: ...
    def eventTest(self, event: QtCore.QEvent | None) -> bool: ...
    def onTransition(self, event: QtCore.QEvent | None) -> None: ...
    def setHitTestPath(self, path: QtGui.QPainterPath) -> None: ...
    def hitTestPath(self) -> QtGui.QPainterPath: ...
    def setModifierMask(
        self, modifiers: QtCore.Qt.KeyboardModifier
    ) -> None: ...
    def modifierMask(self) -> QtCore.Qt.KeyboardModifier: ...
    def setButton(self, button: QtCore.Qt.MouseButton) -> None: ...
    def button(self) -> QtCore.Qt.MouseButton: ...

class QSignalTransition(QAbstractTransition):
    @typing.overload
    def __init__(self, sourceState: QState | None = ...) -> None: ...
    @typing.overload
    def __init__(
        self, signal: pyqtBoundSignal, sourceState: QState | None = ...
    ) -> None: ...

    signalChanged: typing.ClassVar[QtCore.pyqtSignal]
    senderObjectChanged: typing.ClassVar[QtCore.pyqtSignal]
    def event(self, e: QtCore.QEvent | None) -> bool: ...
    def onTransition(self, event: QtCore.QEvent | None) -> None: ...
    def eventTest(self, event: QtCore.QEvent | None) -> bool: ...
    def setSignal(
        self, signal: QtCore.QByteArray | bytes | bytearray | memoryview
    ) -> None: ...
    def signal(self) -> QtCore.QByteArray: ...
    def setSenderObject(self, sender: QtCore.QObject | None) -> None: ...
    def senderObject(self) -> QtCore.QObject | None: ...

class QState(QAbstractState):
    class RestorePolicy(enum.Enum):
        DontRestoreProperties = ...
        RestoreProperties = ...

    class ChildMode(enum.Enum):
        ExclusiveStates = ...
        ParallelStates = ...

    @typing.overload
    def __init__(self, parent: QState | None = ...) -> None: ...
    @typing.overload
    def __init__(
        self, childMode: QState.ChildMode, parent: QState | None = ...
    ) -> None: ...
    def event(self, e: QtCore.QEvent | None) -> bool: ...
    def onExit(self, event: QtCore.QEvent | None) -> None: ...
    def onEntry(self, event: QtCore.QEvent | None) -> None: ...
    errorStateChanged: typing.ClassVar[QtCore.pyqtSignal]
    initialStateChanged: typing.ClassVar[QtCore.pyqtSignal]
    childModeChanged: typing.ClassVar[QtCore.pyqtSignal]
    propertiesAssigned: typing.ClassVar[QtCore.pyqtSignal]
    finished: typing.ClassVar[QtCore.pyqtSignal]
    def assignProperty(
        self,
        object: QtCore.QObject | None,
        name: str | None,
        value: typing.Any,
    ) -> None: ...
    def setChildMode(self, mode: QState.ChildMode) -> None: ...
    def childMode(self) -> QState.ChildMode: ...
    def setInitialState(self, state: QAbstractState | None) -> None: ...
    def initialState(self) -> QAbstractState | None: ...
    def transitions(self) -> list[QAbstractTransition]: ...
    def removeTransition(
        self, transition: QAbstractTransition | None
    ) -> None: ...
    @typing.overload
    def addTransition(
        self, transition: QAbstractTransition | None
    ) -> None: ...
    @typing.overload
    def addTransition(
        self, signal: pyqtBoundSignal, target: QAbstractState | None
    ) -> QSignalTransition | None: ...
    @typing.overload
    def addTransition(
        self, target: QAbstractState | None
    ) -> QAbstractTransition | None: ...
    def setErrorState(self, state: QAbstractState | None) -> None: ...
    def errorState(self) -> QAbstractState | None: ...

class QStateMachine(QState):
    class Error(enum.Enum):
        NoError = ...
        NoInitialStateError = ...
        NoDefaultStateInHistoryStateError = ...
        NoCommonAncestorForTransitionError = ...
        StateMachineChildModeSetToParallelError = ...

    class EventPriority(enum.Enum):
        NormalPriority = ...
        HighPriority = ...

    class SignalEvent(QtCore.QEvent):
        def arguments(self) -> list[typing.Any]: ...
        def signalIndex(self) -> int: ...
        def sender(self) -> QtCore.QObject | None: ...

    class WrappedEvent(QtCore.QEvent):
        def event(self) -> QtCore.QEvent | None: ...
        def object(self) -> QtCore.QObject | None: ...

    @typing.overload
    def __init__(self, parent: QtCore.QObject | None = ...) -> None: ...
    @typing.overload
    def __init__(
        self, childMode: QState.ChildMode, parent: QtCore.QObject | None = ...
    ) -> None: ...
    def event(self, e: QtCore.QEvent | None) -> bool: ...
    def onExit(self, event: QtCore.QEvent | None) -> None: ...
    def onEntry(self, event: QtCore.QEvent | None) -> None: ...
    runningChanged: typing.ClassVar[QtCore.pyqtSignal]
    stopped: typing.ClassVar[QtCore.pyqtSignal]
    started: typing.ClassVar[QtCore.pyqtSignal]
    def setRunning(self, running: bool) -> None: ...
    def stop(self) -> None: ...
    def start(self) -> None: ...
    def eventFilter(
        self, watched: QtCore.QObject | None, event: QtCore.QEvent | None
    ) -> bool: ...
    def configuration(self) -> set[QAbstractState]: ...
    def cancelDelayedEvent(self, id: int) -> bool: ...
    def postDelayedEvent(
        self, event: QtCore.QEvent | None, delay: int
    ) -> int: ...
    def postEvent(
        self,
        event: QtCore.QEvent | None,
        priority: QStateMachine.EventPriority = ...,
    ) -> None: ...
    def setGlobalRestorePolicy(
        self, restorePolicy: QState.RestorePolicy
    ) -> None: ...
    def globalRestorePolicy(self) -> QState.RestorePolicy: ...
    def removeDefaultAnimation(
        self, animation: QtCore.QAbstractAnimation | None
    ) -> None: ...
    def defaultAnimations(self) -> list[QtCore.QAbstractAnimation]: ...
    def addDefaultAnimation(
        self, animation: QtCore.QAbstractAnimation | None
    ) -> None: ...
    def setAnimated(self, enabled: bool) -> None: ...
    def isAnimated(self) -> bool: ...
    def isRunning(self) -> bool: ...
    def clearError(self) -> None: ...
    def errorString(self) -> str: ...
    def error(self) -> QStateMachine.Error: ...
    def removeState(self, state: QAbstractState | None) -> None: ...
    def addState(self, state: QAbstractState | None) -> None: ...
