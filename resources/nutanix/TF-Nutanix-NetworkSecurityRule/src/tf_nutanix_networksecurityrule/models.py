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
    AdRuleAction: Optional[str]
    AdRuleTargetGroupDefaultInternalPolicy: Optional[str]
    AdRuleTargetGroupFilterKindList: Optional[Sequence[str]]
    AdRuleTargetGroupFilterType: Optional[str]
    AdRuleTargetGroupPeerSpecificationType: Optional[str]
    AllowIpv6Traffic: Optional[bool]
    ApiVersion: Optional[str]
    AppRuleAction: Optional[str]
    AppRuleTargetGroupDefaultInternalPolicy: Optional[str]
    AppRuleTargetGroupFilterKindList: Optional[Sequence[str]]
    AppRuleTargetGroupFilterType: Optional[str]
    AppRuleTargetGroupPeerSpecificationType: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    IsPolicyHitlogEnabled: Optional[bool]
    IsolationRuleAction: Optional[str]
    IsolationRuleFirstEntityFilterKindList: Optional[Sequence[str]]
    IsolationRuleFirstEntityFilterType: Optional[str]
    IsolationRuleSecondEntityFilterKindList: Optional[Sequence[str]]
    IsolationRuleSecondEntityFilterType: Optional[str]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Name: Optional[str]
    OwnerReference: Optional[Sequence["_OwnerReferenceDefinition"]]
    ProjectReference: Optional[Sequence["_ProjectReferenceDefinition"]]
    AdRuleInboundAllowList: Optional[Sequence["_AdRuleInboundAllowListDefinition"]]
    AdRuleOutboundAllowList: Optional[Sequence["_AdRuleOutboundAllowListDefinition"]]
    AdRuleTargetGroupFilterParams: Optional[Sequence["_AdRuleTargetGroupFilterParamsDefinition"]]
    AppRuleInboundAllowList: Optional[Sequence["_AppRuleInboundAllowListDefinition"]]
    AppRuleOutboundAllowList: Optional[Sequence["_AppRuleOutboundAllowListDefinition"]]
    AppRuleTargetGroupFilterParams: Optional[Sequence["_AppRuleTargetGroupFilterParamsDefinition"]]
    Categories: Optional[Sequence["_CategoriesDefinition"]]
    IsolationRuleFirstEntityFilterParams: Optional[Sequence["_IsolationRuleFirstEntityFilterParamsDefinition"]]
    IsolationRuleSecondEntityFilterParams: Optional[Sequence["_IsolationRuleSecondEntityFilterParamsDefinition"]]

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
            AdRuleAction=json_data.get("AdRuleAction"),
            AdRuleTargetGroupDefaultInternalPolicy=json_data.get("AdRuleTargetGroupDefaultInternalPolicy"),
            AdRuleTargetGroupFilterKindList=json_data.get("AdRuleTargetGroupFilterKindList"),
            AdRuleTargetGroupFilterType=json_data.get("AdRuleTargetGroupFilterType"),
            AdRuleTargetGroupPeerSpecificationType=json_data.get("AdRuleTargetGroupPeerSpecificationType"),
            AllowIpv6Traffic=json_data.get("AllowIpv6Traffic"),
            ApiVersion=json_data.get("ApiVersion"),
            AppRuleAction=json_data.get("AppRuleAction"),
            AppRuleTargetGroupDefaultInternalPolicy=json_data.get("AppRuleTargetGroupDefaultInternalPolicy"),
            AppRuleTargetGroupFilterKindList=json_data.get("AppRuleTargetGroupFilterKindList"),
            AppRuleTargetGroupFilterType=json_data.get("AppRuleTargetGroupFilterType"),
            AppRuleTargetGroupPeerSpecificationType=json_data.get("AppRuleTargetGroupPeerSpecificationType"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            IsPolicyHitlogEnabled=json_data.get("IsPolicyHitlogEnabled"),
            IsolationRuleAction=json_data.get("IsolationRuleAction"),
            IsolationRuleFirstEntityFilterKindList=json_data.get("IsolationRuleFirstEntityFilterKindList"),
            IsolationRuleFirstEntityFilterType=json_data.get("IsolationRuleFirstEntityFilterType"),
            IsolationRuleSecondEntityFilterKindList=json_data.get("IsolationRuleSecondEntityFilterKindList"),
            IsolationRuleSecondEntityFilterType=json_data.get("IsolationRuleSecondEntityFilterType"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Name=json_data.get("Name"),
            OwnerReference=deserialize_list(json_data.get("OwnerReference"), OwnerReferenceDefinition),
            ProjectReference=deserialize_list(json_data.get("ProjectReference"), ProjectReferenceDefinition),
            AdRuleInboundAllowList=deserialize_list(json_data.get("AdRuleInboundAllowList"), AdRuleInboundAllowListDefinition),
            AdRuleOutboundAllowList=deserialize_list(json_data.get("AdRuleOutboundAllowList"), AdRuleOutboundAllowListDefinition),
            AdRuleTargetGroupFilterParams=deserialize_list(json_data.get("AdRuleTargetGroupFilterParams"), AdRuleTargetGroupFilterParamsDefinition),
            AppRuleInboundAllowList=deserialize_list(json_data.get("AppRuleInboundAllowList"), AppRuleInboundAllowListDefinition),
            AppRuleOutboundAllowList=deserialize_list(json_data.get("AppRuleOutboundAllowList"), AppRuleOutboundAllowListDefinition),
            AppRuleTargetGroupFilterParams=deserialize_list(json_data.get("AppRuleTargetGroupFilterParams"), AppRuleTargetGroupFilterParamsDefinition),
            Categories=deserialize_list(json_data.get("Categories"), CategoriesDefinition),
            IsolationRuleFirstEntityFilterParams=deserialize_list(json_data.get("IsolationRuleFirstEntityFilterParams"), IsolationRuleFirstEntityFilterParamsDefinition),
            IsolationRuleSecondEntityFilterParams=deserialize_list(json_data.get("IsolationRuleSecondEntityFilterParams"), IsolationRuleSecondEntityFilterParamsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MetadataDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataDefinition = MetadataDefinition


@dataclass
class OwnerReferenceDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OwnerReferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OwnerReferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OwnerReferenceDefinition = OwnerReferenceDefinition


@dataclass
class ProjectReferenceDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProjectReferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProjectReferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProjectReferenceDefinition = ProjectReferenceDefinition


@dataclass
class AdRuleInboundAllowListDefinition(BaseModel):
    ExpirationTime: Optional[str]
    FilterKindList: Optional[Sequence[str]]
    FilterType: Optional[str]
    IpSubnet: Optional[str]
    IpSubnetPrefixLength: Optional[str]
    NetworkFunctionChainReference: Optional[Sequence["_NetworkFunctionChainReferenceDefinition"]]
    PeerSpecificationType: Optional[str]
    Protocol: Optional[str]
    FilterParams: Optional[Sequence["_FilterParamsDefinition"]]
    IcmpTypeCodeList: Optional[Sequence["_IcmpTypeCodeListDefinition"]]
    TcpPortRangeList: Optional[Sequence["_TcpPortRangeListDefinition"]]
    UdpPortRangeList: Optional[Sequence["_UdpPortRangeListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AdRuleInboundAllowListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdRuleInboundAllowListDefinition"]:
        if not json_data:
            return None
        return cls(
            ExpirationTime=json_data.get("ExpirationTime"),
            FilterKindList=json_data.get("FilterKindList"),
            FilterType=json_data.get("FilterType"),
            IpSubnet=json_data.get("IpSubnet"),
            IpSubnetPrefixLength=json_data.get("IpSubnetPrefixLength"),
            NetworkFunctionChainReference=deserialize_list(json_data.get("NetworkFunctionChainReference"), NetworkFunctionChainReferenceDefinition),
            PeerSpecificationType=json_data.get("PeerSpecificationType"),
            Protocol=json_data.get("Protocol"),
            FilterParams=deserialize_list(json_data.get("FilterParams"), FilterParamsDefinition),
            IcmpTypeCodeList=deserialize_list(json_data.get("IcmpTypeCodeList"), IcmpTypeCodeListDefinition),
            TcpPortRangeList=deserialize_list(json_data.get("TcpPortRangeList"), TcpPortRangeListDefinition),
            UdpPortRangeList=deserialize_list(json_data.get("UdpPortRangeList"), UdpPortRangeListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdRuleInboundAllowListDefinition = AdRuleInboundAllowListDefinition


@dataclass
class NetworkFunctionChainReferenceDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkFunctionChainReferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkFunctionChainReferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkFunctionChainReferenceDefinition = NetworkFunctionChainReferenceDefinition


@dataclass
class FilterParamsDefinition(BaseModel):
    Name: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_FilterParamsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterParamsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterParamsDefinition = FilterParamsDefinition


@dataclass
class IcmpTypeCodeListDefinition(BaseModel):
    Code: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IcmpTypeCodeListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IcmpTypeCodeListDefinition"]:
        if not json_data:
            return None
        return cls(
            Code=json_data.get("Code"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IcmpTypeCodeListDefinition = IcmpTypeCodeListDefinition


@dataclass
class TcpPortRangeListDefinition(BaseModel):
    EndPort: Optional[float]
    StartPort: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TcpPortRangeListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TcpPortRangeListDefinition"]:
        if not json_data:
            return None
        return cls(
            EndPort=json_data.get("EndPort"),
            StartPort=json_data.get("StartPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TcpPortRangeListDefinition = TcpPortRangeListDefinition


@dataclass
class UdpPortRangeListDefinition(BaseModel):
    EndPort: Optional[float]
    StartPort: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_UdpPortRangeListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UdpPortRangeListDefinition"]:
        if not json_data:
            return None
        return cls(
            EndPort=json_data.get("EndPort"),
            StartPort=json_data.get("StartPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UdpPortRangeListDefinition = UdpPortRangeListDefinition


@dataclass
class AdRuleOutboundAllowListDefinition(BaseModel):
    ExpirationTime: Optional[str]
    FilterKindList: Optional[Sequence[str]]
    FilterType: Optional[str]
    IpSubnet: Optional[str]
    IpSubnetPrefixLength: Optional[str]
    NetworkFunctionChainReference: Optional[Sequence["_NetworkFunctionChainReferenceDefinition2"]]
    PeerSpecificationType: Optional[str]
    Protocol: Optional[str]
    FilterParams: Optional[Sequence["_FilterParamsDefinition"]]
    IcmpTypeCodeList: Optional[Sequence["_IcmpTypeCodeListDefinition"]]
    TcpPortRangeList: Optional[Sequence["_TcpPortRangeListDefinition"]]
    UdpPortRangeList: Optional[Sequence["_UdpPortRangeListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AdRuleOutboundAllowListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdRuleOutboundAllowListDefinition"]:
        if not json_data:
            return None
        return cls(
            ExpirationTime=json_data.get("ExpirationTime"),
            FilterKindList=json_data.get("FilterKindList"),
            FilterType=json_data.get("FilterType"),
            IpSubnet=json_data.get("IpSubnet"),
            IpSubnetPrefixLength=json_data.get("IpSubnetPrefixLength"),
            NetworkFunctionChainReference=deserialize_list(json_data.get("NetworkFunctionChainReference"), NetworkFunctionChainReferenceDefinition2),
            PeerSpecificationType=json_data.get("PeerSpecificationType"),
            Protocol=json_data.get("Protocol"),
            FilterParams=deserialize_list(json_data.get("FilterParams"), FilterParamsDefinition),
            IcmpTypeCodeList=deserialize_list(json_data.get("IcmpTypeCodeList"), IcmpTypeCodeListDefinition),
            TcpPortRangeList=deserialize_list(json_data.get("TcpPortRangeList"), TcpPortRangeListDefinition),
            UdpPortRangeList=deserialize_list(json_data.get("UdpPortRangeList"), UdpPortRangeListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdRuleOutboundAllowListDefinition = AdRuleOutboundAllowListDefinition


@dataclass
class NetworkFunctionChainReferenceDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkFunctionChainReferenceDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkFunctionChainReferenceDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkFunctionChainReferenceDefinition2 = NetworkFunctionChainReferenceDefinition2


@dataclass
class AdRuleTargetGroupFilterParamsDefinition(BaseModel):
    Name: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AdRuleTargetGroupFilterParamsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdRuleTargetGroupFilterParamsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdRuleTargetGroupFilterParamsDefinition = AdRuleTargetGroupFilterParamsDefinition


@dataclass
class AppRuleInboundAllowListDefinition(BaseModel):
    ExpirationTime: Optional[str]
    FilterKindList: Optional[Sequence[str]]
    FilterType: Optional[str]
    IpSubnet: Optional[str]
    IpSubnetPrefixLength: Optional[str]
    NetworkFunctionChainReference: Optional[Sequence["_NetworkFunctionChainReferenceDefinition3"]]
    PeerSpecificationType: Optional[str]
    Protocol: Optional[str]
    FilterParams: Optional[Sequence["_FilterParamsDefinition"]]
    IcmpTypeCodeList: Optional[Sequence["_IcmpTypeCodeListDefinition"]]
    TcpPortRangeList: Optional[Sequence["_TcpPortRangeListDefinition"]]
    UdpPortRangeList: Optional[Sequence["_UdpPortRangeListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AppRuleInboundAllowListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AppRuleInboundAllowListDefinition"]:
        if not json_data:
            return None
        return cls(
            ExpirationTime=json_data.get("ExpirationTime"),
            FilterKindList=json_data.get("FilterKindList"),
            FilterType=json_data.get("FilterType"),
            IpSubnet=json_data.get("IpSubnet"),
            IpSubnetPrefixLength=json_data.get("IpSubnetPrefixLength"),
            NetworkFunctionChainReference=deserialize_list(json_data.get("NetworkFunctionChainReference"), NetworkFunctionChainReferenceDefinition3),
            PeerSpecificationType=json_data.get("PeerSpecificationType"),
            Protocol=json_data.get("Protocol"),
            FilterParams=deserialize_list(json_data.get("FilterParams"), FilterParamsDefinition),
            IcmpTypeCodeList=deserialize_list(json_data.get("IcmpTypeCodeList"), IcmpTypeCodeListDefinition),
            TcpPortRangeList=deserialize_list(json_data.get("TcpPortRangeList"), TcpPortRangeListDefinition),
            UdpPortRangeList=deserialize_list(json_data.get("UdpPortRangeList"), UdpPortRangeListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AppRuleInboundAllowListDefinition = AppRuleInboundAllowListDefinition


@dataclass
class NetworkFunctionChainReferenceDefinition3(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkFunctionChainReferenceDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkFunctionChainReferenceDefinition3"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkFunctionChainReferenceDefinition3 = NetworkFunctionChainReferenceDefinition3


@dataclass
class AppRuleOutboundAllowListDefinition(BaseModel):
    ExpirationTime: Optional[str]
    FilterKindList: Optional[Sequence[str]]
    FilterType: Optional[str]
    IpSubnet: Optional[str]
    IpSubnetPrefixLength: Optional[str]
    NetworkFunctionChainReference: Optional[Sequence["_NetworkFunctionChainReferenceDefinition4"]]
    PeerSpecificationType: Optional[str]
    Protocol: Optional[str]
    FilterParams: Optional[Sequence["_FilterParamsDefinition"]]
    IcmpTypeCodeList: Optional[Sequence["_IcmpTypeCodeListDefinition"]]
    TcpPortRangeList: Optional[Sequence["_TcpPortRangeListDefinition"]]
    UdpPortRangeList: Optional[Sequence["_UdpPortRangeListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AppRuleOutboundAllowListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AppRuleOutboundAllowListDefinition"]:
        if not json_data:
            return None
        return cls(
            ExpirationTime=json_data.get("ExpirationTime"),
            FilterKindList=json_data.get("FilterKindList"),
            FilterType=json_data.get("FilterType"),
            IpSubnet=json_data.get("IpSubnet"),
            IpSubnetPrefixLength=json_data.get("IpSubnetPrefixLength"),
            NetworkFunctionChainReference=deserialize_list(json_data.get("NetworkFunctionChainReference"), NetworkFunctionChainReferenceDefinition4),
            PeerSpecificationType=json_data.get("PeerSpecificationType"),
            Protocol=json_data.get("Protocol"),
            FilterParams=deserialize_list(json_data.get("FilterParams"), FilterParamsDefinition),
            IcmpTypeCodeList=deserialize_list(json_data.get("IcmpTypeCodeList"), IcmpTypeCodeListDefinition),
            TcpPortRangeList=deserialize_list(json_data.get("TcpPortRangeList"), TcpPortRangeListDefinition),
            UdpPortRangeList=deserialize_list(json_data.get("UdpPortRangeList"), UdpPortRangeListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AppRuleOutboundAllowListDefinition = AppRuleOutboundAllowListDefinition


@dataclass
class NetworkFunctionChainReferenceDefinition4(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkFunctionChainReferenceDefinition4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkFunctionChainReferenceDefinition4"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkFunctionChainReferenceDefinition4 = NetworkFunctionChainReferenceDefinition4


@dataclass
class AppRuleTargetGroupFilterParamsDefinition(BaseModel):
    Name: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AppRuleTargetGroupFilterParamsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AppRuleTargetGroupFilterParamsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AppRuleTargetGroupFilterParamsDefinition = AppRuleTargetGroupFilterParamsDefinition


@dataclass
class CategoriesDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CategoriesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CategoriesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CategoriesDefinition = CategoriesDefinition


@dataclass
class IsolationRuleFirstEntityFilterParamsDefinition(BaseModel):
    Name: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_IsolationRuleFirstEntityFilterParamsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IsolationRuleFirstEntityFilterParamsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IsolationRuleFirstEntityFilterParamsDefinition = IsolationRuleFirstEntityFilterParamsDefinition


@dataclass
class IsolationRuleSecondEntityFilterParamsDefinition(BaseModel):
    Name: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_IsolationRuleSecondEntityFilterParamsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IsolationRuleSecondEntityFilterParamsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IsolationRuleSecondEntityFilterParamsDefinition = IsolationRuleSecondEntityFilterParamsDefinition


