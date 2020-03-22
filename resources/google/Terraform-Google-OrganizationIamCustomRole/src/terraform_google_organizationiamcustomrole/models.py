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
    Deleted: Optional[bool]
    Description: Optional[str]
    Id: Optional[str]
    OrgId: Optional[str]
    Permissions: Optional[Sequence[str]]
    RoleId: Optional[str]
    Stage: Optional[str]
    Title: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Deleted=json_data.get("Deleted"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            OrgId=json_data.get("OrgId"),
            Permissions=json_data.get("Permissions"),
            RoleId=json_data.get("RoleId"),
            Stage=json_data.get("Stage"),
            Title=json_data.get("Title"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


