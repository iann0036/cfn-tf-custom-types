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
    AccessPolicyObjectIds: Optional[Sequence[str]]
    CosmosdbKeyVaultKeyVersionlessId: Optional[str]
    CosmosdbThroughput: Optional[float]
    Id: Optional[str]
    Kind: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    PublicNetworkAccessEnabled: Optional[bool]
    ResourceGroupName: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    AuthenticationConfiguration: Optional[Sequence["_AuthenticationConfigurationDefinition"]]
    CorsConfiguration: Optional[Sequence["_CorsConfigurationDefinition"]]
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
            AccessPolicyObjectIds=json_data.get("AccessPolicyObjectIds"),
            CosmosdbKeyVaultKeyVersionlessId=json_data.get("CosmosdbKeyVaultKeyVersionlessId"),
            CosmosdbThroughput=json_data.get("CosmosdbThroughput"),
            Id=json_data.get("Id"),
            Kind=json_data.get("Kind"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            PublicNetworkAccessEnabled=json_data.get("PublicNetworkAccessEnabled"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            AuthenticationConfiguration=deserialize_list(json_data.get("AuthenticationConfiguration"), AuthenticationConfigurationDefinition),
            CorsConfiguration=deserialize_list(json_data.get("CorsConfiguration"), CorsConfigurationDefinition),
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
class AuthenticationConfigurationDefinition(BaseModel):
    Audience: Optional[str]
    Authority: Optional[str]
    SmartProxyEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AuthenticationConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthenticationConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            Audience=json_data.get("Audience"),
            Authority=json_data.get("Authority"),
            SmartProxyEnabled=json_data.get("SmartProxyEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthenticationConfigurationDefinition = AuthenticationConfigurationDefinition


@dataclass
class CorsConfigurationDefinition(BaseModel):
    AllowCredentials: Optional[bool]
    AllowedHeaders: Optional[Sequence[str]]
    AllowedMethods: Optional[Sequence[str]]
    AllowedOrigins: Optional[Sequence[str]]
    MaxAgeInSeconds: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CorsConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CorsConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowCredentials=json_data.get("AllowCredentials"),
            AllowedHeaders=json_data.get("AllowedHeaders"),
            AllowedMethods=json_data.get("AllowedMethods"),
            AllowedOrigins=json_data.get("AllowedOrigins"),
            MaxAgeInSeconds=json_data.get("MaxAgeInSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CorsConfigurationDefinition = CorsConfigurationDefinition


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


