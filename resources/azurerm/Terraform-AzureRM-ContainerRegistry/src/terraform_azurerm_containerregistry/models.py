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
    AdminEnabled: Optional[bool]
    AdminPassword: Optional[str]
    AdminUsername: Optional[str]
    GeoreplicationLocations: Optional[Sequence[str]]
    Location: Optional[str]
    LoginServer: Optional[str]
    Name: Optional[str]
    NetworkRuleSet: Optional[Sequence["_NetworkRuleSet"]]
    ResourceGroupName: Optional[str]
    Sku: Optional[str]
    StorageAccountId: Optional[str]
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
            AdminEnabled=json_data.get("AdminEnabled"),
            AdminPassword=json_data.get("AdminPassword"),
            AdminUsername=json_data.get("AdminUsername"),
            GeoreplicationLocations=json_data.get("GeoreplicationLocations"),
            Location=json_data.get("Location"),
            LoginServer=json_data.get("LoginServer"),
            Name=json_data.get("Name"),
            NetworkRuleSet=json_data.get("NetworkRuleSet"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Sku=json_data.get("Sku"),
            StorageAccountId=json_data.get("StorageAccountId"),
            Tags=json_data.get("Tags"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class NetworkRuleSet:
    DefaultAction: Optional[str]
    IpRule: Optional[Sequence["_IpRule"]]
    VirtualNetwork: Optional[Sequence["_VirtualNetwork"]]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkRuleSet"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkRuleSet"]:
        if not json_data:
            return None
        return cls(
            DefaultAction=json_data.get("DefaultAction"),
            IpRule=json_data.get("IpRule"),
            VirtualNetwork=json_data.get("VirtualNetwork"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkRuleSet = NetworkRuleSet


@dataclass
class IpRule:
    Action: Optional[str]
    IpRange: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpRule"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            IpRange=json_data.get("IpRange"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpRule = IpRule


@dataclass
class VirtualNetwork:
    Action: Optional[str]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualNetwork"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualNetwork"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualNetwork = VirtualNetwork


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


