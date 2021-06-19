# DO NOT modify this file by hand, changes will be overwritten
import sys
from dataclasses import dataclass
from inspect import getmembers, isclass
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
    BaseModel,
    BaseResourceHandlerRequest,
)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

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
class ResourceModel(BaseModel):
    tfcfnid: Optional[str]
    Description: Optional[str]
    DisplayName: Optional[str]
    Id: Optional[str]
    NsxId: Optional[str]
    Path: Optional[str]
    Revision: Optional[float]
    Severities: Optional[Sequence[str]]
    Criteria: Optional[Sequence["_CriteriaDefinition"]]
    OverriddenSignature: Optional[Sequence["_OverriddenSignatureDefinition"]]
    Tag: Optional[Sequence["_TagDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            NsxId=json_data.get("NsxId"),
            Path=json_data.get("Path"),
            Revision=json_data.get("Revision"),
            Severities=json_data.get("Severities"),
            Criteria=deserialize_list(json_data.get("Criteria"), CriteriaDefinition),
            OverriddenSignature=deserialize_list(json_data.get("OverriddenSignature"), OverriddenSignatureDefinition),
            Tag=deserialize_list(json_data.get("Tag"), TagDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CriteriaDefinition(BaseModel):
    AttackTargets: Optional[Sequence[str]]
    AttackTypes: Optional[Sequence[str]]
    Cvss: Optional[Sequence[str]]
    ProductsAffected: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_CriteriaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CriteriaDefinition"]:
        if not json_data:
            return None
        return cls(
            AttackTargets=json_data.get("AttackTargets"),
            AttackTypes=json_data.get("AttackTypes"),
            Cvss=json_data.get("Cvss"),
            ProductsAffected=json_data.get("ProductsAffected"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CriteriaDefinition = CriteriaDefinition


@dataclass
class OverriddenSignatureDefinition(BaseModel):
    Action: Optional[str]
    Enabled: Optional[bool]
    SignatureId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OverriddenSignatureDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OverriddenSignatureDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Enabled=json_data.get("Enabled"),
            SignatureId=json_data.get("SignatureId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OverriddenSignatureDefinition = OverriddenSignatureDefinition


@dataclass
class TagDefinition(BaseModel):
    Scope: Optional[str]
    Tag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagDefinition"]:
        if not json_data:
            return None
        return cls(
            Scope=json_data.get("Scope"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagDefinition = TagDefinition


