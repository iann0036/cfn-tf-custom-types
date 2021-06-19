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
    AlgorithmSigner: Optional[str]
    AllowBareDomains: Optional[bool]
    AllowHostCertificates: Optional[bool]
    AllowSubdomains: Optional[bool]
    AllowUserCertificates: Optional[bool]
    AllowUserKeyIds: Optional[bool]
    AllowedCriticalOptions: Optional[str]
    AllowedDomains: Optional[str]
    AllowedExtensions: Optional[str]
    AllowedUserKeyLengths: Optional[Sequence["_AllowedUserKeyLengthsDefinition"]]
    AllowedUsers: Optional[str]
    AllowedUsersTemplate: Optional[bool]
    Backend: Optional[str]
    CidrList: Optional[str]
    DefaultCriticalOptions: Optional[Sequence["_DefaultCriticalOptionsDefinition"]]
    DefaultExtensions: Optional[Sequence["_DefaultExtensionsDefinition"]]
    DefaultUser: Optional[str]
    Id: Optional[str]
    KeyIdFormat: Optional[str]
    KeyType: Optional[str]
    MaxTtl: Optional[str]
    Name: Optional[str]
    Ttl: Optional[str]

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
            AlgorithmSigner=json_data.get("AlgorithmSigner"),
            AllowBareDomains=json_data.get("AllowBareDomains"),
            AllowHostCertificates=json_data.get("AllowHostCertificates"),
            AllowSubdomains=json_data.get("AllowSubdomains"),
            AllowUserCertificates=json_data.get("AllowUserCertificates"),
            AllowUserKeyIds=json_data.get("AllowUserKeyIds"),
            AllowedCriticalOptions=json_data.get("AllowedCriticalOptions"),
            AllowedDomains=json_data.get("AllowedDomains"),
            AllowedExtensions=json_data.get("AllowedExtensions"),
            AllowedUserKeyLengths=deserialize_list(json_data.get("AllowedUserKeyLengths"), AllowedUserKeyLengthsDefinition),
            AllowedUsers=json_data.get("AllowedUsers"),
            AllowedUsersTemplate=json_data.get("AllowedUsersTemplate"),
            Backend=json_data.get("Backend"),
            CidrList=json_data.get("CidrList"),
            DefaultCriticalOptions=deserialize_list(json_data.get("DefaultCriticalOptions"), DefaultCriticalOptionsDefinition),
            DefaultExtensions=deserialize_list(json_data.get("DefaultExtensions"), DefaultExtensionsDefinition),
            DefaultUser=json_data.get("DefaultUser"),
            Id=json_data.get("Id"),
            KeyIdFormat=json_data.get("KeyIdFormat"),
            KeyType=json_data.get("KeyType"),
            MaxTtl=json_data.get("MaxTtl"),
            Name=json_data.get("Name"),
            Ttl=json_data.get("Ttl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AllowedUserKeyLengthsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AllowedUserKeyLengthsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AllowedUserKeyLengthsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AllowedUserKeyLengthsDefinition = AllowedUserKeyLengthsDefinition


@dataclass
class DefaultCriticalOptionsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultCriticalOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultCriticalOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultCriticalOptionsDefinition = DefaultCriticalOptionsDefinition


@dataclass
class DefaultExtensionsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultExtensionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultExtensionsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultExtensionsDefinition = DefaultExtensionsDefinition


