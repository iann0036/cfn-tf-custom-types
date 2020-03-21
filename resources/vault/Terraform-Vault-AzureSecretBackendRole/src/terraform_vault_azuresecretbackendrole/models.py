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
    ApplicationObjectId: Optional[str]
    Backend: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    MaxTtl: Optional[str]
    Role: Optional[str]
    Ttl: Optional[str]
    AzureRoles: Optional[Sequence["_AzureRoles"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ApplicationObjectId=json_data.get("ApplicationObjectId"),
            Backend=json_data.get("Backend"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            MaxTtl=json_data.get("MaxTtl"),
            Role=json_data.get("Role"),
            Ttl=json_data.get("Ttl"),
            AzureRoles=json_data.get("AzureRoles"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AzureRoles:
    RoleName: Optional[str]
    Scope: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AzureRoles"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureRoles"]:
        if not json_data:
            return None
        return cls(
            RoleName=json_data.get("RoleName"),
            Scope=json_data.get("Scope"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureRoles = AzureRoles


