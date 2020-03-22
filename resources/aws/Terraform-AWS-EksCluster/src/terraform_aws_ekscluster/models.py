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
    Arn: Optional[str]
    CertificateAuthority: Optional[Sequence["_CertificateAuthority"]]
    CreatedAt: Optional[str]
    EnabledClusterLogTypes: Optional[Sequence[str]]
    Endpoint: Optional[str]
    Id: Optional[str]
    Identity: Optional[Sequence["_Identity"]]
    Name: Optional[str]
    PlatformVersion: Optional[str]
    RoleArn: Optional[str]
    Status: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Version: Optional[str]
    EncryptionConfig: Optional[Sequence["_EncryptionConfig"]]
    Timeouts: Optional["_Timeouts"]
    VpcConfig: Optional[Sequence["_VpcConfig"]]
    Provider: Optional[Sequence["_Provider"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            CertificateAuthority=json_data.get("CertificateAuthority"),
            CreatedAt=json_data.get("CreatedAt"),
            EnabledClusterLogTypes=json_data.get("EnabledClusterLogTypes"),
            Endpoint=json_data.get("Endpoint"),
            Id=json_data.get("Id"),
            Identity=json_data.get("Identity"),
            Name=json_data.get("Name"),
            PlatformVersion=json_data.get("PlatformVersion"),
            RoleArn=json_data.get("RoleArn"),
            Status=json_data.get("Status"),
            Tags=json_data.get("Tags"),
            Version=json_data.get("Version"),
            EncryptionConfig=json_data.get("EncryptionConfig"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            VpcConfig=json_data.get("VpcConfig"),
            Provider=json_data.get("Provider"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CertificateAuthority:
    Data: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateAuthority"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateAuthority"]:
        if not json_data:
            return None
        return cls(
            Data=json_data.get("Data"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateAuthority = CertificateAuthority


@dataclass
class Identity:
    Oidc: Optional[Sequence["_Oidc"]]

    @classmethod
    def _deserialize(
        cls: Type["_Identity"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Identity"]:
        if not json_data:
            return None
        return cls(
            Oidc=json_data.get("Oidc"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Identity = Identity


@dataclass
class Oidc:
    Issuer: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Oidc"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Oidc"]:
        if not json_data:
            return None
        return cls(
            Issuer=json_data.get("Issuer"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Oidc = Oidc


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
class EncryptionConfig:
    Resources: Optional[Sequence[str]]
    Provider: Optional[Sequence["_Provider"]]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionConfig"]:
        if not json_data:
            return None
        return cls(
            Resources=json_data.get("Resources"),
            Provider=json_data.get("Provider"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionConfig = EncryptionConfig


@dataclass
class Provider:
    KeyArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Provider"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Provider"]:
        if not json_data:
            return None
        return cls(
            KeyArn=json_data.get("KeyArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Provider = Provider


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


@dataclass
class VpcConfig:
    EndpointPrivateAccess: Optional[bool]
    EndpointPublicAccess: Optional[bool]
    PublicAccessCidrs: Optional[Sequence[str]]
    SecurityGroupIds: Optional[Sequence[str]]
    SubnetIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_VpcConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcConfig"]:
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
_VpcConfig = VpcConfig


