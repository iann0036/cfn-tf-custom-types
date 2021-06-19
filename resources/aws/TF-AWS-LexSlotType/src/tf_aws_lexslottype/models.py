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
    Checksum: Optional[str]
    CreateVersion: Optional[bool]
    CreatedDate: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    LastUpdatedDate: Optional[str]
    Name: Optional[str]
    ValueSelectionStrategy: Optional[str]
    Version: Optional[str]
    EnumerationValue: Optional[Sequence["_EnumerationValueDefinition"]]
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
            Checksum=json_data.get("Checksum"),
            CreateVersion=json_data.get("CreateVersion"),
            CreatedDate=json_data.get("CreatedDate"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            LastUpdatedDate=json_data.get("LastUpdatedDate"),
            Name=json_data.get("Name"),
            ValueSelectionStrategy=json_data.get("ValueSelectionStrategy"),
            Version=json_data.get("Version"),
            EnumerationValue=deserialize_list(json_data.get("EnumerationValue"), EnumerationValueDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EnumerationValueDefinition(BaseModel):
    Synonyms: Optional[Sequence[str]]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EnumerationValueDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnumerationValueDefinition"]:
        if not json_data:
            return None
        return cls(
            Synonyms=json_data.get("Synonyms"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnumerationValueDefinition = EnumerationValueDefinition


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


