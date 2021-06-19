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
    AccountMoid: Optional[str]
    AdditionalProperties: Optional[str]
    Ancestors: Optional[Sequence["_AncestorsDefinition"]]
    Cdn: Optional[Sequence["_CdnDefinition"]]
    ClassId: Optional[str]
    CreateTime: Optional[str]
    DomainGroupMoid: Optional[str]
    EthAdapterPolicy: Optional[Sequence["_EthAdapterPolicyDefinition"]]
    EthNetworkPolicy: Optional[Sequence["_EthNetworkPolicyDefinition"]]
    EthQosPolicy: Optional[Sequence["_EthQosPolicyDefinition"]]
    FabricEthNetworkControlPolicy: Optional[Sequence["_FabricEthNetworkControlPolicyDefinition"]]
    FabricEthNetworkGroupPolicy: Optional[Sequence["_FabricEthNetworkGroupPolicyDefinition"]]
    FailoverEnabled: Optional[bool]
    Id: Optional[str]
    IpLease: Optional[Sequence["_IpLeaseDefinition"]]
    IscsiBootPolicy: Optional[Sequence["_IscsiBootPolicyDefinition"]]
    IscsiIpV4AddressAllocationType: Optional[str]
    IscsiIpV4Config: Optional[Sequence["_IscsiIpV4ConfigDefinition"]]
    IscsiIpv4Address: Optional[str]
    LanConnectivityPolicy: Optional[Sequence["_LanConnectivityPolicyDefinition"]]
    LcpVnic: Optional[Sequence["_LcpVnicDefinition"]]
    MacAddress: Optional[str]
    MacAddressType: Optional[str]
    MacLease: Optional[Sequence["_MacLeaseDefinition"]]
    MacPool: Optional[Sequence["_MacPoolDefinition"]]
    ModTime: Optional[str]
    Moid: Optional[str]
    Name: Optional[str]
    ObjectType: Optional[str]
    Order: Optional[float]
    Owners: Optional[Sequence[str]]
    Parent: Optional[Sequence["_ParentDefinition"]]
    PermissionResources: Optional[Sequence["_PermissionResourcesDefinition"]]
    Placement: Optional[Sequence["_PlacementDefinition"]]
    Profile: Optional[Sequence["_ProfileDefinition"]]
    SharedScope: Optional[str]
    SpVnics: Optional[Sequence["_SpVnicsDefinition"]]
    StandbyVifId: Optional[float]
    StaticMacAddress: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    UsnicSettings: Optional[Sequence["_UsnicSettingsDefinition"]]
    VersionContext: Optional[Sequence["_VersionContextDefinition3"]]
    VifId: Optional[float]
    VmqSettings: Optional[Sequence["_VmqSettingsDefinition"]]

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
            AccountMoid=json_data.get("AccountMoid"),
            AdditionalProperties=json_data.get("AdditionalProperties"),
            Ancestors=deserialize_list(json_data.get("Ancestors"), AncestorsDefinition),
            Cdn=deserialize_list(json_data.get("Cdn"), CdnDefinition),
            ClassId=json_data.get("ClassId"),
            CreateTime=json_data.get("CreateTime"),
            DomainGroupMoid=json_data.get("DomainGroupMoid"),
            EthAdapterPolicy=deserialize_list(json_data.get("EthAdapterPolicy"), EthAdapterPolicyDefinition),
            EthNetworkPolicy=deserialize_list(json_data.get("EthNetworkPolicy"), EthNetworkPolicyDefinition),
            EthQosPolicy=deserialize_list(json_data.get("EthQosPolicy"), EthQosPolicyDefinition),
            FabricEthNetworkControlPolicy=deserialize_list(json_data.get("FabricEthNetworkControlPolicy"), FabricEthNetworkControlPolicyDefinition),
            FabricEthNetworkGroupPolicy=deserialize_list(json_data.get("FabricEthNetworkGroupPolicy"), FabricEthNetworkGroupPolicyDefinition),
            FailoverEnabled=json_data.get("FailoverEnabled"),
            Id=json_data.get("Id"),
            IpLease=deserialize_list(json_data.get("IpLease"), IpLeaseDefinition),
            IscsiBootPolicy=deserialize_list(json_data.get("IscsiBootPolicy"), IscsiBootPolicyDefinition),
            IscsiIpV4AddressAllocationType=json_data.get("IscsiIpV4AddressAllocationType"),
            IscsiIpV4Config=deserialize_list(json_data.get("IscsiIpV4Config"), IscsiIpV4ConfigDefinition),
            IscsiIpv4Address=json_data.get("IscsiIpv4Address"),
            LanConnectivityPolicy=deserialize_list(json_data.get("LanConnectivityPolicy"), LanConnectivityPolicyDefinition),
            LcpVnic=deserialize_list(json_data.get("LcpVnic"), LcpVnicDefinition),
            MacAddress=json_data.get("MacAddress"),
            MacAddressType=json_data.get("MacAddressType"),
            MacLease=deserialize_list(json_data.get("MacLease"), MacLeaseDefinition),
            MacPool=deserialize_list(json_data.get("MacPool"), MacPoolDefinition),
            ModTime=json_data.get("ModTime"),
            Moid=json_data.get("Moid"),
            Name=json_data.get("Name"),
            ObjectType=json_data.get("ObjectType"),
            Order=json_data.get("Order"),
            Owners=json_data.get("Owners"),
            Parent=deserialize_list(json_data.get("Parent"), ParentDefinition),
            PermissionResources=deserialize_list(json_data.get("PermissionResources"), PermissionResourcesDefinition),
            Placement=deserialize_list(json_data.get("Placement"), PlacementDefinition),
            Profile=deserialize_list(json_data.get("Profile"), ProfileDefinition),
            SharedScope=json_data.get("SharedScope"),
            SpVnics=deserialize_list(json_data.get("SpVnics"), SpVnicsDefinition),
            StandbyVifId=json_data.get("StandbyVifId"),
            StaticMacAddress=json_data.get("StaticMacAddress"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            UsnicSettings=deserialize_list(json_data.get("UsnicSettings"), UsnicSettingsDefinition),
            VersionContext=deserialize_list(json_data.get("VersionContext"), VersionContextDefinition3),
            VifId=json_data.get("VifId"),
            VmqSettings=deserialize_list(json_data.get("VmqSettings"), VmqSettingsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AncestorsDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AncestorsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AncestorsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AncestorsDefinition = AncestorsDefinition


@dataclass
class CdnDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    NrSource: Optional[str]
    ObjectType: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CdnDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CdnDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            NrSource=json_data.get("NrSource"),
            ObjectType=json_data.get("ObjectType"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CdnDefinition = CdnDefinition


@dataclass
class EthAdapterPolicyDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EthAdapterPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EthAdapterPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EthAdapterPolicyDefinition = EthAdapterPolicyDefinition


@dataclass
class EthNetworkPolicyDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EthNetworkPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EthNetworkPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EthNetworkPolicyDefinition = EthNetworkPolicyDefinition


@dataclass
class EthQosPolicyDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EthQosPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EthQosPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EthQosPolicyDefinition = EthQosPolicyDefinition


@dataclass
class FabricEthNetworkControlPolicyDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FabricEthNetworkControlPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FabricEthNetworkControlPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FabricEthNetworkControlPolicyDefinition = FabricEthNetworkControlPolicyDefinition


@dataclass
class FabricEthNetworkGroupPolicyDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FabricEthNetworkGroupPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FabricEthNetworkGroupPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FabricEthNetworkGroupPolicyDefinition = FabricEthNetworkGroupPolicyDefinition


@dataclass
class IpLeaseDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpLeaseDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpLeaseDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpLeaseDefinition = IpLeaseDefinition


@dataclass
class IscsiBootPolicyDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IscsiBootPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IscsiBootPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IscsiBootPolicyDefinition = IscsiBootPolicyDefinition


@dataclass
class IscsiIpV4ConfigDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Gateway: Optional[str]
    Netmask: Optional[str]
    ObjectType: Optional[str]
    PrimaryDns: Optional[str]
    SecondaryDns: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IscsiIpV4ConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IscsiIpV4ConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Gateway=json_data.get("Gateway"),
            Netmask=json_data.get("Netmask"),
            ObjectType=json_data.get("ObjectType"),
            PrimaryDns=json_data.get("PrimaryDns"),
            SecondaryDns=json_data.get("SecondaryDns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IscsiIpV4ConfigDefinition = IscsiIpV4ConfigDefinition


@dataclass
class LanConnectivityPolicyDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LanConnectivityPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LanConnectivityPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LanConnectivityPolicyDefinition = LanConnectivityPolicyDefinition


@dataclass
class LcpVnicDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LcpVnicDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LcpVnicDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LcpVnicDefinition = LcpVnicDefinition


@dataclass
class MacLeaseDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MacLeaseDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MacLeaseDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MacLeaseDefinition = MacLeaseDefinition


@dataclass
class MacPoolDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MacPoolDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MacPoolDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MacPoolDefinition = MacPoolDefinition


@dataclass
class ParentDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParentDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParentDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParentDefinition = ParentDefinition


@dataclass
class PermissionResourcesDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PermissionResourcesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PermissionResourcesDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PermissionResourcesDefinition = PermissionResourcesDefinition


@dataclass
class PlacementDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Id: Optional[str]
    ObjectType: Optional[str]
    PciLink: Optional[float]
    SwitchId: Optional[str]
    Uplink: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PlacementDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlacementDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Id=json_data.get("Id"),
            ObjectType=json_data.get("ObjectType"),
            PciLink=json_data.get("PciLink"),
            SwitchId=json_data.get("SwitchId"),
            Uplink=json_data.get("Uplink"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlacementDefinition = PlacementDefinition


@dataclass
class ProfileDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProfileDefinition = ProfileDefinition


@dataclass
class SpVnicsDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SpVnicsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpVnicsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpVnicsDefinition = SpVnicsDefinition


@dataclass
class TagsDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class UsnicSettingsDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Cos: Optional[float]
    NrCount: Optional[float]
    ObjectType: Optional[str]
    UsnicAdapterPolicy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UsnicSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UsnicSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Cos=json_data.get("Cos"),
            NrCount=json_data.get("NrCount"),
            ObjectType=json_data.get("ObjectType"),
            UsnicAdapterPolicy=json_data.get("UsnicAdapterPolicy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UsnicSettingsDefinition = UsnicSettingsDefinition


@dataclass
class VersionContextDefinition3(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    InterestedMos: Optional[Sequence["_VersionContextDefinition"]]
    NrVersion: Optional[str]
    ObjectType: Optional[str]
    RefMo: Optional[Sequence["_VersionContextDefinition2"]]
    Timestamp: Optional[str]
    VersionType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VersionContextDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VersionContextDefinition3"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            InterestedMos=deserialize_list(json_data.get("InterestedMos"), VersionContextDefinition),
            NrVersion=json_data.get("NrVersion"),
            ObjectType=json_data.get("ObjectType"),
            RefMo=deserialize_list(json_data.get("RefMo"), VersionContextDefinition2),
            Timestamp=json_data.get("Timestamp"),
            VersionType=json_data.get("VersionType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VersionContextDefinition3 = VersionContextDefinition3


@dataclass
class VersionContextDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VersionContextDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VersionContextDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VersionContextDefinition = VersionContextDefinition


@dataclass
class VersionContextDefinition2(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VersionContextDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VersionContextDefinition2"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VersionContextDefinition2 = VersionContextDefinition2


@dataclass
class VmqSettingsDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Enabled: Optional[bool]
    MultiQueueSupport: Optional[bool]
    NumInterrupts: Optional[float]
    NumSubVnics: Optional[float]
    NumVmqs: Optional[float]
    ObjectType: Optional[str]
    VmmqAdapterPolicy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VmqSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VmqSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Enabled=json_data.get("Enabled"),
            MultiQueueSupport=json_data.get("MultiQueueSupport"),
            NumInterrupts=json_data.get("NumInterrupts"),
            NumSubVnics=json_data.get("NumSubVnics"),
            NumVmqs=json_data.get("NumVmqs"),
            ObjectType=json_data.get("ObjectType"),
            VmmqAdapterPolicy=json_data.get("VmmqAdapterPolicy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VmqSettingsDefinition = VmqSettingsDefinition


