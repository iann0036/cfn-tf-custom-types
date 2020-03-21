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
    XssMatchTuple: Optional[Sequence["_XssMatchTuple"]]
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
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            XssMatchTuple=json_data.get("XssMatchTuple"),
            FieldToMatch=json_data.get("FieldToMatch"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class XssMatchTuple:
    TextTransformation: Optional[str]
    FieldToMatch: Optional[Sequence["_FieldToMatch"]]

    @classmethod
    def _deserialize(
        cls: Type["_XssMatchTuple"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_XssMatchTuple"]:
        if not json_data:
            return None
        return cls(
            TextTransformation=json_data.get("TextTransformation"),
            FieldToMatch=json_data.get("FieldToMatch"),
        )


# work around possible type aliasing issues when variable has same name as a model
_XssMatchTuple = XssMatchTuple


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


