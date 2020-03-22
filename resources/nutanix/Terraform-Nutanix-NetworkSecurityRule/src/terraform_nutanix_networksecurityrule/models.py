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
    ApiVersion: Optional[str]
    AppRuleAction: Optional[str]
    AppRuleTargetGroupDefaultInternalPolicy: Optional[str]
    AppRuleTargetGroupFilterKindList: Optional[Sequence[str]]
    AppRuleTargetGroupFilterType: Optional[str]
    AppRuleTargetGroupPeerSpecificationType: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    IsolationRuleAction: Optional[str]
    IsolationRuleFirstEntityFilterKindList: Optional[Sequence[str]]
    IsolationRuleFirstEntityFilterType: Optional[str]
    IsolationRuleSecondEntityFilterKindList: Optional[Sequence[str]]
    IsolationRuleSecondEntityFilterType: Optional[str]
    Metadata: Optional[Sequence["_Metadata"]]
    Name: Optional[str]
    OwnerReference: Optional[Sequence["_OwnerReference"]]
    ProjectReference: Optional[Sequence["_ProjectReference"]]
    AppRuleInboundAllowList: Optional[Sequence["_AppRuleInboundAllowList"]]
    AppRuleOutboundAllowList: Optional[Sequence["_AppRuleOutboundAllowList"]]
    AppRuleTargetGroupFilterParams: Optional[Sequence["_AppRuleTargetGroupFilterParams"]]
    Categories: Optional[Sequence["_Categories"]]
    IsolationRuleFirstEntityFilterParams: Optional[Sequence["_IsolationRuleFirstEntityFilterParams"]]
    IsolationRuleSecondEntityFilterParams: Optional[Sequence["_IsolationRuleSecondEntityFilterParams"]]
    FilterParams: Optional[Sequence["_FilterParams"]]
    IcmpTypeCodeList: Optional[Sequence["_IcmpTypeCodeList"]]
    TcpPortRangeList: Optional[Sequence["_TcpPortRangeList"]]
    UdpPortRangeList: Optional[Sequence["_UdpPortRangeList"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ApiVersion=json_data.get("ApiVersion"),
            AppRuleAction=json_data.get("AppRuleAction"),
            AppRuleTargetGroupDefaultInternalPolicy=json_data.get("AppRuleTargetGroupDefaultInternalPolicy"),
            AppRuleTargetGroupFilterKindList=json_data.get("AppRuleTargetGroupFilterKindList"),
            AppRuleTargetGroupFilterType=json_data.get("AppRuleTargetGroupFilterType"),
            AppRuleTargetGroupPeerSpecificationType=json_data.get("AppRuleTargetGroupPeerSpecificationType"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            IsolationRuleAction=json_data.get("IsolationRuleAction"),
            IsolationRuleFirstEntityFilterKindList=json_data.get("IsolationRuleFirstEntityFilterKindList"),
            IsolationRuleFirstEntityFilterType=json_data.get("IsolationRuleFirstEntityFilterType"),
            IsolationRuleSecondEntityFilterKindList=json_data.get("IsolationRuleSecondEntityFilterKindList"),
            IsolationRuleSecondEntityFilterType=json_data.get("IsolationRuleSecondEntityFilterType"),
            Metadata=json_data.get("Metadata"),
            Name=json_data.get("Name"),
            OwnerReference=json_data.get("OwnerReference"),
            ProjectReference=json_data.get("ProjectReference"),
            AppRuleInboundAllowList=json_data.get("AppRuleInboundAllowList"),
            AppRuleOutboundAllowList=json_data.get("AppRuleOutboundAllowList"),
            AppRuleTargetGroupFilterParams=json_data.get("AppRuleTargetGroupFilterParams"),
            Categories=json_data.get("Categories"),
            IsolationRuleFirstEntityFilterParams=json_data.get("IsolationRuleFirstEntityFilterParams"),
            IsolationRuleSecondEntityFilterParams=json_data.get("IsolationRuleSecondEntityFilterParams"),
            FilterParams=json_data.get("FilterParams"),
            IcmpTypeCodeList=json_data.get("IcmpTypeCodeList"),
            TcpPortRangeList=json_data.get("TcpPortRangeList"),
            UdpPortRangeList=json_data.get("UdpPortRangeList"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Metadata:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Metadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metadata"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Metadata = Metadata


@dataclass
class OwnerReference:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OwnerReference"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OwnerReference"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OwnerReference = OwnerReference


@dataclass
class ProjectReference:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProjectReference"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProjectReference"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProjectReference = ProjectReference


@dataclass
class AppRuleInboundAllowList:
    ExpirationTime: Optional[str]
    FilterKindList: Optional[Sequence[str]]
    FilterType: Optional[str]
    IpSubnet: Optional[str]
    IpSubnetPrefixLength: Optional[str]
    NetworkFunctionChainReference: Optional[Sequence["_NetworkFunctionChainReference"]]
    PeerSpecificationType: Optional[str]
    Protocol: Optional[str]
    FilterParams: Optional[Sequence["_FilterParams"]]
    IcmpTypeCodeList: Optional[Sequence["_IcmpTypeCodeList"]]
    TcpPortRangeList: Optional[Sequence["_TcpPortRangeList"]]
    UdpPortRangeList: Optional[Sequence["_UdpPortRangeList"]]

    @classmethod
    def _deserialize(
        cls: Type["_AppRuleInboundAllowList"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AppRuleInboundAllowList"]:
        if not json_data:
            return None
        return cls(
            ExpirationTime=json_data.get("ExpirationTime"),
            FilterKindList=json_data.get("FilterKindList"),
            FilterType=json_data.get("FilterType"),
            IpSubnet=json_data.get("IpSubnet"),
            IpSubnetPrefixLength=json_data.get("IpSubnetPrefixLength"),
            NetworkFunctionChainReference=json_data.get("NetworkFunctionChainReference"),
            PeerSpecificationType=json_data.get("PeerSpecificationType"),
            Protocol=json_data.get("Protocol"),
            FilterParams=json_data.get("FilterParams"),
            IcmpTypeCodeList=json_data.get("IcmpTypeCodeList"),
            TcpPortRangeList=json_data.get("TcpPortRangeList"),
            UdpPortRangeList=json_data.get("UdpPortRangeList"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AppRuleInboundAllowList = AppRuleInboundAllowList


@dataclass
class NetworkFunctionChainReference:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkFunctionChainReference"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkFunctionChainReference"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkFunctionChainReference = NetworkFunctionChainReference


@dataclass
class FilterParams:
    Name: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_FilterParams"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterParams"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterParams = FilterParams


@dataclass
class IcmpTypeCodeList:
    Code: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IcmpTypeCodeList"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IcmpTypeCodeList"]:
        if not json_data:
            return None
        return cls(
            Code=json_data.get("Code"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IcmpTypeCodeList = IcmpTypeCodeList


@dataclass
class TcpPortRangeList:
    EndPort: Optional[float]
    StartPort: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TcpPortRangeList"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TcpPortRangeList"]:
        if not json_data:
            return None
        return cls(
            EndPort=json_data.get("EndPort"),
            StartPort=json_data.get("StartPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TcpPortRangeList = TcpPortRangeList


@dataclass
class UdpPortRangeList:
    EndPort: Optional[float]
    StartPort: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_UdpPortRangeList"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UdpPortRangeList"]:
        if not json_data:
            return None
        return cls(
            EndPort=json_data.get("EndPort"),
            StartPort=json_data.get("StartPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UdpPortRangeList = UdpPortRangeList


@dataclass
class AppRuleOutboundAllowList:
    ExpirationTime: Optional[str]
    FilterKindList: Optional[Sequence[str]]
    FilterType: Optional[str]
    IpSubnet: Optional[str]
    IpSubnetPrefixLength: Optional[str]
    NetworkFunctionChainReference: Optional[Sequence["_NetworkFunctionChainReference2"]]
    PeerSpecificationType: Optional[str]
    Protocol: Optional[str]
    FilterParams: Optional[Sequence["_FilterParams"]]
    IcmpTypeCodeList: Optional[Sequence["_IcmpTypeCodeList"]]
    TcpPortRangeList: Optional[Sequence["_TcpPortRangeList"]]
    UdpPortRangeList: Optional[Sequence["_UdpPortRangeList"]]

    @classmethod
    def _deserialize(
        cls: Type["_AppRuleOutboundAllowList"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AppRuleOutboundAllowList"]:
        if not json_data:
            return None
        return cls(
            ExpirationTime=json_data.get("ExpirationTime"),
            FilterKindList=json_data.get("FilterKindList"),
            FilterType=json_data.get("FilterType"),
            IpSubnet=json_data.get("IpSubnet"),
            IpSubnetPrefixLength=json_data.get("IpSubnetPrefixLength"),
            NetworkFunctionChainReference=json_data.get("NetworkFunctionChainReference"),
            PeerSpecificationType=json_data.get("PeerSpecificationType"),
            Protocol=json_data.get("Protocol"),
            FilterParams=json_data.get("FilterParams"),
            IcmpTypeCodeList=json_data.get("IcmpTypeCodeList"),
            TcpPortRangeList=json_data.get("TcpPortRangeList"),
            UdpPortRangeList=json_data.get("UdpPortRangeList"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AppRuleOutboundAllowList = AppRuleOutboundAllowList


@dataclass
class NetworkFunctionChainReference2:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkFunctionChainReference2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkFunctionChainReference2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkFunctionChainReference2 = NetworkFunctionChainReference2


@dataclass
class AppRuleTargetGroupFilterParams:
    Name: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AppRuleTargetGroupFilterParams"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AppRuleTargetGroupFilterParams"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AppRuleTargetGroupFilterParams = AppRuleTargetGroupFilterParams


@dataclass
class Categories:
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Categories"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Categories"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Categories = Categories


@dataclass
class IsolationRuleFirstEntityFilterParams:
    Name: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_IsolationRuleFirstEntityFilterParams"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IsolationRuleFirstEntityFilterParams"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IsolationRuleFirstEntityFilterParams = IsolationRuleFirstEntityFilterParams


@dataclass
class IsolationRuleSecondEntityFilterParams:
    Name: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_IsolationRuleSecondEntityFilterParams"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IsolationRuleSecondEntityFilterParams"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IsolationRuleSecondEntityFilterParams = IsolationRuleSecondEntityFilterParams


