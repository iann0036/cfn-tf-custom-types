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
    BalancerVips: Optional[Sequence[str]]
    CanonicalHostName: Optional[str]
    CloudgateCapable: Optional[bool]
    Description: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    IpNetwork: Optional[str]
    Name: Optional[str]
    ParentLoadBalancer: Optional[str]
    PermittedClients: Optional[Sequence[str]]
    PermittedMethods: Optional[Sequence[str]]
    Policies: Optional[Sequence[str]]
    Region: Optional[str]
    Scheme: Optional[str]
    ServerPool: Optional[str]
    Tags: Optional[Sequence[str]]
    Uri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            BalancerVips=json_data.get("BalancerVips"),
            CanonicalHostName=json_data.get("CanonicalHostName"),
            CloudgateCapable=json_data.get("CloudgateCapable"),
            Description=json_data.get("Description"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            IpNetwork=json_data.get("IpNetwork"),
            Name=json_data.get("Name"),
            ParentLoadBalancer=json_data.get("ParentLoadBalancer"),
            PermittedClients=json_data.get("PermittedClients"),
            PermittedMethods=json_data.get("PermittedMethods"),
            Policies=json_data.get("Policies"),
            Region=json_data.get("Region"),
            Scheme=json_data.get("Scheme"),
            ServerPool=json_data.get("ServerPool"),
            Tags=json_data.get("Tags"),
            Uri=json_data.get("Uri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


