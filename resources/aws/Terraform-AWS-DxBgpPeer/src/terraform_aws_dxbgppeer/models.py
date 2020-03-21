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
    AddressFamily: Optional[str]
    AmazonAddress: Optional[str]
    AwsDevice: Optional[str]
    BgpAsn: Optional[float]
    BgpAuthKey: Optional[str]
    BgpPeerId: Optional[str]
    BgpStatus: Optional[str]
    CustomerAddress: Optional[str]
    Id: Optional[str]
    VirtualInterfaceId: Optional[str]
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
            AddressFamily=json_data.get("AddressFamily"),
            AmazonAddress=json_data.get("AmazonAddress"),
            AwsDevice=json_data.get("AwsDevice"),
            BgpAsn=json_data.get("BgpAsn"),
            BgpAuthKey=json_data.get("BgpAuthKey"),
            BgpPeerId=json_data.get("BgpPeerId"),
            BgpStatus=json_data.get("BgpStatus"),
            CustomerAddress=json_data.get("CustomerAddress"),
            Id=json_data.get("Id"),
            VirtualInterfaceId=json_data.get("VirtualInterfaceId"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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


