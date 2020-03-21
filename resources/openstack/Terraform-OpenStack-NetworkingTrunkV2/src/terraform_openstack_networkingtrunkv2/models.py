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
    AdminStateUp: Optional[bool]
    AllTags: Optional[Sequence[str]]
    Description: Optional[str]
    Name: Optional[str]
    PortId: Optional[str]
    Region: Optional[str]
    Tags: Optional[Sequence[str]]
    TenantId: Optional[str]
    SubPort: Optional[Sequence["_SubPort"]]
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
            AdminStateUp=json_data.get("AdminStateUp"),
            AllTags=json_data.get("AllTags"),
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            PortId=json_data.get("PortId"),
            Region=json_data.get("Region"),
            Tags=json_data.get("Tags"),
            TenantId=json_data.get("TenantId"),
            SubPort=json_data.get("SubPort"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SubPort:
    PortId: Optional[str]
    SegmentationId: Optional[float]
    SegmentationType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SubPort"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubPort"]:
        if not json_data:
            return None
        return cls(
            PortId=json_data.get("PortId"),
            SegmentationId=json_data.get("SegmentationId"),
            SegmentationType=json_data.get("SegmentationType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubPort = SubPort


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


