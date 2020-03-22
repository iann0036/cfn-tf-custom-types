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
    AutoUpgradeMinorVersion: Optional[bool]
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    ProtectedSettings: Optional[str]
    Publisher: Optional[str]
    ResourceGroupName: Optional[str]
    Settings: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Type: Optional[str]
    TypeHandlerVersion: Optional[str]
    VirtualMachineName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AutoUpgradeMinorVersion=json_data.get("AutoUpgradeMinorVersion"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            ProtectedSettings=json_data.get("ProtectedSettings"),
            Publisher=json_data.get("Publisher"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Settings=json_data.get("Settings"),
            Tags=json_data.get("Tags"),
            Type=json_data.get("Type"),
            TypeHandlerVersion=json_data.get("TypeHandlerVersion"),
            VirtualMachineName=json_data.get("VirtualMachineName"),
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


