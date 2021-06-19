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
    CustomRoles: Optional[Sequence[str]]
    DefaultApiVersion: Optional[float]
    Expire: Optional[float]
    Id: Optional[str]
    Name: Optional[str]
    Role: Optional[str]
    ServiceToken: Optional[bool]
    Token: Optional[str]
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
            CustomRoles=json_data.get("CustomRoles"),
            DefaultApiVersion=json_data.get("DefaultApiVersion"),
            Expire=json_data.get("Expire"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Role=json_data.get("Role"),
            ServiceToken=json_data.get("ServiceToken"),
            Token=json_data.get("Token"),
            PolicyStatements=deserialize_list(json_data.get("PolicyStatements"), PolicyStatementsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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


