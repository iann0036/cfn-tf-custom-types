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
    BufferSize: Optional[float]
    CertificatePem: Optional[str]
    CertificatePrivateKey: Optional[str]
    Id: Optional[str]
    Locked: Optional[bool]
    Name: Optional[str]
    Nodes: Optional[Sequence[str]]
    Policy: Optional[str]
    Sslv3: Optional[bool]
    Status: Optional[str]
    Healthcheck: Optional[Sequence["_Healthcheck"]]
    Listener: Optional[Sequence["_Listener"]]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            BufferSize=json_data.get("BufferSize"),
            CertificatePem=json_data.get("CertificatePem"),
            CertificatePrivateKey=json_data.get("CertificatePrivateKey"),
            Id=json_data.get("Id"),
            Locked=json_data.get("Locked"),
            Name=json_data.get("Name"),
            Nodes=json_data.get("Nodes"),
            Policy=json_data.get("Policy"),
            Sslv3=json_data.get("Sslv3"),
            Status=json_data.get("Status"),
            Healthcheck=json_data.get("Healthcheck"),
            Listener=json_data.get("Listener"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Healthcheck:
    Interval: Optional[float]
    Port: Optional[float]
    Request: Optional[str]
    ThresholdDown: Optional[float]
    ThresholdUp: Optional[float]
    Timeout: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Healthcheck"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Healthcheck"]:
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
_Healthcheck = Healthcheck


@dataclass
class Listener:
    In: Optional[float]
    Out: Optional[float]
    Protocol: Optional[str]
    Timeout: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Listener"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Listener"]:
        if not json_data:
            return None
        return cls(
            In=json_data.get("In"),
            Out=json_data.get("Out"),
            Protocol=json_data.get("Protocol"),
            Timeout=json_data.get("Timeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Listener = Listener


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


