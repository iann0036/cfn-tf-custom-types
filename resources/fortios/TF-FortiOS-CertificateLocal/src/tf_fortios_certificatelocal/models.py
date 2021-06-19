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
    AutoRegenerateDays: Optional[float]
    AutoRegenerateDaysWarning: Optional[float]
    CaIdentifier: Optional[str]
    Certificate: Optional[str]
    CmpPath: Optional[str]
    CmpRegenerationMethod: Optional[str]
    CmpServer: Optional[str]
    CmpServerCert: Optional[str]
    Comments: Optional[str]
    Csr: Optional[str]
    EnrollProtocol: Optional[str]
    Id: Optional[str]
    IkeLocalid: Optional[str]
    IkeLocalidType: Optional[str]
    LastUpdated: Optional[float]
    Name: Optional[str]
    NameEncoding: Optional[str]
    Password: Optional[str]
    PrivateKey: Optional[str]
    Range: Optional[str]
    ScepPassword: Optional[str]
    ScepUrl: Optional[str]
    Source: Optional[str]
    SourceIp: Optional[str]
    State: Optional[str]
    Vdomparam: Optional[str]

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
            AutoRegenerateDays=json_data.get("AutoRegenerateDays"),
            AutoRegenerateDaysWarning=json_data.get("AutoRegenerateDaysWarning"),
            CaIdentifier=json_data.get("CaIdentifier"),
            Certificate=json_data.get("Certificate"),
            CmpPath=json_data.get("CmpPath"),
            CmpRegenerationMethod=json_data.get("CmpRegenerationMethod"),
            CmpServer=json_data.get("CmpServer"),
            CmpServerCert=json_data.get("CmpServerCert"),
            Comments=json_data.get("Comments"),
            Csr=json_data.get("Csr"),
            EnrollProtocol=json_data.get("EnrollProtocol"),
            Id=json_data.get("Id"),
            IkeLocalid=json_data.get("IkeLocalid"),
            IkeLocalidType=json_data.get("IkeLocalidType"),
            LastUpdated=json_data.get("LastUpdated"),
            Name=json_data.get("Name"),
            NameEncoding=json_data.get("NameEncoding"),
            Password=json_data.get("Password"),
            PrivateKey=json_data.get("PrivateKey"),
            Range=json_data.get("Range"),
            ScepPassword=json_data.get("ScepPassword"),
            ScepUrl=json_data.get("ScepUrl"),
            Source=json_data.get("Source"),
            SourceIp=json_data.get("SourceIp"),
            State=json_data.get("State"),
            Vdomparam=json_data.get("Vdomparam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


