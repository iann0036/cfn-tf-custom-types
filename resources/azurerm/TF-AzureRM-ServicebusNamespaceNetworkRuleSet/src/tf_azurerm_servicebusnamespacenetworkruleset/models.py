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
    DefaultAction: Optional[str]
    Id: Optional[str]
    IpRules: Optional[Sequence[str]]
    NamespaceName: Optional[str]
    ResourceGroupName: Optional[str]
    NetworkRules: Optional[Sequence["_NetworkRulesDefinition"]]
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
            DefaultAction=json_data.get("DefaultAction"),
            Id=json_data.get("Id"),
            IpRules=json_data.get("IpRules"),
            NamespaceName=json_data.get("NamespaceName"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            NetworkRules=deserialize_list(json_data.get("NetworkRules"), NetworkRulesDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class NetworkRulesDefinition(BaseModel):
    IgnoreMissingVnetServiceEndpoint: Optional[bool]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            IgnoreMissingVnetServiceEndpoint=json_data.get("IgnoreMissingVnetServiceEndpoint"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkRulesDefinition = NetworkRulesDefinition


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


