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
    B64: Optional[str]
    B64Std: Optional[str]
    B64Url: Optional[str]
    ByteLength: Optional[float]
    Dec: Optional[str]
    Hex: Optional[str]
    Id: Optional[str]
    Keepers: Optional[Sequence["_Keepers"]]
    Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            B64=json_data.get("B64"),
            B64Std=json_data.get("B64Std"),
            B64Url=json_data.get("B64Url"),
            ByteLength=json_data.get("ByteLength"),
            Dec=json_data.get("Dec"),
            Hex=json_data.get("Hex"),
            Id=json_data.get("Id"),
            Keepers=json_data.get("Keepers"),
            Prefix=json_data.get("Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Keepers:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Keepers"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Keepers"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Keepers = Keepers


