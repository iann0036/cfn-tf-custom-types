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
    CloudInstanceId: Optional[str]
    CloudType: Optional[float]
    CustomerManagedKeys: Optional[str]
    CustomizedSpokeVpcRoutes: Optional[str]
    Eip: Optional[str]
    EnableActiveMesh: Optional[bool]
    EnableAutoAdvertiseS2cCidrs: Optional[bool]
    EnableEncryptVolume: Optional[bool]
    EnableJumboFrame: Optional[bool]
    EnableMonitorGatewaySubnets: Optional[bool]
    EnablePrivateOob: Optional[bool]
    EnablePrivateVpcDefaultRoute: Optional[bool]
    EnableSkipPublicRouteTableUpdate: Optional[bool]
    EnableVpcDnsServer: Optional[bool]
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
    HaOobAvailabilityZone: Optional[str]
    HaOobManagementSubnet: Optional[str]
    HaPrivateIp: Optional[str]
    HaSubnet: Optional[str]
    HaZone: Optional[str]
    Id: Optional[str]
    IncludedAdvertisedSpokeRoutes: Optional[str]
    InsaneMode: Optional[bool]
    InsaneModeAz: Optional[str]
    ManageTransitGatewayAttachment: Optional[bool]
    MonitorExcludeList: Optional[Sequence[str]]
    OobAvailabilityZone: Optional[str]
    OobManagementSubnet: Optional[str]
    PrivateIp: Optional[str]
    SecurityGroupId: Optional[str]
    SingleAzHa: Optional[bool]
    SingleIpSnat: Optional[bool]
    StorageName: Optional[str]
    Subnet: Optional[str]
    TagList: Optional[Sequence[str]]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TransitGw: Optional[str]
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
            CloudInstanceId=json_data.get("CloudInstanceId"),
            CloudType=json_data.get("CloudType"),
            CustomerManagedKeys=json_data.get("CustomerManagedKeys"),
            CustomizedSpokeVpcRoutes=json_data.get("CustomizedSpokeVpcRoutes"),
            Eip=json_data.get("Eip"),
            EnableActiveMesh=json_data.get("EnableActiveMesh"),
            EnableAutoAdvertiseS2cCidrs=json_data.get("EnableAutoAdvertiseS2cCidrs"),
            EnableEncryptVolume=json_data.get("EnableEncryptVolume"),
            EnableJumboFrame=json_data.get("EnableJumboFrame"),
            EnableMonitorGatewaySubnets=json_data.get("EnableMonitorGatewaySubnets"),
            EnablePrivateOob=json_data.get("EnablePrivateOob"),
            EnablePrivateVpcDefaultRoute=json_data.get("EnablePrivateVpcDefaultRoute"),
            EnableSkipPublicRouteTableUpdate=json_data.get("EnableSkipPublicRouteTableUpdate"),
            EnableVpcDnsServer=json_data.get("EnableVpcDnsServer"),
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
            HaOobAvailabilityZone=json_data.get("HaOobAvailabilityZone"),
            HaOobManagementSubnet=json_data.get("HaOobManagementSubnet"),
            HaPrivateIp=json_data.get("HaPrivateIp"),
            HaSubnet=json_data.get("HaSubnet"),
            HaZone=json_data.get("HaZone"),
            Id=json_data.get("Id"),
            IncludedAdvertisedSpokeRoutes=json_data.get("IncludedAdvertisedSpokeRoutes"),
            InsaneMode=json_data.get("InsaneMode"),
            InsaneModeAz=json_data.get("InsaneModeAz"),
            ManageTransitGatewayAttachment=json_data.get("ManageTransitGatewayAttachment"),
            MonitorExcludeList=json_data.get("MonitorExcludeList"),
            OobAvailabilityZone=json_data.get("OobAvailabilityZone"),
            OobManagementSubnet=json_data.get("OobManagementSubnet"),
            PrivateIp=json_data.get("PrivateIp"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            SingleAzHa=json_data.get("SingleAzHa"),
            SingleIpSnat=json_data.get("SingleIpSnat"),
            StorageName=json_data.get("StorageName"),
            Subnet=json_data.get("Subnet"),
            TagList=json_data.get("TagList"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TransitGw=json_data.get("TransitGw"),
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


