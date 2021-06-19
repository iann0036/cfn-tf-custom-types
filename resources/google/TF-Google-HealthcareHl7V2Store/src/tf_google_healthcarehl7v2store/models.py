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
    Dataset: Optional[str]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Name: Optional[str]
    SelfLink: Optional[str]
    NotificationConfig: Optional[Sequence["_NotificationConfigDefinition"]]
    NotificationConfigs: Optional[Sequence["_NotificationConfigsDefinition"]]
    ParserConfig: Optional[Sequence["_ParserConfigDefinition"]]
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
            Dataset=json_data.get("Dataset"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Name=json_data.get("Name"),
            SelfLink=json_data.get("SelfLink"),
            NotificationConfig=deserialize_list(json_data.get("NotificationConfig"), NotificationConfigDefinition),
            NotificationConfigs=deserialize_list(json_data.get("NotificationConfigs"), NotificationConfigsDefinition),
            ParserConfig=deserialize_list(json_data.get("ParserConfig"), ParserConfigDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class NotificationConfigDefinition(BaseModel):
    PubsubTopic: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NotificationConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotificationConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            PubsubTopic=json_data.get("PubsubTopic"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotificationConfigDefinition = NotificationConfigDefinition


@dataclass
class NotificationConfigsDefinition(BaseModel):
    Filter: Optional[str]
    PubsubTopic: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NotificationConfigsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotificationConfigsDefinition"]:
        if not json_data:
            return None
        return cls(
            Filter=json_data.get("Filter"),
            PubsubTopic=json_data.get("PubsubTopic"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotificationConfigsDefinition = NotificationConfigsDefinition


@dataclass
class ParserConfigDefinition(BaseModel):
    AllowNullHeader: Optional[bool]
    Schema: Optional[str]
    SegmentTerminator: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParserConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParserConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowNullHeader=json_data.get("AllowNullHeader"),
            Schema=json_data.get("Schema"),
            SegmentTerminator=json_data.get("SegmentTerminator"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParserConfigDefinition = ParserConfigDefinition


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


