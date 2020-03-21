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
    Project: Optional[str]
    Size: Optional[float]
    Url: Optional[str]
    PubsubConfigs: Optional[Sequence["_PubsubConfigs"]]
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
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            Size=json_data.get("Size"),
            Url=json_data.get("Url"),
            PubsubConfigs=json_data.get("PubsubConfigs"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PubsubConfigs:
    MessageFormat: Optional[str]
    ServiceAccountEmail: Optional[str]
    Topic: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PubsubConfigs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PubsubConfigs"]:
        if not json_data:
            return None
        return cls(
            MessageFormat=json_data.get("MessageFormat"),
            ServiceAccountEmail=json_data.get("ServiceAccountEmail"),
            Topic=json_data.get("Topic"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PubsubConfigs = PubsubConfigs


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


