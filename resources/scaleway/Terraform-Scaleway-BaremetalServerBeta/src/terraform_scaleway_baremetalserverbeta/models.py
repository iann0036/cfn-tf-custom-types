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
    Domain: Optional[str]
    Id: Optional[str]
    Ips: Optional[Sequence["_Ips"]]
    Name: Optional[str]
    Offer: Optional[str]
    OfferId: Optional[str]
    OrganizationId: Optional[str]
    OsId: Optional[str]
    SshKeyIds: Optional[Sequence[str]]
    Tags: Optional[Sequence[str]]
    Zone: Optional[str]
    Timeouts: Optional["_Timeouts"]

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
            Domain=json_data.get("Domain"),
            Id=json_data.get("Id"),
            Ips=json_data.get("Ips"),
            Name=json_data.get("Name"),
            Offer=json_data.get("Offer"),
            OfferId=json_data.get("OfferId"),
            OrganizationId=json_data.get("OrganizationId"),
            OsId=json_data.get("OsId"),
            SshKeyIds=json_data.get("SshKeyIds"),
            Tags=json_data.get("Tags"),
            Zone=json_data.get("Zone"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Ips:
    Address: Optional[str]
    Id: Optional[str]
    Reverse: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ips"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ips"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Id=json_data.get("Id"),
            Reverse=json_data.get("Reverse"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ips = Ips


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


