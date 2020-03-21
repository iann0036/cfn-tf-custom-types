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
    AuthCodes: Optional[Sequence[str]]
    Delicense: Optional[bool]
    Licenses: Optional[Sequence["_Licenses"]]
    Mode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AuthCodes=json_data.get("AuthCodes"),
            Delicense=json_data.get("Delicense"),
            Licenses=json_data.get("Licenses"),
            Mode=json_data.get("Mode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Licenses:
    AuthCode: Optional[str]
    Description: Optional[str]
    Expired: Optional[str]
    Expires: Optional[str]
    Feature: Optional[str]
    Issued: Optional[str]
    Serial: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Licenses"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Licenses"]:
        if not json_data:
            return None
        return cls(
            AuthCode=json_data.get("AuthCode"),
            Description=json_data.get("Description"),
            Expired=json_data.get("Expired"),
            Expires=json_data.get("Expires"),
            Feature=json_data.get("Feature"),
            Issued=json_data.get("Issued"),
            Serial=json_data.get("Serial"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Licenses = Licenses


