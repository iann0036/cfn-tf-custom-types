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
    AmazonSideAsn: Optional[str]
    Arn: Optional[str]
    AwsDevice: Optional[str]
    BgpAsn: Optional[float]
    BgpAuthKey: Optional[str]
    ConnectionId: Optional[str]
    CustomerAddress: Optional[str]
    DxGatewayId: Optional[str]
    Id: Optional[str]
    JumboFrameCapable: Optional[bool]
    Mtu: Optional[float]
    Name: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Vlan: Optional[float]
    VpnGatewayId: Optional[str]
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
            AmazonSideAsn=json_data.get("AmazonSideAsn"),
            Arn=json_data.get("Arn"),
            AwsDevice=json_data.get("AwsDevice"),
            BgpAsn=json_data.get("BgpAsn"),
            BgpAuthKey=json_data.get("BgpAuthKey"),
            ConnectionId=json_data.get("ConnectionId"),
            CustomerAddress=json_data.get("CustomerAddress"),
            DxGatewayId=json_data.get("DxGatewayId"),
            Id=json_data.get("Id"),
            JumboFrameCapable=json_data.get("JumboFrameCapable"),
            Mtu=json_data.get("Mtu"),
            Name=json_data.get("Name"),
            Tags=json_data.get("Tags"),
            Vlan=json_data.get("Vlan"),
            VpnGatewayId=json_data.get("VpnGatewayId"),
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
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


