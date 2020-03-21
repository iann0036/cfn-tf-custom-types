# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
from typing import (
    AbstractSet,
    Any,
    Generic,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
)

from cloudformation_cli_python_lib.interface import (
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

T = TypeVar("T")


def set_or_none(value: Optional[Sequence[T]]) -> Optional[AbstractSet[T]]:
    if value:
        return set(value)
    return None


@dataclass
class ResourceHandlerRequest(BaseResourceHandlerRequest):
    # pylint: disable=invalid-name
    desiredResourceState: Optional["ResourceModel"]
    previousResourceState: Optional["ResourceModel"]


@dataclass
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    DisplayName: Optional[str]
    IsInternal: Optional[bool]
    Name: Optional[str]
    Period: Optional[str]
    Project: Optional[str]
    SelectedRegions: Optional[Sequence[str]]
    Timeout: Optional[str]
    UptimeCheckId: Optional[str]
    ContentMatchers: Optional[Sequence["_ContentMatchers"]]
    HttpCheck: Optional[Sequence["_HttpCheck"]]
    InternalCheckers: Optional[Sequence["_InternalCheckers"]]
    MonitoredResource: Optional[Sequence["_MonitoredResource"]]
    ResourceGroup: Optional[Sequence["_ResourceGroup"]]
    TcpCheck: Optional[Sequence["_TcpCheck"]]
    Timeouts: Optional["_Timeouts"]
    AuthInfo: Optional[Sequence["_AuthInfo"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DisplayName=json_data.get("DisplayName"),
            IsInternal=json_data.get("IsInternal"),
            Name=json_data.get("Name"),
            Period=json_data.get("Period"),
            Project=json_data.get("Project"),
            SelectedRegions=json_data.get("SelectedRegions"),
            Timeout=json_data.get("Timeout"),
            UptimeCheckId=json_data.get("UptimeCheckId"),
            ContentMatchers=json_data.get("ContentMatchers"),
            HttpCheck=json_data.get("HttpCheck"),
            InternalCheckers=json_data.get("InternalCheckers"),
            MonitoredResource=json_data.get("MonitoredResource"),
            ResourceGroup=json_data.get("ResourceGroup"),
            TcpCheck=json_data.get("TcpCheck"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            AuthInfo=json_data.get("AuthInfo"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ContentMatchers:
    Content: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ContentMatchers"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContentMatchers"]:
        if not json_data:
            return None
        return cls(
            Content=json_data.get("Content"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContentMatchers = ContentMatchers


@dataclass
class HttpCheck:
    Headers: Optional[Sequence["_Headers"]]
    MaskHeaders: Optional[bool]
    Path: Optional[str]
    Port: Optional[float]
    UseSsl: Optional[bool]
    ValidateSsl: Optional[bool]
    AuthInfo: Optional[Sequence["_AuthInfo"]]

    @classmethod
    def _deserialize(
        cls: Type["_HttpCheck"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpCheck"]:
        if not json_data:
            return None
        return cls(
            Headers=json_data.get("Headers"),
            MaskHeaders=json_data.get("MaskHeaders"),
            Path=json_data.get("Path"),
            Port=json_data.get("Port"),
            UseSsl=json_data.get("UseSsl"),
            ValidateSsl=json_data.get("ValidateSsl"),
            AuthInfo=json_data.get("AuthInfo"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpCheck = HttpCheck


@dataclass
class Headers:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Headers"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Headers"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Headers = Headers


@dataclass
class AuthInfo:
    Password: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthInfo"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthInfo = AuthInfo


@dataclass
class InternalCheckers:
    DisplayName: Optional[str]
    GcpZone: Optional[str]
    Name: Optional[str]
    Network: Optional[str]
    PeerProjectId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InternalCheckers"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InternalCheckers"]:
        if not json_data:
            return None
        return cls(
            DisplayName=json_data.get("DisplayName"),
            GcpZone=json_data.get("GcpZone"),
            Name=json_data.get("Name"),
            Network=json_data.get("Network"),
            PeerProjectId=json_data.get("PeerProjectId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InternalCheckers = InternalCheckers


@dataclass
class MonitoredResource:
    Labels: Optional[Sequence["_Labels"]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MonitoredResource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MonitoredResource"]:
        if not json_data:
            return None
        return cls(
            Labels=json_data.get("Labels"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MonitoredResource = MonitoredResource


@dataclass
class Labels:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Labels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Labels"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Labels = Labels


@dataclass
class ResourceGroup:
    GroupId: Optional[str]
    ResourceType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceGroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceGroup"]:
        if not json_data:
            return None
        return cls(
            GroupId=json_data.get("GroupId"),
            ResourceType=json_data.get("ResourceType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceGroup = ResourceGroup


@dataclass
class TcpCheck:
    Port: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TcpCheck"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TcpCheck"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TcpCheck = TcpCheck


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


