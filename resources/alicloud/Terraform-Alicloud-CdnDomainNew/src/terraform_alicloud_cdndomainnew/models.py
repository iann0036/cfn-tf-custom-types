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
    CdnType: Optional[str]
    DomainName: Optional[str]
    Id: Optional[str]
    ResourceGroupId: Optional[str]
    Scope: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    CertificateConfig: Optional[Sequence["_CertificateConfig"]]
    Sources: Optional[Sequence["_Sources"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CdnType=json_data.get("CdnType"),
            DomainName=json_data.get("DomainName"),
            Id=json_data.get("Id"),
            ResourceGroupId=json_data.get("ResourceGroupId"),
            Scope=json_data.get("Scope"),
            Tags=json_data.get("Tags"),
            CertificateConfig=json_data.get("CertificateConfig"),
            Sources=json_data.get("Sources"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class CertificateConfig:
    CertName: Optional[str]
    CertType: Optional[str]
    ForceSet: Optional[str]
    PrivateKey: Optional[str]
    ServerCertificate: Optional[str]
    ServerCertificateStatus: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateConfig"]:
        if not json_data:
            return None
        return cls(
            CertName=json_data.get("CertName"),
            CertType=json_data.get("CertType"),
            ForceSet=json_data.get("ForceSet"),
            PrivateKey=json_data.get("PrivateKey"),
            ServerCertificate=json_data.get("ServerCertificate"),
            ServerCertificateStatus=json_data.get("ServerCertificateStatus"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateConfig = CertificateConfig


@dataclass
class Sources:
    Content: Optional[str]
    Port: Optional[float]
    Priority: Optional[float]
    Type: Optional[str]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Sources"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Sources"]:
        if not json_data:
            return None
        return cls(
            Content=json_data.get("Content"),
            Port=json_data.get("Port"),
            Priority=json_data.get("Priority"),
            Type=json_data.get("Type"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Sources = Sources


