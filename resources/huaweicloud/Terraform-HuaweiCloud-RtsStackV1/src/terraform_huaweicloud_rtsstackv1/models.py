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
    Capabilities: Optional[Sequence[str]]
    DisableRollback: Optional[bool]
    Environment: Optional[str]
    Files: Optional[Sequence["_Files"]]
    Id: Optional[str]
    Name: Optional[str]
    NotificationTopics: Optional[Sequence[str]]
    Outputs: Optional[Sequence["_Outputs"]]
    Parameters: Optional[Sequence["_Parameters"]]
    Region: Optional[str]
    Status: Optional[str]
    StatusReason: Optional[str]
    TemplateBody: Optional[str]
    TemplateUrl: Optional[str]
    TimeoutMins: Optional[float]
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
            Capabilities=json_data.get("Capabilities"),
            DisableRollback=json_data.get("DisableRollback"),
            Environment=json_data.get("Environment"),
            Files=json_data.get("Files"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            NotificationTopics=json_data.get("NotificationTopics"),
            Outputs=json_data.get("Outputs"),
            Parameters=json_data.get("Parameters"),
            Region=json_data.get("Region"),
            Status=json_data.get("Status"),
            StatusReason=json_data.get("StatusReason"),
            TemplateBody=json_data.get("TemplateBody"),
            TemplateUrl=json_data.get("TemplateUrl"),
            TimeoutMins=json_data.get("TimeoutMins"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Files:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Files"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Files"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Files = Files


@dataclass
class Outputs:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Outputs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Outputs"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Outputs = Outputs


@dataclass
class Parameters:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Parameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Parameters"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Parameters = Parameters


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


