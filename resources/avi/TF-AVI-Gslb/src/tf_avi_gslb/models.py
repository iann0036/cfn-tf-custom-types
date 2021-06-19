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
    AsyncInterval: Optional[float]
    ClearOnMaxRetries: Optional[float]
    Description: Optional[str]
    EnableConfigByMembers: Optional[bool]
    ErrorResyncInterval: Optional[float]
    Id: Optional[str]
    IsFederated: Optional[bool]
    LeaderClusterUuid: Optional[str]
    MaintenanceMode: Optional[bool]
    Name: Optional[str]
    SendInterval: Optional[float]
    SendIntervalPriorToMaintenanceMode: Optional[float]
    TenantRef: Optional[str]
    TenantScoped: Optional[bool]
    Uuid: Optional[str]
    ViewId: Optional[float]
    ClientIpAddrGroup: Optional[Sequence["_ClientIpAddrGroupDefinition"]]
    DnsConfigs: Optional[Sequence["_DnsConfigsDefinition"]]
    ReplicationPolicy: Optional[Sequence["_ReplicationPolicyDefinition"]]
    Sites: Optional[Sequence["_SitesDefinition"]]
    ThirdPartySites: Optional[Sequence["_ThirdPartySitesDefinition"]]

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
            AsyncInterval=json_data.get("AsyncInterval"),
            ClearOnMaxRetries=json_data.get("ClearOnMaxRetries"),
            Description=json_data.get("Description"),
            EnableConfigByMembers=json_data.get("EnableConfigByMembers"),
            ErrorResyncInterval=json_data.get("ErrorResyncInterval"),
            Id=json_data.get("Id"),
            IsFederated=json_data.get("IsFederated"),
            LeaderClusterUuid=json_data.get("LeaderClusterUuid"),
            MaintenanceMode=json_data.get("MaintenanceMode"),
            Name=json_data.get("Name"),
            SendInterval=json_data.get("SendInterval"),
            SendIntervalPriorToMaintenanceMode=json_data.get("SendIntervalPriorToMaintenanceMode"),
            TenantRef=json_data.get("TenantRef"),
            TenantScoped=json_data.get("TenantScoped"),
            Uuid=json_data.get("Uuid"),
            ViewId=json_data.get("ViewId"),
            ClientIpAddrGroup=deserialize_list(json_data.get("ClientIpAddrGroup"), ClientIpAddrGroupDefinition),
            DnsConfigs=deserialize_list(json_data.get("DnsConfigs"), DnsConfigsDefinition),
            ReplicationPolicy=deserialize_list(json_data.get("ReplicationPolicy"), ReplicationPolicyDefinition),
            Sites=deserialize_list(json_data.get("Sites"), SitesDefinition),
            ThirdPartySites=deserialize_list(json_data.get("ThirdPartySites"), ThirdPartySitesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ClientIpAddrGroupDefinition(BaseModel):
    Type: Optional[str]
    Addrs: Optional[Sequence["_AddrsDefinition"]]
    Prefixes: Optional[Sequence["_PrefixesDefinition"]]
    Ranges: Optional[Sequence["_RangesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ClientIpAddrGroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientIpAddrGroupDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Addrs=deserialize_list(json_data.get("Addrs"), AddrsDefinition),
            Prefixes=deserialize_list(json_data.get("Prefixes"), PrefixesDefinition),
            Ranges=deserialize_list(json_data.get("Ranges"), RangesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientIpAddrGroupDefinition = ClientIpAddrGroupDefinition


@dataclass
class AddrsDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AddrsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AddrsDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AddrsDefinition = AddrsDefinition


@dataclass
class PrefixesDefinition(BaseModel):
    Mask: Optional[float]
    IpAddr: Optional[Sequence["_IpAddrDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PrefixesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrefixesDefinition"]:
        if not json_data:
            return None
        return cls(
            Mask=json_data.get("Mask"),
            IpAddr=deserialize_list(json_data.get("IpAddr"), IpAddrDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrefixesDefinition = PrefixesDefinition


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
class RangesDefinition(BaseModel):
    Begin: Optional[Sequence["_BeginDefinition"]]
    End: Optional[Sequence["_EndDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RangesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RangesDefinition"]:
        if not json_data:
            return None
        return cls(
            Begin=deserialize_list(json_data.get("Begin"), BeginDefinition),
            End=deserialize_list(json_data.get("End"), EndDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RangesDefinition = RangesDefinition


@dataclass
class BeginDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BeginDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BeginDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BeginDefinition = BeginDefinition


@dataclass
class EndDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EndDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndDefinition = EndDefinition


@dataclass
class DnsConfigsDefinition(BaseModel):
    DomainName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DnsConfigsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsConfigsDefinition"]:
        if not json_data:
            return None
        return cls(
            DomainName=json_data.get("DomainName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsConfigsDefinition = DnsConfigsDefinition


@dataclass
class ReplicationPolicyDefinition(BaseModel):
    CheckpointRef: Optional[str]
    ReplicationMode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReplicationPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReplicationPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            CheckpointRef=json_data.get("CheckpointRef"),
            ReplicationMode=json_data.get("ReplicationMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReplicationPolicyDefinition = ReplicationPolicyDefinition


@dataclass
class SitesDefinition(BaseModel):
    Address: Optional[str]
    ClusterUuid: Optional[str]
    Enabled: Optional[bool]
    HmShardEnabled: Optional[bool]
    MemberType: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Port: Optional[float]
    Ratio: Optional[float]
    SuspendMode: Optional[bool]
    Username: Optional[str]
    Uuid: Optional[str]
    DnsVses: Optional[Sequence["_DnsVsesDefinition"]]
    HmProxies: Optional[Sequence["_HmProxiesDefinition"]]
    IpAddresses: Optional[Sequence["_IpAddressesDefinition"]]
    Location: Optional[Sequence["_LocationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SitesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SitesDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            ClusterUuid=json_data.get("ClusterUuid"),
            Enabled=json_data.get("Enabled"),
            HmShardEnabled=json_data.get("HmShardEnabled"),
            MemberType=json_data.get("MemberType"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            Ratio=json_data.get("Ratio"),
            SuspendMode=json_data.get("SuspendMode"),
            Username=json_data.get("Username"),
            Uuid=json_data.get("Uuid"),
            DnsVses=deserialize_list(json_data.get("DnsVses"), DnsVsesDefinition),
            HmProxies=deserialize_list(json_data.get("HmProxies"), HmProxiesDefinition),
            IpAddresses=deserialize_list(json_data.get("IpAddresses"), IpAddressesDefinition),
            Location=deserialize_list(json_data.get("Location"), LocationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SitesDefinition = SitesDefinition


@dataclass
class DnsVsesDefinition(BaseModel):
    DnsVsUuid: Optional[str]
    DomainNames: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_DnsVsesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsVsesDefinition"]:
        if not json_data:
            return None
        return cls(
            DnsVsUuid=json_data.get("DnsVsUuid"),
            DomainNames=json_data.get("DomainNames"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsVsesDefinition = DnsVsesDefinition


@dataclass
class HmProxiesDefinition(BaseModel):
    ProxyType: Optional[str]
    SiteUuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HmProxiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HmProxiesDefinition"]:
        if not json_data:
            return None
        return cls(
            ProxyType=json_data.get("ProxyType"),
            SiteUuid=json_data.get("SiteUuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HmProxiesDefinition = HmProxiesDefinition


@dataclass
class IpAddressesDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpAddressesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpAddressesDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpAddressesDefinition = IpAddressesDefinition


@dataclass
class LocationDefinition(BaseModel):
    Latitude: Optional[float]
    Longitude: Optional[float]
    Name: Optional[str]
    Tag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LocationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LocationDefinition"]:
        if not json_data:
            return None
        return cls(
            Latitude=json_data.get("Latitude"),
            Longitude=json_data.get("Longitude"),
            Name=json_data.get("Name"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LocationDefinition = LocationDefinition


@dataclass
class ThirdPartySitesDefinition(BaseModel):
    Enabled: Optional[bool]
    Name: Optional[str]
    Ratio: Optional[float]
    Uuid: Optional[str]
    HmProxies: Optional[Sequence["_HmProxiesDefinition"]]
    Location: Optional[Sequence["_LocationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ThirdPartySitesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThirdPartySitesDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Name=json_data.get("Name"),
            Ratio=json_data.get("Ratio"),
            Uuid=json_data.get("Uuid"),
            HmProxies=deserialize_list(json_data.get("HmProxies"), HmProxiesDefinition),
            Location=deserialize_list(json_data.get("Location"), LocationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThirdPartySitesDefinition = ThirdPartySitesDefinition


