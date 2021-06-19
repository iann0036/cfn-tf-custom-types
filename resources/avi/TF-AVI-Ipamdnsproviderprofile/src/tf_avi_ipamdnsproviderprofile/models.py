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
    AllocateIpInVrf: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    TenantRef: Optional[str]
    Type: Optional[str]
    Uuid: Optional[str]
    AwsProfile: Optional[Sequence["_AwsProfileDefinition"]]
    AzureProfile: Optional[Sequence["_AzureProfileDefinition"]]
    CustomProfile: Optional[Sequence["_CustomProfileDefinition"]]
    GcpProfile: Optional[Sequence["_GcpProfileDefinition"]]
    InfobloxProfile: Optional[Sequence["_InfobloxProfileDefinition"]]
    InternalProfile: Optional[Sequence["_InternalProfileDefinition"]]
    Markers: Optional[Sequence["_MarkersDefinition"]]
    OciProfile: Optional[Sequence["_OciProfileDefinition"]]
    OpenstackProfile: Optional[Sequence["_OpenstackProfileDefinition"]]
    ProxyConfiguration: Optional[Sequence["_ProxyConfigurationDefinition"]]
    TencentProfile: Optional[Sequence["_TencentProfileDefinition"]]

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
            AllocateIpInVrf=json_data.get("AllocateIpInVrf"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            TenantRef=json_data.get("TenantRef"),
            Type=json_data.get("Type"),
            Uuid=json_data.get("Uuid"),
            AwsProfile=deserialize_list(json_data.get("AwsProfile"), AwsProfileDefinition),
            AzureProfile=deserialize_list(json_data.get("AzureProfile"), AzureProfileDefinition),
            CustomProfile=deserialize_list(json_data.get("CustomProfile"), CustomProfileDefinition),
            GcpProfile=deserialize_list(json_data.get("GcpProfile"), GcpProfileDefinition),
            InfobloxProfile=deserialize_list(json_data.get("InfobloxProfile"), InfobloxProfileDefinition),
            InternalProfile=deserialize_list(json_data.get("InternalProfile"), InternalProfileDefinition),
            Markers=deserialize_list(json_data.get("Markers"), MarkersDefinition),
            OciProfile=deserialize_list(json_data.get("OciProfile"), OciProfileDefinition),
            OpenstackProfile=deserialize_list(json_data.get("OpenstackProfile"), OpenstackProfileDefinition),
            ProxyConfiguration=deserialize_list(json_data.get("ProxyConfiguration"), ProxyConfigurationDefinition),
            TencentProfile=deserialize_list(json_data.get("TencentProfile"), TencentProfileDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AwsProfileDefinition(BaseModel):
    AccessKeyId: Optional[str]
    EgressServiceSubnets: Optional[Sequence[str]]
    IamAssumeRole: Optional[str]
    PublishVipToPublicZone: Optional[bool]
    Region: Optional[str]
    SecretAccessKey: Optional[str]
    Ttl: Optional[float]
    UsableDomains: Optional[Sequence[str]]
    UsableNetworkUuids: Optional[Sequence[str]]
    UseIamRoles: Optional[bool]
    Vpc: Optional[str]
    VpcId: Optional[str]
    Zones: Optional[Sequence["_ZonesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessKeyId=json_data.get("AccessKeyId"),
            EgressServiceSubnets=json_data.get("EgressServiceSubnets"),
            IamAssumeRole=json_data.get("IamAssumeRole"),
            PublishVipToPublicZone=json_data.get("PublishVipToPublicZone"),
            Region=json_data.get("Region"),
            SecretAccessKey=json_data.get("SecretAccessKey"),
            Ttl=json_data.get("Ttl"),
            UsableDomains=json_data.get("UsableDomains"),
            UsableNetworkUuids=json_data.get("UsableNetworkUuids"),
            UseIamRoles=json_data.get("UseIamRoles"),
            Vpc=json_data.get("Vpc"),
            VpcId=json_data.get("VpcId"),
            Zones=deserialize_list(json_data.get("Zones"), ZonesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsProfileDefinition = AwsProfileDefinition


@dataclass
class ZonesDefinition(BaseModel):
    AvailabilityZone: Optional[str]
    UsableSubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ZonesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ZonesDefinition"]:
        if not json_data:
            return None
        return cls(
            AvailabilityZone=json_data.get("AvailabilityZone"),
            UsableSubnetId=json_data.get("UsableSubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ZonesDefinition = ZonesDefinition


@dataclass
class AzureProfileDefinition(BaseModel):
    EgressServiceSubnets: Optional[Sequence[str]]
    ResourceGroup: Optional[str]
    SubscriptionId: Optional[str]
    UsableDomains: Optional[Sequence[str]]
    UsableNetworkUuids: Optional[Sequence[str]]
    UseEnhancedHa: Optional[bool]
    UseStandardAlb: Optional[bool]
    VirtualNetworkIds: Optional[Sequence[str]]
    AzureServiceprincipal: Optional[Sequence["_AzureServiceprincipalDefinition"]]
    AzureUserpass: Optional[Sequence["_AzureUserpassDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AzureProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            EgressServiceSubnets=json_data.get("EgressServiceSubnets"),
            ResourceGroup=json_data.get("ResourceGroup"),
            SubscriptionId=json_data.get("SubscriptionId"),
            UsableDomains=json_data.get("UsableDomains"),
            UsableNetworkUuids=json_data.get("UsableNetworkUuids"),
            UseEnhancedHa=json_data.get("UseEnhancedHa"),
            UseStandardAlb=json_data.get("UseStandardAlb"),
            VirtualNetworkIds=json_data.get("VirtualNetworkIds"),
            AzureServiceprincipal=deserialize_list(json_data.get("AzureServiceprincipal"), AzureServiceprincipalDefinition),
            AzureUserpass=deserialize_list(json_data.get("AzureUserpass"), AzureUserpassDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureProfileDefinition = AzureProfileDefinition


@dataclass
class AzureServiceprincipalDefinition(BaseModel):
    ApplicationId: Optional[str]
    AuthenticationToken: Optional[str]
    TenantId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AzureServiceprincipalDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureServiceprincipalDefinition"]:
        if not json_data:
            return None
        return cls(
            ApplicationId=json_data.get("ApplicationId"),
            AuthenticationToken=json_data.get("AuthenticationToken"),
            TenantId=json_data.get("TenantId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureServiceprincipalDefinition = AzureServiceprincipalDefinition


@dataclass
class AzureUserpassDefinition(BaseModel):
    Password: Optional[str]
    TenantName: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AzureUserpassDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureUserpassDefinition"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            TenantName=json_data.get("TenantName"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureUserpassDefinition = AzureUserpassDefinition


@dataclass
class CustomProfileDefinition(BaseModel):
    CustomIpamDnsProfileRef: Optional[str]
    UsableDomains: Optional[Sequence[str]]
    DynamicParams: Optional[Sequence["_DynamicParamsDefinition"]]
    UsableSubnets: Optional[Sequence["_UsableSubnetsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CustomProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            CustomIpamDnsProfileRef=json_data.get("CustomIpamDnsProfileRef"),
            UsableDomains=json_data.get("UsableDomains"),
            DynamicParams=deserialize_list(json_data.get("DynamicParams"), DynamicParamsDefinition),
            UsableSubnets=deserialize_list(json_data.get("UsableSubnets"), UsableSubnetsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomProfileDefinition = CustomProfileDefinition


@dataclass
class DynamicParamsDefinition(BaseModel):
    IsDynamic: Optional[bool]
    IsSensitive: Optional[bool]
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DynamicParamsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DynamicParamsDefinition"]:
        if not json_data:
            return None
        return cls(
            IsDynamic=json_data.get("IsDynamic"),
            IsSensitive=json_data.get("IsSensitive"),
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DynamicParamsDefinition = DynamicParamsDefinition


@dataclass
class UsableSubnetsDefinition(BaseModel):
    Mask: Optional[float]
    IpAddr: Optional[Sequence["_IpAddrDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_UsableSubnetsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UsableSubnetsDefinition"]:
        if not json_data:
            return None
        return cls(
            Mask=json_data.get("Mask"),
            IpAddr=deserialize_list(json_data.get("IpAddr"), IpAddrDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_UsableSubnetsDefinition = UsableSubnetsDefinition


@dataclass
class IpAddrDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpAddrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpAddrDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpAddrDefinition = IpAddrDefinition


@dataclass
class GcpProfileDefinition(BaseModel):
    MatchSeGroupSubnet: Optional[bool]
    NetworkHostProjectId: Optional[str]
    RegionName: Optional[str]
    SeProjectId: Optional[str]
    UsableNetworkRefs: Optional[Sequence[str]]
    UseGcpNetwork: Optional[bool]
    VpcNetworkName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GcpProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GcpProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchSeGroupSubnet=json_data.get("MatchSeGroupSubnet"),
            NetworkHostProjectId=json_data.get("NetworkHostProjectId"),
            RegionName=json_data.get("RegionName"),
            SeProjectId=json_data.get("SeProjectId"),
            UsableNetworkRefs=json_data.get("UsableNetworkRefs"),
            UseGcpNetwork=json_data.get("UseGcpNetwork"),
            VpcNetworkName=json_data.get("VpcNetworkName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GcpProfileDefinition = GcpProfileDefinition


@dataclass
class InfobloxProfileDefinition(BaseModel):
    DnsView: Optional[str]
    NetworkView: Optional[str]
    Password: Optional[str]
    UsableDomains: Optional[Sequence[str]]
    Username: Optional[str]
    WapiVersion: Optional[str]
    ExtensibleAttributes: Optional[Sequence["_ExtensibleAttributesDefinition"]]
    IpAddress: Optional[Sequence["_IpAddressDefinition"]]
    UsableAllocSubnets: Optional[Sequence["_UsableAllocSubnetsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InfobloxProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InfobloxProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            DnsView=json_data.get("DnsView"),
            NetworkView=json_data.get("NetworkView"),
            Password=json_data.get("Password"),
            UsableDomains=json_data.get("UsableDomains"),
            Username=json_data.get("Username"),
            WapiVersion=json_data.get("WapiVersion"),
            ExtensibleAttributes=deserialize_list(json_data.get("ExtensibleAttributes"), ExtensibleAttributesDefinition),
            IpAddress=deserialize_list(json_data.get("IpAddress"), IpAddressDefinition),
            UsableAllocSubnets=deserialize_list(json_data.get("UsableAllocSubnets"), UsableAllocSubnetsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InfobloxProfileDefinition = InfobloxProfileDefinition


@dataclass
class ExtensibleAttributesDefinition(BaseModel):
    IsDynamic: Optional[bool]
    IsSensitive: Optional[bool]
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExtensibleAttributesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtensibleAttributesDefinition"]:
        if not json_data:
            return None
        return cls(
            IsDynamic=json_data.get("IsDynamic"),
            IsSensitive=json_data.get("IsSensitive"),
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtensibleAttributesDefinition = ExtensibleAttributesDefinition


@dataclass
class IpAddressDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpAddressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpAddressDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpAddressDefinition = IpAddressDefinition


@dataclass
class UsableAllocSubnetsDefinition(BaseModel):
    Subnet: Optional[Sequence["_SubnetDefinition"]]
    Subnet6: Optional[Sequence["_Subnet6Definition"]]

    @classmethod
    def _deserialize(
        cls: Type["_UsableAllocSubnetsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UsableAllocSubnetsDefinition"]:
        if not json_data:
            return None
        return cls(
            Subnet=deserialize_list(json_data.get("Subnet"), SubnetDefinition),
            Subnet6=deserialize_list(json_data.get("Subnet6"), Subnet6Definition),
        )


# work around possible type aliasing issues when variable has same name as a model
_UsableAllocSubnetsDefinition = UsableAllocSubnetsDefinition


@dataclass
class SubnetDefinition(BaseModel):
    Mask: Optional[float]
    IpAddr: Optional[Sequence["_IpAddrDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SubnetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubnetDefinition"]:
        if not json_data:
            return None
        return cls(
            Mask=json_data.get("Mask"),
            IpAddr=deserialize_list(json_data.get("IpAddr"), IpAddrDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubnetDefinition = SubnetDefinition


@dataclass
class Subnet6Definition(BaseModel):
    Mask: Optional[float]
    IpAddr: Optional[Sequence["_IpAddrDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_Subnet6Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Subnet6Definition"]:
        if not json_data:
            return None
        return cls(
            Mask=json_data.get("Mask"),
            IpAddr=deserialize_list(json_data.get("IpAddr"), IpAddrDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_Subnet6Definition = Subnet6Definition


@dataclass
class InternalProfileDefinition(BaseModel):
    DnsVirtualserviceRef: Optional[str]
    Ttl: Optional[float]
    DnsServiceDomain: Optional[Sequence["_DnsServiceDomainDefinition"]]
    UsableNetworks: Optional[Sequence["_UsableNetworksDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InternalProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InternalProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            DnsVirtualserviceRef=json_data.get("DnsVirtualserviceRef"),
            Ttl=json_data.get("Ttl"),
            DnsServiceDomain=deserialize_list(json_data.get("DnsServiceDomain"), DnsServiceDomainDefinition),
            UsableNetworks=deserialize_list(json_data.get("UsableNetworks"), UsableNetworksDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InternalProfileDefinition = InternalProfileDefinition


@dataclass
class DnsServiceDomainDefinition(BaseModel):
    DomainName: Optional[str]
    PassThrough: Optional[bool]
    RecordTtl: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DnsServiceDomainDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsServiceDomainDefinition"]:
        if not json_data:
            return None
        return cls(
            DomainName=json_data.get("DomainName"),
            PassThrough=json_data.get("PassThrough"),
            RecordTtl=json_data.get("RecordTtl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsServiceDomainDefinition = DnsServiceDomainDefinition


@dataclass
class UsableNetworksDefinition(BaseModel):
    NwRef: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_UsableNetworksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UsableNetworksDefinition"]:
        if not json_data:
            return None
        return cls(
            NwRef=json_data.get("NwRef"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_UsableNetworksDefinition = UsableNetworksDefinition


@dataclass
class LabelsDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class MarkersDefinition(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MarkersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MarkersDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MarkersDefinition = MarkersDefinition


@dataclass
class OciProfileDefinition(BaseModel):
    CloudCredentialsRef: Optional[str]
    Region: Optional[str]
    Tenancy: Optional[str]
    VcnCompartmentId: Optional[str]
    VcnId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OciProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OciProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            CloudCredentialsRef=json_data.get("CloudCredentialsRef"),
            Region=json_data.get("Region"),
            Tenancy=json_data.get("Tenancy"),
            VcnCompartmentId=json_data.get("VcnCompartmentId"),
            VcnId=json_data.get("VcnId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OciProfileDefinition = OciProfileDefinition


@dataclass
class OpenstackProfileDefinition(BaseModel):
    KeystoneHost: Optional[str]
    Password: Optional[str]
    Region: Optional[str]
    Tenant: Optional[str]
    Username: Optional[str]
    VipNetworkName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OpenstackProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OpenstackProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            KeystoneHost=json_data.get("KeystoneHost"),
            Password=json_data.get("Password"),
            Region=json_data.get("Region"),
            Tenant=json_data.get("Tenant"),
            Username=json_data.get("Username"),
            VipNetworkName=json_data.get("VipNetworkName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OpenstackProfileDefinition = OpenstackProfileDefinition


@dataclass
class ProxyConfigurationDefinition(BaseModel):
    Host: Optional[str]
    Password: Optional[str]
    Port: Optional[float]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProxyConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProxyConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            Host=json_data.get("Host"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProxyConfigurationDefinition = ProxyConfigurationDefinition


@dataclass
class TencentProfileDefinition(BaseModel):
    CloudCredentialsRef: Optional[str]
    Region: Optional[str]
    UsableSubnetIds: Optional[Sequence[str]]
    VpcId: Optional[str]
    Zones: Optional[Sequence["_ZonesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TencentProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TencentProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            CloudCredentialsRef=json_data.get("CloudCredentialsRef"),
            Region=json_data.get("Region"),
            UsableSubnetIds=json_data.get("UsableSubnetIds"),
            VpcId=json_data.get("VpcId"),
            Zones=deserialize_list(json_data.get("Zones"), ZonesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TencentProfileDefinition = TencentProfileDefinition


