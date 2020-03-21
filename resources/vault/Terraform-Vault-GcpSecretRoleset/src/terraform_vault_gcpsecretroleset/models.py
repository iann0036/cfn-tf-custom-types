# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    Backend: Optional[str]
    Id: Optional[str]
    Project: Optional[str]
    Roleset: Optional[str]
    SecretType: Optional[str]
    ServiceAccountEmail: Optional[str]
    TokenScopes: Optional[Sequence[str]]
    Binding: Optional[Sequence["_Binding"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Backend=json_data.get("Backend"),
            Id=json_data.get("Id"),
            Project=json_data.get("Project"),
            Roleset=json_data.get("Roleset"),
            SecretType=json_data.get("SecretType"),
            ServiceAccountEmail=json_data.get("ServiceAccountEmail"),
            TokenScopes=json_data.get("TokenScopes"),
            Binding=json_data.get("Binding"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Binding:
    Resource: Optional[str]
    Roles: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Binding"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Binding"]:
        if not json_data:
            return None
        return cls(
            Resource=json_data.get("Resource"),
            Roles=json_data.get("Roles"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Binding = Binding


