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
    FailTimeout: Optional[float]
    HealthCheckPath: Optional[str]
    Hostname: Optional[str]
    Id: Optional[str]
    IgnoreInvalidBackendTls: Optional[bool]
    MaxConns: Optional[float]
    MaxRequestSize: Optional[float]
    Policy: Optional[str]
    Port: Optional[float]
    Protocol: Optional[str]
    TlsCertificate: Optional[str]
    TlsKey: Optional[str]
    Backend: Optional[Sequence["_BackendDefinition"]]

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
            FailTimeout=json_data.get("FailTimeout"),
            HealthCheckPath=json_data.get("HealthCheckPath"),
            Hostname=json_data.get("Hostname"),
            Id=json_data.get("Id"),
            IgnoreInvalidBackendTls=json_data.get("IgnoreInvalidBackendTls"),
            MaxConns=json_data.get("MaxConns"),
            MaxRequestSize=json_data.get("MaxRequestSize"),
            Policy=json_data.get("Policy"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            TlsCertificate=json_data.get("TlsCertificate"),
            TlsKey=json_data.get("TlsKey"),
            Backend=deserialize_list(json_data.get("Backend"), BackendDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BackendDefinition(BaseModel):
    InstanceId: Optional[str]
    Port: Optional[float]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BackendDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackendDefinition"]:
        if not json_data:
            return None
        return cls(
            InstanceId=json_data.get("InstanceId"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackendDefinition = BackendDefinition


