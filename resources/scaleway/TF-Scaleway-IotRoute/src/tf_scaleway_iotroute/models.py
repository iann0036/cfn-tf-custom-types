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
    CreatedAt: Optional[str]
    HubId: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Region: Optional[str]
    Topic: Optional[str]
    Database: Optional[Sequence["_DatabaseDefinition"]]
    Rest: Optional[Sequence["_RestDefinition"]]
    S3: Optional[Sequence["_S3Definition"]]

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
            CreatedAt=json_data.get("CreatedAt"),
            HubId=json_data.get("HubId"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Region=json_data.get("Region"),
            Topic=json_data.get("Topic"),
            Database=deserialize_list(json_data.get("Database"), DatabaseDefinition),
            Rest=deserialize_list(json_data.get("Rest"), RestDefinition),
            S3=deserialize_list(json_data.get("S3"), S3Definition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DatabaseDefinition(BaseModel):
    Dbname: Optional[str]
    Host: Optional[str]
    Password: Optional[str]
    Port: Optional[float]
    Query: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DatabaseDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatabaseDefinition"]:
        if not json_data:
            return None
        return cls(
            Dbname=json_data.get("Dbname"),
            Host=json_data.get("Host"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            Query=json_data.get("Query"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatabaseDefinition = DatabaseDefinition


@dataclass
class RestDefinition(BaseModel):
    Headers: Optional[Sequence["_HeadersDefinition"]]
    Uri: Optional[str]
    Verb: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RestDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RestDefinition"]:
        if not json_data:
            return None
        return cls(
            Headers=deserialize_list(json_data.get("Headers"), HeadersDefinition),
            Uri=json_data.get("Uri"),
            Verb=json_data.get("Verb"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RestDefinition = RestDefinition


@dataclass
class HeadersDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeadersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeadersDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeadersDefinition = HeadersDefinition


@dataclass
class S3Definition(BaseModel):
    BucketName: Optional[str]
    BucketRegion: Optional[str]
    ObjectPrefix: Optional[str]
    Strategy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Definition"]:
        if not json_data:
            return None
        return cls(
            BucketName=json_data.get("BucketName"),
            BucketRegion=json_data.get("BucketRegion"),
            ObjectPrefix=json_data.get("ObjectPrefix"),
            Strategy=json_data.get("Strategy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Definition = S3Definition


