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
    Id: Optional[str]
    Name: Optional[str]
    Tag: Optional[float]
    Interfaces: Optional[Sequence["_Interfaces"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Tag=json_data.get("Tag"),
            Interfaces=json_data.get("Interfaces"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Interfaces:
    Tagged: Optional[bool]
    Vlanport: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Interfaces"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Interfaces"]:
        if not json_data:
            return None
        return cls(
            Tagged=json_data.get("Tagged"),
            Vlanport=json_data.get("Vlanport"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Interfaces = Interfaces


