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
    AcceptedCiphers: Optional[str]
    CipherEnums: Optional[Sequence[str]]
    Ciphersuites: Optional[str]
    Description: Optional[str]
    Dhparam: Optional[str]
    EnableEarlyData: Optional[bool]
    EnableSslSessionReuse: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    PreferClientCipherOrdering: Optional[bool]
    SendCloseNotify: Optional[bool]
    SslSessionTimeout: Optional[float]
    TenantRef: Optional[str]
    Type: Optional[str]
    Uuid: Optional[str]
    AcceptedVersions: Optional[Sequence["_AcceptedVersionsDefinition"]]
    Markers: Optional[Sequence["_MarkersDefinition"]]
    SslRating: Optional[Sequence["_SslRatingDefinition"]]
    Tags: Optional[Sequence["_TagsDefinition"]]

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
            AcceptedCiphers=json_data.get("AcceptedCiphers"),
            CipherEnums=json_data.get("CipherEnums"),
            Ciphersuites=json_data.get("Ciphersuites"),
            Description=json_data.get("Description"),
            Dhparam=json_data.get("Dhparam"),
            EnableEarlyData=json_data.get("EnableEarlyData"),
            EnableSslSessionReuse=json_data.get("EnableSslSessionReuse"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PreferClientCipherOrdering=json_data.get("PreferClientCipherOrdering"),
            SendCloseNotify=json_data.get("SendCloseNotify"),
            SslSessionTimeout=json_data.get("SslSessionTimeout"),
            TenantRef=json_data.get("TenantRef"),
            Type=json_data.get("Type"),
            Uuid=json_data.get("Uuid"),
            AcceptedVersions=deserialize_list(json_data.get("AcceptedVersions"), AcceptedVersionsDefinition),
            Markers=deserialize_list(json_data.get("Markers"), MarkersDefinition),
            SslRating=deserialize_list(json_data.get("SslRating"), SslRatingDefinition),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AcceptedVersionsDefinition(BaseModel):
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AcceptedVersionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AcceptedVersionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AcceptedVersionsDefinition = AcceptedVersionsDefinition


@dataclass
class MarkersDefinition(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MarkersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MarkersDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MarkersDefinition = MarkersDefinition


@dataclass
class SslRatingDefinition(BaseModel):
    CompatibilityRating: Optional[str]
    PerformanceRating: Optional[str]
    SecurityScore: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SslRatingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SslRatingDefinition"]:
        if not json_data:
            return None
        return cls(
            CompatibilityRating=json_data.get("CompatibilityRating"),
            PerformanceRating=json_data.get("PerformanceRating"),
            SecurityScore=json_data.get("SecurityScore"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SslRatingDefinition = SslRatingDefinition


@dataclass
class TagsDefinition(BaseModel):
    Type: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


