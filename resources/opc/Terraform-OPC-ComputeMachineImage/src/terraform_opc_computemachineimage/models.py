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
    Account: Optional[str]
    Attributes: Optional[str]
    Description: Optional[str]
    ErrorReason: Optional[str]
    File: Optional[str]
    Hypervisor: Optional[Sequence["_Hypervisor"]]
    ImageFormat: Optional[str]
    Name: Optional[str]
    NoUpload: Optional[bool]
    Platform: Optional[str]
    State: Optional[str]
    Uri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Account=json_data.get("Account"),
            Attributes=json_data.get("Attributes"),
            Description=json_data.get("Description"),
            ErrorReason=json_data.get("ErrorReason"),
            File=json_data.get("File"),
            Hypervisor=json_data.get("Hypervisor"),
            ImageFormat=json_data.get("ImageFormat"),
            Name=json_data.get("Name"),
            NoUpload=json_data.get("NoUpload"),
            Platform=json_data.get("Platform"),
            State=json_data.get("State"),
            Uri=json_data.get("Uri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Hypervisor:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Hypervisor"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Hypervisor"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Hypervisor = Hypervisor


