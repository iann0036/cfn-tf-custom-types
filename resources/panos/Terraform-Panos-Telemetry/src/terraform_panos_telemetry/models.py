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
    ApplicationReports: Optional[bool]
    FileTypeIdentificationReports: Optional[bool]
    Id: Optional[str]
    PassiveDnsMonitoring: Optional[bool]
    ProductUsageStats: Optional[bool]
    ThreatPreventionData: Optional[bool]
    ThreatPreventionPacketCaptures: Optional[bool]
    ThreatPreventionReports: Optional[bool]
    UrlReports: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ApplicationReports=json_data.get("ApplicationReports"),
            FileTypeIdentificationReports=json_data.get("FileTypeIdentificationReports"),
            Id=json_data.get("Id"),
            PassiveDnsMonitoring=json_data.get("PassiveDnsMonitoring"),
            ProductUsageStats=json_data.get("ProductUsageStats"),
            ThreatPreventionData=json_data.get("ThreatPreventionData"),
            ThreatPreventionPacketCaptures=json_data.get("ThreatPreventionPacketCaptures"),
            ThreatPreventionReports=json_data.get("ThreatPreventionReports"),
            UrlReports=json_data.get("UrlReports"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


