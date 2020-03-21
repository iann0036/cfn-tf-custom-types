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
    AdminUsers: Optional[Sequence[str]]
    BackupBlobContainerUri: Optional[str]
    EnablePowerBiService: Optional[bool]
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    QuerypoolConnectionMode: Optional[str]
    ResourceGroupName: Optional[str]
    ServerFullName: Optional[str]
    Sku: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Ipv4FirewallRule: Optional[Sequence["_Ipv4FirewallRule"]]
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
            AdminUsers=json_data.get("AdminUsers"),
            BackupBlobContainerUri=json_data.get("BackupBlobContainerUri"),
            EnablePowerBiService=json_data.get("EnablePowerBiService"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            QuerypoolConnectionMode=json_data.get("QuerypoolConnectionMode"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            ServerFullName=json_data.get("ServerFullName"),
            Sku=json_data.get("Sku"),
            Tags=json_data.get("Tags"),
            Ipv4FirewallRule=json_data.get("Ipv4FirewallRule"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class Ipv4FirewallRule:
    Name: Optional[str]
    RangeEnd: Optional[str]
    RangeStart: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ipv4FirewallRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ipv4FirewallRule"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            RangeEnd=json_data.get("RangeEnd"),
            RangeStart=json_data.get("RangeStart"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ipv4FirewallRule = Ipv4FirewallRule


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


