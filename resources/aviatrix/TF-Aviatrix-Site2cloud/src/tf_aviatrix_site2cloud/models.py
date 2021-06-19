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
    BackupGatewayName: Optional[str]
    BackupLocalTunnelIp: Optional[str]
    BackupPreSharedKey: Optional[str]
    BackupRemoteGatewayIp: Optional[str]
    BackupRemoteGatewayLatitude: Optional[float]
    BackupRemoteGatewayLongitude: Optional[float]
    BackupRemoteTunnelIp: Optional[str]
    ConnectionName: Optional[str]
    ConnectionType: Optional[str]
    CustomAlgorithms: Optional[bool]
    CustomMapped: Optional[bool]
    EnableActiveActive: Optional[bool]
    EnableDeadPeerDetection: Optional[bool]
    EnableEventTriggeredHa: Optional[bool]
    EnableIkev2: Optional[bool]
    EnableSingleIpHa: Optional[bool]
    ForwardTrafficToTransit: Optional[bool]
    HaEnabled: Optional[bool]
    Id: Optional[str]
    LocalDestinationRealCidrs: Optional[Sequence[str]]
    LocalDestinationVirtualCidrs: Optional[Sequence[str]]
    LocalSourceRealCidrs: Optional[Sequence[str]]
    LocalSourceVirtualCidrs: Optional[Sequence[str]]
    LocalSubnetCidr: Optional[str]
    LocalSubnetVirtual: Optional[str]
    LocalTunnelIp: Optional[str]
    Phase1RemoteIdentifier: Optional[Sequence[str]]
    Phase1Authentication: Optional[str]
    Phase1DhGroups: Optional[str]
    Phase1Encryption: Optional[str]
    Phase2Authentication: Optional[str]
    Phase2DhGroups: Optional[str]
    Phase2Encryption: Optional[str]
    PreSharedKey: Optional[str]
    PrimaryCloudGatewayName: Optional[str]
    PrivateRouteEncryption: Optional[bool]
    RemoteDestinationRealCidrs: Optional[Sequence[str]]
    RemoteDestinationVirtualCidrs: Optional[Sequence[str]]
    RemoteGatewayIp: Optional[str]
    RemoteGatewayLatitude: Optional[float]
    RemoteGatewayLongitude: Optional[float]
    RemoteGatewayType: Optional[str]
    RemoteSourceRealCidrs: Optional[Sequence[str]]
    RemoteSourceVirtualCidrs: Optional[Sequence[str]]
    RemoteSubnetCidr: Optional[str]
    RemoteSubnetVirtual: Optional[str]
    RemoteTunnelIp: Optional[str]
    RouteTableList: Optional[Sequence[str]]
    SslServerPool: Optional[str]
    TunnelType: Optional[str]
    VpcId: Optional[str]

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
            BackupGatewayName=json_data.get("BackupGatewayName"),
            BackupLocalTunnelIp=json_data.get("BackupLocalTunnelIp"),
            BackupPreSharedKey=json_data.get("BackupPreSharedKey"),
            BackupRemoteGatewayIp=json_data.get("BackupRemoteGatewayIp"),
            BackupRemoteGatewayLatitude=json_data.get("BackupRemoteGatewayLatitude"),
            BackupRemoteGatewayLongitude=json_data.get("BackupRemoteGatewayLongitude"),
            BackupRemoteTunnelIp=json_data.get("BackupRemoteTunnelIp"),
            ConnectionName=json_data.get("ConnectionName"),
            ConnectionType=json_data.get("ConnectionType"),
            CustomAlgorithms=json_data.get("CustomAlgorithms"),
            CustomMapped=json_data.get("CustomMapped"),
            EnableActiveActive=json_data.get("EnableActiveActive"),
            EnableDeadPeerDetection=json_data.get("EnableDeadPeerDetection"),
            EnableEventTriggeredHa=json_data.get("EnableEventTriggeredHa"),
            EnableIkev2=json_data.get("EnableIkev2"),
            EnableSingleIpHa=json_data.get("EnableSingleIpHa"),
            ForwardTrafficToTransit=json_data.get("ForwardTrafficToTransit"),
            HaEnabled=json_data.get("HaEnabled"),
            Id=json_data.get("Id"),
            LocalDestinationRealCidrs=json_data.get("LocalDestinationRealCidrs"),
            LocalDestinationVirtualCidrs=json_data.get("LocalDestinationVirtualCidrs"),
            LocalSourceRealCidrs=json_data.get("LocalSourceRealCidrs"),
            LocalSourceVirtualCidrs=json_data.get("LocalSourceVirtualCidrs"),
            LocalSubnetCidr=json_data.get("LocalSubnetCidr"),
            LocalSubnetVirtual=json_data.get("LocalSubnetVirtual"),
            LocalTunnelIp=json_data.get("LocalTunnelIp"),
            Phase1RemoteIdentifier=json_data.get("Phase1RemoteIdentifier"),
            Phase1Authentication=json_data.get("Phase1Authentication"),
            Phase1DhGroups=json_data.get("Phase1DhGroups"),
            Phase1Encryption=json_data.get("Phase1Encryption"),
            Phase2Authentication=json_data.get("Phase2Authentication"),
            Phase2DhGroups=json_data.get("Phase2DhGroups"),
            Phase2Encryption=json_data.get("Phase2Encryption"),
            PreSharedKey=json_data.get("PreSharedKey"),
            PrimaryCloudGatewayName=json_data.get("PrimaryCloudGatewayName"),
            PrivateRouteEncryption=json_data.get("PrivateRouteEncryption"),
            RemoteDestinationRealCidrs=json_data.get("RemoteDestinationRealCidrs"),
            RemoteDestinationVirtualCidrs=json_data.get("RemoteDestinationVirtualCidrs"),
            RemoteGatewayIp=json_data.get("RemoteGatewayIp"),
            RemoteGatewayLatitude=json_data.get("RemoteGatewayLatitude"),
            RemoteGatewayLongitude=json_data.get("RemoteGatewayLongitude"),
            RemoteGatewayType=json_data.get("RemoteGatewayType"),
            RemoteSourceRealCidrs=json_data.get("RemoteSourceRealCidrs"),
            RemoteSourceVirtualCidrs=json_data.get("RemoteSourceVirtualCidrs"),
            RemoteSubnetCidr=json_data.get("RemoteSubnetCidr"),
            RemoteSubnetVirtual=json_data.get("RemoteSubnetVirtual"),
            RemoteTunnelIp=json_data.get("RemoteTunnelIp"),
            RouteTableList=json_data.get("RouteTableList"),
            SslServerPool=json_data.get("SslServerPool"),
            TunnelType=json_data.get("TunnelType"),
            VpcId=json_data.get("VpcId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


