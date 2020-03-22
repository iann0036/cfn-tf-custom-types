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
    CreationTimestamp: Optional[str]
    CustomFeatures: Optional[Sequence[str]]
    Description: Optional[str]
    EnabledFeatures: Optional[Sequence[str]]
    Fingerprint: Optional[str]
    Id: Optional[str]
    MinTlsVersion: Optional[str]
    Name: Optional[str]
    Profile: Optional[str]
    Project: Optional[str]
    SelfLink: Optional[str]
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
            CreationTimestamp=json_data.get("CreationTimestamp"),
            CustomFeatures=json_data.get("CustomFeatures"),
            Description=json_data.get("Description"),
            EnabledFeatures=json_data.get("EnabledFeatures"),
            Fingerprint=json_data.get("Fingerprint"),
            Id=json_data.get("Id"),
            MinTlsVersion=json_data.get("MinTlsVersion"),
            Name=json_data.get("Name"),
            Profile=json_data.get("Profile"),
            Project=json_data.get("Project"),
            SelfLink=json_data.get("SelfLink"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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


