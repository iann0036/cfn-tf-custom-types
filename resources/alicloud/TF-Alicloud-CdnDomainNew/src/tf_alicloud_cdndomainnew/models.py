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
    CdnType: Optional[str]
    Cname: Optional[str]
    DomainName: Optional[str]
    Id: Optional[str]
    ResourceGroupId: Optional[str]
    Scope: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    CertificateConfig: Optional[Sequence["_CertificateConfigDefinition"]]
    Sources: Optional[Sequence["_SourcesDefinition"]]

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
            CdnType=json_data.get("CdnType"),
            Cname=json_data.get("Cname"),
            DomainName=json_data.get("DomainName"),
            Id=json_data.get("Id"),
            ResourceGroupId=json_data.get("ResourceGroupId"),
            Scope=json_data.get("Scope"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            CertificateConfig=deserialize_list(json_data.get("CertificateConfig"), CertificateConfigDefinition),
            Sources=deserialize_list(json_data.get("Sources"), SourcesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class CertificateConfigDefinition(BaseModel):
    CertName: Optional[str]
    CertType: Optional[str]
    ForceSet: Optional[str]
    PrivateKey: Optional[str]
    ServerCertificate: Optional[str]
    ServerCertificateStatus: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateConfigDefinition"]:
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
_CertificateConfigDefinition = CertificateConfigDefinition


@dataclass
class SourcesDefinition(BaseModel):
    Content: Optional[str]
    Port: Optional[float]
    Priority: Optional[float]
    Type: Optional[str]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SourcesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourcesDefinition"]:
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
_SourcesDefinition = SourcesDefinition


