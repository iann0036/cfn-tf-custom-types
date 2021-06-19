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
    ChangeTime: Optional[str]
    CreateTime: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Labels: Optional[Sequence[str]]
    LocationName: Optional[str]
    Name: Optional[str]
    Network: Optional[Sequence["_NetworkDefinition"]]
    Private: Optional[bool]
    Status: Optional[str]
    RulesV4In: Optional[Sequence["_RulesV4InDefinition"]]
    RulesV4Out: Optional[Sequence["_RulesV4OutDefinition"]]
    RulesV6In: Optional[Sequence["_RulesV6InDefinition"]]
    RulesV6Out: Optional[Sequence["_RulesV6OutDefinition"]]
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
            ChangeTime=json_data.get("ChangeTime"),
            CreateTime=json_data.get("CreateTime"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Labels=json_data.get("Labels"),
            LocationName=json_data.get("LocationName"),
            Name=json_data.get("Name"),
            Network=deserialize_list(json_data.get("Network"), NetworkDefinition),
            Private=json_data.get("Private"),
            Status=json_data.get("Status"),
            RulesV4In=deserialize_list(json_data.get("RulesV4In"), RulesV4InDefinition),
            RulesV4Out=deserialize_list(json_data.get("RulesV4Out"), RulesV4OutDefinition),
            RulesV6In=deserialize_list(json_data.get("RulesV6In"), RulesV6InDefinition),
            RulesV6Out=deserialize_list(json_data.get("RulesV6Out"), RulesV6OutDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class NetworkDefinition(BaseModel):
    CreateTime: Optional[str]
    NetworkName: Optional[str]
    NetworkUuid: Optional[str]
    ObjectName: Optional[str]
    ObjectUuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            CreateTime=json_data.get("CreateTime"),
            NetworkName=json_data.get("NetworkName"),
            NetworkUuid=json_data.get("NetworkUuid"),
            ObjectName=json_data.get("ObjectName"),
            ObjectUuid=json_data.get("ObjectUuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkDefinition = NetworkDefinition


@dataclass
class RulesV4InDefinition(BaseModel):
    Action: Optional[str]
    Comment: Optional[str]
    DstCidr: Optional[str]
    DstPort: Optional[str]
    Order: Optional[float]
    Protocol: Optional[str]
    SrcCidr: Optional[str]
    SrcPort: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RulesV4InDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RulesV4InDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Comment=json_data.get("Comment"),
            DstCidr=json_data.get("DstCidr"),
            DstPort=json_data.get("DstPort"),
            Order=json_data.get("Order"),
            Protocol=json_data.get("Protocol"),
            SrcCidr=json_data.get("SrcCidr"),
            SrcPort=json_data.get("SrcPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RulesV4InDefinition = RulesV4InDefinition


@dataclass
class RulesV4OutDefinition(BaseModel):
    Action: Optional[str]
    Comment: Optional[str]
    DstCidr: Optional[str]
    DstPort: Optional[str]
    Order: Optional[float]
    Protocol: Optional[str]
    SrcCidr: Optional[str]
    SrcPort: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RulesV4OutDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RulesV4OutDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Comment=json_data.get("Comment"),
            DstCidr=json_data.get("DstCidr"),
            DstPort=json_data.get("DstPort"),
            Order=json_data.get("Order"),
            Protocol=json_data.get("Protocol"),
            SrcCidr=json_data.get("SrcCidr"),
            SrcPort=json_data.get("SrcPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RulesV4OutDefinition = RulesV4OutDefinition


@dataclass
class RulesV6InDefinition(BaseModel):
    Action: Optional[str]
    Comment: Optional[str]
    DstCidr: Optional[str]
    DstPort: Optional[str]
    Order: Optional[float]
    Protocol: Optional[str]
    SrcCidr: Optional[str]
    SrcPort: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RulesV6InDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RulesV6InDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Comment=json_data.get("Comment"),
            DstCidr=json_data.get("DstCidr"),
            DstPort=json_data.get("DstPort"),
            Order=json_data.get("Order"),
            Protocol=json_data.get("Protocol"),
            SrcCidr=json_data.get("SrcCidr"),
            SrcPort=json_data.get("SrcPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RulesV6InDefinition = RulesV6InDefinition


@dataclass
class RulesV6OutDefinition(BaseModel):
    Action: Optional[str]
    Comment: Optional[str]
    DstCidr: Optional[str]
    DstPort: Optional[str]
    Order: Optional[float]
    Protocol: Optional[str]
    SrcCidr: Optional[str]
    SrcPort: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RulesV6OutDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RulesV6OutDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Comment=json_data.get("Comment"),
            DstCidr=json_data.get("DstCidr"),
            DstPort=json_data.get("DstPort"),
            Order=json_data.get("Order"),
            Protocol=json_data.get("Protocol"),
            SrcCidr=json_data.get("SrcCidr"),
            SrcPort=json_data.get("SrcPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RulesV6OutDefinition = RulesV6OutDefinition


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


