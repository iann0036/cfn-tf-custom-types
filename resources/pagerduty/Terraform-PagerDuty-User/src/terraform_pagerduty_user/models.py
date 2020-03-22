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
    AvatarUrl: Optional[str]
    Color: Optional[str]
    Description: Optional[str]
    Email: Optional[str]
    HtmlUrl: Optional[str]
    Id: Optional[str]
    InvitationSent: Optional[bool]
    JobTitle: Optional[str]
    Name: Optional[str]
    Role: Optional[str]
    Teams: Optional[Sequence[str]]
    TimeZone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AvatarUrl=json_data.get("AvatarUrl"),
            Color=json_data.get("Color"),
            Description=json_data.get("Description"),
            Email=json_data.get("Email"),
            HtmlUrl=json_data.get("HtmlUrl"),
            Id=json_data.get("Id"),
            InvitationSent=json_data.get("InvitationSent"),
            JobTitle=json_data.get("JobTitle"),
            Name=json_data.get("Name"),
            Role=json_data.get("Role"),
            Teams=json_data.get("Teams"),
            TimeZone=json_data.get("TimeZone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


