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
    AuthType: Optional[float]
    CertificateId: Optional[str]
    ClientCertificateId: Optional[str]
    ClientCertificateIds: Optional[Sequence[str]]
    CreateTime: Optional[str]
    ForwardProtocol: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Port: Optional[float]
    Protocol: Optional[str]
    ProxyId: Optional[str]
    Status: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AuthType=json_data.get("AuthType"),
            CertificateId=json_data.get("CertificateId"),
            ClientCertificateId=json_data.get("ClientCertificateId"),
            ClientCertificateIds=json_data.get("ClientCertificateIds"),
            CreateTime=json_data.get("CreateTime"),
            ForwardProtocol=json_data.get("ForwardProtocol"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            ProxyId=json_data.get("ProxyId"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


