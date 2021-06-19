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
    Id: Optional[str]
    Name: Optional[str]
    OutboundTraffic: Optional[bool]
    Routable: Optional[bool]
    ShutdownAtTime: Optional[str]
    ShutdownOnIdle: Optional[float]
    SuspendAtTime: Optional[str]
    SuspendOnIdle: Optional[float]
    Tags: Optional[Sequence[str]]
    TemplateId: Optional[str]
    UserData: Optional[str]
    Label: Optional[Sequence["_LabelDefinition"]]
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
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            OutboundTraffic=json_data.get("OutboundTraffic"),
            Routable=json_data.get("Routable"),
            ShutdownAtTime=json_data.get("ShutdownAtTime"),
            ShutdownOnIdle=json_data.get("ShutdownOnIdle"),
            SuspendAtTime=json_data.get("SuspendAtTime"),
            SuspendOnIdle=json_data.get("SuspendOnIdle"),
            Tags=json_data.get("Tags"),
            TemplateId=json_data.get("TemplateId"),
            UserData=json_data.get("UserData"),
            Label=deserialize_list(json_data.get("Label"), LabelDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LabelDefinition(BaseModel):
    Category: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelDefinition"]:
        if not json_data:
            return None
        return cls(
            Category=json_data.get("Category"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelDefinition = LabelDefinition


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


