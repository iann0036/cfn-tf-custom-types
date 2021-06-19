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
    Id: Optional[str]
    Key: Optional[str]
    Name: Optional[str]
    Policy: Optional[Sequence["_PolicyDefinition"]]
    PolicyStatements: Optional[Sequence["_PolicyStatementsDefinition"]]

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
            Id=json_data.get("Id"),
            Key=json_data.get("Key"),
            Name=json_data.get("Name"),
            Policy=deserialize_list(json_data.get("Policy"), PolicyDefinition),
            PolicyStatements=deserialize_list(json_data.get("PolicyStatements"), PolicyStatementsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PolicyDefinition(BaseModel):
    Actions: Optional[Sequence[str]]
    Effect: Optional[str]
    Resources: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Actions=json_data.get("Actions"),
            Effect=json_data.get("Effect"),
            Resources=json_data.get("Resources"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PolicyDefinition = PolicyDefinition


@dataclass
class PolicyStatementsDefinition(BaseModel):
    Actions: Optional[Sequence[str]]
    Effect: Optional[str]
    NotActions: Optional[Sequence[str]]
    NotResources: Optional[Sequence[str]]
    Resources: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PolicyStatementsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PolicyStatementsDefinition"]:
        if not json_data:
            return None
        return cls(
            Actions=json_data.get("Actions"),
            Effect=json_data.get("Effect"),
            NotActions=json_data.get("NotActions"),
            NotResources=json_data.get("NotResources"),
            Resources=json_data.get("Resources"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PolicyStatementsDefinition = PolicyStatementsDefinition


