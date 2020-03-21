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
    AvailabilityZoneReference: Optional[Sequence["_AvailabilityZoneReference"]]
    ClusterName: Optional[str]
    ClusterUuid: Optional[str]
    DefaultGatewayIp: Optional[str]
    Description: Optional[str]
    DhcpDomainNameServerList: Optional[Sequence[str]]
    DhcpDomainSearchList: Optional[Sequence[str]]
    DhcpOptions: Optional[Sequence["_DhcpOptions"]]
    DhcpServerAddress: Optional[Sequence["_DhcpServerAddress"]]
    DhcpServerAddressPort: Optional[float]
    Id: Optional[str]
    IpConfigPoolListRanges: Optional[Sequence[str]]
    Metadata: Optional[Sequence["_Metadata"]]
    Name: Optional[str]
    NetworkFunctionChainReference: Optional[Sequence["_NetworkFunctionChainReference"]]
    OwnerReference: Optional[Sequence["_OwnerReference"]]
    PrefixLength: Optional[float]
    ProjectReference: Optional[Sequence["_ProjectReference"]]
    State: Optional[str]
    SubnetIp: Optional[str]
    SubnetType: Optional[str]
    VlanId: Optional[float]
    VswitchName: Optional[str]
    Categories: Optional[Sequence["_Categories"]]

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
            AvailabilityZoneReference=json_data.get("AvailabilityZoneReference"),
            ClusterName=json_data.get("ClusterName"),
            ClusterUuid=json_data.get("ClusterUuid"),
            DefaultGatewayIp=json_data.get("DefaultGatewayIp"),
            Description=json_data.get("Description"),
            DhcpDomainNameServerList=json_data.get("DhcpDomainNameServerList"),
            DhcpDomainSearchList=json_data.get("DhcpDomainSearchList"),
            DhcpOptions=json_data.get("DhcpOptions"),
            DhcpServerAddress=json_data.get("DhcpServerAddress"),
            DhcpServerAddressPort=json_data.get("DhcpServerAddressPort"),
            Id=json_data.get("Id"),
            IpConfigPoolListRanges=json_data.get("IpConfigPoolListRanges"),
            Metadata=json_data.get("Metadata"),
            Name=json_data.get("Name"),
            NetworkFunctionChainReference=json_data.get("NetworkFunctionChainReference"),
            OwnerReference=json_data.get("OwnerReference"),
            PrefixLength=json_data.get("PrefixLength"),
            ProjectReference=json_data.get("ProjectReference"),
            State=json_data.get("State"),
            SubnetIp=json_data.get("SubnetIp"),
            SubnetType=json_data.get("SubnetType"),
            VlanId=json_data.get("VlanId"),
            VswitchName=json_data.get("VswitchName"),
            Categories=json_data.get("Categories"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AvailabilityZoneReference:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AvailabilityZoneReference"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AvailabilityZoneReference"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AvailabilityZoneReference = AvailabilityZoneReference


@dataclass
class DhcpOptions:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DhcpOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DhcpOptions"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DhcpOptions = DhcpOptions


@dataclass
class DhcpServerAddress:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DhcpServerAddress"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DhcpServerAddress"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DhcpServerAddress = DhcpServerAddress


@dataclass
class Metadata:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Metadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metadata"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Metadata = Metadata


@dataclass
class NetworkFunctionChainReference:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkFunctionChainReference"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkFunctionChainReference"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkFunctionChainReference = NetworkFunctionChainReference


@dataclass
class OwnerReference:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OwnerReference"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OwnerReference"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OwnerReference = OwnerReference


@dataclass
class ProjectReference:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProjectReference"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProjectReference"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProjectReference = ProjectReference


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


