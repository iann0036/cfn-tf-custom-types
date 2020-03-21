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
    AutomationAccountName: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    ModuleLink: Optional[Sequence["_ModuleLink"]]
    Timeouts: Optional["_Timeouts"]
    Hash: Optional[Sequence["_Hash"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AutomationAccountName=json_data.get("AutomationAccountName"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            ModuleLink=json_data.get("ModuleLink"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            Hash=json_data.get("Hash"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ModuleLink:
    Uri: Optional[str]
    Hash: Optional[Sequence["_Hash"]]

    @classmethod
    def _deserialize(
        cls: Type["_ModuleLink"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ModuleLink"]:
        if not json_data:
            return None
        return cls(
            Uri=json_data.get("Uri"),
            Hash=json_data.get("Hash"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ModuleLink = ModuleLink


@dataclass
class Hash:
    Algorithm: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Hash"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Hash"]:
        if not json_data:
            return None
        return cls(
            Algorithm=json_data.get("Algorithm"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Hash = Hash


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


