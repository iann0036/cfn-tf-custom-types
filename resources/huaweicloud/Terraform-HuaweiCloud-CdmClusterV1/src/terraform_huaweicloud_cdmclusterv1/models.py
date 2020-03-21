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
    AvailabilityZone: Optional[str]
    Created: Optional[str]
    Email: Optional[Sequence[str]]
    EnterpriseProjectId: Optional[Sequence[str]]
    FlavorId: Optional[str]
    Instances: Optional[Sequence["_Instances"]]
    IsAutoOff: Optional[bool]
    Name: Optional[str]
    PhoneNum: Optional[Sequence[str]]
    PublidIp: Optional[str]
    ScheduleBootTime: Optional[str]
    ScheduleOffTime: Optional[str]
    SecurityGroupId: Optional[str]
    SubnetId: Optional[str]
    Version: Optional[str]
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
            AvailabilityZone=json_data.get("AvailabilityZone"),
            Created=json_data.get("Created"),
            Email=json_data.get("Email"),
            EnterpriseProjectId=json_data.get("EnterpriseProjectId"),
            FlavorId=json_data.get("FlavorId"),
            Instances=json_data.get("Instances"),
            IsAutoOff=json_data.get("IsAutoOff"),
            Name=json_data.get("Name"),
            PhoneNum=json_data.get("PhoneNum"),
            PublidIp=json_data.get("PublidIp"),
            ScheduleBootTime=json_data.get("ScheduleBootTime"),
            ScheduleOffTime=json_data.get("ScheduleOffTime"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            SubnetId=json_data.get("SubnetId"),
            Version=json_data.get("Version"),
            VpcId=json_data.get("VpcId"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Instances:
    Id: Optional[str]
    Name: Optional[str]
    PublicIp: Optional[str]
    Role: Optional[str]
    TrafficIp: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Instances"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Instances"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PublicIp=json_data.get("PublicIp"),
            Role=json_data.get("Role"),
            TrafficIp=json_data.get("TrafficIp"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Instances = Instances


@dataclass
class Timeouts:
    Create: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


