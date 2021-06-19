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
    BandwidthShapeName: Optional[str]
    BgpIpv6sessionState: Optional[str]
    BgpManagement: Optional[str]
    BgpSessionState: Optional[str]
    CompartmentId: Optional[str]
    CustomerAsn: Optional[str]
    CustomerBgpAsn: Optional[float]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    DisplayName: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    GatewayId: Optional[str]
    Id: Optional[str]
    OracleBgpAsn: Optional[float]
    ProviderServiceId: Optional[str]
    ProviderServiceKeyName: Optional[str]
    ProviderState: Optional[str]
    ReferenceComment: Optional[str]
    Region: Optional[str]
    RoutingPolicy: Optional[Sequence[str]]
    ServiceType: Optional[str]
    State: Optional[str]
    TimeCreated: Optional[str]
    Type: Optional[str]
    CrossConnectMappings: Optional[Sequence["_CrossConnectMappingsDefinition"]]
    PublicPrefixes: Optional[Sequence["_PublicPrefixesDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            BandwidthShapeName=json_data.get("BandwidthShapeName"),
            BgpIpv6sessionState=json_data.get("BgpIpv6sessionState"),
            BgpManagement=json_data.get("BgpManagement"),
            BgpSessionState=json_data.get("BgpSessionState"),
            CompartmentId=json_data.get("CompartmentId"),
            CustomerAsn=json_data.get("CustomerAsn"),
            CustomerBgpAsn=json_data.get("CustomerBgpAsn"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            GatewayId=json_data.get("GatewayId"),
            Id=json_data.get("Id"),
            OracleBgpAsn=json_data.get("OracleBgpAsn"),
            ProviderServiceId=json_data.get("ProviderServiceId"),
            ProviderServiceKeyName=json_data.get("ProviderServiceKeyName"),
            ProviderState=json_data.get("ProviderState"),
            ReferenceComment=json_data.get("ReferenceComment"),
            Region=json_data.get("Region"),
            RoutingPolicy=json_data.get("RoutingPolicy"),
            ServiceType=json_data.get("ServiceType"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            Type=json_data.get("Type"),
            CrossConnectMappings=deserialize_list(json_data.get("CrossConnectMappings"), CrossConnectMappingsDefinition),
            PublicPrefixes=deserialize_list(json_data.get("PublicPrefixes"), PublicPrefixesDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefinedTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTagsDefinition = DefinedTagsDefinition


@dataclass
class FreeformTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTagsDefinition = FreeformTagsDefinition


@dataclass
class CrossConnectMappingsDefinition(BaseModel):
    BgpMd5authKey: Optional[str]
    CrossConnectOrCrossConnectGroupId: Optional[str]
    CustomerBgpPeeringIp: Optional[str]
    CustomerBgpPeeringIpv6: Optional[str]
    OracleBgpPeeringIp: Optional[str]
    OracleBgpPeeringIpv6: Optional[str]
    Vlan: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CrossConnectMappingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CrossConnectMappingsDefinition"]:
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
_CrossConnectMappingsDefinition = CrossConnectMappingsDefinition


@dataclass
class PublicPrefixesDefinition(BaseModel):
    CidrBlock: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PublicPrefixesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublicPrefixesDefinition"]:
        if not json_data:
            return None
        return cls(
            CidrBlock=json_data.get("CidrBlock"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublicPrefixesDefinition = PublicPrefixesDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


