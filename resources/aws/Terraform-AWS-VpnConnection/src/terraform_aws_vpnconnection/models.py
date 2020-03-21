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
    CustomerGatewayConfiguration: Optional[str]
    CustomerGatewayId: Optional[str]
    Id: Optional[str]
    Routes: Optional[Sequence["_Routes"]]
    StaticRoutesOnly: Optional[bool]
    Tags: Optional[Sequence["_Tags"]]
    TransitGatewayAttachmentId: Optional[str]
    TransitGatewayId: Optional[str]
    Tunnel1Address: Optional[str]
    Tunnel1BgpAsn: Optional[str]
    Tunnel1BgpHoldtime: Optional[float]
    Tunnel1CgwInsideAddress: Optional[str]
    Tunnel1InsideCidr: Optional[str]
    Tunnel1PresharedKey: Optional[str]
    Tunnel1VgwInsideAddress: Optional[str]
    Tunnel2Address: Optional[str]
    Tunnel2BgpAsn: Optional[str]
    Tunnel2BgpHoldtime: Optional[float]
    Tunnel2CgwInsideAddress: Optional[str]
    Tunnel2InsideCidr: Optional[str]
    Tunnel2PresharedKey: Optional[str]
    Tunnel2VgwInsideAddress: Optional[str]
    Type: Optional[str]
    VgwTelemetry: Optional[Sequence["_VgwTelemetry"]]
    VpnGatewayId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CustomerGatewayConfiguration=json_data.get("CustomerGatewayConfiguration"),
            CustomerGatewayId=json_data.get("CustomerGatewayId"),
            Id=json_data.get("Id"),
            Routes=json_data.get("Routes"),
            StaticRoutesOnly=json_data.get("StaticRoutesOnly"),
            Tags=json_data.get("Tags"),
            TransitGatewayAttachmentId=json_data.get("TransitGatewayAttachmentId"),
            TransitGatewayId=json_data.get("TransitGatewayId"),
            Tunnel1Address=json_data.get("Tunnel1Address"),
            Tunnel1BgpAsn=json_data.get("Tunnel1BgpAsn"),
            Tunnel1BgpHoldtime=json_data.get("Tunnel1BgpHoldtime"),
            Tunnel1CgwInsideAddress=json_data.get("Tunnel1CgwInsideAddress"),
            Tunnel1InsideCidr=json_data.get("Tunnel1InsideCidr"),
            Tunnel1PresharedKey=json_data.get("Tunnel1PresharedKey"),
            Tunnel1VgwInsideAddress=json_data.get("Tunnel1VgwInsideAddress"),
            Tunnel2Address=json_data.get("Tunnel2Address"),
            Tunnel2BgpAsn=json_data.get("Tunnel2BgpAsn"),
            Tunnel2BgpHoldtime=json_data.get("Tunnel2BgpHoldtime"),
            Tunnel2CgwInsideAddress=json_data.get("Tunnel2CgwInsideAddress"),
            Tunnel2InsideCidr=json_data.get("Tunnel2InsideCidr"),
            Tunnel2PresharedKey=json_data.get("Tunnel2PresharedKey"),
            Tunnel2VgwInsideAddress=json_data.get("Tunnel2VgwInsideAddress"),
            Type=json_data.get("Type"),
            VgwTelemetry=json_data.get("VgwTelemetry"),
            VpnGatewayId=json_data.get("VpnGatewayId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Routes:
    DestinationCidrBlock: Optional[str]
    Source: Optional[str]
    State: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Routes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Routes"]:
        if not json_data:
            return None
        return cls(
            DestinationCidrBlock=json_data.get("DestinationCidrBlock"),
            Source=json_data.get("Source"),
            State=json_data.get("State"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Routes = Routes


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class VgwTelemetry:
    AcceptedRouteCount: Optional[float]
    LastStatusChange: Optional[str]
    OutsideIpAddress: Optional[str]
    Status: Optional[str]
    StatusMessage: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VgwTelemetry"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VgwTelemetry"]:
        if not json_data:
            return None
        return cls(
            AcceptedRouteCount=json_data.get("AcceptedRouteCount"),
            LastStatusChange=json_data.get("LastStatusChange"),
            OutsideIpAddress=json_data.get("OutsideIpAddress"),
            Status=json_data.get("Status"),
            StatusMessage=json_data.get("StatusMessage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VgwTelemetry = VgwTelemetry


