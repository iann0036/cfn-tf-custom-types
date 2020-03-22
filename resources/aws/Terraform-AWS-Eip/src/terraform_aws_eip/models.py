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
    AllocationId: Optional[str]
    AssociateWithPrivateIp: Optional[str]
    AssociationId: Optional[str]
    Domain: Optional[str]
    Id: Optional[str]
    Instance: Optional[str]
    NetworkInterface: Optional[str]
    PrivateDns: Optional[str]
    PrivateIp: Optional[str]
    PublicDns: Optional[str]
    PublicIp: Optional[str]
    PublicIpv4Pool: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Vpc: Optional[bool]
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
            AllocationId=json_data.get("AllocationId"),
            AssociateWithPrivateIp=json_data.get("AssociateWithPrivateIp"),
            AssociationId=json_data.get("AssociationId"),
            Domain=json_data.get("Domain"),
            Id=json_data.get("Id"),
            Instance=json_data.get("Instance"),
            NetworkInterface=json_data.get("NetworkInterface"),
            PrivateDns=json_data.get("PrivateDns"),
            PrivateIp=json_data.get("PrivateIp"),
            PublicDns=json_data.get("PublicDns"),
            PublicIp=json_data.get("PublicIp"),
            PublicIpv4Pool=json_data.get("PublicIpv4Pool"),
            Tags=json_data.get("Tags"),
            Vpc=json_data.get("Vpc"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class Timeouts:
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


