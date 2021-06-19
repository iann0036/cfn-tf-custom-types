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
    AccountId: Optional[str]
    ActionId: Optional[str]
    ActionType: Optional[str]
    ApprovalModel: Optional[str]
    Arn: Optional[str]
    BudgetName: Optional[str]
    ExecutionRoleArn: Optional[str]
    Id: Optional[str]
    NotificationType: Optional[str]
    Status: Optional[str]
    ActionThreshold: Optional[Sequence["_ActionThresholdDefinition"]]
    Definition: Optional[Sequence["_DefinitionDefinition"]]
    Subscriber: Optional[Sequence["_SubscriberDefinition"]]

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
            AccountId=json_data.get("AccountId"),
            ActionId=json_data.get("ActionId"),
            ActionType=json_data.get("ActionType"),
            ApprovalModel=json_data.get("ApprovalModel"),
            Arn=json_data.get("Arn"),
            BudgetName=json_data.get("BudgetName"),
            ExecutionRoleArn=json_data.get("ExecutionRoleArn"),
            Id=json_data.get("Id"),
            NotificationType=json_data.get("NotificationType"),
            Status=json_data.get("Status"),
            ActionThreshold=deserialize_list(json_data.get("ActionThreshold"), ActionThresholdDefinition),
            Definition=deserialize_list(json_data.get("Definition"), DefinitionDefinition),
            Subscriber=deserialize_list(json_data.get("Subscriber"), SubscriberDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ActionThresholdDefinition(BaseModel):
    ActionThresholdType: Optional[str]
    ActionThresholdValue: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ActionThresholdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionThresholdDefinition"]:
        if not json_data:
            return None
        return cls(
            ActionThresholdType=json_data.get("ActionThresholdType"),
            ActionThresholdValue=json_data.get("ActionThresholdValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionThresholdDefinition = ActionThresholdDefinition


@dataclass
class DefinitionDefinition(BaseModel):
    IamActionDefinition: Optional[Sequence["_IamActionDefinitionDefinition"]]
    ScpActionDefinition: Optional[Sequence["_ScpActionDefinitionDefinition"]]
    SsmActionDefinition: Optional[Sequence["_SsmActionDefinitionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinitionDefinition"]:
        if not json_data:
            return None
        return cls(
            IamActionDefinition=deserialize_list(json_data.get("IamActionDefinition"), IamActionDefinitionDefinition),
            ScpActionDefinition=deserialize_list(json_data.get("ScpActionDefinition"), ScpActionDefinitionDefinition),
            SsmActionDefinition=deserialize_list(json_data.get("SsmActionDefinition"), SsmActionDefinitionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinitionDefinition = DefinitionDefinition


@dataclass
class IamActionDefinitionDefinition(BaseModel):
    Groups: Optional[Sequence[str]]
    PolicyArn: Optional[str]
    Roles: Optional[Sequence[str]]
    Users: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_IamActionDefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IamActionDefinitionDefinition"]:
        if not json_data:
            return None
        return cls(
            Groups=json_data.get("Groups"),
            PolicyArn=json_data.get("PolicyArn"),
            Roles=json_data.get("Roles"),
            Users=json_data.get("Users"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IamActionDefinitionDefinition = IamActionDefinitionDefinition


@dataclass
class ScpActionDefinitionDefinition(BaseModel):
    PolicyId: Optional[str]
    TargetIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ScpActionDefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScpActionDefinitionDefinition"]:
        if not json_data:
            return None
        return cls(
            PolicyId=json_data.get("PolicyId"),
            TargetIds=json_data.get("TargetIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScpActionDefinitionDefinition = ScpActionDefinitionDefinition


@dataclass
class SsmActionDefinitionDefinition(BaseModel):
    ActionSubType: Optional[str]
    InstanceIds: Optional[Sequence[str]]
    Region: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SsmActionDefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SsmActionDefinitionDefinition"]:
        if not json_data:
            return None
        return cls(
            ActionSubType=json_data.get("ActionSubType"),
            InstanceIds=json_data.get("InstanceIds"),
            Region=json_data.get("Region"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SsmActionDefinitionDefinition = SsmActionDefinitionDefinition


@dataclass
class SubscriberDefinition(BaseModel):
    Address: Optional[str]
    SubscriptionType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SubscriberDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubscriberDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            SubscriptionType=json_data.get("SubscriptionType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubscriberDefinition = SubscriberDefinition


