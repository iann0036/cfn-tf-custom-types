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
    Arn: Optional[str]
    CertificateAuthority: Optional[Sequence["_CertificateAuthorityDefinition"]]
    CreatedAt: Optional[str]
    EnabledClusterLogTypes: Optional[Sequence[str]]
    Endpoint: Optional[str]
    Id: Optional[str]
    Identity: Optional[Sequence["_IdentityDefinition2"]]
    Name: Optional[str]
    PlatformVersion: Optional[str]
    RoleArn: Optional[str]
    Status: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Version: Optional[str]
    EncryptionConfig: Optional[Sequence["_EncryptionConfigDefinition"]]
    KubernetesNetworkConfig: Optional[Sequence["_KubernetesNetworkConfigDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    VpcConfig: Optional[Sequence["_VpcConfigDefinition"]]

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
            Arn=json_data.get("Arn"),
            CertificateAuthority=deserialize_list(json_data.get("CertificateAuthority"), CertificateAuthorityDefinition),
            CreatedAt=json_data.get("CreatedAt"),
            EnabledClusterLogTypes=json_data.get("EnabledClusterLogTypes"),
            Endpoint=json_data.get("Endpoint"),
            Id=json_data.get("Id"),
            Identity=deserialize_list(json_data.get("Identity"), IdentityDefinition2),
            Name=json_data.get("Name"),
            PlatformVersion=json_data.get("PlatformVersion"),
            RoleArn=json_data.get("RoleArn"),
            Status=json_data.get("Status"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Version=json_data.get("Version"),
            EncryptionConfig=deserialize_list(json_data.get("EncryptionConfig"), EncryptionConfigDefinition),
            KubernetesNetworkConfig=deserialize_list(json_data.get("KubernetesNetworkConfig"), KubernetesNetworkConfigDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            VpcConfig=deserialize_list(json_data.get("VpcConfig"), VpcConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CertificateAuthorityDefinition(BaseModel):
    Data: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateAuthorityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateAuthorityDefinition"]:
        if not json_data:
            return None
        return cls(
            Data=json_data.get("Data"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateAuthorityDefinition = CertificateAuthorityDefinition


@dataclass
class IdentityDefinition2(BaseModel):
    Oidc: Optional[Sequence["_IdentityDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IdentityDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IdentityDefinition2"]:
        if not json_data:
            return None
        return cls(
            Oidc=deserialize_list(json_data.get("Oidc"), IdentityDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IdentityDefinition2 = IdentityDefinition2


@dataclass
class IdentityDefinition(BaseModel):
    Issuer: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IdentityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IdentityDefinition"]:
        if not json_data:
            return None
        return cls(
            Issuer=json_data.get("Issuer"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IdentityDefinition = IdentityDefinition


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
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class EncryptionConfigDefinition(BaseModel):
    Resources: Optional[Sequence[str]]
    Provider: Optional[Sequence["_ProviderDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Resources=json_data.get("Resources"),
            Provider=deserialize_list(json_data.get("Provider"), ProviderDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionConfigDefinition = EncryptionConfigDefinition


@dataclass
class ProviderDefinition(BaseModel):
    KeyArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProviderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProviderDefinition"]:
        if not json_data:
            return None
        return cls(
            KeyArn=json_data.get("KeyArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProviderDefinition = ProviderDefinition


@dataclass
class KubernetesNetworkConfigDefinition(BaseModel):
    ServiceIpv4Cidr: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KubernetesNetworkConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KubernetesNetworkConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            ServiceIpv4Cidr=json_data.get("ServiceIpv4Cidr"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KubernetesNetworkConfigDefinition = KubernetesNetworkConfigDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


@dataclass
class VpcConfigDefinition(BaseModel):
    EndpointPrivateAccess: Optional[bool]
    EndpointPublicAccess: Optional[bool]
    PublicAccessCidrs: Optional[Sequence[str]]
    SecurityGroupIds: Optional[Sequence[str]]
    SubnetIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_VpcConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            EndpointPrivateAccess=json_data.get("EndpointPrivateAccess"),
            EndpointPublicAccess=json_data.get("EndpointPublicAccess"),
            PublicAccessCidrs=json_data.get("PublicAccessCidrs"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SubnetIds=json_data.get("SubnetIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcConfigDefinition = VpcConfigDefinition


