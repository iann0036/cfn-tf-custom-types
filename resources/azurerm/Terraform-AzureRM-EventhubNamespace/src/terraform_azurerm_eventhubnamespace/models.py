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
    AutoInflateEnabled: Optional[bool]
    Capacity: Optional[float]
    DefaultPrimaryConnectionString: Optional[str]
    DefaultPrimaryKey: Optional[str]
    DefaultSecondaryConnectionString: Optional[str]
    DefaultSecondaryKey: Optional[str]
    Location: Optional[str]
    MaximumThroughputUnits: Optional[float]
    Name: Optional[str]
    NetworkRulesets: Optional[Sequence["_NetworkRulesets"]]
    ResourceGroupName: Optional[str]
    Sku: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
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
            AutoInflateEnabled=json_data.get("AutoInflateEnabled"),
            Capacity=json_data.get("Capacity"),
            DefaultPrimaryConnectionString=json_data.get("DefaultPrimaryConnectionString"),
            DefaultPrimaryKey=json_data.get("DefaultPrimaryKey"),
            DefaultSecondaryConnectionString=json_data.get("DefaultSecondaryConnectionString"),
            DefaultSecondaryKey=json_data.get("DefaultSecondaryKey"),
            Location=json_data.get("Location"),
            MaximumThroughputUnits=json_data.get("MaximumThroughputUnits"),
            Name=json_data.get("Name"),
            NetworkRulesets=json_data.get("NetworkRulesets"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Sku=json_data.get("Sku"),
            Tags=json_data.get("Tags"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class NetworkRulesets:
    DefaultAction: Optional[str]
    IpRule: Optional[Sequence["_IpRule"]]
    VirtualNetworkRule: Optional[Sequence["_VirtualNetworkRule"]]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkRulesets"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkRulesets"]:
        if not json_data:
            return None
        return cls(
            DefaultAction=json_data.get("DefaultAction"),
            IpRule=json_data.get("IpRule"),
            VirtualNetworkRule=json_data.get("VirtualNetworkRule"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkRulesets = NetworkRulesets


@dataclass
class IpRule:
    Action: Optional[str]
    IpMask: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpRule"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            IpMask=json_data.get("IpMask"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpRule = IpRule


@dataclass
class VirtualNetworkRule:
    IgnoreMissingVirtualNetworkServiceEndpoint: Optional[bool]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualNetworkRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualNetworkRule"]:
        if not json_data:
            return None
        return cls(
            IgnoreMissingVirtualNetworkServiceEndpoint=json_data.get("IgnoreMissingVirtualNetworkServiceEndpoint"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualNetworkRule = VirtualNetworkRule


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


