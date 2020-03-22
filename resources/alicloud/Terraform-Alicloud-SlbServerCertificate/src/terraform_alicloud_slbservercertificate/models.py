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
    AlicloudCertifacteId: Optional[str]
    AlicloudCertifacteName: Optional[str]
    AlicloudCertificateId: Optional[str]
    AlicloudCertificateName: Optional[str]
    AlicloudCertificateRegionId: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    PrivateKey: Optional[str]
    ResourceGroupId: Optional[str]
    ServerCertificate: Optional[str]
    Tags: Optional[Sequence["_Tags"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AlicloudCertifacteId=json_data.get("AlicloudCertifacteId"),
            AlicloudCertifacteName=json_data.get("AlicloudCertifacteName"),
            AlicloudCertificateId=json_data.get("AlicloudCertificateId"),
            AlicloudCertificateName=json_data.get("AlicloudCertificateName"),
            AlicloudCertificateRegionId=json_data.get("AlicloudCertificateRegionId"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PrivateKey=json_data.get("PrivateKey"),
            ResourceGroupId=json_data.get("ResourceGroupId"),
            ServerCertificate=json_data.get("ServerCertificate"),
            Tags=json_data.get("Tags"),
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


