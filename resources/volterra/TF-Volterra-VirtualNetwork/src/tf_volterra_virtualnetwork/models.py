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
    GlobalNetwork: Optional[bool]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    LegacyType: Optional[str]
    Name: Optional[str]
    Namespace: Optional[str]
    SiteLocalInsideNetwork: Optional[bool]
    SiteLocalNetwork: Optional[bool]
    Srv6Network: Optional[Sequence["_Srv6NetworkDefinition"]]
    StaticRoutes: Optional[Sequence["_StaticRoutesDefinition"]]

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
            GlobalNetwork=json_data.get("GlobalNetwork"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            LegacyType=json_data.get("LegacyType"),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            SiteLocalInsideNetwork=json_data.get("SiteLocalInsideNetwork"),
            SiteLocalNetwork=json_data.get("SiteLocalNetwork"),
            Srv6Network=deserialize_list(json_data.get("Srv6Network"), Srv6NetworkDefinition),
            StaticRoutes=deserialize_list(json_data.get("StaticRoutes"), StaticRoutesDefinition),
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
class Srv6NetworkDefinition(BaseModel):
    AnycastVip: Optional[str]
    InterfaceIpSnatPool: Optional[bool]
    InterfaceIpVip: Optional[bool]
    NoNamespaceNetwork: Optional[bool]
    RemoteSidStatsPlen: Optional[float]
    AccessNetworkRtargets: Optional[Sequence["_AccessNetworkRtargetsDefinition"]]
    EnterpriseNetworkRtargets: Optional[Sequence["_EnterpriseNetworkRtargetsDefinition"]]
    ExportRtargets: Optional[Sequence["_ExportRtargetsDefinition"]]
    FleetSnatPool: Optional[Sequence["_FleetSnatPoolDefinition"]]
    FleetVip: Optional[Sequence["_FleetVipDefinition"]]
    Fleets: Optional[Sequence["_FleetsDefinition"]]
    InternetRtargets: Optional[Sequence["_InternetRtargetsDefinition"]]
    SiteSnatPool: Optional[Sequence["_SiteSnatPoolDefinition"]]
    Slice: Optional[Sequence["_SliceDefinition"]]
    Srv6NetworkNsParams: Optional[Sequence["_Srv6NetworkNsParamsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_Srv6NetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Srv6NetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            AnycastVip=json_data.get("AnycastVip"),
            InterfaceIpSnatPool=json_data.get("InterfaceIpSnatPool"),
            InterfaceIpVip=json_data.get("InterfaceIpVip"),
            NoNamespaceNetwork=json_data.get("NoNamespaceNetwork"),
            RemoteSidStatsPlen=json_data.get("RemoteSidStatsPlen"),
            AccessNetworkRtargets=deserialize_list(json_data.get("AccessNetworkRtargets"), AccessNetworkRtargetsDefinition),
            EnterpriseNetworkRtargets=deserialize_list(json_data.get("EnterpriseNetworkRtargets"), EnterpriseNetworkRtargetsDefinition),
            ExportRtargets=deserialize_list(json_data.get("ExportRtargets"), ExportRtargetsDefinition),
            FleetSnatPool=deserialize_list(json_data.get("FleetSnatPool"), FleetSnatPoolDefinition),
            FleetVip=deserialize_list(json_data.get("FleetVip"), FleetVipDefinition),
            Fleets=deserialize_list(json_data.get("Fleets"), FleetsDefinition),
            InternetRtargets=deserialize_list(json_data.get("InternetRtargets"), InternetRtargetsDefinition),
            SiteSnatPool=deserialize_list(json_data.get("SiteSnatPool"), SiteSnatPoolDefinition),
            Slice=deserialize_list(json_data.get("Slice"), SliceDefinition),
            Srv6NetworkNsParams=deserialize_list(json_data.get("Srv6NetworkNsParams"), Srv6NetworkNsParamsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_Srv6NetworkDefinition = Srv6NetworkDefinition


@dataclass
class AccessNetworkRtargetsDefinition(BaseModel):
    Asn2byteRtarget: Optional[Sequence["_Asn2byteRtargetDefinition"]]
    Asn4byteRtarget: Optional[Sequence["_Asn4byteRtargetDefinition"]]
    Ipv4AddrRtarget: Optional[Sequence["_Ipv4AddrRtargetDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AccessNetworkRtargetsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessNetworkRtargetsDefinition"]:
        if not json_data:
            return None
        return cls(
            Asn2byteRtarget=deserialize_list(json_data.get("Asn2byteRtarget"), Asn2byteRtargetDefinition),
            Asn4byteRtarget=deserialize_list(json_data.get("Asn4byteRtarget"), Asn4byteRtargetDefinition),
            Ipv4AddrRtarget=deserialize_list(json_data.get("Ipv4AddrRtarget"), Ipv4AddrRtargetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessNetworkRtargetsDefinition = AccessNetworkRtargetsDefinition


@dataclass
class Asn2byteRtargetDefinition(BaseModel):
    AsNumber: Optional[float]
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Asn2byteRtargetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Asn2byteRtargetDefinition"]:
        if not json_data:
            return None
        return cls(
            AsNumber=json_data.get("AsNumber"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Asn2byteRtargetDefinition = Asn2byteRtargetDefinition


@dataclass
class Asn4byteRtargetDefinition(BaseModel):
    AsNumber: Optional[float]
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Asn4byteRtargetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Asn4byteRtargetDefinition"]:
        if not json_data:
            return None
        return cls(
            AsNumber=json_data.get("AsNumber"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Asn4byteRtargetDefinition = Asn4byteRtargetDefinition


@dataclass
class Ipv4AddrRtargetDefinition(BaseModel):
    Address: Optional[str]
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Ipv4AddrRtargetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ipv4AddrRtargetDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ipv4AddrRtargetDefinition = Ipv4AddrRtargetDefinition


@dataclass
class EnterpriseNetworkRtargetsDefinition(BaseModel):
    Asn2byteRtarget: Optional[Sequence["_Asn2byteRtargetDefinition"]]
    Asn4byteRtarget: Optional[Sequence["_Asn4byteRtargetDefinition"]]
    Ipv4AddrRtarget: Optional[Sequence["_Ipv4AddrRtargetDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EnterpriseNetworkRtargetsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnterpriseNetworkRtargetsDefinition"]:
        if not json_data:
            return None
        return cls(
            Asn2byteRtarget=deserialize_list(json_data.get("Asn2byteRtarget"), Asn2byteRtargetDefinition),
            Asn4byteRtarget=deserialize_list(json_data.get("Asn4byteRtarget"), Asn4byteRtargetDefinition),
            Ipv4AddrRtarget=deserialize_list(json_data.get("Ipv4AddrRtarget"), Ipv4AddrRtargetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnterpriseNetworkRtargetsDefinition = EnterpriseNetworkRtargetsDefinition


@dataclass
class ExportRtargetsDefinition(BaseModel):
    Asn2byteRtarget: Optional[Sequence["_Asn2byteRtargetDefinition"]]
    Asn4byteRtarget: Optional[Sequence["_Asn4byteRtargetDefinition"]]
    Ipv4AddrRtarget: Optional[Sequence["_Ipv4AddrRtargetDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ExportRtargetsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExportRtargetsDefinition"]:
        if not json_data:
            return None
        return cls(
            Asn2byteRtarget=deserialize_list(json_data.get("Asn2byteRtarget"), Asn2byteRtargetDefinition),
            Asn4byteRtarget=deserialize_list(json_data.get("Asn4byteRtarget"), Asn4byteRtargetDefinition),
            Ipv4AddrRtarget=deserialize_list(json_data.get("Ipv4AddrRtarget"), Ipv4AddrRtargetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExportRtargetsDefinition = ExportRtargetsDefinition


@dataclass
class FleetSnatPoolDefinition(BaseModel):
    SnatPoolAllocator: Optional[Sequence["_SnatPoolAllocatorDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FleetSnatPoolDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FleetSnatPoolDefinition"]:
        if not json_data:
            return None
        return cls(
            SnatPoolAllocator=deserialize_list(json_data.get("SnatPoolAllocator"), SnatPoolAllocatorDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FleetSnatPoolDefinition = FleetSnatPoolDefinition


@dataclass
class SnatPoolAllocatorDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SnatPoolAllocatorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnatPoolAllocatorDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnatPoolAllocatorDefinition = SnatPoolAllocatorDefinition


@dataclass
class FleetVipDefinition(BaseModel):
    VipAllocator: Optional[Sequence["_VipAllocatorDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FleetVipDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FleetVipDefinition"]:
        if not json_data:
            return None
        return cls(
            VipAllocator=deserialize_list(json_data.get("VipAllocator"), VipAllocatorDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FleetVipDefinition = FleetVipDefinition


@dataclass
class VipAllocatorDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VipAllocatorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VipAllocatorDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VipAllocatorDefinition = VipAllocatorDefinition


@dataclass
class FleetsDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FleetsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FleetsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FleetsDefinition = FleetsDefinition


@dataclass
class InternetRtargetsDefinition(BaseModel):
    Asn2byteRtarget: Optional[Sequence["_Asn2byteRtargetDefinition"]]
    Asn4byteRtarget: Optional[Sequence["_Asn4byteRtargetDefinition"]]
    Ipv4AddrRtarget: Optional[Sequence["_Ipv4AddrRtargetDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InternetRtargetsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InternetRtargetsDefinition"]:
        if not json_data:
            return None
        return cls(
            Asn2byteRtarget=deserialize_list(json_data.get("Asn2byteRtarget"), Asn2byteRtargetDefinition),
            Asn4byteRtarget=deserialize_list(json_data.get("Asn4byteRtarget"), Asn4byteRtargetDefinition),
            Ipv4AddrRtarget=deserialize_list(json_data.get("Ipv4AddrRtarget"), Ipv4AddrRtargetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InternetRtargetsDefinition = InternetRtargetsDefinition


@dataclass
class SiteSnatPoolDefinition(BaseModel):
    NodeSnatPool: Optional[Sequence["_NodeSnatPoolDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SiteSnatPoolDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SiteSnatPoolDefinition"]:
        if not json_data:
            return None
        return cls(
            NodeSnatPool=deserialize_list(json_data.get("NodeSnatPool"), NodeSnatPoolDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SiteSnatPoolDefinition = SiteSnatPoolDefinition


@dataclass
class NodeSnatPoolDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[Sequence["_ValueDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NodeSnatPoolDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeSnatPoolDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=deserialize_list(json_data.get("Value"), ValueDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeSnatPoolDefinition = NodeSnatPoolDefinition


@dataclass
class ValueDefinition(BaseModel):
    Ipv4Prefixes: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ValueDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ValueDefinition"]:
        if not json_data:
            return None
        return cls(
            Ipv4Prefixes=json_data.get("Ipv4Prefixes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ValueDefinition = ValueDefinition


@dataclass
class SliceDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SliceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SliceDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SliceDefinition = SliceDefinition


@dataclass
class Srv6NetworkNsParamsDefinition(BaseModel):
    Namespace: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Srv6NetworkNsParamsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Srv6NetworkNsParamsDefinition"]:
        if not json_data:
            return None
        return cls(
            Namespace=json_data.get("Namespace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Srv6NetworkNsParamsDefinition = Srv6NetworkNsParamsDefinition


@dataclass
class StaticRoutesDefinition(BaseModel):
    Attrs: Optional[Sequence[str]]
    DefaultGateway: Optional[bool]
    IpAddress: Optional[str]
    IpPrefixes: Optional[Sequence[str]]
    Interface: Optional[Sequence["_InterfaceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_StaticRoutesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StaticRoutesDefinition"]:
        if not json_data:
            return None
        return cls(
            Attrs=json_data.get("Attrs"),
            DefaultGateway=json_data.get("DefaultGateway"),
            IpAddress=json_data.get("IpAddress"),
            IpPrefixes=json_data.get("IpPrefixes"),
            Interface=deserialize_list(json_data.get("Interface"), InterfaceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_StaticRoutesDefinition = StaticRoutesDefinition


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


