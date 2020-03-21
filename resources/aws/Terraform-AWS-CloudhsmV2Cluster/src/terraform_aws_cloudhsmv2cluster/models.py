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
    ClusterCertificates: Optional[Sequence["_ClusterCertificates"]]
    ClusterId: Optional[str]
    ClusterState: Optional[str]
    HsmType: Optional[str]
    SecurityGroupId: Optional[str]
    SourceBackupIdentifier: Optional[str]
    SubnetIds: Optional[Sequence[str]]
    Tags: Optional[Sequence["_Tags"]]
    VpcId: Optional[str]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ClusterCertificates=json_data.get("ClusterCertificates"),
            ClusterId=json_data.get("ClusterId"),
            ClusterState=json_data.get("ClusterState"),
            HsmType=json_data.get("HsmType"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            SourceBackupIdentifier=json_data.get("SourceBackupIdentifier"),
            SubnetIds=json_data.get("SubnetIds"),
            Tags=json_data.get("Tags"),
            VpcId=json_data.get("VpcId"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ClusterCertificates:
    AwsHardwareCertificate: Optional[str]
    ClusterCertificate: Optional[str]
    ClusterCsr: Optional[str]
    HsmCertificate: Optional[str]
    ManufacturerHardwareCertificate: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterCertificates"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterCertificates"]:
        if not json_data:
            return None
        return cls(
            AwsHardwareCertificate=json_data.get("AwsHardwareCertificate"),
            ClusterCertificate=json_data.get("ClusterCertificate"),
            ClusterCsr=json_data.get("ClusterCsr"),
            HsmCertificate=json_data.get("HsmCertificate"),
            ManufacturerHardwareCertificate=json_data.get("ManufacturerHardwareCertificate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClusterCertificates = ClusterCertificates


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


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


