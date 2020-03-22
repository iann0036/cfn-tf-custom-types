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
    Arn: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    RegexMatchTuple: Optional[Sequence["_RegexMatchTuple"]]
    FieldToMatch: Optional[Sequence["_FieldToMatch"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            RegexMatchTuple=json_data.get("RegexMatchTuple"),
            FieldToMatch=json_data.get("FieldToMatch"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RegexMatchTuple:
    RegexPatternSetId: Optional[str]
    TextTransformation: Optional[str]
    FieldToMatch: Optional[Sequence["_FieldToMatch"]]

    @classmethod
    def _deserialize(
        cls: Type["_RegexMatchTuple"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RegexMatchTuple"]:
        if not json_data:
            return None
        return cls(
            RegexPatternSetId=json_data.get("RegexPatternSetId"),
            TextTransformation=json_data.get("TextTransformation"),
            FieldToMatch=json_data.get("FieldToMatch"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RegexMatchTuple = RegexMatchTuple


@dataclass
class FieldToMatch:
    Data: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FieldToMatch"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FieldToMatch"]:
        if not json_data:
            return None
        return cls(
            Data=json_data.get("Data"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FieldToMatch = FieldToMatch


