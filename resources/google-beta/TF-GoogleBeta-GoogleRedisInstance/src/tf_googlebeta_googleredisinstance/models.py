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
    AlternativeLocationId: Optional[str]
    AuthEnabled: Optional[bool]
    AuthString: Optional[str]
    AuthorizedNetwork: Optional[str]
    ConnectMode: Optional[str]
    CreateTime: Optional[str]
    CurrentLocationId: Optional[str]
    DisplayName: Optional[str]
    Host: Optional[str]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    LocationId: Optional[str]
    MemorySizeGb: Optional[float]
    Name: Optional[str]
    PersistenceIamIdentity: Optional[str]
    Port: Optional[float]
    Project: Optional[str]
    RedisConfigs: Optional[Sequence["_RedisConfigsDefinition"]]
    RedisVersion: Optional[str]
    Region: Optional[str]
    ReservedIpRange: Optional[str]
    ServerCaCerts: Optional[Sequence["_ServerCaCertsDefinition"]]
    Tier: Optional[str]
    TransitEncryptionMode: Optional[str]
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
            AlternativeLocationId=json_data.get("AlternativeLocationId"),
            AuthEnabled=json_data.get("AuthEnabled"),
            AuthString=json_data.get("AuthString"),
            AuthorizedNetwork=json_data.get("AuthorizedNetwork"),
            ConnectMode=json_data.get("ConnectMode"),
            CreateTime=json_data.get("CreateTime"),
            CurrentLocationId=json_data.get("CurrentLocationId"),
            DisplayName=json_data.get("DisplayName"),
            Host=json_data.get("Host"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            LocationId=json_data.get("LocationId"),
            MemorySizeGb=json_data.get("MemorySizeGb"),
            Name=json_data.get("Name"),
            PersistenceIamIdentity=json_data.get("PersistenceIamIdentity"),
            Port=json_data.get("Port"),
            Project=json_data.get("Project"),
            RedisConfigs=deserialize_list(json_data.get("RedisConfigs"), RedisConfigsDefinition),
            RedisVersion=json_data.get("RedisVersion"),
            Region=json_data.get("Region"),
            ReservedIpRange=json_data.get("ReservedIpRange"),
            ServerCaCerts=deserialize_list(json_data.get("ServerCaCerts"), ServerCaCertsDefinition),
            Tier=json_data.get("Tier"),
            TransitEncryptionMode=json_data.get("TransitEncryptionMode"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class RedisConfigsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RedisConfigsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedisConfigsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedisConfigsDefinition = RedisConfigsDefinition


@dataclass
class ServerCaCertsDefinition(BaseModel):
    Cert: Optional[str]
    CreateTime: Optional[str]
    ExpireTime: Optional[str]
    SerialNumber: Optional[str]
    Sha1Fingerprint: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerCaCertsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerCaCertsDefinition"]:
        if not json_data:
            return None
        return cls(
            Cert=json_data.get("Cert"),
            CreateTime=json_data.get("CreateTime"),
            ExpireTime=json_data.get("ExpireTime"),
            SerialNumber=json_data.get("SerialNumber"),
            Sha1Fingerprint=json_data.get("Sha1Fingerprint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerCaCertsDefinition = ServerCaCertsDefinition


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


