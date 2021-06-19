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
    Constraint: Optional[str]
    Etag: Optional[str]
    Id: Optional[str]
    Project: Optional[str]
    UpdateTime: Optional[str]
    Version: Optional[float]
    BooleanPolicy: Optional[Sequence["_BooleanPolicyDefinition"]]
    ListPolicy: Optional[Sequence["_ListPolicyDefinition"]]
    RestorePolicy: Optional[Sequence["_RestorePolicyDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            Constraint=json_data.get("Constraint"),
            Etag=json_data.get("Etag"),
            Id=json_data.get("Id"),
            Project=json_data.get("Project"),
            UpdateTime=json_data.get("UpdateTime"),
            Version=json_data.get("Version"),
            BooleanPolicy=deserialize_list(json_data.get("BooleanPolicy"), BooleanPolicyDefinition),
            ListPolicy=deserialize_list(json_data.get("ListPolicy"), ListPolicyDefinition),
            RestorePolicy=deserialize_list(json_data.get("RestorePolicy"), RestorePolicyDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BooleanPolicyDefinition(BaseModel):
    Enforced: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_BooleanPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BooleanPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Enforced=json_data.get("Enforced"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BooleanPolicyDefinition = BooleanPolicyDefinition


@dataclass
class ListPolicyDefinition(BaseModel):
    InheritFromParent: Optional[bool]
    SuggestedValue: Optional[str]
    Allow: Optional[Sequence["_AllowDefinition"]]
    Deny: Optional[Sequence["_DenyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ListPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ListPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            InheritFromParent=json_data.get("InheritFromParent"),
            SuggestedValue=json_data.get("SuggestedValue"),
            Allow=deserialize_list(json_data.get("Allow"), AllowDefinition),
            Deny=deserialize_list(json_data.get("Deny"), DenyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ListPolicyDefinition = ListPolicyDefinition


@dataclass
class AllowDefinition(BaseModel):
    All: Optional[bool]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AllowDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AllowDefinition"]:
        if not json_data:
            return None
        return cls(
            All=json_data.get("All"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AllowDefinition = AllowDefinition


@dataclass
class DenyDefinition(BaseModel):
    All: Optional[bool]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_DenyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DenyDefinition"]:
        if not json_data:
            return None
        return cls(
            All=json_data.get("All"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DenyDefinition = DenyDefinition


@dataclass
class RestorePolicyDefinition(BaseModel):
    Default: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_RestorePolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RestorePolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Default=json_data.get("Default"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RestorePolicyDefinition = RestorePolicyDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


