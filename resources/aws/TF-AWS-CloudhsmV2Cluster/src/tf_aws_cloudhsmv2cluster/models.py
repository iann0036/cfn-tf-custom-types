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
    ClusterCertificates: Optional[Sequence["_ClusterCertificatesDefinition"]]
    ClusterId: Optional[str]
    ClusterState: Optional[str]
    HsmType: Optional[str]
    Id: Optional[str]
    SecurityGroupId: Optional[str]
    SourceBackupIdentifier: Optional[str]
    SubnetIds: Optional[Sequence[str]]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    VpcId: Optional[str]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            ClusterCertificates=deserialize_list(json_data.get("ClusterCertificates"), ClusterCertificatesDefinition),
            ClusterId=json_data.get("ClusterId"),
            ClusterState=json_data.get("ClusterState"),
            HsmType=json_data.get("HsmType"),
            Id=json_data.get("Id"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            SourceBackupIdentifier=json_data.get("SourceBackupIdentifier"),
            SubnetIds=json_data.get("SubnetIds"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            VpcId=json_data.get("VpcId"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ClusterCertificatesDefinition(BaseModel):
    AwsHardwareCertificate: Optional[str]
    ClusterCertificate: Optional[str]
    ClusterCsr: Optional[str]
    HsmCertificate: Optional[str]
    ManufacturerHardwareCertificate: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterCertificatesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterCertificatesDefinition"]:
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
_ClusterCertificatesDefinition = ClusterCertificatesDefinition


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


