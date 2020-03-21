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
    Constraint: Optional[str]
    Etag: Optional[str]
    Id: Optional[str]
    Project: Optional[str]
    UpdateTime: Optional[str]
    Version: Optional[float]
    BooleanPolicy: Optional[Sequence["_BooleanPolicy"]]
    ListPolicy: Optional[Sequence["_ListPolicy"]]
    RestorePolicy: Optional[Sequence["_RestorePolicy"]]
    Timeouts: Optional["_Timeouts"]
    Allow: Optional[Sequence["_Allow"]]
    Deny: Optional[Sequence["_Deny"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Constraint=json_data.get("Constraint"),
            Etag=json_data.get("Etag"),
            Id=json_data.get("Id"),
            Project=json_data.get("Project"),
            UpdateTime=json_data.get("UpdateTime"),
            Version=json_data.get("Version"),
            BooleanPolicy=json_data.get("BooleanPolicy"),
            ListPolicy=json_data.get("ListPolicy"),
            RestorePolicy=json_data.get("RestorePolicy"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            Allow=json_data.get("Allow"),
            Deny=json_data.get("Deny"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BooleanPolicy:
    Enforced: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_BooleanPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BooleanPolicy"]:
        if not json_data:
            return None
        return cls(
            Enforced=json_data.get("Enforced"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BooleanPolicy = BooleanPolicy


@dataclass
class ListPolicy:
    InheritFromParent: Optional[bool]
    SuggestedValue: Optional[str]
    Allow: Optional[Sequence["_Allow"]]
    Deny: Optional[Sequence["_Deny"]]

    @classmethod
    def _deserialize(
        cls: Type["_ListPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ListPolicy"]:
        if not json_data:
            return None
        return cls(
            InheritFromParent=json_data.get("InheritFromParent"),
            SuggestedValue=json_data.get("SuggestedValue"),
            Allow=json_data.get("Allow"),
            Deny=json_data.get("Deny"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ListPolicy = ListPolicy


@dataclass
class Allow:
    All: Optional[bool]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Allow"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Allow"]:
        if not json_data:
            return None
        return cls(
            All=json_data.get("All"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Allow = Allow


@dataclass
class Deny:
    All: Optional[bool]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Deny"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Deny"]:
        if not json_data:
            return None
        return cls(
            All=json_data.get("All"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Deny = Deny


@dataclass
class RestorePolicy:
    Default: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_RestorePolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RestorePolicy"]:
        if not json_data:
            return None
        return cls(
            Default=json_data.get("Default"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RestorePolicy = RestorePolicy


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


