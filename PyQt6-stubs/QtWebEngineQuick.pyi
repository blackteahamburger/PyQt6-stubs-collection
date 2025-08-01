# The PEP 484 type hints stub file for the QtWebEngineQuick module.
#
# Generated by SIP 6.10.0
#
# Copyright (c) 2025 Riverbank Computing Limited <info@riverbankcomputing.com>
#
# This file is part of PyQt6-WebEngine.
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

import PyQt6.sip
from PyQt6 import QtCore, QtWebEngineCore

# Support for QDate, QDateTime and QTime.

# Convenient type aliases.
type PYQT_SIGNAL = QtCore.pyqtSignal | QtCore.pyqtBoundSignal
type PYQT_SLOT = collections.abc.Callable[..., Any] | QtCore.pyqtBoundSignal

class QQuickWebEngineProfile(QtCore.QObject):
    class PersistentPermissionsPolicy(enum.Enum):
        AskEveryTime = ...
        StoreInMemory = ...
        StoreOnDisk = ...

    class PersistentCookiesPolicy(enum.Enum):
        NoPersistentCookies = ...
        AllowPersistentCookies = ...
        ForcePersistentCookies = ...

    class HttpCacheType(enum.Enum):
        MemoryHttpCache = ...
        DiskHttpCache = ...
        NoCache = ...

    @typing.overload
    def __init__(self, parent: QtCore.QObject | None = ...) -> None: ...
    @typing.overload
    def __init__(
        self, storageName: str | None, parent: QtCore.QObject | None = ...
    ) -> None: ...

    persistentPermissionsPolicyChanged: typing.ClassVar[QtCore.pyqtSignal]
    def listPermissionsForPermissionType(
        self,
        permissionType: QtWebEngineCore.QWebEnginePermission.PermissionType,
    ) -> list[QtWebEngineCore.QWebEnginePermission]: ...
    def listPermissionsForOrigin(
        self, securityOrigin: QtCore.QUrl
    ) -> list[QtWebEngineCore.QWebEnginePermission]: ...
    def listAllPermissions(
        self,
    ) -> list[QtWebEngineCore.QWebEnginePermission]: ...
    def queryPermission(
        self,
        securityOrigin: QtCore.QUrl,
        permissionType: QtWebEngineCore.QWebEnginePermission.PermissionType,
    ) -> QtWebEngineCore.QWebEnginePermission: ...
    def clientHints(self) -> QtWebEngineCore.QWebEngineClientHints | None: ...
    def setPersistentPermissionsPolicy(
        self, a0: QQuickWebEngineProfile.PersistentPermissionsPolicy
    ) -> None: ...
    def persistentPermissionsPolicy(
        self,
    ) -> QQuickWebEngineProfile.PersistentPermissionsPolicy: ...
    clearHttpCacheCompleted: typing.ClassVar[QtCore.pyqtSignal]
    pushServiceEnabledChanged: typing.ClassVar[QtCore.pyqtSignal]
    def setPushServiceEnabled(self, enable: bool) -> None: ...
    def isPushServiceEnabled(self) -> bool: ...
    presentNotification: typing.ClassVar[QtCore.pyqtSignal]
    downloadPathChanged: typing.ClassVar[QtCore.pyqtSignal]
    def clientCertificateStore(
        self,
    ) -> QtWebEngineCore.QWebEngineClientCertificateStore | None: ...
    def setDownloadPath(self, path: str | None) -> None: ...
    def downloadPath(self) -> str: ...
    spellCheckEnabledChanged: typing.ClassVar[QtCore.pyqtSignal]
    spellCheckLanguagesChanged: typing.ClassVar[QtCore.pyqtSignal]
    def isSpellCheckEnabled(self) -> bool: ...
    def setSpellCheckEnabled(self, enabled: bool) -> None: ...
    def spellCheckLanguages(self) -> list[str]: ...
    def setSpellCheckLanguages(
        self, languages: collections.abc.Iterable[str | None]
    ) -> None: ...
    httpAcceptLanguageChanged: typing.ClassVar[QtCore.pyqtSignal]
    httpCacheMaximumSizeChanged: typing.ClassVar[QtCore.pyqtSignal]
    persistentCookiesPolicyChanged: typing.ClassVar[QtCore.pyqtSignal]
    httpCacheTypeChanged: typing.ClassVar[QtCore.pyqtSignal]
    httpUserAgentChanged: typing.ClassVar[QtCore.pyqtSignal]
    cachePathChanged: typing.ClassVar[QtCore.pyqtSignal]
    persistentStoragePathChanged: typing.ClassVar[QtCore.pyqtSignal]
    offTheRecordChanged: typing.ClassVar[QtCore.pyqtSignal]
    storageNameChanged: typing.ClassVar[QtCore.pyqtSignal]
    @staticmethod
    def defaultProfile() -> QQuickWebEngineProfile | None: ...
    def clearHttpCache(self) -> None: ...
    def removeAllUrlSchemeHandlers(self) -> None: ...
    def removeUrlSchemeHandler(
        self, a0: QtWebEngineCore.QWebEngineUrlSchemeHandler | None
    ) -> None: ...
    def removeUrlScheme(
        self, scheme: QtCore.QByteArray | bytes | bytearray | memoryview
    ) -> None: ...
    def installUrlSchemeHandler(
        self,
        scheme: QtCore.QByteArray | bytes | bytearray | memoryview,
        a1: QtWebEngineCore.QWebEngineUrlSchemeHandler | None,
    ) -> None: ...
    def urlSchemeHandler(
        self, a0: QtCore.QByteArray | bytes | bytearray | memoryview
    ) -> QtWebEngineCore.QWebEngineUrlSchemeHandler | None: ...
    def setUrlRequestInterceptor(
        self,
        interceptor: QtWebEngineCore.QWebEngineUrlRequestInterceptor | None,
    ) -> None: ...
    def cookieStore(self) -> QtWebEngineCore.QWebEngineCookieStore | None: ...
    def setHttpAcceptLanguage(
        self, httpAcceptLanguage: str | None
    ) -> None: ...
    def httpAcceptLanguage(self) -> str: ...
    def setHttpCacheMaximumSize(self, maxSize: int) -> None: ...
    def httpCacheMaximumSize(self) -> int: ...
    def setPersistentCookiesPolicy(
        self, a0: QQuickWebEngineProfile.PersistentCookiesPolicy
    ) -> None: ...
    def persistentCookiesPolicy(
        self,
    ) -> QQuickWebEngineProfile.PersistentCookiesPolicy: ...
    def setHttpCacheType(
        self, a0: QQuickWebEngineProfile.HttpCacheType
    ) -> None: ...
    def httpCacheType(self) -> QQuickWebEngineProfile.HttpCacheType: ...
    def setHttpUserAgent(self, userAgent: str | None) -> None: ...
    def httpUserAgent(self) -> str: ...
    def setCachePath(self, path: str | None) -> None: ...
    def cachePath(self) -> str: ...
    def setPersistentStoragePath(self, path: str | None) -> None: ...
    def persistentStoragePath(self) -> str: ...
    def setOffTheRecord(self, offTheRecord: bool) -> None: ...
    def isOffTheRecord(self) -> bool: ...
    def setStorageName(self, name: str | None) -> None: ...
    def storageName(self) -> str: ...

class QtWebEngineQuick(PyQt6.sip.simplewrapper):
    def initialize(self) -> None: ...
