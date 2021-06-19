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
    BufferSize: Optional[float]
    CertificatePem: Optional[str]
    CertificatePrivateKey: Optional[str]
    Domains: Optional[Sequence[str]]
    HttpsRedirect: Optional[bool]
    Id: Optional[str]
    Locked: Optional[bool]
    Name: Optional[str]
    Nodes: Optional[Sequence[str]]
    Policy: Optional[str]
    SslMinimumVersion: Optional[str]
    Sslv3: Optional[bool]
    Status: Optional[str]
    Healthcheck: Optional[Sequence["_HealthcheckDefinition"]]
    Listener: Optional[Sequence["_ListenerDefinition"]]
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
            BufferSize=json_data.get("BufferSize"),
            CertificatePem=json_data.get("CertificatePem"),
            CertificatePrivateKey=json_data.get("CertificatePrivateKey"),
            Domains=json_data.get("Domains"),
            HttpsRedirect=json_data.get("HttpsRedirect"),
            Id=json_data.get("Id"),
            Locked=json_data.get("Locked"),
            Name=json_data.get("Name"),
            Nodes=json_data.get("Nodes"),
            Policy=json_data.get("Policy"),
            SslMinimumVersion=json_data.get("SslMinimumVersion"),
            Sslv3=json_data.get("Sslv3"),
            Status=json_data.get("Status"),
            Healthcheck=deserialize_list(json_data.get("Healthcheck"), HealthcheckDefinition),
            Listener=deserialize_list(json_data.get("Listener"), ListenerDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class HealthcheckDefinition(BaseModel):
    Interval: Optional[float]
    Port: Optional[float]
    Request: Optional[str]
    ThresholdDown: Optional[float]
    ThresholdUp: Optional[float]
    Timeout: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HealthcheckDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthcheckDefinition"]:
        if not json_data:
            return None
        return cls(
            Interval=json_data.get("Interval"),
            Port=json_data.get("Port"),
            Request=json_data.get("Request"),
            ThresholdDown=json_data.get("ThresholdDown"),
            ThresholdUp=json_data.get("ThresholdUp"),
            Timeout=json_data.get("Timeout"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthcheckDefinition = HealthcheckDefinition


@dataclass
class ListenerDefinition(BaseModel):
    In: Optional[float]
    Out: Optional[float]
    Protocol: Optional[str]
    ProxyProtocol: Optional[str]
    Timeout: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ListenerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ListenerDefinition"]:
        if not json_data:
            return None
        return cls(
            In=json_data.get("In"),
            Out=json_data.get("Out"),
            Protocol=json_data.get("Protocol"),
            ProxyProtocol=json_data.get("ProxyProtocol"),
            Timeout=json_data.get("Timeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ListenerDefinition = ListenerDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


