# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    AllowBareDomains: Optional[bool]
    AllowHostCertificates: Optional[bool]
    AllowSubdomains: Optional[bool]
    AllowUserCertificates: Optional[bool]
    AllowUserKeyIds: Optional[bool]
    AllowedCriticalOptions: Optional[str]
    AllowedDomains: Optional[str]
    AllowedExtensions: Optional[str]
    AllowedUserKeyLengths: Optional[Sequence["_AllowedUserKeyLengths"]]
    AllowedUsers: Optional[str]
    Backend: Optional[str]
    CidrList: Optional[str]
    DefaultCriticalOptions: Optional[Sequence["_DefaultCriticalOptions"]]
    DefaultExtensions: Optional[Sequence["_DefaultExtensions"]]
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
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AllowBareDomains=json_data.get("AllowBareDomains"),
            AllowHostCertificates=json_data.get("AllowHostCertificates"),
            AllowSubdomains=json_data.get("AllowSubdomains"),
            AllowUserCertificates=json_data.get("AllowUserCertificates"),
            AllowUserKeyIds=json_data.get("AllowUserKeyIds"),
            AllowedCriticalOptions=json_data.get("AllowedCriticalOptions"),
            AllowedDomains=json_data.get("AllowedDomains"),
            AllowedExtensions=json_data.get("AllowedExtensions"),
            AllowedUserKeyLengths=json_data.get("AllowedUserKeyLengths"),
            AllowedUsers=json_data.get("AllowedUsers"),
            Backend=json_data.get("Backend"),
            CidrList=json_data.get("CidrList"),
            DefaultCriticalOptions=json_data.get("DefaultCriticalOptions"),
            DefaultExtensions=json_data.get("DefaultExtensions"),
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
class AllowedUserKeyLengths:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AllowedUserKeyLengths"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AllowedUserKeyLengths"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AllowedUserKeyLengths = AllowedUserKeyLengths


@dataclass
class DefaultCriticalOptions:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultCriticalOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultCriticalOptions"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultCriticalOptions = DefaultCriticalOptions


@dataclass
class DefaultExtensions:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultExtensions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultExtensions"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultExtensions = DefaultExtensions


