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
    CompartmentId: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    Id: Optional[str]
    IsProtected: Optional[bool]
    Name: Optional[str]
    Nameservers: Optional[Sequence["_NameserversDefinition"]]
    Scope: Optional[str]
    Self: Optional[str]
    Serial: Optional[float]
    State: Optional[str]
    TimeCreated: Optional[str]
    Version: Optional[str]
    ViewId: Optional[str]
    ZoneType: Optional[str]
    ExternalMasters: Optional[Sequence["_ExternalMastersDefinition"]]
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
            CompartmentId=json_data.get("CompartmentId"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            Id=json_data.get("Id"),
            IsProtected=json_data.get("IsProtected"),
            Name=json_data.get("Name"),
            Nameservers=deserialize_list(json_data.get("Nameservers"), NameserversDefinition),
            Scope=json_data.get("Scope"),
            Self=json_data.get("Self"),
            Serial=json_data.get("Serial"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            Version=json_data.get("Version"),
            ViewId=json_data.get("ViewId"),
            ZoneType=json_data.get("ZoneType"),
            ExternalMasters=deserialize_list(json_data.get("ExternalMasters"), ExternalMastersDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefinedTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTagsDefinition = DefinedTagsDefinition


@dataclass
class FreeformTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTagsDefinition = FreeformTagsDefinition


@dataclass
class NameserversDefinition(BaseModel):
    Hostname: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NameserversDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NameserversDefinition"]:
        if not json_data:
            return None
        return cls(
            Hostname=json_data.get("Hostname"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NameserversDefinition = NameserversDefinition


@dataclass
class ExternalMastersDefinition(BaseModel):
    Address: Optional[str]
    Port: Optional[float]
    TsigKeyId: Optional[str]
    Tsig: Optional[Sequence["_TsigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ExternalMastersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExternalMastersDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Port=json_data.get("Port"),
            TsigKeyId=json_data.get("TsigKeyId"),
            Tsig=deserialize_list(json_data.get("Tsig"), TsigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExternalMastersDefinition = ExternalMastersDefinition


@dataclass
class TsigDefinition(BaseModel):
    Algorithm: Optional[str]
    Name: Optional[str]
    Secret: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TsigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TsigDefinition"]:
        if not json_data:
            return None
        return cls(
            Algorithm=json_data.get("Algorithm"),
            Name=json_data.get("Name"),
            Secret=json_data.get("Secret"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TsigDefinition = TsigDefinition


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


