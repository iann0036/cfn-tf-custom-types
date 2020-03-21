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
    Id: Optional[str]
    Identifier: Optional[str]
    Name: Optional[str]
    ScopeIdentifiers: Optional[Sequence[str]]
    UserPoolId: Optional[str]
    Scope: Optional[Sequence["_Scope"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Id=json_data.get("Id"),
            Identifier=json_data.get("Identifier"),
            Name=json_data.get("Name"),
            ScopeIdentifiers=json_data.get("ScopeIdentifiers"),
            UserPoolId=json_data.get("UserPoolId"),
            Scope=json_data.get("Scope"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Scope:
    ScopeDescription: Optional[str]
    ScopeName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Scope"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Scope"]:
        if not json_data:
            return None
        return cls(
            ScopeDescription=json_data.get("ScopeDescription"),
            ScopeName=json_data.get("ScopeName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Scope = Scope


