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
    Attributes: Optional[Sequence["_Attributes"]]
    FixedRate: Optional[float]
    Host: Optional[str]
    HttpMethod: Optional[str]
    Id: Optional[str]
    Priority: Optional[float]
    ReservoirSize: Optional[float]
    ResourceArn: Optional[str]
    RuleName: Optional[str]
    ServiceName: Optional[str]
    ServiceType: Optional[str]
    UrlPath: Optional[str]
    Version: Optional[float]

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
            Attributes=json_data.get("Attributes"),
            FixedRate=json_data.get("FixedRate"),
            Host=json_data.get("Host"),
            HttpMethod=json_data.get("HttpMethod"),
            Id=json_data.get("Id"),
            Priority=json_data.get("Priority"),
            ReservoirSize=json_data.get("ReservoirSize"),
            ResourceArn=json_data.get("ResourceArn"),
            RuleName=json_data.get("RuleName"),
            ServiceName=json_data.get("ServiceName"),
            ServiceType=json_data.get("ServiceType"),
            UrlPath=json_data.get("UrlPath"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Attributes:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Attributes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Attributes"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Attributes = Attributes


