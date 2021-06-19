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
    AccountName: Optional[str]
    AllocateNewEip: Optional[bool]
    AvailabilityDomain: Optional[str]
    BgpEcmp: Optional[bool]
    BgpHoldTime: Optional[float]
    BgpManualSpokeAdvertiseCidrs: Optional[str]
    BgpPollingTime: Optional[str]
    CloudInstanceId: Optional[str]
    CloudType: Optional[float]
    ConnectedTransit: Optional[bool]
    CustomerManagedKeys: Optional[str]
    CustomizedSpokeVpcRoutes: Optional[str]
    CustomizedTransitVpcRoutes: Optional[Sequence[str]]
    Eip: Optional[str]
    EnableActiveMesh: Optional[bool]
    EnableActiveStandby: Optional[bool]
    EnableAdvertiseTransitCidr: Optional[bool]
    EnableBgpOverLan: Optional[bool]
    EnableEgressTransitFirenet: Optional[bool]
    EnableEncryptVolume: Optional[bool]
    EnableFirenet: Optional[bool]
    EnableGatewayLoadBalancer: Optional[bool]
    EnableHybridConnection: Optional[bool]
    EnableJumboFrame: Optional[bool]
    EnableLearnedCidrsApproval: Optional[bool]
    EnableMonitorGatewaySubnets: Optional[bool]
    EnableMultiTierTransit: Optional[bool]
    EnablePrivateOob: Optional[bool]
    EnableSegmentation: Optional[bool]
    EnableTransitFirenet: Optional[bool]
    EnableTransitSummarizeCidrToTgw: Optional[bool]
    EnableVpcDnsServer: Optional[bool]
    ExcludedAdvertisedSpokeRoutes: Optional[str]
    FaultDomain: Optional[str]
    FilteredSpokeVpcRoutes: Optional[str]
    GwName: Optional[str]
    GwSize: Optional[str]
    HaAvailabilityDomain: Optional[str]
    HaCloudInstanceId: Optional[str]
    HaEip: Optional[str]
    HaFaultDomain: Optional[str]
    HaGwName: Optional[str]
    HaGwSize: Optional[str]
    HaInsaneModeAz: Optional[str]
    HaLanInterfaceCidr: Optional[str]
    HaOobAvailabilityZone: Optional[str]
    HaOobManagementSubnet: Optional[str]
    HaPrivateIp: Optional[str]
    HaSubnet: Optional[str]
    HaZone: Optional[str]
    Id: Optional[str]
    InsaneMode: Optional[bool]
    InsaneModeAz: Optional[str]
    LanInterfaceCidr: Optional[str]
    LanPrivateSubnet: Optional[str]
    LanVpcId: Optional[str]
    LearnedCidrsApprovalMode: Optional[str]
    LocalAsNumber: Optional[str]
    MonitorExcludeList: Optional[Sequence[str]]
    OobAvailabilityZone: Optional[str]
    OobManagementSubnet: Optional[str]
    PrependAsPath: Optional[Sequence[str]]
    PrivateIp: Optional[str]
    SecurityGroupId: Optional[str]
    SingleAzHa: Optional[bool]
    SingleIpSnat: Optional[bool]
    StorageName: Optional[str]
    Subnet: Optional[str]
    TagList: Optional[Sequence[str]]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TunnelDetectionTime: Optional[float]
    VpcId: Optional[str]
    VpcReg: Optional[str]
    Zone: Optional[str]

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
            AccountName=json_data.get("AccountName"),
            AllocateNewEip=json_data.get("AllocateNewEip"),
            AvailabilityDomain=json_data.get("AvailabilityDomain"),
            BgpEcmp=json_data.get("BgpEcmp"),
            BgpHoldTime=json_data.get("BgpHoldTime"),
            BgpManualSpokeAdvertiseCidrs=json_data.get("BgpManualSpokeAdvertiseCidrs"),
            BgpPollingTime=json_data.get("BgpPollingTime"),
            CloudInstanceId=json_data.get("CloudInstanceId"),
            CloudType=json_data.get("CloudType"),
            ConnectedTransit=json_data.get("ConnectedTransit"),
            CustomerManagedKeys=json_data.get("CustomerManagedKeys"),
            CustomizedSpokeVpcRoutes=json_data.get("CustomizedSpokeVpcRoutes"),
            CustomizedTransitVpcRoutes=json_data.get("CustomizedTransitVpcRoutes"),
            Eip=json_data.get("Eip"),
            EnableActiveMesh=json_data.get("EnableActiveMesh"),
            EnableActiveStandby=json_data.get("EnableActiveStandby"),
            EnableAdvertiseTransitCidr=json_data.get("EnableAdvertiseTransitCidr"),
            EnableBgpOverLan=json_data.get("EnableBgpOverLan"),
            EnableEgressTransitFirenet=json_data.get("EnableEgressTransitFirenet"),
            EnableEncryptVolume=json_data.get("EnableEncryptVolume"),
            EnableFirenet=json_data.get("EnableFirenet"),
            EnableGatewayLoadBalancer=json_data.get("EnableGatewayLoadBalancer"),
            EnableHybridConnection=json_data.get("EnableHybridConnection"),
            EnableJumboFrame=json_data.get("EnableJumboFrame"),
            EnableLearnedCidrsApproval=json_data.get("EnableLearnedCidrsApproval"),
            EnableMonitorGatewaySubnets=json_data.get("EnableMonitorGatewaySubnets"),
            EnableMultiTierTransit=json_data.get("EnableMultiTierTransit"),
            EnablePrivateOob=json_data.get("EnablePrivateOob"),
            EnableSegmentation=json_data.get("EnableSegmentation"),
            EnableTransitFirenet=json_data.get("EnableTransitFirenet"),
            EnableTransitSummarizeCidrToTgw=json_data.get("EnableTransitSummarizeCidrToTgw"),
            EnableVpcDnsServer=json_data.get("EnableVpcDnsServer"),
            ExcludedAdvertisedSpokeRoutes=json_data.get("ExcludedAdvertisedSpokeRoutes"),
            FaultDomain=json_data.get("FaultDomain"),
            FilteredSpokeVpcRoutes=json_data.get("FilteredSpokeVpcRoutes"),
            GwName=json_data.get("GwName"),
            GwSize=json_data.get("GwSize"),
            HaAvailabilityDomain=json_data.get("HaAvailabilityDomain"),
            HaCloudInstanceId=json_data.get("HaCloudInstanceId"),
            HaEip=json_data.get("HaEip"),
            HaFaultDomain=json_data.get("HaFaultDomain"),
            HaGwName=json_data.get("HaGwName"),
            HaGwSize=json_data.get("HaGwSize"),
            HaInsaneModeAz=json_data.get("HaInsaneModeAz"),
            HaLanInterfaceCidr=json_data.get("HaLanInterfaceCidr"),
            HaOobAvailabilityZone=json_data.get("HaOobAvailabilityZone"),
            HaOobManagementSubnet=json_data.get("HaOobManagementSubnet"),
            HaPrivateIp=json_data.get("HaPrivateIp"),
            HaSubnet=json_data.get("HaSubnet"),
            HaZone=json_data.get("HaZone"),
            Id=json_data.get("Id"),
            InsaneMode=json_data.get("InsaneMode"),
            InsaneModeAz=json_data.get("InsaneModeAz"),
            LanInterfaceCidr=json_data.get("LanInterfaceCidr"),
            LanPrivateSubnet=json_data.get("LanPrivateSubnet"),
            LanVpcId=json_data.get("LanVpcId"),
            LearnedCidrsApprovalMode=json_data.get("LearnedCidrsApprovalMode"),
            LocalAsNumber=json_data.get("LocalAsNumber"),
            MonitorExcludeList=json_data.get("MonitorExcludeList"),
            OobAvailabilityZone=json_data.get("OobAvailabilityZone"),
            OobManagementSubnet=json_data.get("OobManagementSubnet"),
            PrependAsPath=json_data.get("PrependAsPath"),
            PrivateIp=json_data.get("PrivateIp"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            SingleAzHa=json_data.get("SingleAzHa"),
            SingleIpSnat=json_data.get("SingleIpSnat"),
            StorageName=json_data.get("StorageName"),
            Subnet=json_data.get("Subnet"),
            TagList=json_data.get("TagList"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TunnelDetectionTime=json_data.get("TunnelDetectionTime"),
            VpcId=json_data.get("VpcId"),
            VpcReg=json_data.get("VpcReg"),
            Zone=json_data.get("Zone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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


