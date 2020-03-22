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
    CertificateCaId: Optional[str]
    CertificateId: Optional[str]
    CertificateSslMode: Optional[str]
    ClbId: Optional[str]
    HealthCheckHealthNum: Optional[float]
    HealthCheckIntervalTime: Optional[float]
    HealthCheckSwitch: Optional[bool]
    HealthCheckTimeOut: Optional[float]
    HealthCheckUnhealthNum: Optional[float]
    Id: Optional[str]
    ListenerName: Optional[str]
    Port: Optional[float]
    Protocol: Optional[str]
    Scheduler: Optional[str]
    SessionExpireTime: Optional[float]
    SniSwitch: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CertificateCaId=json_data.get("CertificateCaId"),
            CertificateId=json_data.get("CertificateId"),
            CertificateSslMode=json_data.get("CertificateSslMode"),
            ClbId=json_data.get("ClbId"),
            HealthCheckHealthNum=json_data.get("HealthCheckHealthNum"),
            HealthCheckIntervalTime=json_data.get("HealthCheckIntervalTime"),
            HealthCheckSwitch=json_data.get("HealthCheckSwitch"),
            HealthCheckTimeOut=json_data.get("HealthCheckTimeOut"),
            HealthCheckUnhealthNum=json_data.get("HealthCheckUnhealthNum"),
            Id=json_data.get("Id"),
            ListenerName=json_data.get("ListenerName"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            Scheduler=json_data.get("Scheduler"),
            SessionExpireTime=json_data.get("SessionExpireTime"),
            SniSwitch=json_data.get("SniSwitch"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


