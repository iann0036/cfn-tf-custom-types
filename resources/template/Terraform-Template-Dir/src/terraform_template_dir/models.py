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
    DestinationDir: Optional[str]
    Id: Optional[str]
    SourceDir: Optional[str]
    Vars: Optional[Sequence["_Vars"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DestinationDir=json_data.get("DestinationDir"),
            Id=json_data.get("Id"),
            SourceDir=json_data.get("SourceDir"),
            Vars=json_data.get("Vars"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Vars:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Vars"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Vars"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Vars = Vars


