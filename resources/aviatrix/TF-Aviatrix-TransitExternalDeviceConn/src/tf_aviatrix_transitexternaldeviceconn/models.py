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
    ApprovedCidrs: Optional[Sequence[str]]
    BackupBgpRemoteAsNum: Optional[str]
    BackupDirectConnect: Optional[bool]
    BackupLocalLanIp: Optional[str]
    BackupLocalTunnelCidr: Optional[str]
    BackupPreSharedKey: Optional[str]
    BackupRemoteGatewayIp: Optional[str]
    BackupRemoteLanIp: Optional[str]
    BackupRemoteTunnelCidr: Optional[str]
    BgpLocalAsNum: Optional[str]
    BgpRemoteAsNum: Optional[str]
    ConnectionName: Optional[str]
    ConnectionType: Optional[str]
    CustomAlgorithms: Optional[bool]
    DirectConnect: Optional[bool]
    EnableEdgeSegmentation: Optional[bool]
    EnableEventTriggeredHa: Optional[bool]
    EnableIkev2: Optional[bool]
    EnableLearnedCidrsApproval: Optional[bool]
    GwName: Optional[str]
    HaEnabled: Optional[bool]
    Id: Optional[str]
    LocalLanIp: Optional[str]
    LocalTunnelCidr: Optional[str]
    ManualBgpAdvertisedCidrs: Optional[Sequence[str]]
    Phase1RemoteIdentifier: Optional[Sequence[str]]
    Phase1Authentication: Optional[str]
    Phase1DhGroups: Optional[str]
    Phase1Encryption: Optional[str]
    Phase2Authentication: Optional[str]
    Phase2DhGroups: Optional[str]
    Phase2Encryption: Optional[str]
    PreSharedKey: Optional[str]
    RemoteGatewayIp: Optional[str]
    RemoteLanIp: Optional[str]
    RemoteSubnet: Optional[str]
    RemoteTunnelCidr: Optional[str]
    RemoteVpcName: Optional[str]
    SwitchToHaStandbyGateway: Optional[bool]
    TunnelProtocol: Optional[str]
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
            ApprovedCidrs=json_data.get("ApprovedCidrs"),
            BackupBgpRemoteAsNum=json_data.get("BackupBgpRemoteAsNum"),
            BackupDirectConnect=json_data.get("BackupDirectConnect"),
            BackupLocalLanIp=json_data.get("BackupLocalLanIp"),
            BackupLocalTunnelCidr=json_data.get("BackupLocalTunnelCidr"),
            BackupPreSharedKey=json_data.get("BackupPreSharedKey"),
            BackupRemoteGatewayIp=json_data.get("BackupRemoteGatewayIp"),
            BackupRemoteLanIp=json_data.get("BackupRemoteLanIp"),
            BackupRemoteTunnelCidr=json_data.get("BackupRemoteTunnelCidr"),
            BgpLocalAsNum=json_data.get("BgpLocalAsNum"),
            BgpRemoteAsNum=json_data.get("BgpRemoteAsNum"),
            ConnectionName=json_data.get("ConnectionName"),
            ConnectionType=json_data.get("ConnectionType"),
            CustomAlgorithms=json_data.get("CustomAlgorithms"),
            DirectConnect=json_data.get("DirectConnect"),
            EnableEdgeSegmentation=json_data.get("EnableEdgeSegmentation"),
            EnableEventTriggeredHa=json_data.get("EnableEventTriggeredHa"),
            EnableIkev2=json_data.get("EnableIkev2"),
            EnableLearnedCidrsApproval=json_data.get("EnableLearnedCidrsApproval"),
            GwName=json_data.get("GwName"),
            HaEnabled=json_data.get("HaEnabled"),
            Id=json_data.get("Id"),
            LocalLanIp=json_data.get("LocalLanIp"),
            LocalTunnelCidr=json_data.get("LocalTunnelCidr"),
            ManualBgpAdvertisedCidrs=json_data.get("ManualBgpAdvertisedCidrs"),
            Phase1RemoteIdentifier=json_data.get("Phase1RemoteIdentifier"),
            Phase1Authentication=json_data.get("Phase1Authentication"),
            Phase1DhGroups=json_data.get("Phase1DhGroups"),
            Phase1Encryption=json_data.get("Phase1Encryption"),
            Phase2Authentication=json_data.get("Phase2Authentication"),
            Phase2DhGroups=json_data.get("Phase2DhGroups"),
            Phase2Encryption=json_data.get("Phase2Encryption"),
            PreSharedKey=json_data.get("PreSharedKey"),
            RemoteGatewayIp=json_data.get("RemoteGatewayIp"),
            RemoteLanIp=json_data.get("RemoteLanIp"),
            RemoteSubnet=json_data.get("RemoteSubnet"),
            RemoteTunnelCidr=json_data.get("RemoteTunnelCidr"),
            RemoteVpcName=json_data.get("RemoteVpcName"),
            SwitchToHaStandbyGateway=json_data.get("SwitchToHaStandbyGateway"),
            TunnelProtocol=json_data.get("TunnelProtocol"),
            VpcId=json_data.get("VpcId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


