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
    AkIkeGateway: Optional[str]
    AkIpsecCryptoProfile: Optional[str]
    AntiReplay: Optional[bool]
    CopyFlowLabel: Optional[bool]
    CopyTos: Optional[bool]
    Disabled: Optional[bool]
    EnableIpv6: Optional[bool]
    EnableTunnelMonitor: Optional[bool]
    GpsCertificateProfile: Optional[str]
    GpsInterface: Optional[str]
    GpsInterfaceFloatingIpIpv4: Optional[str]
    GpsInterfaceFloatingIpIpv6: Optional[str]
    GpsInterfaceIpIpv4: Optional[str]
    GpsInterfaceIpIpv6: Optional[str]
    GpsLocalCertificate: Optional[str]
    GpsPortalAddress: Optional[str]
    GpsPreferIpv6: Optional[bool]
    GpsPublishConnectedRoutes: Optional[bool]
    GpsPublishRoutes: Optional[Sequence[str]]
    Id: Optional[str]
    MkAuthKey: Optional[str]
    MkAuthKeyEnc: Optional[str]
    MkAuthType: Optional[str]
    MkEspEncryptionKey: Optional[str]
    MkEspEncryptionKeyEnc: Optional[str]
    MkEspEncryptionType: Optional[str]
    MkInterface: Optional[str]
    MkLocalAddressFloatingIp: Optional[str]
    MkLocalAddressIp: Optional[str]
    MkLocalSpi: Optional[str]
    MkProtocol: Optional[str]
    MkRemoteAddress: Optional[str]
    MkRemoteSpi: Optional[str]
    Name: Optional[str]
    Template: Optional[str]
    TunnelInterface: Optional[str]
    TunnelMonitorDestinationIp: Optional[str]
    TunnelMonitorProfile: Optional[str]
    TunnelMonitorProxyId: Optional[str]
    TunnelMonitorSourceIp: Optional[str]
    Type: Optional[str]

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
            AkIkeGateway=json_data.get("AkIkeGateway"),
            AkIpsecCryptoProfile=json_data.get("AkIpsecCryptoProfile"),
            AntiReplay=json_data.get("AntiReplay"),
            CopyFlowLabel=json_data.get("CopyFlowLabel"),
            CopyTos=json_data.get("CopyTos"),
            Disabled=json_data.get("Disabled"),
            EnableIpv6=json_data.get("EnableIpv6"),
            EnableTunnelMonitor=json_data.get("EnableTunnelMonitor"),
            GpsCertificateProfile=json_data.get("GpsCertificateProfile"),
            GpsInterface=json_data.get("GpsInterface"),
            GpsInterfaceFloatingIpIpv4=json_data.get("GpsInterfaceFloatingIpIpv4"),
            GpsInterfaceFloatingIpIpv6=json_data.get("GpsInterfaceFloatingIpIpv6"),
            GpsInterfaceIpIpv4=json_data.get("GpsInterfaceIpIpv4"),
            GpsInterfaceIpIpv6=json_data.get("GpsInterfaceIpIpv6"),
            GpsLocalCertificate=json_data.get("GpsLocalCertificate"),
            GpsPortalAddress=json_data.get("GpsPortalAddress"),
            GpsPreferIpv6=json_data.get("GpsPreferIpv6"),
            GpsPublishConnectedRoutes=json_data.get("GpsPublishConnectedRoutes"),
            GpsPublishRoutes=json_data.get("GpsPublishRoutes"),
            Id=json_data.get("Id"),
            MkAuthKey=json_data.get("MkAuthKey"),
            MkAuthKeyEnc=json_data.get("MkAuthKeyEnc"),
            MkAuthType=json_data.get("MkAuthType"),
            MkEspEncryptionKey=json_data.get("MkEspEncryptionKey"),
            MkEspEncryptionKeyEnc=json_data.get("MkEspEncryptionKeyEnc"),
            MkEspEncryptionType=json_data.get("MkEspEncryptionType"),
            MkInterface=json_data.get("MkInterface"),
            MkLocalAddressFloatingIp=json_data.get("MkLocalAddressFloatingIp"),
            MkLocalAddressIp=json_data.get("MkLocalAddressIp"),
            MkLocalSpi=json_data.get("MkLocalSpi"),
            MkProtocol=json_data.get("MkProtocol"),
            MkRemoteAddress=json_data.get("MkRemoteAddress"),
            MkRemoteSpi=json_data.get("MkRemoteSpi"),
            Name=json_data.get("Name"),
            Template=json_data.get("Template"),
            TunnelInterface=json_data.get("TunnelInterface"),
            TunnelMonitorDestinationIp=json_data.get("TunnelMonitorDestinationIp"),
            TunnelMonitorProfile=json_data.get("TunnelMonitorProfile"),
            TunnelMonitorProxyId=json_data.get("TunnelMonitorProxyId"),
            TunnelMonitorSourceIp=json_data.get("TunnelMonitorSourceIp"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


