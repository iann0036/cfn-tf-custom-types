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
    AcceptReloadReq: Optional[float]
    Age: Optional[float]
    DefaultPolicyNocache: Optional[float]
    DisableInsertAge: Optional[float]
    DisableInsertVia: Optional[float]
    Id: Optional[str]
    Logging: Optional[str]
    MaxCacheSize: Optional[float]
    MaxContentSize: Optional[float]
    MinContentSize: Optional[float]
    Name: Optional[str]
    RemoveCookies: Optional[float]
    ReplacementPolicy: Optional[str]
    UserTag: Optional[str]
    Uuid: Optional[str]
    VerifyHost: Optional[float]
    LocalUriPolicy: Optional[Sequence["_LocalUriPolicyDefinition"]]
    SamplingEnable: Optional[Sequence["_SamplingEnableDefinition"]]
    UriPolicy: Optional[Sequence["_UriPolicyDefinition"]]

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
            AcceptReloadReq=json_data.get("AcceptReloadReq"),
            Age=json_data.get("Age"),
            DefaultPolicyNocache=json_data.get("DefaultPolicyNocache"),
            DisableInsertAge=json_data.get("DisableInsertAge"),
            DisableInsertVia=json_data.get("DisableInsertVia"),
            Id=json_data.get("Id"),
            Logging=json_data.get("Logging"),
            MaxCacheSize=json_data.get("MaxCacheSize"),
            MaxContentSize=json_data.get("MaxContentSize"),
            MinContentSize=json_data.get("MinContentSize"),
            Name=json_data.get("Name"),
            RemoveCookies=json_data.get("RemoveCookies"),
            ReplacementPolicy=json_data.get("ReplacementPolicy"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
            VerifyHost=json_data.get("VerifyHost"),
            LocalUriPolicy=deserialize_list(json_data.get("LocalUriPolicy"), LocalUriPolicyDefinition),
            SamplingEnable=deserialize_list(json_data.get("SamplingEnable"), SamplingEnableDefinition),
            UriPolicy=deserialize_list(json_data.get("UriPolicy"), UriPolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LocalUriPolicyDefinition(BaseModel):
    LocalUri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LocalUriPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LocalUriPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            LocalUri=json_data.get("LocalUri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LocalUriPolicyDefinition = LocalUriPolicyDefinition


@dataclass
class SamplingEnableDefinition(BaseModel):
    Counters1: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SamplingEnableDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SamplingEnableDefinition"]:
        if not json_data:
            return None
        return cls(
            Counters1=json_data.get("Counters1"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SamplingEnableDefinition = SamplingEnableDefinition


@dataclass
class UriPolicyDefinition(BaseModel):
    CacheAction: Optional[str]
    CacheValue: Optional[float]
    Invalidate: Optional[str]
    Uri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UriPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UriPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            CacheAction=json_data.get("CacheAction"),
            CacheValue=json_data.get("CacheValue"),
            Invalidate=json_data.get("Invalidate"),
            Uri=json_data.get("Uri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UriPolicyDefinition = UriPolicyDefinition


