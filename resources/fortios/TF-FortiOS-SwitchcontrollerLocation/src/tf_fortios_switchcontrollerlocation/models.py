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
    Id: Optional[str]
    Name: Optional[str]
    Vdomparam: Optional[str]
    AddressCivic: Optional[Sequence["_AddressCivicDefinition"]]
    Coordinates: Optional[Sequence["_CoordinatesDefinition"]]
    ElinNumber: Optional[Sequence["_ElinNumberDefinition"]]

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
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Vdomparam=json_data.get("Vdomparam"),
            AddressCivic=deserialize_list(json_data.get("AddressCivic"), AddressCivicDefinition),
            Coordinates=deserialize_list(json_data.get("Coordinates"), CoordinatesDefinition),
            ElinNumber=deserialize_list(json_data.get("ElinNumber"), ElinNumberDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AddressCivicDefinition(BaseModel):
    Additional: Optional[str]
    AdditionalCode: Optional[str]
    Block: Optional[str]
    BranchRoad: Optional[str]
    Building: Optional[str]
    City: Optional[str]
    CityDivision: Optional[str]
    Country: Optional[str]
    CountrySubdivision: Optional[str]
    County: Optional[str]
    Direction: Optional[str]
    Floor: Optional[str]
    Landmark: Optional[str]
    Language: Optional[str]
    Name: Optional[str]
    Number: Optional[str]
    NumberSuffix: Optional[str]
    ParentKey: Optional[str]
    PlaceType: Optional[str]
    PostOfficeBox: Optional[str]
    PostalCommunity: Optional[str]
    PrimaryRoad: Optional[str]
    RoadSection: Optional[str]
    Room: Optional[str]
    Script: Optional[str]
    Seat: Optional[str]
    Street: Optional[str]
    StreetNamePostMod: Optional[str]
    StreetNamePreMod: Optional[str]
    StreetSuffix: Optional[str]
    SubBranchRoad: Optional[str]
    TrailingStrSuffix: Optional[str]
    Unit: Optional[str]
    Zip: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AddressCivicDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AddressCivicDefinition"]:
        if not json_data:
            return None
        return cls(
            Additional=json_data.get("Additional"),
            AdditionalCode=json_data.get("AdditionalCode"),
            Block=json_data.get("Block"),
            BranchRoad=json_data.get("BranchRoad"),
            Building=json_data.get("Building"),
            City=json_data.get("City"),
            CityDivision=json_data.get("CityDivision"),
            Country=json_data.get("Country"),
            CountrySubdivision=json_data.get("CountrySubdivision"),
            County=json_data.get("County"),
            Direction=json_data.get("Direction"),
            Floor=json_data.get("Floor"),
            Landmark=json_data.get("Landmark"),
            Language=json_data.get("Language"),
            Name=json_data.get("Name"),
            Number=json_data.get("Number"),
            NumberSuffix=json_data.get("NumberSuffix"),
            ParentKey=json_data.get("ParentKey"),
            PlaceType=json_data.get("PlaceType"),
            PostOfficeBox=json_data.get("PostOfficeBox"),
            PostalCommunity=json_data.get("PostalCommunity"),
            PrimaryRoad=json_data.get("PrimaryRoad"),
            RoadSection=json_data.get("RoadSection"),
            Room=json_data.get("Room"),
            Script=json_data.get("Script"),
            Seat=json_data.get("Seat"),
            Street=json_data.get("Street"),
            StreetNamePostMod=json_data.get("StreetNamePostMod"),
            StreetNamePreMod=json_data.get("StreetNamePreMod"),
            StreetSuffix=json_data.get("StreetSuffix"),
            SubBranchRoad=json_data.get("SubBranchRoad"),
            TrailingStrSuffix=json_data.get("TrailingStrSuffix"),
            Unit=json_data.get("Unit"),
            Zip=json_data.get("Zip"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AddressCivicDefinition = AddressCivicDefinition


@dataclass
class CoordinatesDefinition(BaseModel):
    Altitude: Optional[str]
    AltitudeUnit: Optional[str]
    Datum: Optional[str]
    Latitude: Optional[str]
    Longitude: Optional[str]
    ParentKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CoordinatesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CoordinatesDefinition"]:
        if not json_data:
            return None
        return cls(
            Altitude=json_data.get("Altitude"),
            AltitudeUnit=json_data.get("AltitudeUnit"),
            Datum=json_data.get("Datum"),
            Latitude=json_data.get("Latitude"),
            Longitude=json_data.get("Longitude"),
            ParentKey=json_data.get("ParentKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CoordinatesDefinition = CoordinatesDefinition


@dataclass
class ElinNumberDefinition(BaseModel):
    ElinNum: Optional[str]
    ParentKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ElinNumberDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ElinNumberDefinition"]:
        if not json_data:
            return None
        return cls(
            ElinNum=json_data.get("ElinNum"),
            ParentKey=json_data.get("ParentKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ElinNumberDefinition = ElinNumberDefinition


