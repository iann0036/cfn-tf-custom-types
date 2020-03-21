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
    CompatibleRuntimes: Optional[Sequence[str]]
    CreatedDate: Optional[str]
    Description: Optional[str]
    Filename: Optional[str]
    LayerArn: Optional[str]
    LayerName: Optional[str]
    LicenseInfo: Optional[str]
    S3Bucket: Optional[str]
    S3Key: Optional[str]
    S3ObjectVersion: Optional[str]
    SourceCodeHash: Optional[str]
    SourceCodeSize: Optional[float]
    Version: Optional[str]

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
            CompatibleRuntimes=json_data.get("CompatibleRuntimes"),
            CreatedDate=json_data.get("CreatedDate"),
            Description=json_data.get("Description"),
            Filename=json_data.get("Filename"),
            LayerArn=json_data.get("LayerArn"),
            LayerName=json_data.get("LayerName"),
            LicenseInfo=json_data.get("LicenseInfo"),
            S3Bucket=json_data.get("S3Bucket"),
            S3Key=json_data.get("S3Key"),
            S3ObjectVersion=json_data.get("S3ObjectVersion"),
            SourceCodeHash=json_data.get("SourceCodeHash"),
            SourceCodeSize=json_data.get("SourceCodeSize"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


