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
    Backend: Optional[str]
    Id: Optional[str]
    Project: Optional[str]
    Roleset: Optional[str]
    SecretType: Optional[str]
    ServiceAccountEmail: Optional[str]
    TokenScopes: Optional[Sequence[str]]
    Binding: Optional[Sequence["_BindingDefinition"]]

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
            Backend=json_data.get("Backend"),
            Id=json_data.get("Id"),
            Project=json_data.get("Project"),
            Roleset=json_data.get("Roleset"),
            SecretType=json_data.get("SecretType"),
            ServiceAccountEmail=json_data.get("ServiceAccountEmail"),
            TokenScopes=json_data.get("TokenScopes"),
            Binding=deserialize_list(json_data.get("Binding"), BindingDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BindingDefinition(BaseModel):
    Resource: Optional[str]
    Roles: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_BindingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BindingDefinition"]:
        if not json_data:
            return None
        return cls(
            Resource=json_data.get("Resource"),
            Roles=json_data.get("Roles"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BindingDefinition = BindingDefinition

