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
    Channel: Optional[str]
    CreatedOrUpdatedBy: Optional[str]
    CreatedOrUpdatedTime: Optional[str]
    Enabled: Optional[bool]
    HecToken: Optional[str]
    Host: Optional[str]
    Id: Optional[str]
    IntgGuid: Optional[str]
    Name: Optional[str]
    OrgLevel: Optional[bool]
    Port: Optional[float]
    Ssl: Optional[bool]
    TypeName: Optional[str]
    EventData: Optional[Sequence["_EventDataDefinition"]]

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
            Channel=json_data.get("Channel"),
            CreatedOrUpdatedBy=json_data.get("CreatedOrUpdatedBy"),
            CreatedOrUpdatedTime=json_data.get("CreatedOrUpdatedTime"),
            Enabled=json_data.get("Enabled"),
            HecToken=json_data.get("HecToken"),
            Host=json_data.get("Host"),
            Id=json_data.get("Id"),
            IntgGuid=json_data.get("IntgGuid"),
            Name=json_data.get("Name"),
            OrgLevel=json_data.get("OrgLevel"),
            Port=json_data.get("Port"),
            Ssl=json_data.get("Ssl"),
            TypeName=json_data.get("TypeName"),
            EventData=deserialize_list(json_data.get("EventData"), EventDataDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EventDataDefinition(BaseModel):
    Index: Optional[str]
    Source: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EventDataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EventDataDefinition"]:
        if not json_data:
            return None
        return cls(
            Index=json_data.get("Index"),
            Source=json_data.get("Source"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EventDataDefinition = EventDataDefinition


