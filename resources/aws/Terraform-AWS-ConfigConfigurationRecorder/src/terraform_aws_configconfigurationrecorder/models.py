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
    Name: Optional[str]
    RoleArn: Optional[str]
    RecordingGroup: Optional[Sequence["_RecordingGroup"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Name=json_data.get("Name"),
            RoleArn=json_data.get("RoleArn"),
            RecordingGroup=json_data.get("RecordingGroup"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RecordingGroup:
    AllSupported: Optional[bool]
    IncludeGlobalResourceTypes: Optional[bool]
    ResourceTypes: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_RecordingGroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecordingGroup"]:
        if not json_data:
            return None
        return cls(
            AllSupported=json_data.get("AllSupported"),
            IncludeGlobalResourceTypes=json_data.get("IncludeGlobalResourceTypes"),
            ResourceTypes=json_data.get("ResourceTypes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecordingGroup = RecordingGroup


