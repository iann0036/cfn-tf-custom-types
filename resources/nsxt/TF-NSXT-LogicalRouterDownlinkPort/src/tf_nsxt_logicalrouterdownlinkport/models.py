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
    Description: Optional[str]
    DisplayName: Optional[str]
    Id: Optional[str]
    IpAddress: Optional[str]
    LinkedLogicalSwitchPortId: Optional[str]
    LogicalRouterId: Optional[str]
    MacAddress: Optional[str]
    Revision: Optional[float]
    UrpfMode: Optional[str]
    ServiceBinding: Optional[Sequence["_ServiceBindingDefinition"]]
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
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            IpAddress=json_data.get("IpAddress"),
            LinkedLogicalSwitchPortId=json_data.get("LinkedLogicalSwitchPortId"),
            LogicalRouterId=json_data.get("LogicalRouterId"),
            MacAddress=json_data.get("MacAddress"),
            Revision=json_data.get("Revision"),
            UrpfMode=json_data.get("UrpfMode"),
            ServiceBinding=deserialize_list(json_data.get("ServiceBinding"), ServiceBindingDefinition),
            Tag=deserialize_list(json_data.get("Tag"), TagDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ServiceBindingDefinition(BaseModel):
    TargetId: Optional[str]
    TargetType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceBindingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceBindingDefinition"]:
        if not json_data:
            return None
        return cls(
            TargetId=json_data.get("TargetId"),
            TargetType=json_data.get("TargetType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceBindingDefinition = ServiceBindingDefinition


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

