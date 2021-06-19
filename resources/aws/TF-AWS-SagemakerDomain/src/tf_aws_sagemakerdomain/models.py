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
    AppNetworkAccessType: Optional[str]
    Arn: Optional[str]
    AuthMode: Optional[str]
    DomainName: Optional[str]
    HomeEfsFileSystemId: Optional[str]
    Id: Optional[str]
    KmsKeyId: Optional[str]
    SingleSignOnManagedApplicationInstanceId: Optional[str]
    SubnetIds: Optional[Sequence[str]]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Url: Optional[str]
    VpcId: Optional[str]
    DefaultUserSettings: Optional[Sequence["_DefaultUserSettingsDefinition"]]

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
            AppNetworkAccessType=json_data.get("AppNetworkAccessType"),
            Arn=json_data.get("Arn"),
            AuthMode=json_data.get("AuthMode"),
            DomainName=json_data.get("DomainName"),
            HomeEfsFileSystemId=json_data.get("HomeEfsFileSystemId"),
            Id=json_data.get("Id"),
            KmsKeyId=json_data.get("KmsKeyId"),
            SingleSignOnManagedApplicationInstanceId=json_data.get("SingleSignOnManagedApplicationInstanceId"),
            SubnetIds=json_data.get("SubnetIds"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Url=json_data.get("Url"),
            VpcId=json_data.get("VpcId"),
            DefaultUserSettings=deserialize_list(json_data.get("DefaultUserSettings"), DefaultUserSettingsDefinition),
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
class DefaultUserSettingsDefinition(BaseModel):
    ExecutionRole: Optional[str]
    SecurityGroups: Optional[Sequence[str]]
    JupyterServerAppSettings: Optional[Sequence["_JupyterServerAppSettingsDefinition"]]
    KernelGatewayAppSettings: Optional[Sequence["_KernelGatewayAppSettingsDefinition"]]
    SharingSettings: Optional[Sequence["_SharingSettingsDefinition"]]
    TensorBoardAppSettings: Optional[Sequence["_TensorBoardAppSettingsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultUserSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultUserSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            ExecutionRole=json_data.get("ExecutionRole"),
            SecurityGroups=json_data.get("SecurityGroups"),
            JupyterServerAppSettings=deserialize_list(json_data.get("JupyterServerAppSettings"), JupyterServerAppSettingsDefinition),
            KernelGatewayAppSettings=deserialize_list(json_data.get("KernelGatewayAppSettings"), KernelGatewayAppSettingsDefinition),
            SharingSettings=deserialize_list(json_data.get("SharingSettings"), SharingSettingsDefinition),
            TensorBoardAppSettings=deserialize_list(json_data.get("TensorBoardAppSettings"), TensorBoardAppSettingsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultUserSettingsDefinition = DefaultUserSettingsDefinition


@dataclass
class JupyterServerAppSettingsDefinition(BaseModel):
    DefaultResourceSpec: Optional[Sequence["_DefaultResourceSpecDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_JupyterServerAppSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JupyterServerAppSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultResourceSpec=deserialize_list(json_data.get("DefaultResourceSpec"), DefaultResourceSpecDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_JupyterServerAppSettingsDefinition = JupyterServerAppSettingsDefinition


@dataclass
class DefaultResourceSpecDefinition(BaseModel):
    InstanceType: Optional[str]
    SagemakerImageArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultResourceSpecDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultResourceSpecDefinition"]:
        if not json_data:
            return None
        return cls(
            InstanceType=json_data.get("InstanceType"),
            SagemakerImageArn=json_data.get("SagemakerImageArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultResourceSpecDefinition = DefaultResourceSpecDefinition


@dataclass
class KernelGatewayAppSettingsDefinition(BaseModel):
    CustomImage: Optional[Sequence["_CustomImageDefinition"]]
    DefaultResourceSpec: Optional[Sequence["_DefaultResourceSpecDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_KernelGatewayAppSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KernelGatewayAppSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            CustomImage=deserialize_list(json_data.get("CustomImage"), CustomImageDefinition),
            DefaultResourceSpec=deserialize_list(json_data.get("DefaultResourceSpec"), DefaultResourceSpecDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_KernelGatewayAppSettingsDefinition = KernelGatewayAppSettingsDefinition


@dataclass
class CustomImageDefinition(BaseModel):
    AppImageConfigName: Optional[str]
    ImageName: Optional[str]
    ImageVersionNumber: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CustomImageDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomImageDefinition"]:
        if not json_data:
            return None
        return cls(
            AppImageConfigName=json_data.get("AppImageConfigName"),
            ImageName=json_data.get("ImageName"),
            ImageVersionNumber=json_data.get("ImageVersionNumber"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomImageDefinition = CustomImageDefinition


@dataclass
class SharingSettingsDefinition(BaseModel):
    NotebookOutputOption: Optional[str]
    S3KmsKeyId: Optional[str]
    S3OutputPath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SharingSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SharingSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            NotebookOutputOption=json_data.get("NotebookOutputOption"),
            S3KmsKeyId=json_data.get("S3KmsKeyId"),
            S3OutputPath=json_data.get("S3OutputPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SharingSettingsDefinition = SharingSettingsDefinition


@dataclass
class TensorBoardAppSettingsDefinition(BaseModel):
    DefaultResourceSpec: Optional[Sequence["_DefaultResourceSpecDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TensorBoardAppSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TensorBoardAppSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultResourceSpec=deserialize_list(json_data.get("DefaultResourceSpec"), DefaultResourceSpecDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TensorBoardAppSettingsDefinition = TensorBoardAppSettingsDefinition


