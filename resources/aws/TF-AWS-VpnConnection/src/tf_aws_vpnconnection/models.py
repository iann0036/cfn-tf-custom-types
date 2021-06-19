# DO NOT modify this file by hand, changes will be overwritten
import sys
from dataclasses import dataclass
from inspect import getmembers, isclass
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
    BaseModel,
    BaseResourceHandlerRequest,
)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

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
class ResourceModel(BaseModel):
    tfcfnid: Optional[str]
    Arn: Optional[str]
    CustomerGatewayConfiguration: Optional[str]
    CustomerGatewayId: Optional[str]
    EnableAcceleration: Optional[bool]
    Id: Optional[str]
    LocalIpv4NetworkCidr: Optional[str]
    LocalIpv6NetworkCidr: Optional[str]
    RemoteIpv4NetworkCidr: Optional[str]
    RemoteIpv6NetworkCidr: Optional[str]
    Routes: Optional[Sequence["_RoutesDefinition"]]
    StaticRoutesOnly: Optional[bool]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    TransitGatewayAttachmentId: Optional[str]
    TransitGatewayId: Optional[str]
    Tunnel1Address: Optional[str]
    Tunnel1BgpAsn: Optional[str]
    Tunnel1BgpHoldtime: Optional[float]
    Tunnel1CgwInsideAddress: Optional[str]
    Tunnel1DpdTimeoutAction: Optional[str]
    Tunnel1DpdTimeoutSeconds: Optional[float]
    Tunnel1IkeVersions: Optional[Sequence[str]]
    Tunnel1InsideCidr: Optional[str]
    Tunnel1InsideIpv6Cidr: Optional[str]
    Tunnel1Phase1DhGroupNumbers: Optional[Sequence[float]]
    Tunnel1Phase1EncryptionAlgorithms: Optional[Sequence[str]]
    Tunnel1Phase1IntegrityAlgorithms: Optional[Sequence[str]]
    Tunnel1Phase1LifetimeSeconds: Optional[float]
    Tunnel1Phase2DhGroupNumbers: Optional[Sequence[float]]
    Tunnel1Phase2EncryptionAlgorithms: Optional[Sequence[str]]
    Tunnel1Phase2IntegrityAlgorithms: Optional[Sequence[str]]
    Tunnel1Phase2LifetimeSeconds: Optional[float]
    Tunnel1PresharedKey: Optional[str]
    Tunnel1RekeyFuzzPercentage: Optional[float]
    Tunnel1RekeyMarginTimeSeconds: Optional[float]
    Tunnel1ReplayWindowSize: Optional[float]
    Tunnel1StartupAction: Optional[str]
    Tunnel1VgwInsideAddress: Optional[str]
    Tunnel2Address: Optional[str]
    Tunnel2BgpAsn: Optional[str]
    Tunnel2BgpHoldtime: Optional[float]
    Tunnel2CgwInsideAddress: Optional[str]
    Tunnel2DpdTimeoutAction: Optional[str]
    Tunnel2DpdTimeoutSeconds: Optional[float]
    Tunnel2IkeVersions: Optional[Sequence[str]]
    Tunnel2InsideCidr: Optional[str]
    Tunnel2InsideIpv6Cidr: Optional[str]
    Tunnel2Phase1DhGroupNumbers: Optional[Sequence[float]]
    Tunnel2Phase1EncryptionAlgorithms: Optional[Sequence[str]]
    Tunnel2Phase1IntegrityAlgorithms: Optional[Sequence[str]]
    Tunnel2Phase1LifetimeSeconds: Optional[float]
    Tunnel2Phase2DhGroupNumbers: Optional[Sequence[float]]
    Tunnel2Phase2EncryptionAlgorithms: Optional[Sequence[str]]
    Tunnel2Phase2IntegrityAlgorithms: Optional[Sequence[str]]
    Tunnel2Phase2LifetimeSeconds: Optional[float]
    Tunnel2PresharedKey: Optional[str]
    Tunnel2RekeyFuzzPercentage: Optional[float]
    Tunnel2RekeyMarginTimeSeconds: Optional[float]
    Tunnel2ReplayWindowSize: Optional[float]
    Tunnel2StartupAction: Optional[str]
    Tunnel2VgwInsideAddress: Optional[str]
    TunnelInsideIpVersion: Optional[str]
    Type: Optional[str]
    VgwTelemetry: Optional[Sequence["_VgwTelemetryDefinition"]]
    VpnGatewayId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            CustomerGatewayConfiguration=json_data.get("CustomerGatewayConfiguration"),
            CustomerGatewayId=json_data.get("CustomerGatewayId"),
            EnableAcceleration=json_data.get("EnableAcceleration"),
            Id=json_data.get("Id"),
            LocalIpv4NetworkCidr=json_data.get("LocalIpv4NetworkCidr"),
            LocalIpv6NetworkCidr=json_data.get("LocalIpv6NetworkCidr"),
            RemoteIpv4NetworkCidr=json_data.get("RemoteIpv4NetworkCidr"),
            RemoteIpv6NetworkCidr=json_data.get("RemoteIpv6NetworkCidr"),
            Routes=deserialize_list(json_data.get("Routes"), RoutesDefinition),
            StaticRoutesOnly=json_data.get("StaticRoutesOnly"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            TransitGatewayAttachmentId=json_data.get("TransitGatewayAttachmentId"),
            TransitGatewayId=json_data.get("TransitGatewayId"),
            Tunnel1Address=json_data.get("Tunnel1Address"),
            Tunnel1BgpAsn=json_data.get("Tunnel1BgpAsn"),
            Tunnel1BgpHoldtime=json_data.get("Tunnel1BgpHoldtime"),
            Tunnel1CgwInsideAddress=json_data.get("Tunnel1CgwInsideAddress"),
            Tunnel1DpdTimeoutAction=json_data.get("Tunnel1DpdTimeoutAction"),
            Tunnel1DpdTimeoutSeconds=json_data.get("Tunnel1DpdTimeoutSeconds"),
            Tunnel1IkeVersions=json_data.get("Tunnel1IkeVersions"),
            Tunnel1InsideCidr=json_data.get("Tunnel1InsideCidr"),
            Tunnel1InsideIpv6Cidr=json_data.get("Tunnel1InsideIpv6Cidr"),
            Tunnel1Phase1DhGroupNumbers=json_data.get("Tunnel1Phase1DhGroupNumbers"),
            Tunnel1Phase1EncryptionAlgorithms=json_data.get("Tunnel1Phase1EncryptionAlgorithms"),
            Tunnel1Phase1IntegrityAlgorithms=json_data.get("Tunnel1Phase1IntegrityAlgorithms"),
            Tunnel1Phase1LifetimeSeconds=json_data.get("Tunnel1Phase1LifetimeSeconds"),
            Tunnel1Phase2DhGroupNumbers=json_data.get("Tunnel1Phase2DhGroupNumbers"),
            Tunnel1Phase2EncryptionAlgorithms=json_data.get("Tunnel1Phase2EncryptionAlgorithms"),
            Tunnel1Phase2IntegrityAlgorithms=json_data.get("Tunnel1Phase2IntegrityAlgorithms"),
            Tunnel1Phase2LifetimeSeconds=json_data.get("Tunnel1Phase2LifetimeSeconds"),
            Tunnel1PresharedKey=json_data.get("Tunnel1PresharedKey"),
            Tunnel1RekeyFuzzPercentage=json_data.get("Tunnel1RekeyFuzzPercentage"),
            Tunnel1RekeyMarginTimeSeconds=json_data.get("Tunnel1RekeyMarginTimeSeconds"),
            Tunnel1ReplayWindowSize=json_data.get("Tunnel1ReplayWindowSize"),
            Tunnel1StartupAction=json_data.get("Tunnel1StartupAction"),
            Tunnel1VgwInsideAddress=json_data.get("Tunnel1VgwInsideAddress"),
            Tunnel2Address=json_data.get("Tunnel2Address"),
            Tunnel2BgpAsn=json_data.get("Tunnel2BgpAsn"),
            Tunnel2BgpHoldtime=json_data.get("Tunnel2BgpHoldtime"),
            Tunnel2CgwInsideAddress=json_data.get("Tunnel2CgwInsideAddress"),
            Tunnel2DpdTimeoutAction=json_data.get("Tunnel2DpdTimeoutAction"),
            Tunnel2DpdTimeoutSeconds=json_data.get("Tunnel2DpdTimeoutSeconds"),
            Tunnel2IkeVersions=json_data.get("Tunnel2IkeVersions"),
            Tunnel2InsideCidr=json_data.get("Tunnel2InsideCidr"),
            Tunnel2InsideIpv6Cidr=json_data.get("Tunnel2InsideIpv6Cidr"),
            Tunnel2Phase1DhGroupNumbers=json_data.get("Tunnel2Phase1DhGroupNumbers"),
            Tunnel2Phase1EncryptionAlgorithms=json_data.get("Tunnel2Phase1EncryptionAlgorithms"),
            Tunnel2Phase1IntegrityAlgorithms=json_data.get("Tunnel2Phase1IntegrityAlgorithms"),
            Tunnel2Phase1LifetimeSeconds=json_data.get("Tunnel2Phase1LifetimeSeconds"),
            Tunnel2Phase2DhGroupNumbers=json_data.get("Tunnel2Phase2DhGroupNumbers"),
            Tunnel2Phase2EncryptionAlgorithms=json_data.get("Tunnel2Phase2EncryptionAlgorithms"),
            Tunnel2Phase2IntegrityAlgorithms=json_data.get("Tunnel2Phase2IntegrityAlgorithms"),
            Tunnel2Phase2LifetimeSeconds=json_data.get("Tunnel2Phase2LifetimeSeconds"),
            Tunnel2PresharedKey=json_data.get("Tunnel2PresharedKey"),
            Tunnel2RekeyFuzzPercentage=json_data.get("Tunnel2RekeyFuzzPercentage"),
            Tunnel2RekeyMarginTimeSeconds=json_data.get("Tunnel2RekeyMarginTimeSeconds"),
            Tunnel2ReplayWindowSize=json_data.get("Tunnel2ReplayWindowSize"),
            Tunnel2StartupAction=json_data.get("Tunnel2StartupAction"),
            Tunnel2VgwInsideAddress=json_data.get("Tunnel2VgwInsideAddress"),
            TunnelInsideIpVersion=json_data.get("TunnelInsideIpVersion"),
            Type=json_data.get("Type"),
            VgwTelemetry=deserialize_list(json_data.get("VgwTelemetry"), VgwTelemetryDefinition),
            VpnGatewayId=json_data.get("VpnGatewayId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RoutesDefinition(BaseModel):
    DestinationCidrBlock: Optional[str]
    Source: Optional[str]
    State: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RoutesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RoutesDefinition"]:
        if not json_data:
            return None
        return cls(
            DestinationCidrBlock=json_data.get("DestinationCidrBlock"),
            Source=json_data.get("Source"),
            State=json_data.get("State"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RoutesDefinition = RoutesDefinition


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class VgwTelemetryDefinition(BaseModel):
    AcceptedRouteCount: Optional[float]
    LastStatusChange: Optional[str]
    OutsideIpAddress: Optional[str]
    Status: Optional[str]
    StatusMessage: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VgwTelemetryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VgwTelemetryDefinition"]:
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
_VgwTelemetryDefinition = VgwTelemetryDefinition


