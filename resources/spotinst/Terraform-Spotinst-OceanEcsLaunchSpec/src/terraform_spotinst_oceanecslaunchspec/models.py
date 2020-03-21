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
    IamInstanceProfile: Optional[str]
    ImageId: Optional[str]
    Name: Optional[str]
    OceanId: Optional[str]
    SecurityGroupIds: Optional[Sequence[str]]
    UserData: Optional[str]
    Attributes: Optional[Sequence["_Attributes"]]
    AutoscaleHeadrooms: Optional[Sequence["_AutoscaleHeadrooms"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            IamInstanceProfile=json_data.get("IamInstanceProfile"),
            ImageId=json_data.get("ImageId"),
            Name=json_data.get("Name"),
            OceanId=json_data.get("OceanId"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            UserData=json_data.get("UserData"),
            Attributes=json_data.get("Attributes"),
            AutoscaleHeadrooms=json_data.get("AutoscaleHeadrooms"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Attributes:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Attributes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Attributes"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Attributes = Attributes


@dataclass
class AutoscaleHeadrooms:
    CpuPerUnit: Optional[float]
    MemoryPerUnit: Optional[float]
    NumOfUnits: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AutoscaleHeadrooms"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoscaleHeadrooms"]:
        if not json_data:
            return None
        return cls(
            CpuPerUnit=json_data.get("CpuPerUnit"),
            MemoryPerUnit=json_data.get("MemoryPerUnit"),
            NumOfUnits=json_data.get("NumOfUnits"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoscaleHeadrooms = AutoscaleHeadrooms


