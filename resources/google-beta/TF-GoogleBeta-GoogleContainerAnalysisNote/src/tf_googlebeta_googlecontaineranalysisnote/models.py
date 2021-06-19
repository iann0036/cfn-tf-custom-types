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
    CreateTime: Optional[str]
    ExpirationTime: Optional[str]
    Id: Optional[str]
    Kind: Optional[str]
    LongDescription: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    RelatedNoteNames: Optional[Sequence[str]]
    ShortDescription: Optional[str]
    UpdateTime: Optional[str]
    AttestationAuthority: Optional[Sequence["_AttestationAuthorityDefinition"]]
    RelatedUrl: Optional[Sequence["_RelatedUrlDefinition"]]
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
            CreateTime=json_data.get("CreateTime"),
            ExpirationTime=json_data.get("ExpirationTime"),
            Id=json_data.get("Id"),
            Kind=json_data.get("Kind"),
            LongDescription=json_data.get("LongDescription"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            RelatedNoteNames=json_data.get("RelatedNoteNames"),
            ShortDescription=json_data.get("ShortDescription"),
            UpdateTime=json_data.get("UpdateTime"),
            AttestationAuthority=deserialize_list(json_data.get("AttestationAuthority"), AttestationAuthorityDefinition),
            RelatedUrl=deserialize_list(json_data.get("RelatedUrl"), RelatedUrlDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AttestationAuthorityDefinition(BaseModel):
    Hint: Optional[Sequence["_HintDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AttestationAuthorityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttestationAuthorityDefinition"]:
        if not json_data:
            return None
        return cls(
            Hint=deserialize_list(json_data.get("Hint"), HintDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttestationAuthorityDefinition = AttestationAuthorityDefinition


@dataclass
class HintDefinition(BaseModel):
    HumanReadableName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HintDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HintDefinition"]:
        if not json_data:
            return None
        return cls(
            HumanReadableName=json_data.get("HumanReadableName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HintDefinition = HintDefinition


@dataclass
class RelatedUrlDefinition(BaseModel):
    Label: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RelatedUrlDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RelatedUrlDefinition"]:
        if not json_data:
            return None
        return cls(
            Label=json_data.get("Label"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RelatedUrlDefinition = RelatedUrlDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


