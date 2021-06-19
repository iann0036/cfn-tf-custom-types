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
    CertificateCaId: Optional[str]
    CertificateId: Optional[str]
    CertificateSslMode: Optional[str]
    ClbId: Optional[str]
    HealthCheckContextType: Optional[str]
    HealthCheckHealthNum: Optional[float]
    HealthCheckHttpCode: Optional[float]
    HealthCheckHttpDomain: Optional[str]
    HealthCheckHttpMethod: Optional[str]
    HealthCheckHttpPath: Optional[str]
    HealthCheckHttpVersion: Optional[str]
    HealthCheckIntervalTime: Optional[float]
    HealthCheckPort: Optional[float]
    HealthCheckRecvContext: Optional[str]
    HealthCheckSendContext: Optional[str]
    HealthCheckSwitch: Optional[bool]
    HealthCheckTimeOut: Optional[float]
    HealthCheckType: Optional[str]
    HealthCheckUnhealthNum: Optional[float]
    Id: Optional[str]
    ListenerId: Optional[str]
    ListenerName: Optional[str]
    Port: Optional[float]
    Protocol: Optional[str]
    Scheduler: Optional[str]
    SessionExpireTime: Optional[float]
    SniSwitch: Optional[bool]
    TargetType: Optional[str]

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
            CertificateCaId=json_data.get("CertificateCaId"),
            CertificateId=json_data.get("CertificateId"),
            CertificateSslMode=json_data.get("CertificateSslMode"),
            ClbId=json_data.get("ClbId"),
            HealthCheckContextType=json_data.get("HealthCheckContextType"),
            HealthCheckHealthNum=json_data.get("HealthCheckHealthNum"),
            HealthCheckHttpCode=json_data.get("HealthCheckHttpCode"),
            HealthCheckHttpDomain=json_data.get("HealthCheckHttpDomain"),
            HealthCheckHttpMethod=json_data.get("HealthCheckHttpMethod"),
            HealthCheckHttpPath=json_data.get("HealthCheckHttpPath"),
            HealthCheckHttpVersion=json_data.get("HealthCheckHttpVersion"),
            HealthCheckIntervalTime=json_data.get("HealthCheckIntervalTime"),
            HealthCheckPort=json_data.get("HealthCheckPort"),
            HealthCheckRecvContext=json_data.get("HealthCheckRecvContext"),
            HealthCheckSendContext=json_data.get("HealthCheckSendContext"),
            HealthCheckSwitch=json_data.get("HealthCheckSwitch"),
            HealthCheckTimeOut=json_data.get("HealthCheckTimeOut"),
            HealthCheckType=json_data.get("HealthCheckType"),
            HealthCheckUnhealthNum=json_data.get("HealthCheckUnhealthNum"),
            Id=json_data.get("Id"),
            ListenerId=json_data.get("ListenerId"),
            ListenerName=json_data.get("ListenerName"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            Scheduler=json_data.get("Scheduler"),
            SessionExpireTime=json_data.get("SessionExpireTime"),
            SniSwitch=json_data.get("SniSwitch"),
            TargetType=json_data.get("TargetType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


