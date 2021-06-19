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
    CorpScope: Optional[str]
    Enabled: Optional[bool]
    Expiration: Optional[str]
    GroupOperator: Optional[str]
    Id: Optional[str]
    Reason: Optional[str]
    Signal: Optional[str]
    SiteShortNames: Optional[Sequence[str]]
    Type: Optional[str]
    Actions: Optional[Sequence["_ActionsDefinition"]]
    Conditions: Optional[Sequence["_ConditionsDefinition"]]

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
            CorpScope=json_data.get("CorpScope"),
            Enabled=json_data.get("Enabled"),
            Expiration=json_data.get("Expiration"),
            GroupOperator=json_data.get("GroupOperator"),
            Id=json_data.get("Id"),
            Reason=json_data.get("Reason"),
            Signal=json_data.get("Signal"),
            SiteShortNames=json_data.get("SiteShortNames"),
            Type=json_data.get("Type"),
            Actions=deserialize_list(json_data.get("Actions"), ActionsDefinition),
            Conditions=deserialize_list(json_data.get("Conditions"), ConditionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ActionsDefinition(BaseModel):
    Signal: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ActionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Signal=json_data.get("Signal"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionsDefinition = ActionsDefinition


@dataclass
class ConditionsDefinition(BaseModel):
    Field: Optional[str]
    GroupOperator: Optional[str]
    Operator: Optional[str]
    Type: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Field=json_data.get("Field"),
            GroupOperator=json_data.get("GroupOperator"),
            Operator=json_data.get("Operator"),
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionsDefinition = ConditionsDefinition


