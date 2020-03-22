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
    CanCreateGroup: Optional[bool]
    Email: Optional[str]
    Id: Optional[str]
    IsAdmin: Optional[bool]
    IsExternal: Optional[bool]
    Name: Optional[str]
    Password: Optional[str]
    ProjectsLimit: Optional[float]
    ResetPassword: Optional[bool]
    SkipConfirmation: Optional[bool]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CanCreateGroup=json_data.get("CanCreateGroup"),
            Email=json_data.get("Email"),
            Id=json_data.get("Id"),
            IsAdmin=json_data.get("IsAdmin"),
            IsExternal=json_data.get("IsExternal"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            ProjectsLimit=json_data.get("ProjectsLimit"),
            ResetPassword=json_data.get("ResetPassword"),
            SkipConfirmation=json_data.get("SkipConfirmation"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


