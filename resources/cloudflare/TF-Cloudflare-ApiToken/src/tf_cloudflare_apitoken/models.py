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
    IssuedOn: Optional[str]
    ModifiedOn: Optional[str]
    Name: Optional[str]
    Status: Optional[str]
    Value: Optional[str]
    Condition: Optional[Sequence["_ConditionDefinition"]]
    Policy: Optional[Sequence["_PolicyDefinition"]]

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
            IssuedOn=json_data.get("IssuedOn"),
            ModifiedOn=json_data.get("ModifiedOn"),
            Name=json_data.get("Name"),
            Status=json_data.get("Status"),
            Value=json_data.get("Value"),
            Condition=deserialize_list(json_data.get("Condition"), ConditionDefinition),
            Policy=deserialize_list(json_data.get("Policy"), PolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ConditionDefinition(BaseModel):
    RequestIp: Optional[Sequence["_RequestIpDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionDefinition"]:
        if not json_data:
            return None
        return cls(
            RequestIp=deserialize_list(json_data.get("RequestIp"), RequestIpDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionDefinition = ConditionDefinition


@dataclass
class RequestIpDefinition(BaseModel):
    In: Optional[Sequence[str]]
    NotIn: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_RequestIpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestIpDefinition"]:
        if not json_data:
            return None
        return cls(
            In=json_data.get("In"),
            NotIn=json_data.get("NotIn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestIpDefinition = RequestIpDefinition


@dataclass
class PolicyDefinition(BaseModel):
    Effect: Optional[str]
    PermissionGroups: Optional[Sequence[str]]
    Resources: Optional[Sequence["_ResourcesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Effect=json_data.get("Effect"),
            PermissionGroups=json_data.get("PermissionGroups"),
            Resources=deserialize_list(json_data.get("Resources"), ResourcesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PolicyDefinition = PolicyDefinition


@dataclass
class ResourcesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourcesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourcesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourcesDefinition = ResourcesDefinition


