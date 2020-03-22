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
    EventhubName: Optional[str]
    Id: Optional[str]
    Listen: Optional[bool]
    Manage: Optional[bool]
    Name: Optional[str]
    NamespaceName: Optional[str]
    PrimaryConnectionString: Optional[str]
    PrimaryKey: Optional[str]
    ResourceGroupName: Optional[str]
    SecondaryConnectionString: Optional[str]
    SecondaryKey: Optional[str]
    Send: Optional[bool]
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
            EventhubName=json_data.get("EventhubName"),
            Id=json_data.get("Id"),
            Listen=json_data.get("Listen"),
            Manage=json_data.get("Manage"),
            Name=json_data.get("Name"),
            NamespaceName=json_data.get("NamespaceName"),
            PrimaryConnectionString=json_data.get("PrimaryConnectionString"),
            PrimaryKey=json_data.get("PrimaryKey"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SecondaryConnectionString=json_data.get("SecondaryConnectionString"),
            SecondaryKey=json_data.get("SecondaryKey"),
            Send=json_data.get("Send"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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


