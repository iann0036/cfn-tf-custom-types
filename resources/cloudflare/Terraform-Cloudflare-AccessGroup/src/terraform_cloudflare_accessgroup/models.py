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
    AccountId: Optional[str]
    Name: Optional[str]
    Exclude: Optional[Sequence["_Exclude"]]
    Include: Optional[Sequence["_Include"]]
    Require: Optional[Sequence["_Require"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AccountId=json_data.get("AccountId"),
            Name=json_data.get("Name"),
            Exclude=json_data.get("Exclude"),
            Include=json_data.get("Include"),
            Require=json_data.get("Require"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Exclude:
    Email: Optional[Sequence[str]]
    EmailDomain: Optional[Sequence[str]]
    Everyone: Optional[bool]
    Group: Optional[Sequence[str]]
    Ip: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Exclude"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Exclude"]:
        if not json_data:
            return None
        return cls(
            Email=json_data.get("Email"),
            EmailDomain=json_data.get("EmailDomain"),
            Everyone=json_data.get("Everyone"),
            Group=json_data.get("Group"),
            Ip=json_data.get("Ip"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Exclude = Exclude


@dataclass
class Include:
    Email: Optional[Sequence[str]]
    EmailDomain: Optional[Sequence[str]]
    Everyone: Optional[bool]
    Group: Optional[Sequence[str]]
    Ip: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Include"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Include"]:
        if not json_data:
            return None
        return cls(
            Email=json_data.get("Email"),
            EmailDomain=json_data.get("EmailDomain"),
            Everyone=json_data.get("Everyone"),
            Group=json_data.get("Group"),
            Ip=json_data.get("Ip"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Include = Include


@dataclass
class Require:
    Email: Optional[Sequence[str]]
    EmailDomain: Optional[Sequence[str]]
    Everyone: Optional[bool]
    Group: Optional[Sequence[str]]
    Ip: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Require"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Require"]:
        if not json_data:
            return None
        return cls(
            Email=json_data.get("Email"),
            EmailDomain=json_data.get("EmailDomain"),
            Everyone=json_data.get("Everyone"),
            Group=json_data.get("Group"),
            Ip=json_data.get("Ip"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Require = Require


