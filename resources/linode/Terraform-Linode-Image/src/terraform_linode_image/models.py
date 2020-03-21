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
    Created: Optional[str]
    CreatedBy: Optional[str]
    Deprecated: Optional[bool]
    Description: Optional[str]
    DiskId: Optional[float]
    Expiry: Optional[str]
    Id: Optional[str]
    IsPublic: Optional[bool]
    Label: Optional[str]
    LinodeId: Optional[float]
    Size: Optional[float]
    Type: Optional[str]
    Vendor: Optional[str]
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
            Created=json_data.get("Created"),
            CreatedBy=json_data.get("CreatedBy"),
            Deprecated=json_data.get("Deprecated"),
            Description=json_data.get("Description"),
            DiskId=json_data.get("DiskId"),
            Expiry=json_data.get("Expiry"),
            Id=json_data.get("Id"),
            IsPublic=json_data.get("IsPublic"),
            Label=json_data.get("Label"),
            LinodeId=json_data.get("LinodeId"),
            Size=json_data.get("Size"),
            Type=json_data.get("Type"),
            Vendor=json_data.get("Vendor"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Timeouts:
    Create: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


