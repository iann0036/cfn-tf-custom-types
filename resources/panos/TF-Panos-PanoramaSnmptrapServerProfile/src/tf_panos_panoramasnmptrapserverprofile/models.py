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
    AuthPasswordEnc: Optional[Sequence["_AuthPasswordEncDefinition"]]
    AuthPasswordRaw: Optional[Sequence["_AuthPasswordRawDefinition"]]
    DeviceGroup: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    PrivPasswordEnc: Optional[Sequence["_PrivPasswordEncDefinition"]]
    PrivPasswordRaw: Optional[Sequence["_PrivPasswordRawDefinition"]]
    Template: Optional[str]
    TemplateStack: Optional[str]
    Vsys: Optional[str]
    V2cServer: Optional[Sequence["_V2cServerDefinition"]]
    V3Server: Optional[Sequence["_V3ServerDefinition"]]

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
            AuthPasswordEnc=deserialize_list(json_data.get("AuthPasswordEnc"), AuthPasswordEncDefinition),
            AuthPasswordRaw=deserialize_list(json_data.get("AuthPasswordRaw"), AuthPasswordRawDefinition),
            DeviceGroup=json_data.get("DeviceGroup"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PrivPasswordEnc=deserialize_list(json_data.get("PrivPasswordEnc"), PrivPasswordEncDefinition),
            PrivPasswordRaw=deserialize_list(json_data.get("PrivPasswordRaw"), PrivPasswordRawDefinition),
            Template=json_data.get("Template"),
            TemplateStack=json_data.get("TemplateStack"),
            Vsys=json_data.get("Vsys"),
            V2cServer=deserialize_list(json_data.get("V2cServer"), V2cServerDefinition),
            V3Server=deserialize_list(json_data.get("V3Server"), V3ServerDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AuthPasswordEncDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthPasswordEncDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthPasswordEncDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthPasswordEncDefinition = AuthPasswordEncDefinition


@dataclass
class AuthPasswordRawDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthPasswordRawDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthPasswordRawDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthPasswordRawDefinition = AuthPasswordRawDefinition


@dataclass
class PrivPasswordEncDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PrivPasswordEncDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivPasswordEncDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivPasswordEncDefinition = PrivPasswordEncDefinition


@dataclass
class PrivPasswordRawDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PrivPasswordRawDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivPasswordRawDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivPasswordRawDefinition = PrivPasswordRawDefinition


@dataclass
class V2cServerDefinition(BaseModel):
    Community: Optional[str]
    Manager: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_V2cServerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_V2cServerDefinition"]:
        if not json_data:
            return None
        return cls(
            Community=json_data.get("Community"),
            Manager=json_data.get("Manager"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_V2cServerDefinition = V2cServerDefinition


@dataclass
class V3ServerDefinition(BaseModel):
    AuthPassword: Optional[str]
    EngineId: Optional[str]
    Manager: Optional[str]
    Name: Optional[str]
    PrivPassword: Optional[str]
    User: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_V3ServerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_V3ServerDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthPassword=json_data.get("AuthPassword"),
            EngineId=json_data.get("EngineId"),
            Manager=json_data.get("Manager"),
            Name=json_data.get("Name"),
            PrivPassword=json_data.get("PrivPassword"),
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_V3ServerDefinition = V3ServerDefinition


