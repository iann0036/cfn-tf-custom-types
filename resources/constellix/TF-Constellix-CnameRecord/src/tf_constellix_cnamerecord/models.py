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
    ContactIds: Optional[Sequence[float]]
    DomainId: Optional[str]
    GeoLocation: Optional[Sequence["_GeoLocationDefinition"]]
    GtdRegion: Optional[float]
    Host: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Noanswer: Optional[bool]
    Note: Optional[str]
    Pools: Optional[Sequence[float]]
    RecordFailoverDisableFlag: Optional[str]
    RecordFailoverFailoverType: Optional[str]
    RecordOption: Optional[str]
    SourceType: Optional[str]
    Ttl: Optional[float]
    Type: Optional[str]
    RecordFailoverValues: Optional[Sequence["_RecordFailoverValuesDefinition"]]

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
            ContactIds=json_data.get("ContactIds"),
            DomainId=json_data.get("DomainId"),
            GeoLocation=deserialize_list(json_data.get("GeoLocation"), GeoLocationDefinition),
            GtdRegion=json_data.get("GtdRegion"),
            Host=json_data.get("Host"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Noanswer=json_data.get("Noanswer"),
            Note=json_data.get("Note"),
            Pools=json_data.get("Pools"),
            RecordFailoverDisableFlag=json_data.get("RecordFailoverDisableFlag"),
            RecordFailoverFailoverType=json_data.get("RecordFailoverFailoverType"),
            RecordOption=json_data.get("RecordOption"),
            SourceType=json_data.get("SourceType"),
            Ttl=json_data.get("Ttl"),
            Type=json_data.get("Type"),
            RecordFailoverValues=deserialize_list(json_data.get("RecordFailoverValues"), RecordFailoverValuesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class GeoLocationDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GeoLocationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GeoLocationDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GeoLocationDefinition = GeoLocationDefinition


@dataclass
class RecordFailoverValuesDefinition(BaseModel):
    CheckId: Optional[float]
    DisableFlag: Optional[str]
    SortOrder: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RecordFailoverValuesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecordFailoverValuesDefinition"]:
        if not json_data:
            return None
        return cls(
            CheckId=json_data.get("CheckId"),
            DisableFlag=json_data.get("DisableFlag"),
            SortOrder=json_data.get("SortOrder"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecordFailoverValuesDefinition = RecordFailoverValuesDefinition


