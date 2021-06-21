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
    DescriptionCustomer: Optional[str]
    DescriptionInternal: Optional[str]
    Id: Optional[str]
    LocationId: Optional[str]
    Locations: Optional[Sequence["_LocationsDefinition"]]
    Name: Optional[str]
    RoleText: Optional[str]
    Status: Optional[str]
    VmProvisioning: Optional[bool]
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
            DescriptionCustomer=json_data.get("DescriptionCustomer"),
            DescriptionInternal=json_data.get("DescriptionInternal"),
            Id=json_data.get("Id"),
            LocationId=json_data.get("LocationId"),
            Locations=deserialize_list(json_data.get("Locations"), LocationsDefinition),
            Name=json_data.get("Name"),
            RoleText=json_data.get("RoleText"),
            Status=json_data.get("Status"),
            VmProvisioning=json_data.get("VmProvisioning"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LocationsDefinition(BaseModel):
    CityCode: Optional[str]
    Code: Optional[str]
    Country: Optional[str]
    Identifier: Optional[str]
    Lat: Optional[str]
    Lon: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LocationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LocationsDefinition"]:
        if not json_data:
            return None
        return cls(
            CityCode=json_data.get("CityCode"),
            Code=json_data.get("Code"),
            Country=json_data.get("Country"),
            Identifier=json_data.get("Identifier"),
            Lat=json_data.get("Lat"),
            Lon=json_data.get("Lon"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LocationsDefinition = LocationsDefinition


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

