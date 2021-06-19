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
    CaCertificateFile: Optional[str]
    ExcludedGateways: Optional[Sequence[str]]
    Id: Optional[str]
    Index: Optional[float]
    Name: Optional[str]
    Notls: Optional[bool]
    Port: Optional[float]
    PrivateKeyFile: Optional[str]
    Protocol: Optional[str]
    PublicCertificateFile: Optional[str]
    Server: Optional[str]
    Status: Optional[str]
    Template: Optional[str]

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
            CaCertificateFile=json_data.get("CaCertificateFile"),
            ExcludedGateways=json_data.get("ExcludedGateways"),
            Id=json_data.get("Id"),
            Index=json_data.get("Index"),
            Name=json_data.get("Name"),
            Notls=json_data.get("Notls"),
            Port=json_data.get("Port"),
            PrivateKeyFile=json_data.get("PrivateKeyFile"),
            Protocol=json_data.get("Protocol"),
            PublicCertificateFile=json_data.get("PublicCertificateFile"),
            Server=json_data.get("Server"),
            Status=json_data.get("Status"),
            Template=json_data.get("Template"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


