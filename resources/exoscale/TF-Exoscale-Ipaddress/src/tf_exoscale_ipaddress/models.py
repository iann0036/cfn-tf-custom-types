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
    HealthcheckInterval: Optional[float]
    HealthcheckMode: Optional[str]
    HealthcheckPath: Optional[str]
    HealthcheckPort: Optional[float]
    HealthcheckStrikesFail: Optional[float]
    HealthcheckStrikesOk: Optional[float]
    HealthcheckTimeout: Optional[float]
    HealthcheckTlsSkipVerify: Optional[bool]
    HealthcheckTlsSni: Optional[str]
    Id: Optional[str]
    IpAddress: Optional[str]
    ReverseDns: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Zone: Optional[str]
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
            HealthcheckInterval=json_data.get("HealthcheckInterval"),
            HealthcheckMode=json_data.get("HealthcheckMode"),
            HealthcheckPath=json_data.get("HealthcheckPath"),
            HealthcheckPort=json_data.get("HealthcheckPort"),
            HealthcheckStrikesFail=json_data.get("HealthcheckStrikesFail"),
            HealthcheckStrikesOk=json_data.get("HealthcheckStrikesOk"),
            HealthcheckTimeout=json_data.get("HealthcheckTimeout"),
            HealthcheckTlsSkipVerify=json_data.get("HealthcheckTlsSkipVerify"),
            HealthcheckTlsSni=json_data.get("HealthcheckTlsSni"),
            Id=json_data.get("Id"),
            IpAddress=json_data.get("IpAddress"),
            ReverseDns=json_data.get("ReverseDns"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Zone=json_data.get("Zone"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


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


