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
    AdditionalArtifacts: Optional[Sequence[str]]
    AdditionalSchemaElements: Optional[Sequence[str]]
    Compression: Optional[str]
    Format: Optional[str]
    ReportName: Optional[str]
    S3Bucket: Optional[str]
    S3Prefix: Optional[str]
    S3Region: Optional[str]
    TimeUnit: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AdditionalArtifacts=json_data.get("AdditionalArtifacts"),
            AdditionalSchemaElements=json_data.get("AdditionalSchemaElements"),
            Compression=json_data.get("Compression"),
            Format=json_data.get("Format"),
            ReportName=json_data.get("ReportName"),
            S3Bucket=json_data.get("S3Bucket"),
            S3Prefix=json_data.get("S3Prefix"),
            S3Region=json_data.get("S3Region"),
            TimeUnit=json_data.get("TimeUnit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


