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
    AllowAsIn: Optional[bool]
    BgpPath: Optional[str]
    Description: Optional[str]
    DisplayName: Optional[str]
    GracefulRestartMode: Optional[str]
    HoldDownTime: Optional[float]
    Id: Optional[str]
    KeepAliveTime: Optional[float]
    MaximumHopLimit: Optional[float]
    NeighborAddress: Optional[str]
    NsxId: Optional[str]
    Password: Optional[str]
    Path: Optional[str]
    RemoteAsNum: Optional[str]
    Revision: Optional[float]
    SourceAddresses: Optional[Sequence[str]]
    BfdConfig: Optional[Sequence["_BfdConfigDefinition"]]
    RouteFiltering: Optional[Sequence["_RouteFilteringDefinition"]]
    Tag: Optional[Sequence["_TagDefinition"]]

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
            AllowAsIn=json_data.get("AllowAsIn"),
            BgpPath=json_data.get("BgpPath"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            GracefulRestartMode=json_data.get("GracefulRestartMode"),
            HoldDownTime=json_data.get("HoldDownTime"),
            Id=json_data.get("Id"),
            KeepAliveTime=json_data.get("KeepAliveTime"),
            MaximumHopLimit=json_data.get("MaximumHopLimit"),
            NeighborAddress=json_data.get("NeighborAddress"),
            NsxId=json_data.get("NsxId"),
            Password=json_data.get("Password"),
            Path=json_data.get("Path"),
            RemoteAsNum=json_data.get("RemoteAsNum"),
            Revision=json_data.get("Revision"),
            SourceAddresses=json_data.get("SourceAddresses"),
            BfdConfig=deserialize_list(json_data.get("BfdConfig"), BfdConfigDefinition),
            RouteFiltering=deserialize_list(json_data.get("RouteFiltering"), RouteFilteringDefinition),
            Tag=deserialize_list(json_data.get("Tag"), TagDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BfdConfigDefinition(BaseModel):
    Enabled: Optional[bool]
    Interval: Optional[float]
    Multiple: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_BfdConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BfdConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Interval=json_data.get("Interval"),
            Multiple=json_data.get("Multiple"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BfdConfigDefinition = BfdConfigDefinition


@dataclass
class RouteFilteringDefinition(BaseModel):
    AddressFamily: Optional[str]
    Enabled: Optional[bool]
    InRouteFilter: Optional[str]
    MaximumRoutes: Optional[float]
    OutRouteFilter: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RouteFilteringDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RouteFilteringDefinition"]:
        if not json_data:
            return None
        return cls(
            AddressFamily=json_data.get("AddressFamily"),
            Enabled=json_data.get("Enabled"),
            InRouteFilter=json_data.get("InRouteFilter"),
            MaximumRoutes=json_data.get("MaximumRoutes"),
            OutRouteFilter=json_data.get("OutRouteFilter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RouteFilteringDefinition = RouteFilteringDefinition


@dataclass
class TagDefinition(BaseModel):
    Scope: Optional[str]
    Tag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagDefinition"]:
        if not json_data:
            return None
        return cls(
            Scope=json_data.get("Scope"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagDefinition = TagDefinition


