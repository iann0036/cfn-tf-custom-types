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
    ApiVersion: Optional[str]
    AvailabilityZoneReference: Optional[Sequence["_AvailabilityZoneReferenceDefinition"]]
    ClusterName: Optional[str]
    ClusterUuid: Optional[str]
    DefaultGatewayIp: Optional[str]
    Description: Optional[str]
    DhcpDomainNameServerList: Optional[Sequence[str]]
    DhcpDomainSearchList: Optional[Sequence[str]]
    DhcpOptions: Optional[Sequence["_DhcpOptionsDefinition"]]
    DhcpServerAddress: Optional[Sequence["_DhcpServerAddressDefinition"]]
    DhcpServerAddressPort: Optional[float]
    Id: Optional[str]
    IpConfigPoolListRanges: Optional[Sequence[str]]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Name: Optional[str]
    NetworkFunctionChainReference: Optional[Sequence["_NetworkFunctionChainReferenceDefinition"]]
    OwnerReference: Optional[Sequence["_OwnerReferenceDefinition"]]
    PrefixLength: Optional[float]
    ProjectReference: Optional[Sequence["_ProjectReferenceDefinition"]]
    State: Optional[str]
    SubnetIp: Optional[str]
    SubnetType: Optional[str]
    VlanId: Optional[float]
    VswitchName: Optional[str]
    Categories: Optional[Sequence["_CategoriesDefinition"]]

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
            ApiVersion=json_data.get("ApiVersion"),
            AvailabilityZoneReference=deserialize_list(json_data.get("AvailabilityZoneReference"), AvailabilityZoneReferenceDefinition),
            ClusterName=json_data.get("ClusterName"),
            ClusterUuid=json_data.get("ClusterUuid"),
            DefaultGatewayIp=json_data.get("DefaultGatewayIp"),
            Description=json_data.get("Description"),
            DhcpDomainNameServerList=json_data.get("DhcpDomainNameServerList"),
            DhcpDomainSearchList=json_data.get("DhcpDomainSearchList"),
            DhcpOptions=deserialize_list(json_data.get("DhcpOptions"), DhcpOptionsDefinition),
            DhcpServerAddress=deserialize_list(json_data.get("DhcpServerAddress"), DhcpServerAddressDefinition),
            DhcpServerAddressPort=json_data.get("DhcpServerAddressPort"),
            Id=json_data.get("Id"),
            IpConfigPoolListRanges=json_data.get("IpConfigPoolListRanges"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Name=json_data.get("Name"),
            NetworkFunctionChainReference=deserialize_list(json_data.get("NetworkFunctionChainReference"), NetworkFunctionChainReferenceDefinition),
            OwnerReference=deserialize_list(json_data.get("OwnerReference"), OwnerReferenceDefinition),
            PrefixLength=json_data.get("PrefixLength"),
            ProjectReference=deserialize_list(json_data.get("ProjectReference"), ProjectReferenceDefinition),
            State=json_data.get("State"),
            SubnetIp=json_data.get("SubnetIp"),
            SubnetType=json_data.get("SubnetType"),
            VlanId=json_data.get("VlanId"),
            VswitchName=json_data.get("VswitchName"),
            Categories=deserialize_list(json_data.get("Categories"), CategoriesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AvailabilityZoneReferenceDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AvailabilityZoneReferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AvailabilityZoneReferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AvailabilityZoneReferenceDefinition = AvailabilityZoneReferenceDefinition


@dataclass
class DhcpOptionsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DhcpOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DhcpOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DhcpOptionsDefinition = DhcpOptionsDefinition


@dataclass
class DhcpServerAddressDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DhcpServerAddressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DhcpServerAddressDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DhcpServerAddressDefinition = DhcpServerAddressDefinition


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


