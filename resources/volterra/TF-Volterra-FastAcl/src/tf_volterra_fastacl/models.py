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
    LegacyAcl: Optional[Sequence["_LegacyAclDefinition"]]
    ProtocolPolicer: Optional[Sequence["_ProtocolPolicerDefinition"]]
    ReAcl: Optional[Sequence["_ReAclDefinition"]]
    SiteAcl: Optional[Sequence["_SiteAclDefinition"]]

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
            LegacyAcl=deserialize_list(json_data.get("LegacyAcl"), LegacyAclDefinition),
            ProtocolPolicer=deserialize_list(json_data.get("ProtocolPolicer"), ProtocolPolicerDefinition),
            ReAcl=deserialize_list(json_data.get("ReAcl"), ReAclDefinition),
            SiteAcl=deserialize_list(json_data.get("SiteAcl"), SiteAclDefinition),
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
class LegacyAclDefinition(BaseModel):
    DestinationType: Optional[Sequence["_DestinationTypeDefinition"]]
    NetworkType: Optional[Sequence["_NetworkTypeDefinition"]]
    SourceRules: Optional[Sequence["_SourceRulesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LegacyAclDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LegacyAclDefinition"]:
        if not json_data:
            return None
        return cls(
            DestinationType=deserialize_list(json_data.get("DestinationType"), DestinationTypeDefinition),
            NetworkType=deserialize_list(json_data.get("NetworkType"), NetworkTypeDefinition),
            SourceRules=deserialize_list(json_data.get("SourceRules"), SourceRulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LegacyAclDefinition = LegacyAclDefinition


@dataclass
class DestinationTypeDefinition(BaseModel):
    AllServices: Optional[bool]
    InterfaceServices: Optional[bool]
    SharedVipServices: Optional[bool]
    VipServices: Optional[bool]
    DestinationIpAddress: Optional[Sequence["_DestinationIpAddressDefinition"]]
    SelectedVipAddress: Optional[Sequence["_SelectedVipAddressDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DestinationTypeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestinationTypeDefinition"]:
        if not json_data:
            return None
        return cls(
            AllServices=json_data.get("AllServices"),
            InterfaceServices=json_data.get("InterfaceServices"),
            SharedVipServices=json_data.get("SharedVipServices"),
            VipServices=json_data.get("VipServices"),
            DestinationIpAddress=deserialize_list(json_data.get("DestinationIpAddress"), DestinationIpAddressDefinition),
            SelectedVipAddress=deserialize_list(json_data.get("SelectedVipAddress"), SelectedVipAddressDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestinationTypeDefinition = DestinationTypeDefinition


@dataclass
class DestinationIpAddressDefinition(BaseModel):
    Protocol: Optional[str]
    Address: Optional[Sequence["_AddressDefinition"]]
    Ports: Optional[Sequence["_PortsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DestinationIpAddressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestinationIpAddressDefinition"]:
        if not json_data:
            return None
        return cls(
            Protocol=json_data.get("Protocol"),
            Address=deserialize_list(json_data.get("Address"), AddressDefinition),
            Ports=deserialize_list(json_data.get("Ports"), PortsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestinationIpAddressDefinition = DestinationIpAddressDefinition


@dataclass
class AddressDefinition(BaseModel):
    Ipv4: Optional[Sequence["_Ipv4Definition"]]
    Ipv6: Optional[Sequence["_Ipv6Definition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AddressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AddressDefinition"]:
        if not json_data:
            return None
        return cls(
            Ipv4=deserialize_list(json_data.get("Ipv4"), Ipv4Definition),
            Ipv6=deserialize_list(json_data.get("Ipv6"), Ipv6Definition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AddressDefinition = AddressDefinition


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
class PortsDefinition(BaseModel):
    All: Optional[bool]
    Dns: Optional[bool]
    UserDefined: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PortsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortsDefinition"]:
        if not json_data:
            return None
        return cls(
            All=json_data.get("All"),
            Dns=json_data.get("Dns"),
            UserDefined=json_data.get("UserDefined"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortsDefinition = PortsDefinition


@dataclass
class SelectedVipAddressDefinition(BaseModel):
    Address: Optional[Sequence["_AddressDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SelectedVipAddressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SelectedVipAddressDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=deserialize_list(json_data.get("Address"), AddressDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SelectedVipAddressDefinition = SelectedVipAddressDefinition


@dataclass
class NetworkTypeDefinition(BaseModel):
    Public: Optional[bool]
    SiteLocal: Optional[bool]
    SiteLocalInside: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkTypeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkTypeDefinition"]:
        if not json_data:
            return None
        return cls(
            Public=json_data.get("Public"),
            SiteLocal=json_data.get("SiteLocal"),
            SiteLocalInside=json_data.get("SiteLocalInside"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkTypeDefinition = NetworkTypeDefinition


@dataclass
class SourceRulesDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceRulesDefinition = SourceRulesDefinition


@dataclass
class ProtocolPolicerDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProtocolPolicerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProtocolPolicerDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProtocolPolicerDefinition = ProtocolPolicerDefinition


@dataclass
class ReAclDefinition(BaseModel):
    AllPublicVips: Optional[bool]
    DefaultTenantVip: Optional[bool]
    FastAclRules: Optional[Sequence["_FastAclRulesDefinition"]]
    SelectedTenantVip: Optional[Sequence["_SelectedTenantVipDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ReAclDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReAclDefinition"]:
        if not json_data:
            return None
        return cls(
            AllPublicVips=json_data.get("AllPublicVips"),
            DefaultTenantVip=json_data.get("DefaultTenantVip"),
            FastAclRules=deserialize_list(json_data.get("FastAclRules"), FastAclRulesDefinition),
            SelectedTenantVip=deserialize_list(json_data.get("SelectedTenantVip"), SelectedTenantVipDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReAclDefinition = ReAclDefinition


@dataclass
class FastAclRulesDefinition(BaseModel):
    Name: Optional[str]
    Action: Optional[Sequence["_ActionDefinition"]]
    IpPrefixSet: Optional[Sequence["_IpPrefixSetDefinition"]]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Port: Optional[Sequence["_PortDefinition"]]
    Prefix: Optional[Sequence["_PrefixDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FastAclRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FastAclRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Action=deserialize_list(json_data.get("Action"), ActionDefinition),
            IpPrefixSet=deserialize_list(json_data.get("IpPrefixSet"), IpPrefixSetDefinition),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Port=deserialize_list(json_data.get("Port"), PortDefinition),
            Prefix=deserialize_list(json_data.get("Prefix"), PrefixDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FastAclRulesDefinition = FastAclRulesDefinition


@dataclass
class ActionDefinition(BaseModel):
    SimpleAction: Optional[str]
    PolicerAction: Optional[Sequence["_PolicerActionDefinition"]]
    ProtocolPolicerAction: Optional[Sequence["_ProtocolPolicerActionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionDefinition"]:
        if not json_data:
            return None
        return cls(
            SimpleAction=json_data.get("SimpleAction"),
            PolicerAction=deserialize_list(json_data.get("PolicerAction"), PolicerActionDefinition),
            ProtocolPolicerAction=deserialize_list(json_data.get("ProtocolPolicerAction"), ProtocolPolicerActionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionDefinition = ActionDefinition


@dataclass
class PolicerActionDefinition(BaseModel):
    Ref: Optional[Sequence["_RefDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PolicerActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PolicerActionDefinition"]:
        if not json_data:
            return None
        return cls(
            Ref=deserialize_list(json_data.get("Ref"), RefDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PolicerActionDefinition = PolicerActionDefinition


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
class ProtocolPolicerActionDefinition(BaseModel):
    Ref: Optional[Sequence["_RefDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ProtocolPolicerActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProtocolPolicerActionDefinition"]:
        if not json_data:
            return None
        return cls(
            Ref=deserialize_list(json_data.get("Ref"), RefDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProtocolPolicerActionDefinition = ProtocolPolicerActionDefinition


@dataclass
class IpPrefixSetDefinition(BaseModel):
    Ref: Optional[Sequence["_RefDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IpPrefixSetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpPrefixSetDefinition"]:
        if not json_data:
            return None
        return cls(
            Ref=deserialize_list(json_data.get("Ref"), RefDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpPrefixSetDefinition = IpPrefixSetDefinition


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
class PortDefinition(BaseModel):
    All: Optional[bool]
    Dns: Optional[bool]
    UserDefined: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PortDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortDefinition"]:
        if not json_data:
            return None
        return cls(
            All=json_data.get("All"),
            Dns=json_data.get("Dns"),
            UserDefined=json_data.get("UserDefined"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortDefinition = PortDefinition


@dataclass
class PrefixDefinition(BaseModel):
    Prefix: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PrefixDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrefixDefinition"]:
        if not json_data:
            return None
        return cls(
            Prefix=json_data.get("Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrefixDefinition = PrefixDefinition


@dataclass
class SelectedTenantVipDefinition(BaseModel):
    DefaultTenantVip: Optional[bool]
    PublicIpRefs: Optional[Sequence["_PublicIpRefsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SelectedTenantVipDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SelectedTenantVipDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultTenantVip=json_data.get("DefaultTenantVip"),
            PublicIpRefs=deserialize_list(json_data.get("PublicIpRefs"), PublicIpRefsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SelectedTenantVipDefinition = SelectedTenantVipDefinition


@dataclass
class PublicIpRefsDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PublicIpRefsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublicIpRefsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublicIpRefsDefinition = PublicIpRefsDefinition


@dataclass
class SiteAclDefinition(BaseModel):
    AllServices: Optional[bool]
    InsideNetwork: Optional[bool]
    InterfaceServices: Optional[bool]
    OutsideNetwork: Optional[bool]
    VipServices: Optional[bool]
    FastAclRules: Optional[Sequence["_FastAclRulesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SiteAclDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SiteAclDefinition"]:
        if not json_data:
            return None
        return cls(
            AllServices=json_data.get("AllServices"),
            InsideNetwork=json_data.get("InsideNetwork"),
            InterfaceServices=json_data.get("InterfaceServices"),
            OutsideNetwork=json_data.get("OutsideNetwork"),
            VipServices=json_data.get("VipServices"),
            FastAclRules=deserialize_list(json_data.get("FastAclRules"), FastAclRulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SiteAclDefinition = SiteAclDefinition


