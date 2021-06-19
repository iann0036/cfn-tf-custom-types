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
    AcceleratorId: Optional[str]
    ForwardingRuleId: Optional[str]
    ForwardingRuleName: Optional[str]
    ForwardingRuleStatus: Optional[str]
    Id: Optional[str]
    ListenerId: Optional[str]
    Priority: Optional[float]
    RuleActions: Optional[Sequence["_RuleActionsDefinition"]]
    RuleConditions: Optional[Sequence["_RuleConditionsDefinition"]]
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
            AcceleratorId=json_data.get("AcceleratorId"),
            ForwardingRuleId=json_data.get("ForwardingRuleId"),
            ForwardingRuleName=json_data.get("ForwardingRuleName"),
            ForwardingRuleStatus=json_data.get("ForwardingRuleStatus"),
            Id=json_data.get("Id"),
            ListenerId=json_data.get("ListenerId"),
            Priority=json_data.get("Priority"),
            RuleActions=deserialize_list(json_data.get("RuleActions"), RuleActionsDefinition),
            RuleConditions=deserialize_list(json_data.get("RuleConditions"), RuleConditionsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RuleActionsDefinition(BaseModel):
    Order: Optional[float]
    RuleActionType: Optional[str]
    ForwardGroupConfig: Optional[Sequence["_ForwardGroupConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RuleActionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleActionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Order=json_data.get("Order"),
            RuleActionType=json_data.get("RuleActionType"),
            ForwardGroupConfig=deserialize_list(json_data.get("ForwardGroupConfig"), ForwardGroupConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleActionsDefinition = RuleActionsDefinition


@dataclass
class ForwardGroupConfigDefinition(BaseModel):
    ServerGroupTuples: Optional[Sequence["_ServerGroupTuplesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ForwardGroupConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ForwardGroupConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            ServerGroupTuples=deserialize_list(json_data.get("ServerGroupTuples"), ServerGroupTuplesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ForwardGroupConfigDefinition = ForwardGroupConfigDefinition


@dataclass
class ServerGroupTuplesDefinition(BaseModel):
    EndpointGroupId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerGroupTuplesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerGroupTuplesDefinition"]:
        if not json_data:
            return None
        return cls(
            EndpointGroupId=json_data.get("EndpointGroupId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerGroupTuplesDefinition = ServerGroupTuplesDefinition


@dataclass
class RuleConditionsDefinition(BaseModel):
    RuleConditionType: Optional[str]
    HostConfig: Optional[Sequence["_HostConfigDefinition"]]
    PathConfig: Optional[Sequence["_PathConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RuleConditionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleConditionsDefinition"]:
        if not json_data:
            return None
        return cls(
            RuleConditionType=json_data.get("RuleConditionType"),
            HostConfig=deserialize_list(json_data.get("HostConfig"), HostConfigDefinition),
            PathConfig=deserialize_list(json_data.get("PathConfig"), PathConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleConditionsDefinition = RuleConditionsDefinition


@dataclass
class HostConfigDefinition(BaseModel):
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_HostConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostConfigDefinition = HostConfigDefinition


@dataclass
class PathConfigDefinition(BaseModel):
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PathConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PathConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PathConfigDefinition = PathConfigDefinition


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


