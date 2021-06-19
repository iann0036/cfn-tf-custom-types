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
    Frequency: Optional[float]
    Id: Optional[str]
    Name: Optional[str]
    Repeating: Optional[bool]
    Teams: Optional[Sequence[float]]
    EscalationRule: Optional[Sequence["_EscalationRuleDefinition"]]

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
            Frequency=json_data.get("Frequency"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Repeating=json_data.get("Repeating"),
            Teams=json_data.get("Teams"),
            EscalationRule=deserialize_list(json_data.get("EscalationRule"), EscalationRuleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EscalationRuleDefinition(BaseModel):
    EscalationTimeout: Optional[float]
    Schedule: Optional[str]
    User: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EscalationRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EscalationRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            EscalationTimeout=json_data.get("EscalationTimeout"),
            Schedule=json_data.get("Schedule"),
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EscalationRuleDefinition = EscalationRuleDefinition


