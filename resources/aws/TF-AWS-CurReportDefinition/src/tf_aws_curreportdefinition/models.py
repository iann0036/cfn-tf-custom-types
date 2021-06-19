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
    AdditionalArtifacts: Optional[Sequence[str]]
    AdditionalSchemaElements: Optional[Sequence[str]]
    Arn: Optional[str]
    Compression: Optional[str]
    Format: Optional[str]
    Id: Optional[str]
    RefreshClosedReports: Optional[bool]
    ReportName: Optional[str]
    ReportVersioning: Optional[str]
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
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AdditionalArtifacts=json_data.get("AdditionalArtifacts"),
            AdditionalSchemaElements=json_data.get("AdditionalSchemaElements"),
            Arn=json_data.get("Arn"),
            Compression=json_data.get("Compression"),
            Format=json_data.get("Format"),
            Id=json_data.get("Id"),
            RefreshClosedReports=json_data.get("RefreshClosedReports"),
            ReportName=json_data.get("ReportName"),
            ReportVersioning=json_data.get("ReportVersioning"),
            S3Bucket=json_data.get("S3Bucket"),
            S3Prefix=json_data.get("S3Prefix"),
            S3Region=json_data.get("S3Region"),
            TimeUnit=json_data.get("TimeUnit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


