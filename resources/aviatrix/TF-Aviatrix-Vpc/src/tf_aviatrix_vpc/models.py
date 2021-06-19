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
    AccountName: Optional[str]
    AviatrixFirenetVpc: Optional[bool]
    AviatrixTransitVpc: Optional[bool]
    AzureVnetResourceId: Optional[str]
    Cidr: Optional[str]
    CloudType: Optional[float]
    EnableNativeGwlb: Optional[bool]
    EnablePrivateOobSubnet: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    NumOfSubnetPairs: Optional[float]
    PrivateSubnets: Optional[Sequence["_PrivateSubnetsDefinition"]]
    PublicSubnets: Optional[Sequence["_PublicSubnetsDefinition"]]
    Region: Optional[str]
    ResourceGroup: Optional[str]
    RouteTables: Optional[Sequence[str]]
    SubnetSize: Optional[float]
    VpcId: Optional[str]
    Subnets: Optional[Sequence["_SubnetsDefinition"]]

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
            AccountName=json_data.get("AccountName"),
            AviatrixFirenetVpc=json_data.get("AviatrixFirenetVpc"),
            AviatrixTransitVpc=json_data.get("AviatrixTransitVpc"),
            AzureVnetResourceId=json_data.get("AzureVnetResourceId"),
            Cidr=json_data.get("Cidr"),
            CloudType=json_data.get("CloudType"),
            EnableNativeGwlb=json_data.get("EnableNativeGwlb"),
            EnablePrivateOobSubnet=json_data.get("EnablePrivateOobSubnet"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            NumOfSubnetPairs=json_data.get("NumOfSubnetPairs"),
            PrivateSubnets=deserialize_list(json_data.get("PrivateSubnets"), PrivateSubnetsDefinition),
            PublicSubnets=deserialize_list(json_data.get("PublicSubnets"), PublicSubnetsDefinition),
            Region=json_data.get("Region"),
            ResourceGroup=json_data.get("ResourceGroup"),
            RouteTables=json_data.get("RouteTables"),
            SubnetSize=json_data.get("SubnetSize"),
            VpcId=json_data.get("VpcId"),
            Subnets=deserialize_list(json_data.get("Subnets"), SubnetsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PrivateSubnetsDefinition(BaseModel):
    Cidr: Optional[str]
    Name: Optional[str]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PrivateSubnetsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivateSubnetsDefinition"]:
        if not json_data:
            return None
        return cls(
            Cidr=json_data.get("Cidr"),
            Name=json_data.get("Name"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivateSubnetsDefinition = PrivateSubnetsDefinition


@dataclass
class PublicSubnetsDefinition(BaseModel):
    Cidr: Optional[str]
    Name: Optional[str]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PublicSubnetsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublicSubnetsDefinition"]:
        if not json_data:
            return None
        return cls(
            Cidr=json_data.get("Cidr"),
            Name=json_data.get("Name"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublicSubnetsDefinition = PublicSubnetsDefinition


@dataclass
class SubnetsDefinition(BaseModel):
    Cidr: Optional[str]
    Name: Optional[str]
    Region: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SubnetsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubnetsDefinition"]:
        if not json_data:
            return None
        return cls(
            Cidr=json_data.get("Cidr"),
            Name=json_data.get("Name"),
            Region=json_data.get("Region"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubnetsDefinition = SubnetsDefinition


