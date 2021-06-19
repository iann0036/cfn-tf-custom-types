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
    AcceptanceRequired: Optional[bool]
    AllowedPrincipals: Optional[Sequence[str]]
    Arn: Optional[str]
    AvailabilityZones: Optional[Sequence[str]]
    BaseEndpointDnsNames: Optional[Sequence[str]]
    GatewayLoadBalancerArns: Optional[Sequence[str]]
    Id: Optional[str]
    ManagesVpcEndpoints: Optional[bool]
    NetworkLoadBalancerArns: Optional[Sequence[str]]
    PrivateDnsName: Optional[str]
    PrivateDnsNameConfiguration: Optional[Sequence["_PrivateDnsNameConfigurationDefinition"]]
    ServiceName: Optional[str]
    ServiceType: Optional[str]
    State: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]

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
            AcceptanceRequired=json_data.get("AcceptanceRequired"),
            AllowedPrincipals=json_data.get("AllowedPrincipals"),
            Arn=json_data.get("Arn"),
            AvailabilityZones=json_data.get("AvailabilityZones"),
            BaseEndpointDnsNames=json_data.get("BaseEndpointDnsNames"),
            GatewayLoadBalancerArns=json_data.get("GatewayLoadBalancerArns"),
            Id=json_data.get("Id"),
            ManagesVpcEndpoints=json_data.get("ManagesVpcEndpoints"),
            NetworkLoadBalancerArns=json_data.get("NetworkLoadBalancerArns"),
            PrivateDnsName=json_data.get("PrivateDnsName"),
            PrivateDnsNameConfiguration=deserialize_list(json_data.get("PrivateDnsNameConfiguration"), PrivateDnsNameConfigurationDefinition),
            ServiceName=json_data.get("ServiceName"),
            ServiceType=json_data.get("ServiceType"),
            State=json_data.get("State"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PrivateDnsNameConfigurationDefinition(BaseModel):
    Name: Optional[str]
    State: Optional[str]
    Type: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PrivateDnsNameConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivateDnsNameConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            State=json_data.get("State"),
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivateDnsNameConfigurationDefinition = PrivateDnsNameConfigurationDefinition


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


