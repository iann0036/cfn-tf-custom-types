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
    Aws: Optional[Sequence["_AwsDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    VaultTls: Optional[Sequence["_VaultTlsDefinition"]]
    VaultToken: Optional[Sequence["_VaultTokenDefinition"]]

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
            Aws=deserialize_list(json_data.get("Aws"), AwsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            VaultTls=deserialize_list(json_data.get("VaultTls"), VaultTlsDefinition),
            VaultToken=deserialize_list(json_data.get("VaultToken"), VaultTokenDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AwsDefinition(BaseModel):
    Name: Optional[str]
    Region: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Region=json_data.get("Region"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsDefinition = AwsDefinition


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
    Default: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Default=json_data.get("Default"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


@dataclass
class VaultTlsDefinition(BaseModel):
    CaCertPath: Optional[str]
    ClientCertPath: Optional[str]
    ClientKeyPath: Optional[str]
    Name: Optional[str]
    ServerAddress: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition2"]]

    @classmethod
    def _deserialize(
        cls: Type["_VaultTlsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VaultTlsDefinition"]:
        if not json_data:
            return None
        return cls(
            CaCertPath=json_data.get("CaCertPath"),
            ClientCertPath=json_data.get("ClientCertPath"),
            ClientKeyPath=json_data.get("ClientKeyPath"),
            Name=json_data.get("Name"),
            ServerAddress=json_data.get("ServerAddress"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition2),
        )


# work around possible type aliasing issues when variable has same name as a model
_VaultTlsDefinition = VaultTlsDefinition


@dataclass
class TagsDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition2 = TagsDefinition2


@dataclass
class VaultTokenDefinition(BaseModel):
    Name: Optional[str]
    ServerAddress: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition3"]]

    @classmethod
    def _deserialize(
        cls: Type["_VaultTokenDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VaultTokenDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            ServerAddress=json_data.get("ServerAddress"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition3),
        )


# work around possible type aliasing issues when variable has same name as a model
_VaultTokenDefinition = VaultTokenDefinition


@dataclass
class TagsDefinition3(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition3"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition3 = TagsDefinition3


