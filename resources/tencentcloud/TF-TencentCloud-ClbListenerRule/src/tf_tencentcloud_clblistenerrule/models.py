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
    Domain: Optional[str]
    ForwardType: Optional[str]
    HealthCheckHealthNum: Optional[float]
    HealthCheckHttpCode: Optional[float]
    HealthCheckHttpDomain: Optional[str]
    HealthCheckHttpMethod: Optional[str]
    HealthCheckHttpPath: Optional[str]
    HealthCheckIntervalTime: Optional[float]
    HealthCheckSwitch: Optional[bool]
    HealthCheckUnhealthNum: Optional[float]
    Http2Switch: Optional[bool]
    Id: Optional[str]
    ListenerId: Optional[str]
    RuleId: Optional[str]
    Scheduler: Optional[str]
    SessionExpireTime: Optional[float]
    TargetType: Optional[str]
    Url: Optional[str]

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
            Domain=json_data.get("Domain"),
            ForwardType=json_data.get("ForwardType"),
            HealthCheckHealthNum=json_data.get("HealthCheckHealthNum"),
            HealthCheckHttpCode=json_data.get("HealthCheckHttpCode"),
            HealthCheckHttpDomain=json_data.get("HealthCheckHttpDomain"),
            HealthCheckHttpMethod=json_data.get("HealthCheckHttpMethod"),
            HealthCheckHttpPath=json_data.get("HealthCheckHttpPath"),
            HealthCheckIntervalTime=json_data.get("HealthCheckIntervalTime"),
            HealthCheckSwitch=json_data.get("HealthCheckSwitch"),
            HealthCheckUnhealthNum=json_data.get("HealthCheckUnhealthNum"),
            Http2Switch=json_data.get("Http2Switch"),
            Id=json_data.get("Id"),
            ListenerId=json_data.get("ListenerId"),
            RuleId=json_data.get("RuleId"),
            Scheduler=json_data.get("Scheduler"),
            SessionExpireTime=json_data.get("SessionExpireTime"),
            TargetType=json_data.get("TargetType"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


