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
    Acl: Optional[str]
    Bucket: Optional[str]
    Id: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    CorsRules: Optional[Sequence["_CorsRules"]]
    LifecycleRules: Optional[Sequence["_LifecycleRules"]]
    Website: Optional[Sequence["_Website"]]
    Expiration: Optional[Sequence["_Expiration"]]
    Transition: Optional[Sequence["_Transition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Acl=json_data.get("Acl"),
            Bucket=json_data.get("Bucket"),
            Id=json_data.get("Id"),
            Tags=json_data.get("Tags"),
            CorsRules=json_data.get("CorsRules"),
            LifecycleRules=json_data.get("LifecycleRules"),
            Website=json_data.get("Website"),
            Expiration=json_data.get("Expiration"),
            Transition=json_data.get("Transition"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class CorsRules:
    AllowedHeaders: Optional[Sequence[str]]
    AllowedMethods: Optional[Sequence[str]]
    AllowedOrigins: Optional[Sequence[str]]
    ExposeHeaders: Optional[Sequence[str]]
    MaxAgeSeconds: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CorsRules"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CorsRules"]:
        if not json_data:
            return None
        return cls(
            AllowedHeaders=json_data.get("AllowedHeaders"),
            AllowedMethods=json_data.get("AllowedMethods"),
            AllowedOrigins=json_data.get("AllowedOrigins"),
            ExposeHeaders=json_data.get("ExposeHeaders"),
            MaxAgeSeconds=json_data.get("MaxAgeSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CorsRules = CorsRules


@dataclass
class LifecycleRules:
    FilterPrefix: Optional[str]
    Expiration: Optional[Sequence["_Expiration"]]
    Transition: Optional[Sequence["_Transition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LifecycleRules"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LifecycleRules"]:
        if not json_data:
            return None
        return cls(
            FilterPrefix=json_data.get("FilterPrefix"),
            Expiration=json_data.get("Expiration"),
            Transition=json_data.get("Transition"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LifecycleRules = LifecycleRules


@dataclass
class Expiration:
    Date: Optional[str]
    Days: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Expiration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Expiration"]:
        if not json_data:
            return None
        return cls(
            Date=json_data.get("Date"),
            Days=json_data.get("Days"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Expiration = Expiration


@dataclass
class Transition:
    Date: Optional[str]
    Days: Optional[float]
    StorageClass: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Transition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Transition"]:
        if not json_data:
            return None
        return cls(
            Date=json_data.get("Date"),
            Days=json_data.get("Days"),
            StorageClass=json_data.get("StorageClass"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Transition = Transition


@dataclass
class Website:
    ErrorDocument: Optional[str]
    IndexDocument: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Website"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Website"]:
        if not json_data:
            return None
        return cls(
            ErrorDocument=json_data.get("ErrorDocument"),
            IndexDocument=json_data.get("IndexDocument"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Website = Website


