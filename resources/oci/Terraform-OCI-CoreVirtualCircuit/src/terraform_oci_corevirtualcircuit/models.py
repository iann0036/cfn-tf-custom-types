# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    BandwidthShapeName: Optional[str]
    BgpManagement: Optional[str]
    BgpSessionState: Optional[str]
    CompartmentId: Optional[str]
    CustomerAsn: Optional[str]
    CustomerBgpAsn: Optional[float]
    DefinedTags: Optional[Sequence["_DefinedTags"]]
    DisplayName: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTags"]]
    GatewayId: Optional[str]
    Id: Optional[str]
    OracleBgpAsn: Optional[float]
    ProviderServiceId: Optional[str]
    ProviderServiceKeyName: Optional[str]
    ProviderState: Optional[str]
    ReferenceComment: Optional[str]
    Region: Optional[str]
    ServiceType: Optional[str]
    State: Optional[str]
    TimeCreated: Optional[str]
    Type: Optional[str]
    CrossConnectMappings: Optional[Sequence["_CrossConnectMappings"]]
    PublicPrefixes: Optional[Sequence["_PublicPrefixes"]]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            BandwidthShapeName=json_data.get("BandwidthShapeName"),
            BgpManagement=json_data.get("BgpManagement"),
            BgpSessionState=json_data.get("BgpSessionState"),
            CompartmentId=json_data.get("CompartmentId"),
            CustomerAsn=json_data.get("CustomerAsn"),
            CustomerBgpAsn=json_data.get("CustomerBgpAsn"),
            DefinedTags=json_data.get("DefinedTags"),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=json_data.get("FreeformTags"),
            GatewayId=json_data.get("GatewayId"),
            Id=json_data.get("Id"),
            OracleBgpAsn=json_data.get("OracleBgpAsn"),
            ProviderServiceId=json_data.get("ProviderServiceId"),
            ProviderServiceKeyName=json_data.get("ProviderServiceKeyName"),
            ProviderState=json_data.get("ProviderState"),
            ReferenceComment=json_data.get("ReferenceComment"),
            Region=json_data.get("Region"),
            ServiceType=json_data.get("ServiceType"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            Type=json_data.get("Type"),
            CrossConnectMappings=json_data.get("CrossConnectMappings"),
            PublicPrefixes=json_data.get("PublicPrefixes"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefinedTags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTags = DefinedTags


@dataclass
class FreeformTags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTags = FreeformTags


@dataclass
class CrossConnectMappings:
    BgpMd5authKey: Optional[str]
    CrossConnectOrCrossConnectGroupId: Optional[str]
    CustomerBgpPeeringIp: Optional[str]
    CustomerBgpPeeringIpv6: Optional[str]
    OracleBgpPeeringIp: Optional[str]
    OracleBgpPeeringIpv6: Optional[str]
    Vlan: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CrossConnectMappings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CrossConnectMappings"]:
        if not json_data:
            return None
        return cls(
            BgpMd5authKey=json_data.get("BgpMd5authKey"),
            CrossConnectOrCrossConnectGroupId=json_data.get("CrossConnectOrCrossConnectGroupId"),
            CustomerBgpPeeringIp=json_data.get("CustomerBgpPeeringIp"),
            CustomerBgpPeeringIpv6=json_data.get("CustomerBgpPeeringIpv6"),
            OracleBgpPeeringIp=json_data.get("OracleBgpPeeringIp"),
            OracleBgpPeeringIpv6=json_data.get("OracleBgpPeeringIpv6"),
            Vlan=json_data.get("Vlan"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CrossConnectMappings = CrossConnectMappings


@dataclass
class PublicPrefixes:
    CidrBlock: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PublicPrefixes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublicPrefixes"]:
        if not json_data:
            return None
        return cls(
            CidrBlock=json_data.get("CidrBlock"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublicPrefixes = PublicPrefixes


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


