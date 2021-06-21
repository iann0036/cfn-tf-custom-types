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
    Address: Optional[str]
    Annotations: Optional[Sequence["_AnnotationsDefinition"]]
    Description: Optional[str]
    Disable: Optional[bool]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    LogsStreamingDisabled: Optional[bool]
    Name: Optional[str]
    Namespace: Optional[str]
    AwsParameters: Optional[Sequence["_AwsParametersDefinition"]]
    Coordinates: Optional[Sequence["_CoordinatesDefinition"]]
    LogReceiver: Optional[Sequence["_LogReceiverDefinition"]]
    Os: Optional[Sequence["_OsDefinition"]]
    Sw: Optional[Sequence["_SwDefinition"]]
    TgwSecurity: Optional[Sequence["_TgwSecurityDefinition"]]
    VnConfig: Optional[Sequence["_VnConfigDefinition"]]
    VpcAttachments: Optional[Sequence["_VpcAttachmentsDefinition"]]

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
            Address=json_data.get("Address"),
            Annotations=deserialize_list(json_data.get("Annotations"), AnnotationsDefinition),
            Description=json_data.get("Description"),
            Disable=json_data.get("Disable"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            LogsStreamingDisabled=json_data.get("LogsStreamingDisabled"),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            AwsParameters=deserialize_list(json_data.get("AwsParameters"), AwsParametersDefinition),
            Coordinates=deserialize_list(json_data.get("Coordinates"), CoordinatesDefinition),
            LogReceiver=deserialize_list(json_data.get("LogReceiver"), LogReceiverDefinition),
            Os=deserialize_list(json_data.get("Os"), OsDefinition),
            Sw=deserialize_list(json_data.get("Sw"), SwDefinition),
            TgwSecurity=deserialize_list(json_data.get("TgwSecurity"), TgwSecurityDefinition),
            VnConfig=deserialize_list(json_data.get("VnConfig"), VnConfigDefinition),
            VpcAttachments=deserialize_list(json_data.get("VpcAttachments"), VpcAttachmentsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AnnotationsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnnotationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnnotationsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnnotationsDefinition = AnnotationsDefinition


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class AwsParametersDefinition(BaseModel):
    Assisted: Optional[bool]
    AwsCertifiedHw: Optional[str]
    AwsRegion: Optional[str]
    DiskSize: Optional[float]
    InstanceType: Optional[str]
    NodesPerAz: Optional[float]
    SshKey: Optional[str]
    VpcId: Optional[str]
    AwsCred: Optional[Sequence["_AwsCredDefinition"]]
    AzNodes: Optional[Sequence["_AzNodesDefinition"]]
    ExistingTgw: Optional[Sequence["_ExistingTgwDefinition"]]
    NewTgw: Optional[Sequence["_NewTgwDefinition"]]
    NewVpc: Optional[Sequence["_NewVpcDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            Assisted=json_data.get("Assisted"),
            AwsCertifiedHw=json_data.get("AwsCertifiedHw"),
            AwsRegion=json_data.get("AwsRegion"),
            DiskSize=json_data.get("DiskSize"),
            InstanceType=json_data.get("InstanceType"),
            NodesPerAz=json_data.get("NodesPerAz"),
            SshKey=json_data.get("SshKey"),
            VpcId=json_data.get("VpcId"),
            AwsCred=deserialize_list(json_data.get("AwsCred"), AwsCredDefinition),
            AzNodes=deserialize_list(json_data.get("AzNodes"), AzNodesDefinition),
            ExistingTgw=deserialize_list(json_data.get("ExistingTgw"), ExistingTgwDefinition),
            NewTgw=deserialize_list(json_data.get("NewTgw"), NewTgwDefinition),
            NewVpc=deserialize_list(json_data.get("NewVpc"), NewVpcDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsParametersDefinition = AwsParametersDefinition


@dataclass
class AwsCredDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCredDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCredDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCredDefinition = AwsCredDefinition


@dataclass
class AzNodesDefinition(BaseModel):
    AwsAzName: Optional[str]
    DiskSize: Optional[float]
    ReservedInsideSubnet: Optional[bool]
    InsideSubnet: Optional[Sequence["_InsideSubnetDefinition"]]
    OutsideSubnet: Optional[Sequence["_OutsideSubnetDefinition"]]
    WorkloadSubnet: Optional[Sequence["_WorkloadSubnetDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AzNodesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzNodesDefinition"]:
        if not json_data:
            return None
        return cls(
            AwsAzName=json_data.get("AwsAzName"),
            DiskSize=json_data.get("DiskSize"),
            ReservedInsideSubnet=json_data.get("ReservedInsideSubnet"),
            InsideSubnet=deserialize_list(json_data.get("InsideSubnet"), InsideSubnetDefinition),
            OutsideSubnet=deserialize_list(json_data.get("OutsideSubnet"), OutsideSubnetDefinition),
            WorkloadSubnet=deserialize_list(json_data.get("WorkloadSubnet"), WorkloadSubnetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzNodesDefinition = AzNodesDefinition


@dataclass
class InsideSubnetDefinition(BaseModel):
    ExistingSubnetId: Optional[str]
    SubnetParam: Optional[Sequence["_SubnetParamDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InsideSubnetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InsideSubnetDefinition"]:
        if not json_data:
            return None
        return cls(
            ExistingSubnetId=json_data.get("ExistingSubnetId"),
            SubnetParam=deserialize_list(json_data.get("SubnetParam"), SubnetParamDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InsideSubnetDefinition = InsideSubnetDefinition


@dataclass
class SubnetParamDefinition(BaseModel):
    Ipv4: Optional[str]
    Ipv6: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SubnetParamDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubnetParamDefinition"]:
        if not json_data:
            return None
        return cls(
            Ipv4=json_data.get("Ipv4"),
            Ipv6=json_data.get("Ipv6"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubnetParamDefinition = SubnetParamDefinition


@dataclass
class OutsideSubnetDefinition(BaseModel):
    ExistingSubnetId: Optional[str]
    SubnetParam: Optional[Sequence["_SubnetParamDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OutsideSubnetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutsideSubnetDefinition"]:
        if not json_data:
            return None
        return cls(
            ExistingSubnetId=json_data.get("ExistingSubnetId"),
            SubnetParam=deserialize_list(json_data.get("SubnetParam"), SubnetParamDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutsideSubnetDefinition = OutsideSubnetDefinition


@dataclass
class WorkloadSubnetDefinition(BaseModel):
    ExistingSubnetId: Optional[str]
    SubnetParam: Optional[Sequence["_SubnetParamDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WorkloadSubnetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkloadSubnetDefinition"]:
        if not json_data:
            return None
        return cls(
            ExistingSubnetId=json_data.get("ExistingSubnetId"),
            SubnetParam=deserialize_list(json_data.get("SubnetParam"), SubnetParamDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkloadSubnetDefinition = WorkloadSubnetDefinition


@dataclass
class ExistingTgwDefinition(BaseModel):
    TgwAsn: Optional[float]
    TgwId: Optional[str]
    VolterraSiteAsn: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ExistingTgwDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExistingTgwDefinition"]:
        if not json_data:
            return None
        return cls(
            TgwAsn=json_data.get("TgwAsn"),
            TgwId=json_data.get("TgwId"),
            VolterraSiteAsn=json_data.get("VolterraSiteAsn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExistingTgwDefinition = ExistingTgwDefinition


@dataclass
class NewTgwDefinition(BaseModel):
    SystemGenerated: Optional[bool]
    UserAssigned: Optional[Sequence["_UserAssignedDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NewTgwDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NewTgwDefinition"]:
        if not json_data:
            return None
        return cls(
            SystemGenerated=json_data.get("SystemGenerated"),
            UserAssigned=deserialize_list(json_data.get("UserAssigned"), UserAssignedDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NewTgwDefinition = NewTgwDefinition


@dataclass
class UserAssignedDefinition(BaseModel):
    TgwAsn: Optional[float]
    VolterraSiteAsn: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_UserAssignedDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserAssignedDefinition"]:
        if not json_data:
            return None
        return cls(
            TgwAsn=json_data.get("TgwAsn"),
            VolterraSiteAsn=json_data.get("VolterraSiteAsn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserAssignedDefinition = UserAssignedDefinition


@dataclass
class NewVpcDefinition(BaseModel):
    AllocateIpv6: Optional[bool]
    Autogenerate: Optional[bool]
    NameTag: Optional[str]
    PrimaryIpv4: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NewVpcDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NewVpcDefinition"]:
        if not json_data:
            return None
        return cls(
            AllocateIpv6=json_data.get("AllocateIpv6"),
            Autogenerate=json_data.get("Autogenerate"),
            NameTag=json_data.get("NameTag"),
            PrimaryIpv4=json_data.get("PrimaryIpv4"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NewVpcDefinition = NewVpcDefinition


@dataclass
class CoordinatesDefinition(BaseModel):
    Latitude: Optional[float]
    Longitude: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CoordinatesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CoordinatesDefinition"]:
        if not json_data:
            return None
        return cls(
            Latitude=json_data.get("Latitude"),
            Longitude=json_data.get("Longitude"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CoordinatesDefinition = CoordinatesDefinition


@dataclass
class LogReceiverDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LogReceiverDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogReceiverDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogReceiverDefinition = LogReceiverDefinition


@dataclass
class OsDefinition(BaseModel):
    DefaultOsVersion: Optional[bool]
    OperatingSystemVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OsDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultOsVersion=json_data.get("DefaultOsVersion"),
            OperatingSystemVersion=json_data.get("OperatingSystemVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OsDefinition = OsDefinition


@dataclass
class SwDefinition(BaseModel):
    DefaultSwVersion: Optional[bool]
    VolterraSoftwareVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SwDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SwDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultSwVersion=json_data.get("DefaultSwVersion"),
            VolterraSoftwareVersion=json_data.get("VolterraSoftwareVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SwDefinition = SwDefinition


@dataclass
class TgwSecurityDefinition(BaseModel):
    EastWestServicePolicyAllowAll: Optional[bool]
    ForwardProxyAllowAll: Optional[bool]
    NoEastWestPolicy: Optional[bool]
    NoForwardProxy: Optional[bool]
    NoNetworkPolicy: Optional[bool]
    ActiveEastWestServicePolicies: Optional[Sequence["_ActiveEastWestServicePoliciesDefinition"]]
    ActiveForwardProxyPolicies: Optional[Sequence["_ActiveForwardProxyPoliciesDefinition"]]
    ActiveNetworkPolicies: Optional[Sequence["_ActiveNetworkPoliciesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TgwSecurityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TgwSecurityDefinition"]:
        if not json_data:
            return None
        return cls(
            EastWestServicePolicyAllowAll=json_data.get("EastWestServicePolicyAllowAll"),
            ForwardProxyAllowAll=json_data.get("ForwardProxyAllowAll"),
            NoEastWestPolicy=json_data.get("NoEastWestPolicy"),
            NoForwardProxy=json_data.get("NoForwardProxy"),
            NoNetworkPolicy=json_data.get("NoNetworkPolicy"),
            ActiveEastWestServicePolicies=deserialize_list(json_data.get("ActiveEastWestServicePolicies"), ActiveEastWestServicePoliciesDefinition),
            ActiveForwardProxyPolicies=deserialize_list(json_data.get("ActiveForwardProxyPolicies"), ActiveForwardProxyPoliciesDefinition),
            ActiveNetworkPolicies=deserialize_list(json_data.get("ActiveNetworkPolicies"), ActiveNetworkPoliciesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TgwSecurityDefinition = TgwSecurityDefinition


@dataclass
class ActiveEastWestServicePoliciesDefinition(BaseModel):
    ServicePolicies: Optional[Sequence["_ServicePoliciesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ActiveEastWestServicePoliciesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActiveEastWestServicePoliciesDefinition"]:
        if not json_data:
            return None
        return cls(
            ServicePolicies=deserialize_list(json_data.get("ServicePolicies"), ServicePoliciesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActiveEastWestServicePoliciesDefinition = ActiveEastWestServicePoliciesDefinition


@dataclass
class ServicePoliciesDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServicePoliciesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServicePoliciesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServicePoliciesDefinition = ServicePoliciesDefinition


@dataclass
class ActiveForwardProxyPoliciesDefinition(BaseModel):
    ForwardProxyPolicies: Optional[Sequence["_ForwardProxyPoliciesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ActiveForwardProxyPoliciesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActiveForwardProxyPoliciesDefinition"]:
        if not json_data:
            return None
        return cls(
            ForwardProxyPolicies=deserialize_list(json_data.get("ForwardProxyPolicies"), ForwardProxyPoliciesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActiveForwardProxyPoliciesDefinition = ActiveForwardProxyPoliciesDefinition


@dataclass
class ForwardProxyPoliciesDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ForwardProxyPoliciesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ForwardProxyPoliciesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ForwardProxyPoliciesDefinition = ForwardProxyPoliciesDefinition


@dataclass
class ActiveNetworkPoliciesDefinition(BaseModel):
    NetworkPolicies: Optional[Sequence["_NetworkPoliciesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ActiveNetworkPoliciesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActiveNetworkPoliciesDefinition"]:
        if not json_data:
            return None
        return cls(
            NetworkPolicies=deserialize_list(json_data.get("NetworkPolicies"), NetworkPoliciesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActiveNetworkPoliciesDefinition = ActiveNetworkPoliciesDefinition


@dataclass
class NetworkPoliciesDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkPoliciesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkPoliciesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkPoliciesDefinition = NetworkPoliciesDefinition


@dataclass
class VnConfigDefinition(BaseModel):
    NoGlobalNetwork: Optional[bool]
    NoInsideStaticRoutes: Optional[bool]
    NoOutsideStaticRoutes: Optional[bool]
    AllowedVipPort: Optional[Sequence["_AllowedVipPortDefinition"]]
    GlobalNetworkList: Optional[Sequence["_GlobalNetworkListDefinition"]]
    InsideStaticRoutes: Optional[Sequence["_InsideStaticRoutesDefinition"]]
    OutsideStaticRoutes: Optional[Sequence["_OutsideStaticRoutesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_VnConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VnConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            NoGlobalNetwork=json_data.get("NoGlobalNetwork"),
            NoInsideStaticRoutes=json_data.get("NoInsideStaticRoutes"),
            NoOutsideStaticRoutes=json_data.get("NoOutsideStaticRoutes"),
            AllowedVipPort=deserialize_list(json_data.get("AllowedVipPort"), AllowedVipPortDefinition),
            GlobalNetworkList=deserialize_list(json_data.get("GlobalNetworkList"), GlobalNetworkListDefinition),
            InsideStaticRoutes=deserialize_list(json_data.get("InsideStaticRoutes"), InsideStaticRoutesDefinition),
            OutsideStaticRoutes=deserialize_list(json_data.get("OutsideStaticRoutes"), OutsideStaticRoutesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_VnConfigDefinition = VnConfigDefinition


@dataclass
class AllowedVipPortDefinition(BaseModel):
    UseHttpHttpsPort: Optional[bool]
    UseHttpPort: Optional[bool]
    UseHttpsPort: Optional[bool]
    CustomPorts: Optional[Sequence["_CustomPortsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AllowedVipPortDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AllowedVipPortDefinition"]:
        if not json_data:
            return None
        return cls(
            UseHttpHttpsPort=json_data.get("UseHttpHttpsPort"),
            UseHttpPort=json_data.get("UseHttpPort"),
            UseHttpsPort=json_data.get("UseHttpsPort"),
            CustomPorts=deserialize_list(json_data.get("CustomPorts"), CustomPortsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AllowedVipPortDefinition = AllowedVipPortDefinition


@dataclass
class CustomPortsDefinition(BaseModel):
    PortRanges: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomPortsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomPortsDefinition"]:
        if not json_data:
            return None
        return cls(
            PortRanges=json_data.get("PortRanges"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomPortsDefinition = CustomPortsDefinition


@dataclass
class GlobalNetworkListDefinition(BaseModel):
    GlobalNetworkConnections: Optional[Sequence["_GlobalNetworkConnectionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_GlobalNetworkListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GlobalNetworkListDefinition"]:
        if not json_data:
            return None
        return cls(
            GlobalNetworkConnections=deserialize_list(json_data.get("GlobalNetworkConnections"), GlobalNetworkConnectionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_GlobalNetworkListDefinition = GlobalNetworkListDefinition


@dataclass
class GlobalNetworkConnectionsDefinition(BaseModel):
    DisableForwardProxy: Optional[bool]
    EnableForwardProxy: Optional[Sequence["_EnableForwardProxyDefinition"]]
    SliToGlobalDr: Optional[Sequence["_SliToGlobalDrDefinition"]]
    SloToGlobalDr: Optional[Sequence["_SloToGlobalDrDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_GlobalNetworkConnectionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GlobalNetworkConnectionsDefinition"]:
        if not json_data:
            return None
        return cls(
            DisableForwardProxy=json_data.get("DisableForwardProxy"),
            EnableForwardProxy=deserialize_list(json_data.get("EnableForwardProxy"), EnableForwardProxyDefinition),
            SliToGlobalDr=deserialize_list(json_data.get("SliToGlobalDr"), SliToGlobalDrDefinition),
            SloToGlobalDr=deserialize_list(json_data.get("SloToGlobalDr"), SloToGlobalDrDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_GlobalNetworkConnectionsDefinition = GlobalNetworkConnectionsDefinition


@dataclass
class EnableForwardProxyDefinition(BaseModel):
    ConnectionTimeout: Optional[float]
    MaxConnectAttempts: Optional[float]
    NoInterception: Optional[bool]
    WhiteListedPorts: Optional[Sequence[float]]
    WhiteListedPrefixes: Optional[Sequence[str]]
    TlsIntercept: Optional[Sequence["_TlsInterceptDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EnableForwardProxyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnableForwardProxyDefinition"]:
        if not json_data:
            return None
        return cls(
            ConnectionTimeout=json_data.get("ConnectionTimeout"),
            MaxConnectAttempts=json_data.get("MaxConnectAttempts"),
            NoInterception=json_data.get("NoInterception"),
            WhiteListedPorts=json_data.get("WhiteListedPorts"),
            WhiteListedPrefixes=json_data.get("WhiteListedPrefixes"),
            TlsIntercept=deserialize_list(json_data.get("TlsIntercept"), TlsInterceptDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnableForwardProxyDefinition = EnableForwardProxyDefinition


@dataclass
class TlsInterceptDefinition(BaseModel):
    EnableForAllDomains: Optional[bool]
    TrustedCaUrl: Optional[str]
    VolterraCertificate: Optional[bool]
    VolterraTrustedCa: Optional[bool]
    CustomCertificate: Optional[Sequence["_CustomCertificateDefinition"]]
    Policy: Optional[Sequence["_PolicyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TlsInterceptDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TlsInterceptDefinition"]:
        if not json_data:
            return None
        return cls(
            EnableForAllDomains=json_data.get("EnableForAllDomains"),
            TrustedCaUrl=json_data.get("TrustedCaUrl"),
            VolterraCertificate=json_data.get("VolterraCertificate"),
            VolterraTrustedCa=json_data.get("VolterraTrustedCa"),
            CustomCertificate=deserialize_list(json_data.get("CustomCertificate"), CustomCertificateDefinition),
            Policy=deserialize_list(json_data.get("Policy"), PolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TlsInterceptDefinition = TlsInterceptDefinition


@dataclass
class CustomCertificateDefinition(BaseModel):
    CertificateUrl: Optional[str]
    Description: Optional[str]
    PrivateKey: Optional[Sequence["_PrivateKeyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CustomCertificateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomCertificateDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateUrl=json_data.get("CertificateUrl"),
            Description=json_data.get("Description"),
            PrivateKey=deserialize_list(json_data.get("PrivateKey"), PrivateKeyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomCertificateDefinition = CustomCertificateDefinition


@dataclass
class PrivateKeyDefinition(BaseModel):
    SecretEncodingType: Optional[str]
    BlindfoldSecretInfo: Optional[Sequence["_BlindfoldSecretInfoDefinition"]]
    BlindfoldSecretInfoInternal: Optional[Sequence["_BlindfoldSecretInfoInternalDefinition"]]
    ClearSecretInfo: Optional[Sequence["_ClearSecretInfoDefinition"]]
    VaultSecretInfo: Optional[Sequence["_VaultSecretInfoDefinition"]]
    WingmanSecretInfo: Optional[Sequence["_WingmanSecretInfoDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PrivateKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivateKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            SecretEncodingType=json_data.get("SecretEncodingType"),
            BlindfoldSecretInfo=deserialize_list(json_data.get("BlindfoldSecretInfo"), BlindfoldSecretInfoDefinition),
            BlindfoldSecretInfoInternal=deserialize_list(json_data.get("BlindfoldSecretInfoInternal"), BlindfoldSecretInfoInternalDefinition),
            ClearSecretInfo=deserialize_list(json_data.get("ClearSecretInfo"), ClearSecretInfoDefinition),
            VaultSecretInfo=deserialize_list(json_data.get("VaultSecretInfo"), VaultSecretInfoDefinition),
            WingmanSecretInfo=deserialize_list(json_data.get("WingmanSecretInfo"), WingmanSecretInfoDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivateKeyDefinition = PrivateKeyDefinition


@dataclass
class BlindfoldSecretInfoDefinition(BaseModel):
    DecryptionProvider: Optional[str]
    Location: Optional[str]
    StoreProvider: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BlindfoldSecretInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BlindfoldSecretInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            DecryptionProvider=json_data.get("DecryptionProvider"),
            Location=json_data.get("Location"),
            StoreProvider=json_data.get("StoreProvider"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BlindfoldSecretInfoDefinition = BlindfoldSecretInfoDefinition


@dataclass
class BlindfoldSecretInfoInternalDefinition(BaseModel):
    DecryptionProvider: Optional[str]
    Location: Optional[str]
    StoreProvider: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BlindfoldSecretInfoInternalDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BlindfoldSecretInfoInternalDefinition"]:
        if not json_data:
            return None
        return cls(
            DecryptionProvider=json_data.get("DecryptionProvider"),
            Location=json_data.get("Location"),
            StoreProvider=json_data.get("StoreProvider"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BlindfoldSecretInfoInternalDefinition = BlindfoldSecretInfoInternalDefinition


@dataclass
class ClearSecretInfoDefinition(BaseModel):
    Provider: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClearSecretInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClearSecretInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            Provider=json_data.get("Provider"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClearSecretInfoDefinition = ClearSecretInfoDefinition


@dataclass
class VaultSecretInfoDefinition(BaseModel):
    Key: Optional[str]
    Location: Optional[str]
    Provider: Optional[str]
    SecretEncoding: Optional[str]
    Version: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_VaultSecretInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VaultSecretInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Location=json_data.get("Location"),
            Provider=json_data.get("Provider"),
            SecretEncoding=json_data.get("SecretEncoding"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VaultSecretInfoDefinition = VaultSecretInfoDefinition


@dataclass
class WingmanSecretInfoDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WingmanSecretInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WingmanSecretInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WingmanSecretInfoDefinition = WingmanSecretInfoDefinition


@dataclass
class PolicyDefinition(BaseModel):
    InterceptionRules: Optional[Sequence["_InterceptionRulesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            InterceptionRules=deserialize_list(json_data.get("InterceptionRules"), InterceptionRulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PolicyDefinition = PolicyDefinition


@dataclass
class InterceptionRulesDefinition(BaseModel):
    DisableInterception: Optional[bool]
    EnableInterception: Optional[bool]
    DomainMatch: Optional[Sequence["_DomainMatchDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InterceptionRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InterceptionRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            DisableInterception=json_data.get("DisableInterception"),
            EnableInterception=json_data.get("EnableInterception"),
            DomainMatch=deserialize_list(json_data.get("DomainMatch"), DomainMatchDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InterceptionRulesDefinition = InterceptionRulesDefinition


@dataclass
class DomainMatchDefinition(BaseModel):
    ExactValue: Optional[str]
    RegexValue: Optional[str]
    SuffixValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DomainMatchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DomainMatchDefinition"]:
        if not json_data:
            return None
        return cls(
            ExactValue=json_data.get("ExactValue"),
            RegexValue=json_data.get("RegexValue"),
            SuffixValue=json_data.get("SuffixValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DomainMatchDefinition = DomainMatchDefinition


@dataclass
class SliToGlobalDrDefinition(BaseModel):
    GlobalVn: Optional[Sequence["_GlobalVnDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SliToGlobalDrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SliToGlobalDrDefinition"]:
        if not json_data:
            return None
        return cls(
            GlobalVn=deserialize_list(json_data.get("GlobalVn"), GlobalVnDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SliToGlobalDrDefinition = SliToGlobalDrDefinition


@dataclass
class GlobalVnDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GlobalVnDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GlobalVnDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GlobalVnDefinition = GlobalVnDefinition


@dataclass
class SloToGlobalDrDefinition(BaseModel):
    GlobalVn: Optional[Sequence["_GlobalVnDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SloToGlobalDrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SloToGlobalDrDefinition"]:
        if not json_data:
            return None
        return cls(
            GlobalVn=deserialize_list(json_data.get("GlobalVn"), GlobalVnDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SloToGlobalDrDefinition = SloToGlobalDrDefinition


@dataclass
class InsideStaticRoutesDefinition(BaseModel):
    StaticRouteList: Optional[Sequence["_StaticRouteListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InsideStaticRoutesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InsideStaticRoutesDefinition"]:
        if not json_data:
            return None
        return cls(
            StaticRouteList=deserialize_list(json_data.get("StaticRouteList"), StaticRouteListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InsideStaticRoutesDefinition = InsideStaticRoutesDefinition


@dataclass
class StaticRouteListDefinition(BaseModel):
    SimpleStaticRoute: Optional[str]
    CustomStaticRoute: Optional[Sequence["_CustomStaticRouteDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_StaticRouteListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StaticRouteListDefinition"]:
        if not json_data:
            return None
        return cls(
            SimpleStaticRoute=json_data.get("SimpleStaticRoute"),
            CustomStaticRoute=deserialize_list(json_data.get("CustomStaticRoute"), CustomStaticRouteDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_StaticRouteListDefinition = StaticRouteListDefinition


@dataclass
class CustomStaticRouteDefinition(BaseModel):
    Attrs: Optional[Sequence[str]]
    Labels: Optional[Sequence["_LabelsDefinition3"]]
    Nexthop: Optional[Sequence["_NexthopDefinition"]]
    Subnets: Optional[Sequence["_SubnetsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CustomStaticRouteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomStaticRouteDefinition"]:
        if not json_data:
            return None
        return cls(
            Attrs=json_data.get("Attrs"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition3),
            Nexthop=deserialize_list(json_data.get("Nexthop"), NexthopDefinition),
            Subnets=deserialize_list(json_data.get("Subnets"), SubnetsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomStaticRouteDefinition = CustomStaticRouteDefinition


@dataclass
class LabelsDefinition3(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition3"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition3 = LabelsDefinition3


@dataclass
class NexthopDefinition(BaseModel):
    Type: Optional[str]
    Interface: Optional[Sequence["_InterfaceDefinition"]]
    NexthopAddress: Optional[Sequence["_NexthopAddressDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NexthopDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NexthopDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Interface=deserialize_list(json_data.get("Interface"), InterfaceDefinition),
            NexthopAddress=deserialize_list(json_data.get("NexthopAddress"), NexthopAddressDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NexthopDefinition = NexthopDefinition


@dataclass
class InterfaceDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InterfaceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InterfaceDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InterfaceDefinition = InterfaceDefinition


@dataclass
class NexthopAddressDefinition(BaseModel):
    Ipv4: Optional[Sequence["_Ipv4Definition"]]
    Ipv6: Optional[Sequence["_Ipv6Definition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NexthopAddressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NexthopAddressDefinition"]:
        if not json_data:
            return None
        return cls(
            Ipv4=deserialize_list(json_data.get("Ipv4"), Ipv4Definition),
            Ipv6=deserialize_list(json_data.get("Ipv6"), Ipv6Definition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NexthopAddressDefinition = NexthopAddressDefinition


@dataclass
class Ipv4Definition(BaseModel):
    Addr: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ipv4Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ipv4Definition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ipv4Definition = Ipv4Definition


@dataclass
class Ipv6Definition(BaseModel):
    Addr: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ipv6Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ipv6Definition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ipv6Definition = Ipv6Definition


@dataclass
class SubnetsDefinition(BaseModel):
    Ipv4: Optional[Sequence["_Ipv4Definition"]]
    Ipv6: Optional[Sequence["_Ipv6Definition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SubnetsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubnetsDefinition"]:
        if not json_data:
            return None
        return cls(
            Ipv4=deserialize_list(json_data.get("Ipv4"), Ipv4Definition),
            Ipv6=deserialize_list(json_data.get("Ipv6"), Ipv6Definition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubnetsDefinition = SubnetsDefinition


@dataclass
class OutsideStaticRoutesDefinition(BaseModel):
    StaticRouteList: Optional[Sequence["_StaticRouteListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OutsideStaticRoutesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutsideStaticRoutesDefinition"]:
        if not json_data:
            return None
        return cls(
            StaticRouteList=deserialize_list(json_data.get("StaticRouteList"), StaticRouteListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutsideStaticRoutesDefinition = OutsideStaticRoutesDefinition


@dataclass
class VpcAttachmentsDefinition(BaseModel):
    VpcList: Optional[Sequence["_VpcListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_VpcAttachmentsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcAttachmentsDefinition"]:
        if not json_data:
            return None
        return cls(
            VpcList=deserialize_list(json_data.get("VpcList"), VpcListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcAttachmentsDefinition = VpcAttachmentsDefinition


@dataclass
class VpcListDefinition(BaseModel):
    Labels: Optional[Sequence["_LabelsDefinition2"]]
    VpcId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VpcListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcListDefinition"]:
        if not json_data:
            return None
        return cls(
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition2),
            VpcId=json_data.get("VpcId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcListDefinition = VpcListDefinition


@dataclass
class LabelsDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition2 = LabelsDefinition2

