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
    Id: Optional[str]
    IpConfiguration: Optional[str]
    JobId: Optional[str]
    Labels: Optional[Sequence["_Labels"]]
    MachineType: Optional[str]
    MaxWorkers: Optional[float]
    Name: Optional[str]
    Network: Optional[str]
    OnDelete: Optional[str]
    Parameters: Optional[Sequence["_Parameters"]]
    Project: Optional[str]
    Region: Optional[str]
    ServiceAccountEmail: Optional[str]
    State: Optional[str]
    Subnetwork: Optional[str]
    TempGcsLocation: Optional[str]
    TemplateGcsPath: Optional[str]
    Type: Optional[str]
    Zone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Id=json_data.get("Id"),
            IpConfiguration=json_data.get("IpConfiguration"),
            JobId=json_data.get("JobId"),
            Labels=json_data.get("Labels"),
            MachineType=json_data.get("MachineType"),
            MaxWorkers=json_data.get("MaxWorkers"),
            Name=json_data.get("Name"),
            Network=json_data.get("Network"),
            OnDelete=json_data.get("OnDelete"),
            Parameters=json_data.get("Parameters"),
            Project=json_data.get("Project"),
            Region=json_data.get("Region"),
            ServiceAccountEmail=json_data.get("ServiceAccountEmail"),
            State=json_data.get("State"),
            Subnetwork=json_data.get("Subnetwork"),
            TempGcsLocation=json_data.get("TempGcsLocation"),
            TemplateGcsPath=json_data.get("TemplateGcsPath"),
            Type=json_data.get("Type"),
            Zone=json_data.get("Zone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Labels:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Labels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Labels"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Labels = Labels


@dataclass
class Parameters:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Parameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Parameters"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Parameters = Parameters


