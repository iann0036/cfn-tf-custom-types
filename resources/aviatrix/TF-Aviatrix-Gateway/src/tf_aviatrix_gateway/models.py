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
    AdditionalCidrs: Optional[str]
    AdditionalCidrsDesignatedGateway: Optional[str]
    AllocateNewEip: Optional[bool]
    AvailabilityDomain: Optional[str]
    CloudInstanceId: Optional[str]
    CloudType: Optional[float]
    CustomerManagedKeys: Optional[str]
    DuoApiHostname: Optional[str]
    DuoIntegrationKey: Optional[str]
    DuoPushMode: Optional[str]
    DuoSecretKey: Optional[str]
    Eip: Optional[str]
    ElbDnsName: Optional[str]
    ElbName: Optional[str]
    EnableDesignatedGateway: Optional[bool]
    EnableElb: Optional[bool]
    EnableEncryptVolume: Optional[bool]
    EnableJumboFrame: Optional[bool]
    EnableLdap: Optional[bool]
    EnableMonitorGatewaySubnets: Optional[bool]
    EnablePublicSubnetFiltering: Optional[bool]
    EnableVpcDnsServer: Optional[bool]
    EnableVpnNat: Optional[bool]
    FaultDomain: Optional[str]
    FqdnLanCidr: Optional[str]
    FqdnLanInterface: Optional[str]
    FqdnLanVpcId: Optional[str]
    GwName: Optional[str]
    GwSize: Optional[str]
    Id: Optional[str]
    IdleTimeout: Optional[float]
    InsaneMode: Optional[bool]
    InsaneModeAz: Optional[str]
    LdapBaseDn: Optional[str]
    LdapBindDn: Optional[str]
    LdapPassword: Optional[str]
    LdapServer: Optional[str]
    LdapUsernameAttribute: Optional[str]
    MaxVpnConn: Optional[str]
    MonitorExcludeList: Optional[Sequence[str]]
    NameServers: Optional[str]
    OktaToken: Optional[str]
    OktaUrl: Optional[str]
    OktaUsernameSuffix: Optional[str]
    OtpMode: Optional[str]
    PeeringHaAvailabilityDomain: Optional[str]
    PeeringHaCloudInstanceId: Optional[str]
    PeeringHaEip: Optional[str]
    PeeringHaFaultDomain: Optional[str]
    PeeringHaGwName: Optional[str]
    PeeringHaGwSize: Optional[str]
    PeeringHaInsaneModeAz: Optional[str]
    PeeringHaPrivateIp: Optional[str]
    PeeringHaSubnet: Optional[str]
    PeeringHaZone: Optional[str]
    PrivateIp: Optional[str]
    PublicDnsServer: Optional[str]
    PublicSubnetFilteringGuardDutyEnforced: Optional[bool]
    PublicSubnetFilteringHaRouteTables: Optional[Sequence[str]]
    PublicSubnetFilteringRouteTables: Optional[Sequence[str]]
    RenegotiationInterval: Optional[float]
    SamlEnabled: Optional[bool]
    SearchDomains: Optional[str]
    SecurityGroupId: Optional[str]
    SingleAzHa: Optional[bool]
    SingleIpSnat: Optional[bool]
    SplitTunnel: Optional[bool]
    StorageName: Optional[str]
    Subnet: Optional[str]
    TagList: Optional[Sequence[str]]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TunnelDetectionTime: Optional[float]
    VpcId: Optional[str]
    VpcReg: Optional[str]
    VpnAccess: Optional[bool]
    VpnCidr: Optional[str]
    VpnProtocol: Optional[str]
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
            AdditionalCidrs=json_data.get("AdditionalCidrs"),
            AdditionalCidrsDesignatedGateway=json_data.get("AdditionalCidrsDesignatedGateway"),
            AllocateNewEip=json_data.get("AllocateNewEip"),
            AvailabilityDomain=json_data.get("AvailabilityDomain"),
            CloudInstanceId=json_data.get("CloudInstanceId"),
            CloudType=json_data.get("CloudType"),
            CustomerManagedKeys=json_data.get("CustomerManagedKeys"),
            DuoApiHostname=json_data.get("DuoApiHostname"),
            DuoIntegrationKey=json_data.get("DuoIntegrationKey"),
            DuoPushMode=json_data.get("DuoPushMode"),
            DuoSecretKey=json_data.get("DuoSecretKey"),
            Eip=json_data.get("Eip"),
            ElbDnsName=json_data.get("ElbDnsName"),
            ElbName=json_data.get("ElbName"),
            EnableDesignatedGateway=json_data.get("EnableDesignatedGateway"),
            EnableElb=json_data.get("EnableElb"),
            EnableEncryptVolume=json_data.get("EnableEncryptVolume"),
            EnableJumboFrame=json_data.get("EnableJumboFrame"),
            EnableLdap=json_data.get("EnableLdap"),
            EnableMonitorGatewaySubnets=json_data.get("EnableMonitorGatewaySubnets"),
            EnablePublicSubnetFiltering=json_data.get("EnablePublicSubnetFiltering"),
            EnableVpcDnsServer=json_data.get("EnableVpcDnsServer"),
            EnableVpnNat=json_data.get("EnableVpnNat"),
            FaultDomain=json_data.get("FaultDomain"),
            FqdnLanCidr=json_data.get("FqdnLanCidr"),
            FqdnLanInterface=json_data.get("FqdnLanInterface"),
            FqdnLanVpcId=json_data.get("FqdnLanVpcId"),
            GwName=json_data.get("GwName"),
            GwSize=json_data.get("GwSize"),
            Id=json_data.get("Id"),
            IdleTimeout=json_data.get("IdleTimeout"),
            InsaneMode=json_data.get("InsaneMode"),
            InsaneModeAz=json_data.get("InsaneModeAz"),
            LdapBaseDn=json_data.get("LdapBaseDn"),
            LdapBindDn=json_data.get("LdapBindDn"),
            LdapPassword=json_data.get("LdapPassword"),
            LdapServer=json_data.get("LdapServer"),
            LdapUsernameAttribute=json_data.get("LdapUsernameAttribute"),
            MaxVpnConn=json_data.get("MaxVpnConn"),
            MonitorExcludeList=json_data.get("MonitorExcludeList"),
            NameServers=json_data.get("NameServers"),
            OktaToken=json_data.get("OktaToken"),
            OktaUrl=json_data.get("OktaUrl"),
            OktaUsernameSuffix=json_data.get("OktaUsernameSuffix"),
            OtpMode=json_data.get("OtpMode"),
            PeeringHaAvailabilityDomain=json_data.get("PeeringHaAvailabilityDomain"),
            PeeringHaCloudInstanceId=json_data.get("PeeringHaCloudInstanceId"),
            PeeringHaEip=json_data.get("PeeringHaEip"),
            PeeringHaFaultDomain=json_data.get("PeeringHaFaultDomain"),
            PeeringHaGwName=json_data.get("PeeringHaGwName"),
            PeeringHaGwSize=json_data.get("PeeringHaGwSize"),
            PeeringHaInsaneModeAz=json_data.get("PeeringHaInsaneModeAz"),
            PeeringHaPrivateIp=json_data.get("PeeringHaPrivateIp"),
            PeeringHaSubnet=json_data.get("PeeringHaSubnet"),
            PeeringHaZone=json_data.get("PeeringHaZone"),
            PrivateIp=json_data.get("PrivateIp"),
            PublicDnsServer=json_data.get("PublicDnsServer"),
            PublicSubnetFilteringGuardDutyEnforced=json_data.get("PublicSubnetFilteringGuardDutyEnforced"),
            PublicSubnetFilteringHaRouteTables=json_data.get("PublicSubnetFilteringHaRouteTables"),
            PublicSubnetFilteringRouteTables=json_data.get("PublicSubnetFilteringRouteTables"),
            RenegotiationInterval=json_data.get("RenegotiationInterval"),
            SamlEnabled=json_data.get("SamlEnabled"),
            SearchDomains=json_data.get("SearchDomains"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            SingleAzHa=json_data.get("SingleAzHa"),
            SingleIpSnat=json_data.get("SingleIpSnat"),
            SplitTunnel=json_data.get("SplitTunnel"),
            StorageName=json_data.get("StorageName"),
            Subnet=json_data.get("Subnet"),
            TagList=json_data.get("TagList"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TunnelDetectionTime=json_data.get("TunnelDetectionTime"),
            VpcId=json_data.get("VpcId"),
            VpcReg=json_data.get("VpcReg"),
            VpnAccess=json_data.get("VpnAccess"),
            VpnCidr=json_data.get("VpnCidr"),
            VpnProtocol=json_data.get("VpnProtocol"),
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


