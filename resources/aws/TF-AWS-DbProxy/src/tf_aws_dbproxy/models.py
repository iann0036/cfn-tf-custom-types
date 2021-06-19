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
    Arn: Optional[str]
    DebugLogging: Optional[bool]
    Endpoint: Optional[str]
    EngineFamily: Optional[str]
    Id: Optional[str]
    IdleClientTimeout: Optional[float]
    Name: Optional[str]
    RequireTls: Optional[bool]
    RoleArn: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    VpcSecurityGroupIds: Optional[Sequence[str]]
    VpcSubnetIds: Optional[Sequence[str]]
    Auth: Optional[Sequence["_AuthDefinition"]]
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
            Arn=json_data.get("Arn"),
            DebugLogging=json_data.get("DebugLogging"),
            Endpoint=json_data.get("Endpoint"),
            EngineFamily=json_data.get("EngineFamily"),
            Id=json_data.get("Id"),
            IdleClientTimeout=json_data.get("IdleClientTimeout"),
            Name=json_data.get("Name"),
            RequireTls=json_data.get("RequireTls"),
            RoleArn=json_data.get("RoleArn"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            VpcSecurityGroupIds=json_data.get("VpcSecurityGroupIds"),
            VpcSubnetIds=json_data.get("VpcSubnetIds"),
            Auth=deserialize_list(json_data.get("Auth"), AuthDefinition),
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
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class AuthDefinition(BaseModel):
    AuthScheme: Optional[str]
    Description: Optional[str]
    IamAuth: Optional[str]
    SecretArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthScheme=json_data.get("AuthScheme"),
            Description=json_data.get("Description"),
            IamAuth=json_data.get("IamAuth"),
            SecretArn=json_data.get("SecretArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthDefinition = AuthDefinition


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


