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
    AcceptanceRequired: Optional[bool]
    AllowedPrincipals: Optional[Sequence[str]]
    AvailabilityZones: Optional[Sequence[str]]
    BaseEndpointDnsNames: Optional[Sequence[str]]
    Id: Optional[str]
    ManagesVpcEndpoints: Optional[bool]
    NetworkLoadBalancerArns: Optional[Sequence[str]]
    PrivateDnsName: Optional[str]
    ServiceName: Optional[str]
    ServiceType: Optional[str]
    State: Optional[str]
    Tags: Optional[Sequence["_Tags"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AcceptanceRequired=json_data.get("AcceptanceRequired"),
            AllowedPrincipals=json_data.get("AllowedPrincipals"),
            AvailabilityZones=json_data.get("AvailabilityZones"),
            BaseEndpointDnsNames=json_data.get("BaseEndpointDnsNames"),
            Id=json_data.get("Id"),
            ManagesVpcEndpoints=json_data.get("ManagesVpcEndpoints"),
            NetworkLoadBalancerArns=json_data.get("NetworkLoadBalancerArns"),
            PrivateDnsName=json_data.get("PrivateDnsName"),
            ServiceName=json_data.get("ServiceName"),
            ServiceType=json_data.get("ServiceType"),
            State=json_data.get("State"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


