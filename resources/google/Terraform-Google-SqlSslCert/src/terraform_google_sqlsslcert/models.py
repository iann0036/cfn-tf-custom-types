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
    Cert: Optional[str]
    CertSerialNumber: Optional[str]
    CommonName: Optional[str]
    CreateTime: Optional[str]
    ExpirationTime: Optional[str]
    Id: Optional[str]
    Instance: Optional[str]
    PrivateKey: Optional[str]
    Project: Optional[str]
    ServerCaCert: Optional[str]
    Sha1Fingerprint: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Cert=json_data.get("Cert"),
            CertSerialNumber=json_data.get("CertSerialNumber"),
            CommonName=json_data.get("CommonName"),
            CreateTime=json_data.get("CreateTime"),
            ExpirationTime=json_data.get("ExpirationTime"),
            Id=json_data.get("Id"),
            Instance=json_data.get("Instance"),
            PrivateKey=json_data.get("PrivateKey"),
            Project=json_data.get("Project"),
            ServerCaCert=json_data.get("ServerCaCert"),
            Sha1Fingerprint=json_data.get("Sha1Fingerprint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


