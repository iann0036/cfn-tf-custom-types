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
    AuthBlackoutTime: Optional[float]
    AuthCaCert: Optional[str]
    AuthCert: Optional[str]
    AuthHttpBasic: Optional[str]
    AuthInvalidMax: Optional[float]
    AuthLockoutDuration: Optional[float]
    AuthLockoutThreshold: Optional[float]
    AuthOnDemand: Optional[str]
    AuthPortalTimeout: Optional[float]
    AuthSecureHttp: Optional[str]
    AuthSrcMac: Optional[str]
    AuthSslAllowRenegotiation: Optional[str]
    AuthSslMinProtoVersion: Optional[str]
    AuthTimeout: Optional[float]
    AuthTimeoutType: Optional[str]
    AuthType: Optional[str]
    DynamicSortSubtable: Optional[str]
    Id: Optional[str]
    PerPolicyDisclaimer: Optional[str]
    RadiusSesTimeoutAct: Optional[str]
    Vdomparam: Optional[str]
    AuthPorts: Optional[Sequence["_AuthPortsDefinition"]]

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
            AuthBlackoutTime=json_data.get("AuthBlackoutTime"),
            AuthCaCert=json_data.get("AuthCaCert"),
            AuthCert=json_data.get("AuthCert"),
            AuthHttpBasic=json_data.get("AuthHttpBasic"),
            AuthInvalidMax=json_data.get("AuthInvalidMax"),
            AuthLockoutDuration=json_data.get("AuthLockoutDuration"),
            AuthLockoutThreshold=json_data.get("AuthLockoutThreshold"),
            AuthOnDemand=json_data.get("AuthOnDemand"),
            AuthPortalTimeout=json_data.get("AuthPortalTimeout"),
            AuthSecureHttp=json_data.get("AuthSecureHttp"),
            AuthSrcMac=json_data.get("AuthSrcMac"),
            AuthSslAllowRenegotiation=json_data.get("AuthSslAllowRenegotiation"),
            AuthSslMinProtoVersion=json_data.get("AuthSslMinProtoVersion"),
            AuthTimeout=json_data.get("AuthTimeout"),
            AuthTimeoutType=json_data.get("AuthTimeoutType"),
            AuthType=json_data.get("AuthType"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Id=json_data.get("Id"),
            PerPolicyDisclaimer=json_data.get("PerPolicyDisclaimer"),
            RadiusSesTimeoutAct=json_data.get("RadiusSesTimeoutAct"),
            Vdomparam=json_data.get("Vdomparam"),
            AuthPorts=deserialize_list(json_data.get("AuthPorts"), AuthPortsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AuthPortsDefinition(BaseModel):
    Id: Optional[float]
    Port: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthPortsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthPortsDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Port=json_data.get("Port"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthPortsDefinition = AuthPortsDefinition


