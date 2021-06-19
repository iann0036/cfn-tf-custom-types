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
    AllowedLocations: Optional[Sequence["_AllowedLocationsDefinition"]]
    AuthenticationMethod: Optional[str]
    Color: Optional[str]
    Comments: Optional[str]
    ConnectDaily: Optional[bool]
    ConnectOnDays: Optional[Sequence[str]]
    Encryption: Optional[Sequence["_EncryptionDefinition"]]
    ExpirationByGlobalProperties: Optional[bool]
    ExpirationDate: Optional[str]
    FromHour: Optional[str]
    Id: Optional[str]
    IgnoreErrors: Optional[bool]
    IgnoreWarnings: Optional[bool]
    Name: Optional[str]
    RadiusServer: Optional[str]
    TacacsServer: Optional[str]
    Tags: Optional[Sequence[str]]
    ToHour: Optional[str]

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
            AllowedLocations=deserialize_list(json_data.get("AllowedLocations"), AllowedLocationsDefinition),
            AuthenticationMethod=json_data.get("AuthenticationMethod"),
            Color=json_data.get("Color"),
            Comments=json_data.get("Comments"),
            ConnectDaily=json_data.get("ConnectDaily"),
            ConnectOnDays=json_data.get("ConnectOnDays"),
            Encryption=deserialize_list(json_data.get("Encryption"), EncryptionDefinition),
            ExpirationByGlobalProperties=json_data.get("ExpirationByGlobalProperties"),
            ExpirationDate=json_data.get("ExpirationDate"),
            FromHour=json_data.get("FromHour"),
            Id=json_data.get("Id"),
            IgnoreErrors=json_data.get("IgnoreErrors"),
            IgnoreWarnings=json_data.get("IgnoreWarnings"),
            Name=json_data.get("Name"),
            RadiusServer=json_data.get("RadiusServer"),
            TacacsServer=json_data.get("TacacsServer"),
            Tags=json_data.get("Tags"),
            ToHour=json_data.get("ToHour"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AllowedLocationsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AllowedLocationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AllowedLocationsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AllowedLocationsDefinition = AllowedLocationsDefinition


@dataclass
class EncryptionDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionDefinition = EncryptionDefinition


