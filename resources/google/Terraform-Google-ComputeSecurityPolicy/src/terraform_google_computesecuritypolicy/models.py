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
    Description: Optional[str]
    Fingerprint: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    SelfLink: Optional[str]
    Rule: Optional[Sequence["_Rule"]]
    Timeouts: Optional["_Timeouts"]
    Match: Optional[Sequence["_Match"]]
    Config: Optional[Sequence["_Config"]]
    Expr: Optional[Sequence["_Expr"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Description=json_data.get("Description"),
            Fingerprint=json_data.get("Fingerprint"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            SelfLink=json_data.get("SelfLink"),
            Rule=json_data.get("Rule"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            Match=json_data.get("Match"),
            Config=json_data.get("Config"),
            Expr=json_data.get("Expr"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Rule:
    Action: Optional[str]
    Description: Optional[str]
    Preview: Optional[bool]
    Priority: Optional[float]
    Match: Optional[Sequence["_Match"]]

    @classmethod
    def _deserialize(
        cls: Type["_Rule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Rule"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Description=json_data.get("Description"),
            Preview=json_data.get("Preview"),
            Priority=json_data.get("Priority"),
            Match=json_data.get("Match"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Rule = Rule


@dataclass
class Match:
    VersionedExpr: Optional[str]
    Config: Optional[Sequence["_Config"]]
    Expr: Optional[Sequence["_Expr"]]

    @classmethod
    def _deserialize(
        cls: Type["_Match"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Match"]:
        if not json_data:
            return None
        return cls(
            VersionedExpr=json_data.get("VersionedExpr"),
            Config=json_data.get("Config"),
            Expr=json_data.get("Expr"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Match = Match


@dataclass
class Config:
    SrcIpRanges: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Config"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Config"]:
        if not json_data:
            return None
        return cls(
            SrcIpRanges=json_data.get("SrcIpRanges"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Config = Config


@dataclass
class Expr:
    Expression: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Expr"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Expr"]:
        if not json_data:
            return None
        return cls(
            Expression=json_data.get("Expression"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Expr = Expr


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


