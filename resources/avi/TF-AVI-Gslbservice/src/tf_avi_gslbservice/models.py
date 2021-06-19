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
    ApplicationPersistenceProfileRef: Optional[str]
    ControllerHealthStatusEnabled: Optional[bool]
    CreatedBy: Optional[str]
    Description: Optional[str]
    DomainNames: Optional[Sequence[str]]
    Enabled: Optional[bool]
    HealthMonitorRefs: Optional[Sequence[str]]
    HealthMonitorScope: Optional[str]
    HmOff: Optional[bool]
    Id: Optional[str]
    IsFederated: Optional[bool]
    MinMembers: Optional[float]
    Name: Optional[str]
    NumDnsIp: Optional[float]
    PoolAlgorithm: Optional[str]
    ResolveCname: Optional[bool]
    SitePersistenceEnabled: Optional[bool]
    TenantRef: Optional[str]
    Ttl: Optional[float]
    UseEdnsClientSubnet: Optional[bool]
    Uuid: Optional[str]
    WildcardMatch: Optional[bool]
    DownResponse: Optional[Sequence["_DownResponseDefinition"]]
    Groups: Optional[Sequence["_GroupsDefinition"]]
    Markers: Optional[Sequence["_MarkersDefinition"]]

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
            ApplicationPersistenceProfileRef=json_data.get("ApplicationPersistenceProfileRef"),
            ControllerHealthStatusEnabled=json_data.get("ControllerHealthStatusEnabled"),
            CreatedBy=json_data.get("CreatedBy"),
            Description=json_data.get("Description"),
            DomainNames=json_data.get("DomainNames"),
            Enabled=json_data.get("Enabled"),
            HealthMonitorRefs=json_data.get("HealthMonitorRefs"),
            HealthMonitorScope=json_data.get("HealthMonitorScope"),
            HmOff=json_data.get("HmOff"),
            Id=json_data.get("Id"),
            IsFederated=json_data.get("IsFederated"),
            MinMembers=json_data.get("MinMembers"),
            Name=json_data.get("Name"),
            NumDnsIp=json_data.get("NumDnsIp"),
            PoolAlgorithm=json_data.get("PoolAlgorithm"),
            ResolveCname=json_data.get("ResolveCname"),
            SitePersistenceEnabled=json_data.get("SitePersistenceEnabled"),
            TenantRef=json_data.get("TenantRef"),
            Ttl=json_data.get("Ttl"),
            UseEdnsClientSubnet=json_data.get("UseEdnsClientSubnet"),
            Uuid=json_data.get("Uuid"),
            WildcardMatch=json_data.get("WildcardMatch"),
            DownResponse=deserialize_list(json_data.get("DownResponse"), DownResponseDefinition),
            Groups=deserialize_list(json_data.get("Groups"), GroupsDefinition),
            Markers=deserialize_list(json_data.get("Markers"), MarkersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DownResponseDefinition(BaseModel):
    Type: Optional[str]
    FallbackIp: Optional[Sequence["_FallbackIpDefinition"]]
    FallbackIp6: Optional[Sequence["_FallbackIp6Definition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DownResponseDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DownResponseDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            FallbackIp=deserialize_list(json_data.get("FallbackIp"), FallbackIpDefinition),
            FallbackIp6=deserialize_list(json_data.get("FallbackIp6"), FallbackIp6Definition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DownResponseDefinition = DownResponseDefinition


@dataclass
class FallbackIpDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FallbackIpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FallbackIpDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FallbackIpDefinition = FallbackIpDefinition


@dataclass
class FallbackIp6Definition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FallbackIp6Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FallbackIp6Definition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FallbackIp6Definition = FallbackIp6Definition


@dataclass
class GroupsDefinition(BaseModel):
    Algorithm: Optional[str]
    ConsistentHashMask: Optional[float]
    ConsistentHashMask6: Optional[float]
    Description: Optional[str]
    Enabled: Optional[bool]
    FallbackAlgorithm: Optional[str]
    MinHealthMonitorsUp: Optional[float]
    Name: Optional[str]
    Priority: Optional[float]
    Members: Optional[Sequence["_MembersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_GroupsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GroupsDefinition"]:
        if not json_data:
            return None
        return cls(
            Algorithm=json_data.get("Algorithm"),
            ConsistentHashMask=json_data.get("ConsistentHashMask"),
            ConsistentHashMask6=json_data.get("ConsistentHashMask6"),
            Description=json_data.get("Description"),
            Enabled=json_data.get("Enabled"),
            FallbackAlgorithm=json_data.get("FallbackAlgorithm"),
            MinHealthMonitorsUp=json_data.get("MinHealthMonitorsUp"),
            Name=json_data.get("Name"),
            Priority=json_data.get("Priority"),
            Members=deserialize_list(json_data.get("Members"), MembersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_GroupsDefinition = GroupsDefinition


@dataclass
class MembersDefinition(BaseModel):
    CloudUuid: Optional[str]
    ClusterUuid: Optional[str]
    Description: Optional[str]
    Enabled: Optional[bool]
    Fqdn: Optional[str]
    Hostname: Optional[str]
    Ratio: Optional[float]
    ResolveFqdnToV6: Optional[bool]
    VsUuid: Optional[str]
    Ip: Optional[Sequence["_IpDefinition"]]
    Location: Optional[Sequence["_LocationDefinition"]]
    PublicIp: Optional[Sequence["_PublicIpDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MembersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MembersDefinition"]:
        if not json_data:
            return None
        return cls(
            CloudUuid=json_data.get("CloudUuid"),
            ClusterUuid=json_data.get("ClusterUuid"),
            Description=json_data.get("Description"),
            Enabled=json_data.get("Enabled"),
            Fqdn=json_data.get("Fqdn"),
            Hostname=json_data.get("Hostname"),
            Ratio=json_data.get("Ratio"),
            ResolveFqdnToV6=json_data.get("ResolveFqdnToV6"),
            VsUuid=json_data.get("VsUuid"),
            Ip=deserialize_list(json_data.get("Ip"), IpDefinition),
            Location=deserialize_list(json_data.get("Location"), LocationDefinition),
            PublicIp=deserialize_list(json_data.get("PublicIp"), PublicIpDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MembersDefinition = MembersDefinition


@dataclass
class IpDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpDefinition = IpDefinition


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
class PublicIpDefinition(BaseModel):
    Ip: Optional[Sequence["_IpDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PublicIpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublicIpDefinition"]:
        if not json_data:
            return None
        return cls(
            Ip=deserialize_list(json_data.get("Ip"), IpDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublicIpDefinition = PublicIpDefinition


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


