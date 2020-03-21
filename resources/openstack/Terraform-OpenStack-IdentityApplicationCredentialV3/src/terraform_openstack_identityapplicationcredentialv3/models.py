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
    Description: Optional[str]
    ExpiresAt: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    ProjectId: Optional[str]
    Region: Optional[str]
    Roles: Optional[Sequence[str]]
    Secret: Optional[str]
    Unrestricted: Optional[bool]
    AccessRules: Optional[Sequence["_AccessRules"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Description=json_data.get("Description"),
            ExpiresAt=json_data.get("ExpiresAt"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ProjectId=json_data.get("ProjectId"),
            Region=json_data.get("Region"),
            Roles=json_data.get("Roles"),
            Secret=json_data.get("Secret"),
            Unrestricted=json_data.get("Unrestricted"),
            AccessRules=json_data.get("AccessRules"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AccessRules:
    Method: Optional[str]
    Path: Optional[str]
    Service: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccessRules"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessRules"]:
        if not json_data:
            return None
        return cls(
            Method=json_data.get("Method"),
            Path=json_data.get("Path"),
            Service=json_data.get("Service"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessRules = AccessRules


