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
    Algorithm: Optional[str]
    Id: Optional[str]
    Labels: Optional[Sequence[str]]
    ListenIpv4Uuid: Optional[str]
    ListenIpv6Uuid: Optional[str]
    LocationUuid: Optional[str]
    Name: Optional[str]
    RedirectHttpToHttps: Optional[bool]
    Status: Optional[str]
    BackendServer: Optional[Sequence["_BackendServerDefinition"]]
    ForwardingRule: Optional[Sequence["_ForwardingRuleDefinition"]]
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
            Algorithm=json_data.get("Algorithm"),
            Id=json_data.get("Id"),
            Labels=json_data.get("Labels"),
            ListenIpv4Uuid=json_data.get("ListenIpv4Uuid"),
            ListenIpv6Uuid=json_data.get("ListenIpv6Uuid"),
            LocationUuid=json_data.get("LocationUuid"),
            Name=json_data.get("Name"),
            RedirectHttpToHttps=json_data.get("RedirectHttpToHttps"),
            Status=json_data.get("Status"),
            BackendServer=deserialize_list(json_data.get("BackendServer"), BackendServerDefinition),
            ForwardingRule=deserialize_list(json_data.get("ForwardingRule"), ForwardingRuleDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BackendServerDefinition(BaseModel):
    Host: Optional[str]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_BackendServerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackendServerDefinition"]:
        if not json_data:
            return None
        return cls(
            Host=json_data.get("Host"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackendServerDefinition = BackendServerDefinition


@dataclass
class ForwardingRuleDefinition(BaseModel):
    CertificateUuid: Optional[str]
    LetsencryptSsl: Optional[str]
    ListenPort: Optional[float]
    Mode: Optional[str]
    TargetPort: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ForwardingRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ForwardingRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateUuid=json_data.get("CertificateUuid"),
            LetsencryptSsl=json_data.get("LetsencryptSsl"),
            ListenPort=json_data.get("ListenPort"),
            Mode=json_data.get("Mode"),
            TargetPort=json_data.get("TargetPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ForwardingRuleDefinition = ForwardingRuleDefinition


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


