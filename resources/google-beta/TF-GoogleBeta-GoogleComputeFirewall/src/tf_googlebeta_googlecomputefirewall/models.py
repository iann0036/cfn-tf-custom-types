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
    CreationTimestamp: Optional[str]
    Description: Optional[str]
    DestinationRanges: Optional[Sequence[str]]
    Direction: Optional[str]
    Disabled: Optional[bool]
    EnableLogging: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    Network: Optional[str]
    Priority: Optional[float]
    Project: Optional[str]
    SelfLink: Optional[str]
    SourceRanges: Optional[Sequence[str]]
    SourceServiceAccounts: Optional[Sequence[str]]
    SourceTags: Optional[Sequence[str]]
    TargetServiceAccounts: Optional[Sequence[str]]
    TargetTags: Optional[Sequence[str]]
    Allow: Optional[Sequence["_AllowDefinition"]]
    Deny: Optional[Sequence["_DenyDefinition"]]
    LogConfig: Optional[Sequence["_LogConfigDefinition"]]
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
            CreationTimestamp=json_data.get("CreationTimestamp"),
            Description=json_data.get("Description"),
            DestinationRanges=json_data.get("DestinationRanges"),
            Direction=json_data.get("Direction"),
            Disabled=json_data.get("Disabled"),
            EnableLogging=json_data.get("EnableLogging"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Network=json_data.get("Network"),
            Priority=json_data.get("Priority"),
            Project=json_data.get("Project"),
            SelfLink=json_data.get("SelfLink"),
            SourceRanges=json_data.get("SourceRanges"),
            SourceServiceAccounts=json_data.get("SourceServiceAccounts"),
            SourceTags=json_data.get("SourceTags"),
            TargetServiceAccounts=json_data.get("TargetServiceAccounts"),
            TargetTags=json_data.get("TargetTags"),
            Allow=deserialize_list(json_data.get("Allow"), AllowDefinition),
            Deny=deserialize_list(json_data.get("Deny"), DenyDefinition),
            LogConfig=deserialize_list(json_data.get("LogConfig"), LogConfigDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AllowDefinition(BaseModel):
    Ports: Optional[Sequence[str]]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AllowDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AllowDefinition"]:
        if not json_data:
            return None
        return cls(
            Ports=json_data.get("Ports"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AllowDefinition = AllowDefinition


@dataclass
class DenyDefinition(BaseModel):
    Ports: Optional[Sequence[str]]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DenyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DenyDefinition"]:
        if not json_data:
            return None
        return cls(
            Ports=json_data.get("Ports"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DenyDefinition = DenyDefinition


@dataclass
class LogConfigDefinition(BaseModel):
    Metadata: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LogConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Metadata=json_data.get("Metadata"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogConfigDefinition = LogConfigDefinition


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


