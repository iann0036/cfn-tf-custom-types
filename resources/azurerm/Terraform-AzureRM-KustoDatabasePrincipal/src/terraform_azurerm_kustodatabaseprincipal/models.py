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
    AppId: Optional[str]
    ClientId: Optional[str]
    ClusterName: Optional[str]
    DatabaseName: Optional[str]
    Email: Optional[str]
    FullyQualifiedName: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    ObjectId: Optional[str]
    ResourceGroupName: Optional[str]
    Role: Optional[str]
    Type: Optional[str]
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
            AppId=json_data.get("AppId"),
            ClientId=json_data.get("ClientId"),
            ClusterName=json_data.get("ClusterName"),
            DatabaseName=json_data.get("DatabaseName"),
            Email=json_data.get("Email"),
            FullyQualifiedName=json_data.get("FullyQualifiedName"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ObjectId=json_data.get("ObjectId"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Role=json_data.get("Role"),
            Type=json_data.get("Type"),
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


