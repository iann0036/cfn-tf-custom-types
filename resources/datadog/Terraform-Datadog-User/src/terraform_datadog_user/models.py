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
    AccessRole: Optional[str]
    Disabled: Optional[bool]
    Email: Optional[str]
    Handle: Optional[str]
    Id: Optional[str]
    IsAdmin: Optional[bool]
    Name: Optional[str]
    Role: Optional[str]
    Verified: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AccessRole=json_data.get("AccessRole"),
            Disabled=json_data.get("Disabled"),
            Email=json_data.get("Email"),
            Handle=json_data.get("Handle"),
            Id=json_data.get("Id"),
            IsAdmin=json_data.get("IsAdmin"),
            Name=json_data.get("Name"),
            Role=json_data.get("Role"),
            Verified=json_data.get("Verified"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


