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
    Id: Optional[str]
    IothubId: Optional[str]
    Name: Optional[str]
    AllowRule: Optional[Sequence["_AllowRuleDefinition"]]
    RangeRule: Optional[Sequence["_RangeRuleDefinition"]]
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
            Id=json_data.get("Id"),
            IothubId=json_data.get("IothubId"),
            Name=json_data.get("Name"),
            AllowRule=deserialize_list(json_data.get("AllowRule"), AllowRuleDefinition),
            RangeRule=deserialize_list(json_data.get("RangeRule"), RangeRuleDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AllowRuleDefinition(BaseModel):
    ConnectionToIpNotAllowed: Optional[Sequence[str]]
    LocalUserNotAllowed: Optional[Sequence[str]]
    ProcessNotAllowed: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AllowRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AllowRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            ConnectionToIpNotAllowed=json_data.get("ConnectionToIpNotAllowed"),
            LocalUserNotAllowed=json_data.get("LocalUserNotAllowed"),
            ProcessNotAllowed=json_data.get("ProcessNotAllowed"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AllowRuleDefinition = AllowRuleDefinition


@dataclass
class RangeRuleDefinition(BaseModel):
    Duration: Optional[str]
    Max: Optional[float]
    Min: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RangeRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RangeRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Duration=json_data.get("Duration"),
            Max=json_data.get("Max"),
            Min=json_data.get("Min"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RangeRuleDefinition = RangeRuleDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


