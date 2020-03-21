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
    BucketDomainName: Optional[str]
    ForceDestroy: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    Region: Optional[str]
    Urn: Optional[str]
    CorsRule: Optional[Sequence["_CorsRule"]]

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
            BucketDomainName=json_data.get("BucketDomainName"),
            ForceDestroy=json_data.get("ForceDestroy"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Region=json_data.get("Region"),
            Urn=json_data.get("Urn"),
            CorsRule=json_data.get("CorsRule"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CorsRule:
    AllowedHeaders: Optional[Sequence[str]]
    AllowedMethods: Optional[Sequence[str]]
    AllowedOrigins: Optional[Sequence[str]]
    MaxAgeSeconds: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CorsRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CorsRule"]:
        if not json_data:
            return None
        return cls(
            AllowedHeaders=json_data.get("AllowedHeaders"),
            AllowedMethods=json_data.get("AllowedMethods"),
            AllowedOrigins=json_data.get("AllowedOrigins"),
            MaxAgeSeconds=json_data.get("MaxAgeSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CorsRule = CorsRule


