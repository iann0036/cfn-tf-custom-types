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
    Annotations: Optional[Sequence["_Annotations"]]
    AuthenticationMode: Optional[str]
    BillingMode: Optional[float]
    CertificateClusters: Optional[Sequence["_CertificateClusters"]]
    CertificateUsers: Optional[Sequence["_CertificateUsers"]]
    ClusterType: Optional[str]
    ClusterVersion: Optional[str]
    ContainerNetworkCidr: Optional[str]
    ContainerNetworkType: Optional[str]
    Description: Optional[str]
    Eip: Optional[str]
    ExtendParam: Optional[Sequence["_ExtendParam"]]
    ExternalApigEndpoint: Optional[str]
    ExternalEndpoint: Optional[str]
    FlavorId: Optional[str]
    HighwaySubnetId: Optional[str]
    Id: Optional[str]
    InternalEndpoint: Optional[str]
    Labels: Optional[Sequence["_Labels"]]
    Name: Optional[str]
    Region: Optional[str]
    SecurityGroupId: Optional[str]
    Status: Optional[str]
    SubnetId: Optional[str]
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
            Annotations=json_data.get("Annotations"),
            AuthenticationMode=json_data.get("AuthenticationMode"),
            BillingMode=json_data.get("BillingMode"),
            CertificateClusters=json_data.get("CertificateClusters"),
            CertificateUsers=json_data.get("CertificateUsers"),
            ClusterType=json_data.get("ClusterType"),
            ClusterVersion=json_data.get("ClusterVersion"),
            ContainerNetworkCidr=json_data.get("ContainerNetworkCidr"),
            ContainerNetworkType=json_data.get("ContainerNetworkType"),
            Description=json_data.get("Description"),
            Eip=json_data.get("Eip"),
            ExtendParam=json_data.get("ExtendParam"),
            ExternalApigEndpoint=json_data.get("ExternalApigEndpoint"),
            ExternalEndpoint=json_data.get("ExternalEndpoint"),
            FlavorId=json_data.get("FlavorId"),
            HighwaySubnetId=json_data.get("HighwaySubnetId"),
            Id=json_data.get("Id"),
            InternalEndpoint=json_data.get("InternalEndpoint"),
            Labels=json_data.get("Labels"),
            Name=json_data.get("Name"),
            Region=json_data.get("Region"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            Status=json_data.get("Status"),
            SubnetId=json_data.get("SubnetId"),
            VpcId=json_data.get("VpcId"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Annotations:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Annotations"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Annotations"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Annotations = Annotations


@dataclass
class CertificateClusters:
    CertificateAuthorityData: Optional[str]
    Name: Optional[str]
    Server: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateClusters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateClusters"]:
        if not json_data:
            return None
        return cls(
            CertificateAuthorityData=json_data.get("CertificateAuthorityData"),
            Name=json_data.get("Name"),
            Server=json_data.get("Server"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateClusters = CertificateClusters


@dataclass
class CertificateUsers:
    ClientCertificateData: Optional[str]
    ClientKeyData: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateUsers"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateUsers"]:
        if not json_data:
            return None
        return cls(
            ClientCertificateData=json_data.get("ClientCertificateData"),
            ClientKeyData=json_data.get("ClientKeyData"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateUsers = CertificateUsers


@dataclass
class ExtendParam:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExtendParam"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtendParam"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtendParam = ExtendParam


@dataclass
class Labels:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Labels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Labels"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Labels = Labels


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


