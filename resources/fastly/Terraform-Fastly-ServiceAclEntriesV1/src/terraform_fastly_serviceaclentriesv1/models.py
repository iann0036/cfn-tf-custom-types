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
    AclId: Optional[str]
    Id: Optional[str]
    ServiceId: Optional[str]
    Entry: Optional[Sequence["_Entry"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AclId=json_data.get("AclId"),
            Id=json_data.get("Id"),
            ServiceId=json_data.get("ServiceId"),
            Entry=json_data.get("Entry"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Entry:
    Comment: Optional[str]
    Ip: Optional[str]
    Negated: Optional[bool]
    Subnet: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Entry"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Entry"]:
        if not json_data:
            return None
        return cls(
            Comment=json_data.get("Comment"),
            Ip=json_data.get("Ip"),
            Negated=json_data.get("Negated"),
            Subnet=json_data.get("Subnet"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Entry = Entry


