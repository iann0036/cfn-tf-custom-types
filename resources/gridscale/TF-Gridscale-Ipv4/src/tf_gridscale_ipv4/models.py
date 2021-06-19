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
    ChangeTime: Optional[str]
    CreateTime: Optional[str]
    CurrentPrice: Optional[float]
    DeleteBlock: Optional[bool]
    Failover: Optional[bool]
    Id: Optional[str]
    Ip: Optional[str]
    Labels: Optional[Sequence[str]]
    LocationCountry: Optional[str]
    LocationIata: Optional[str]
    LocationName: Optional[str]
    LocationUuid: Optional[str]
    Name: Optional[str]
    Prefix: Optional[str]
    ReverseDns: Optional[str]
    Status: Optional[str]
    UsageInMinutes: Optional[float]
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
            ChangeTime=json_data.get("ChangeTime"),
            CreateTime=json_data.get("CreateTime"),
            CurrentPrice=json_data.get("CurrentPrice"),
            DeleteBlock=json_data.get("DeleteBlock"),
            Failover=json_data.get("Failover"),
            Id=json_data.get("Id"),
            Ip=json_data.get("Ip"),
            Labels=json_data.get("Labels"),
            LocationCountry=json_data.get("LocationCountry"),
            LocationIata=json_data.get("LocationIata"),
            LocationName=json_data.get("LocationName"),
            LocationUuid=json_data.get("LocationUuid"),
            Name=json_data.get("Name"),
            Prefix=json_data.get("Prefix"),
            ReverseDns=json_data.get("ReverseDns"),
            Status=json_data.get("Status"),
            UsageInMinutes=json_data.get("UsageInMinutes"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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


