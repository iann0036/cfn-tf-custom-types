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
    BucketName: Optional[str]
    CreationTimestamp: Optional[str]
    CustomResponseHeaders: Optional[Sequence[str]]
    Description: Optional[str]
    EnableCdn: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    SelfLink: Optional[str]
    CdnPolicy: Optional[Sequence["_CdnPolicyDefinition"]]
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
            BucketName=json_data.get("BucketName"),
            CreationTimestamp=json_data.get("CreationTimestamp"),
            CustomResponseHeaders=json_data.get("CustomResponseHeaders"),
            Description=json_data.get("Description"),
            EnableCdn=json_data.get("EnableCdn"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            SelfLink=json_data.get("SelfLink"),
            CdnPolicy=deserialize_list(json_data.get("CdnPolicy"), CdnPolicyDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CdnPolicyDefinition(BaseModel):
    CacheMode: Optional[str]
    ClientTtl: Optional[float]
    DefaultTtl: Optional[float]
    MaxTtl: Optional[float]
    NegativeCaching: Optional[bool]
    ServeWhileStale: Optional[float]
    SignedUrlCacheMaxAgeSec: Optional[float]
    NegativeCachingPolicy: Optional[Sequence["_NegativeCachingPolicyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CdnPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CdnPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            CacheMode=json_data.get("CacheMode"),
            ClientTtl=json_data.get("ClientTtl"),
            DefaultTtl=json_data.get("DefaultTtl"),
            MaxTtl=json_data.get("MaxTtl"),
            NegativeCaching=json_data.get("NegativeCaching"),
            ServeWhileStale=json_data.get("ServeWhileStale"),
            SignedUrlCacheMaxAgeSec=json_data.get("SignedUrlCacheMaxAgeSec"),
            NegativeCachingPolicy=deserialize_list(json_data.get("NegativeCachingPolicy"), NegativeCachingPolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CdnPolicyDefinition = CdnPolicyDefinition


@dataclass
class NegativeCachingPolicyDefinition(BaseModel):
    Code: Optional[float]
    Ttl: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NegativeCachingPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NegativeCachingPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Code=json_data.get("Code"),
            Ttl=json_data.get("Ttl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NegativeCachingPolicyDefinition = NegativeCachingPolicyDefinition


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


