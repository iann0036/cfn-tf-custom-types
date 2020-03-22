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
    AutoDeleteOnIdle: Optional[str]
    DefaultMessageTtl: Optional[str]
    DuplicateDetectionHistoryTimeWindow: Optional[str]
    EnableBatchedOperations: Optional[bool]
    EnableExpress: Optional[bool]
    EnablePartitioning: Optional[bool]
    Id: Optional[str]
    MaxSizeInMegabytes: Optional[float]
    Name: Optional[str]
    NamespaceName: Optional[str]
    RequiresDuplicateDetection: Optional[bool]
    ResourceGroupName: Optional[str]
    Status: Optional[str]
    SupportOrdering: Optional[bool]
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
            AutoDeleteOnIdle=json_data.get("AutoDeleteOnIdle"),
            DefaultMessageTtl=json_data.get("DefaultMessageTtl"),
            DuplicateDetectionHistoryTimeWindow=json_data.get("DuplicateDetectionHistoryTimeWindow"),
            EnableBatchedOperations=json_data.get("EnableBatchedOperations"),
            EnableExpress=json_data.get("EnableExpress"),
            EnablePartitioning=json_data.get("EnablePartitioning"),
            Id=json_data.get("Id"),
            MaxSizeInMegabytes=json_data.get("MaxSizeInMegabytes"),
            Name=json_data.get("Name"),
            NamespaceName=json_data.get("NamespaceName"),
            RequiresDuplicateDetection=json_data.get("RequiresDuplicateDetection"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Status=json_data.get("Status"),
            SupportOrdering=json_data.get("SupportOrdering"),
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


