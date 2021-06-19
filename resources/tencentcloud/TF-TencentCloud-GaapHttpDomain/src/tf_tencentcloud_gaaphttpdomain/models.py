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
    BasicAuth: Optional[bool]
    BasicAuthId: Optional[str]
    CertificateId: Optional[str]
    ClientCertificateId: Optional[str]
    ClientCertificateIds: Optional[Sequence[str]]
    Domain: Optional[str]
    GaapAuth: Optional[bool]
    GaapAuthId: Optional[str]
    Id: Optional[str]
    ListenerId: Optional[str]
    RealserverAuth: Optional[bool]
    RealserverCertificateDomain: Optional[str]
    RealserverCertificateId: Optional[str]
    RealserverCertificateIds: Optional[Sequence[str]]

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
            BasicAuth=json_data.get("BasicAuth"),
            BasicAuthId=json_data.get("BasicAuthId"),
            CertificateId=json_data.get("CertificateId"),
            ClientCertificateId=json_data.get("ClientCertificateId"),
            ClientCertificateIds=json_data.get("ClientCertificateIds"),
            Domain=json_data.get("Domain"),
            GaapAuth=json_data.get("GaapAuth"),
            GaapAuthId=json_data.get("GaapAuthId"),
            Id=json_data.get("Id"),
            ListenerId=json_data.get("ListenerId"),
            RealserverAuth=json_data.get("RealserverAuth"),
            RealserverCertificateDomain=json_data.get("RealserverCertificateDomain"),
            RealserverCertificateId=json_data.get("RealserverCertificateId"),
            RealserverCertificateIds=json_data.get("RealserverCertificateIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


