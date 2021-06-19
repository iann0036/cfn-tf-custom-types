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
    Annotations: Optional[Sequence["_AnnotationsDefinition"]]
    Description: Optional[str]
    Disable: Optional[bool]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Name: Optional[str]
    Namespace: Optional[str]
    BgpParameters: Optional[Sequence["_BgpParametersDefinition"]]
    Peers: Optional[Sequence["_PeersDefinition"]]
    Where: Optional[Sequence["_WhereDefinition"]]

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
            Annotations=deserialize_list(json_data.get("Annotations"), AnnotationsDefinition),
            Description=json_data.get("Description"),
            Disable=json_data.get("Disable"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            BgpParameters=deserialize_list(json_data.get("BgpParameters"), BgpParametersDefinition),
            Peers=deserialize_list(json_data.get("Peers"), PeersDefinition),
            Where=deserialize_list(json_data.get("Where"), WhereDefinition),
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
class BgpParametersDefinition(BaseModel):
    Asn: Optional[float]
    BgpRouterIdKey: Optional[str]
    BgpRouterIdType: Optional[str]
    FromSite: Optional[bool]
    IpAddress: Optional[str]
    LocalAddress: Optional[bool]
    BgpRouterId: Optional[Sequence["_BgpRouterIdDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BgpParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BgpParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            Asn=json_data.get("Asn"),
            BgpRouterIdKey=json_data.get("BgpRouterIdKey"),
            BgpRouterIdType=json_data.get("BgpRouterIdType"),
            FromSite=json_data.get("FromSite"),
            IpAddress=json_data.get("IpAddress"),
            LocalAddress=json_data.get("LocalAddress"),
            BgpRouterId=deserialize_list(json_data.get("BgpRouterId"), BgpRouterIdDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BgpParametersDefinition = BgpParametersDefinition


@dataclass
class BgpRouterIdDefinition(BaseModel):
    Ipv4: Optional[Sequence["_Ipv4Definition"]]
    Ipv6: Optional[Sequence["_Ipv6Definition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BgpRouterIdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BgpRouterIdDefinition"]:
        if not json_data:
            return None
        return cls(
            Ipv4=deserialize_list(json_data.get("Ipv4"), Ipv4Definition),
            Ipv6=deserialize_list(json_data.get("Ipv6"), Ipv6Definition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BgpRouterIdDefinition = BgpRouterIdDefinition


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
class PeersDefinition(BaseModel):
    TargetService: Optional[str]
    External: Optional[Sequence["_ExternalDefinition"]]
    Internal: Optional[Sequence["_InternalDefinition"]]
    Metadata: Optional[Sequence["_MetadataDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PeersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PeersDefinition"]:
        if not json_data:
            return None
        return cls(
            TargetService=json_data.get("TargetService"),
            External=deserialize_list(json_data.get("External"), ExternalDefinition),
            Internal=deserialize_list(json_data.get("Internal"), InternalDefinition),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PeersDefinition = PeersDefinition


@dataclass
class ExternalDefinition(BaseModel):
    Address: Optional[str]
    Asn: Optional[float]
    DefaultGateway: Optional[bool]
    FromSite: Optional[bool]
    InsideInterfaces: Optional[bool]
    OutsideInterfaces: Optional[bool]
    Port: Optional[float]
    SubnetBeginOffset: Optional[float]
    SubnetEndOffset: Optional[float]
    FamilyInet: Optional[Sequence["_FamilyInetDefinition"]]
    Interface: Optional[Sequence["_InterfaceDefinition"]]
    InterfaceList: Optional[Sequence["_InterfaceListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ExternalDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExternalDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Asn=json_data.get("Asn"),
            DefaultGateway=json_data.get("DefaultGateway"),
            FromSite=json_data.get("FromSite"),
            InsideInterfaces=json_data.get("InsideInterfaces"),
            OutsideInterfaces=json_data.get("OutsideInterfaces"),
            Port=json_data.get("Port"),
            SubnetBeginOffset=json_data.get("SubnetBeginOffset"),
            SubnetEndOffset=json_data.get("SubnetEndOffset"),
            FamilyInet=deserialize_list(json_data.get("FamilyInet"), FamilyInetDefinition),
            Interface=deserialize_list(json_data.get("Interface"), InterfaceDefinition),
            InterfaceList=deserialize_list(json_data.get("InterfaceList"), InterfaceListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExternalDefinition = ExternalDefinition


@dataclass
class FamilyInetDefinition(BaseModel):
    Disable: Optional[bool]
    Enable: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_FamilyInetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FamilyInetDefinition"]:
        if not json_data:
            return None
        return cls(
            Disable=json_data.get("Disable"),
            Enable=json_data.get("Enable"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FamilyInetDefinition = FamilyInetDefinition


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
class InterfaceListDefinition(BaseModel):
    Interfaces: Optional[Sequence["_InterfacesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InterfaceListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InterfaceListDefinition"]:
        if not json_data:
            return None
        return cls(
            Interfaces=deserialize_list(json_data.get("Interfaces"), InterfacesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InterfaceListDefinition = InterfaceListDefinition


@dataclass
class InterfacesDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InterfacesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InterfacesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InterfacesDefinition = InterfacesDefinition


@dataclass
class InternalDefinition(BaseModel):
    Address: Optional[str]
    DisableMtls: Optional[bool]
    DnsName: Optional[str]
    EnableMtls: Optional[bool]
    FromSite: Optional[bool]
    Port: Optional[float]
    FamilyInet6vpn: Optional[Sequence["_FamilyInet6vpnDefinition"]]
    FamilyInetvpn: Optional[Sequence["_FamilyInetvpnDefinition"]]
    FamilyRtarget: Optional[Sequence["_FamilyRtargetDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InternalDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InternalDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            DisableMtls=json_data.get("DisableMtls"),
            DnsName=json_data.get("DnsName"),
            EnableMtls=json_data.get("EnableMtls"),
            FromSite=json_data.get("FromSite"),
            Port=json_data.get("Port"),
            FamilyInet6vpn=deserialize_list(json_data.get("FamilyInet6vpn"), FamilyInet6vpnDefinition),
            FamilyInetvpn=deserialize_list(json_data.get("FamilyInetvpn"), FamilyInetvpnDefinition),
            FamilyRtarget=deserialize_list(json_data.get("FamilyRtarget"), FamilyRtargetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InternalDefinition = InternalDefinition


@dataclass
class FamilyInet6vpnDefinition(BaseModel):
    Disable: Optional[bool]
    Enable: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_FamilyInet6vpnDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FamilyInet6vpnDefinition"]:
        if not json_data:
            return None
        return cls(
            Disable=json_data.get("Disable"),
            Enable=json_data.get("Enable"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FamilyInet6vpnDefinition = FamilyInet6vpnDefinition


@dataclass
class FamilyInetvpnDefinition(BaseModel):
    Disable: Optional[bool]
    Enable: Optional[Sequence["_EnableDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FamilyInetvpnDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FamilyInetvpnDefinition"]:
        if not json_data:
            return None
        return cls(
            Disable=json_data.get("Disable"),
            Enable=deserialize_list(json_data.get("Enable"), EnableDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FamilyInetvpnDefinition = FamilyInetvpnDefinition


@dataclass
class EnableDefinition(BaseModel):
    Disable: Optional[bool]
    Enable: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_EnableDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnableDefinition"]:
        if not json_data:
            return None
        return cls(
            Disable=json_data.get("Disable"),
            Enable=json_data.get("Enable"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnableDefinition = EnableDefinition


@dataclass
class FamilyRtargetDefinition(BaseModel):
    Disable: Optional[bool]
    Enable: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_FamilyRtargetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FamilyRtargetDefinition"]:
        if not json_data:
            return None
        return cls(
            Disable=json_data.get("Disable"),
            Enable=json_data.get("Enable"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FamilyRtargetDefinition = FamilyRtargetDefinition


@dataclass
class MetadataDefinition(BaseModel):
    Description: Optional[str]
    Disable: Optional[bool]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Disable=json_data.get("Disable"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataDefinition = MetadataDefinition


@dataclass
class WhereDefinition(BaseModel):
    Site: Optional[Sequence["_SiteDefinition"]]
    VirtualSite: Optional[Sequence["_VirtualSiteDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WhereDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WhereDefinition"]:
        if not json_data:
            return None
        return cls(
            Site=deserialize_list(json_data.get("Site"), SiteDefinition),
            VirtualSite=deserialize_list(json_data.get("VirtualSite"), VirtualSiteDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WhereDefinition = WhereDefinition


@dataclass
class SiteDefinition(BaseModel):
    NetworkType: Optional[str]
    Ref: Optional[Sequence["_RefDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SiteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SiteDefinition"]:
        if not json_data:
            return None
        return cls(
            NetworkType=json_data.get("NetworkType"),
            Ref=deserialize_list(json_data.get("Ref"), RefDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SiteDefinition = SiteDefinition


@dataclass
class RefDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RefDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RefDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RefDefinition = RefDefinition


@dataclass
class VirtualSiteDefinition(BaseModel):
    NetworkType: Optional[str]
    Ref: Optional[Sequence["_RefDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualSiteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualSiteDefinition"]:
        if not json_data:
            return None
        return cls(
            NetworkType=json_data.get("NetworkType"),
            Ref=deserialize_list(json_data.get("Ref"), RefDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualSiteDefinition = VirtualSiteDefinition


