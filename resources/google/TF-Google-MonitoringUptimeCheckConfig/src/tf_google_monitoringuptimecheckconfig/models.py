# DO NOT modify this file by hand, changes will be overwritten
import sys
from dataclasses import dataclass
from inspect import getmembers, isclass
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
    BaseModel,
    BaseResourceHandlerRequest,
)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

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
class ResourceModel(BaseModel):
    tfcfnid: Optional[str]
    DisplayName: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Period: Optional[str]
    Project: Optional[str]
    SelectedRegions: Optional[Sequence[str]]
    Timeout: Optional[str]
    UptimeCheckId: Optional[str]
    ContentMatchers: Optional[Sequence["_ContentMatchersDefinition"]]
    HttpCheck: Optional[Sequence["_HttpCheckDefinition"]]
    MonitoredResource: Optional[Sequence["_MonitoredResourceDefinition"]]
    ResourceGroup: Optional[Sequence["_ResourceGroupDefinition"]]
    TcpCheck: Optional[Sequence["_TcpCheckDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Period=json_data.get("Period"),
            Project=json_data.get("Project"),
            SelectedRegions=json_data.get("SelectedRegions"),
            Timeout=json_data.get("Timeout"),
            UptimeCheckId=json_data.get("UptimeCheckId"),
            ContentMatchers=deserialize_list(json_data.get("ContentMatchers"), ContentMatchersDefinition),
            HttpCheck=deserialize_list(json_data.get("HttpCheck"), HttpCheckDefinition),
            MonitoredResource=deserialize_list(json_data.get("MonitoredResource"), MonitoredResourceDefinition),
            ResourceGroup=deserialize_list(json_data.get("ResourceGroup"), ResourceGroupDefinition),
            TcpCheck=deserialize_list(json_data.get("TcpCheck"), TcpCheckDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ContentMatchersDefinition(BaseModel):
    Content: Optional[str]
    Matcher: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ContentMatchersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContentMatchersDefinition"]:
        if not json_data:
            return None
        return cls(
            Content=json_data.get("Content"),
            Matcher=json_data.get("Matcher"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContentMatchersDefinition = ContentMatchersDefinition


@dataclass
class HttpCheckDefinition(BaseModel):
    Body: Optional[str]
    ContentType: Optional[str]
    Headers: Optional[Sequence["_HeadersDefinition"]]
    MaskHeaders: Optional[bool]
    Path: Optional[str]
    Port: Optional[float]
    RequestMethod: Optional[str]
    UseSsl: Optional[bool]
    ValidateSsl: Optional[bool]
    AuthInfo: Optional[Sequence["_AuthInfoDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HttpCheckDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpCheckDefinition"]:
        if not json_data:
            return None
        return cls(
            Body=json_data.get("Body"),
            ContentType=json_data.get("ContentType"),
            Headers=deserialize_list(json_data.get("Headers"), HeadersDefinition),
            MaskHeaders=json_data.get("MaskHeaders"),
            Path=json_data.get("Path"),
            Port=json_data.get("Port"),
            RequestMethod=json_data.get("RequestMethod"),
            UseSsl=json_data.get("UseSsl"),
            ValidateSsl=json_data.get("ValidateSsl"),
            AuthInfo=deserialize_list(json_data.get("AuthInfo"), AuthInfoDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpCheckDefinition = HttpCheckDefinition


@dataclass
class HeadersDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeadersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeadersDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeadersDefinition = HeadersDefinition


@dataclass
class AuthInfoDefinition(BaseModel):
    Password: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthInfoDefinition = AuthInfoDefinition


@dataclass
class MonitoredResourceDefinition(BaseModel):
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MonitoredResourceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MonitoredResourceDefinition"]:
        if not json_data:
            return None
        return cls(
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MonitoredResourceDefinition = MonitoredResourceDefinition


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class ResourceGroupDefinition(BaseModel):
    GroupId: Optional[str]
    ResourceType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceGroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceGroupDefinition"]:
        if not json_data:
            return None
        return cls(
            GroupId=json_data.get("GroupId"),
            ResourceType=json_data.get("ResourceType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceGroupDefinition = ResourceGroupDefinition


@dataclass
class TcpCheckDefinition(BaseModel):
    Port: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TcpCheckDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TcpCheckDefinition"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TcpCheckDefinition = TcpCheckDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


