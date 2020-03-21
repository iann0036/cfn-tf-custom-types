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
    Keepers: Optional[Sequence["_Keepers"]]
    Length: Optional[float]
    Lower: Optional[bool]
    MinLower: Optional[float]
    MinNumeric: Optional[float]
    MinSpecial: Optional[float]
    MinUpper: Optional[float]
    Number: Optional[bool]
    OverrideSpecial: Optional[str]
    Result: Optional[str]
    Special: Optional[bool]
    Upper: Optional[bool]

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
            Keepers=json_data.get("Keepers"),
            Length=json_data.get("Length"),
            Lower=json_data.get("Lower"),
            MinLower=json_data.get("MinLower"),
            MinNumeric=json_data.get("MinNumeric"),
            MinSpecial=json_data.get("MinSpecial"),
            MinUpper=json_data.get("MinUpper"),
            Number=json_data.get("Number"),
            OverrideSpecial=json_data.get("OverrideSpecial"),
            Result=json_data.get("Result"),
            Special=json_data.get("Special"),
            Upper=json_data.get("Upper"),
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


