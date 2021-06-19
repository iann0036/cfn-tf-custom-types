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
    Action: Optional[str]
    Description: Optional[str]
    Direction: Optional[str]
    EnableLogging: Optional[bool]
    Id: Optional[str]
    PolicyId: Optional[str]
    Preview: Optional[bool]
    Priority: Optional[float]
    TargetResources: Optional[Sequence[str]]
    TargetServiceAccounts: Optional[Sequence[str]]
    Match: Optional[Sequence["_MatchDefinition"]]
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
            Action=json_data.get("Action"),
            Description=json_data.get("Description"),
            Direction=json_data.get("Direction"),
            EnableLogging=json_data.get("EnableLogging"),
            Id=json_data.get("Id"),
            PolicyId=json_data.get("PolicyId"),
            Preview=json_data.get("Preview"),
            Priority=json_data.get("Priority"),
            TargetResources=json_data.get("TargetResources"),
            TargetServiceAccounts=json_data.get("TargetServiceAccounts"),
            Match=deserialize_list(json_data.get("Match"), MatchDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MatchDefinition(BaseModel):
    Description: Optional[str]
    VersionedExpr: Optional[str]
    Config: Optional[Sequence["_ConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MatchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            VersionedExpr=json_data.get("VersionedExpr"),
            Config=deserialize_list(json_data.get("Config"), ConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchDefinition = MatchDefinition


@dataclass
class ConfigDefinition(BaseModel):
    DestIpRanges: Optional[Sequence[str]]
    SrcIpRanges: Optional[Sequence[str]]
    Layer4Config: Optional[Sequence["_Layer4ConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            DestIpRanges=json_data.get("DestIpRanges"),
            SrcIpRanges=json_data.get("SrcIpRanges"),
            Layer4Config=deserialize_list(json_data.get("Layer4Config"), Layer4ConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigDefinition = ConfigDefinition


@dataclass
class Layer4ConfigDefinition(BaseModel):
    IpProtocol: Optional[str]
    Ports: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Layer4ConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Layer4ConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            IpProtocol=json_data.get("IpProtocol"),
            Ports=json_data.get("Ports"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Layer4ConfigDefinition = Layer4ConfigDefinition


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


