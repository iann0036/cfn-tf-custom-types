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
    AvailabilityZone: Optional[str]
    DefaultGateway: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Interface1NoAllowedAddressPairs: Optional[bool]
    Interface1NoFixedIps: Optional[bool]
    Interface2NoAllowedAddressPairs: Optional[bool]
    Interface2NoFixedIps: Optional[bool]
    Interface3NoAllowedAddressPairs: Optional[bool]
    Interface3NoFixedIps: Optional[bool]
    Interface4NoAllowedAddressPairs: Optional[bool]
    Interface4NoFixedIps: Optional[bool]
    Interface5NoAllowedAddressPairs: Optional[bool]
    Interface5NoFixedIps: Optional[bool]
    Interface6NoAllowedAddressPairs: Optional[bool]
    Interface6NoFixedIps: Optional[bool]
    Interface7NoAllowedAddressPairs: Optional[bool]
    Interface7NoFixedIps: Optional[bool]
    Interface8NoAllowedAddressPairs: Optional[bool]
    Interface8NoFixedIps: Optional[bool]
    Name: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TenantId: Optional[str]
    VirtualNetworkAppliancePlanId: Optional[str]
    Interface1AllowedAddressPairs: Optional[Sequence["_Interface1AllowedAddressPairsDefinition"]]
    Interface1FixedIps: Optional[Sequence["_Interface1FixedIpsDefinition"]]
    Interface1Info: Optional[Sequence["_Interface1InfoDefinition"]]
    Interface2AllowedAddressPairs: Optional[Sequence["_Interface2AllowedAddressPairsDefinition"]]
    Interface2FixedIps: Optional[Sequence["_Interface2FixedIpsDefinition"]]
    Interface2Info: Optional[Sequence["_Interface2InfoDefinition"]]
    Interface3AllowedAddressPairs: Optional[Sequence["_Interface3AllowedAddressPairsDefinition"]]
    Interface3FixedIps: Optional[Sequence["_Interface3FixedIpsDefinition"]]
    Interface3Info: Optional[Sequence["_Interface3InfoDefinition"]]
    Interface4AllowedAddressPairs: Optional[Sequence["_Interface4AllowedAddressPairsDefinition"]]
    Interface4FixedIps: Optional[Sequence["_Interface4FixedIpsDefinition"]]
    Interface4Info: Optional[Sequence["_Interface4InfoDefinition"]]
    Interface5AllowedAddressPairs: Optional[Sequence["_Interface5AllowedAddressPairsDefinition"]]
    Interface5FixedIps: Optional[Sequence["_Interface5FixedIpsDefinition"]]
    Interface5Info: Optional[Sequence["_Interface5InfoDefinition"]]
    Interface6AllowedAddressPairs: Optional[Sequence["_Interface6AllowedAddressPairsDefinition"]]
    Interface6FixedIps: Optional[Sequence["_Interface6FixedIpsDefinition"]]
    Interface6Info: Optional[Sequence["_Interface6InfoDefinition"]]
    Interface7AllowedAddressPairs: Optional[Sequence["_Interface7AllowedAddressPairsDefinition"]]
    Interface7FixedIps: Optional[Sequence["_Interface7FixedIpsDefinition"]]
    Interface7Info: Optional[Sequence["_Interface7InfoDefinition"]]
    Interface8AllowedAddressPairs: Optional[Sequence["_Interface8AllowedAddressPairsDefinition"]]
    Interface8FixedIps: Optional[Sequence["_Interface8FixedIpsDefinition"]]
    Interface8Info: Optional[Sequence["_Interface8InfoDefinition"]]
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
            AvailabilityZone=json_data.get("AvailabilityZone"),
            DefaultGateway=json_data.get("DefaultGateway"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Interface1NoAllowedAddressPairs=json_data.get("Interface1NoAllowedAddressPairs"),
            Interface1NoFixedIps=json_data.get("Interface1NoFixedIps"),
            Interface2NoAllowedAddressPairs=json_data.get("Interface2NoAllowedAddressPairs"),
            Interface2NoFixedIps=json_data.get("Interface2NoFixedIps"),
            Interface3NoAllowedAddressPairs=json_data.get("Interface3NoAllowedAddressPairs"),
            Interface3NoFixedIps=json_data.get("Interface3NoFixedIps"),
            Interface4NoAllowedAddressPairs=json_data.get("Interface4NoAllowedAddressPairs"),
            Interface4NoFixedIps=json_data.get("Interface4NoFixedIps"),
            Interface5NoAllowedAddressPairs=json_data.get("Interface5NoAllowedAddressPairs"),
            Interface5NoFixedIps=json_data.get("Interface5NoFixedIps"),
            Interface6NoAllowedAddressPairs=json_data.get("Interface6NoAllowedAddressPairs"),
            Interface6NoFixedIps=json_data.get("Interface6NoFixedIps"),
            Interface7NoAllowedAddressPairs=json_data.get("Interface7NoAllowedAddressPairs"),
            Interface7NoFixedIps=json_data.get("Interface7NoFixedIps"),
            Interface8NoAllowedAddressPairs=json_data.get("Interface8NoAllowedAddressPairs"),
            Interface8NoFixedIps=json_data.get("Interface8NoFixedIps"),
            Name=json_data.get("Name"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TenantId=json_data.get("TenantId"),
            VirtualNetworkAppliancePlanId=json_data.get("VirtualNetworkAppliancePlanId"),
            Interface1AllowedAddressPairs=deserialize_list(json_data.get("Interface1AllowedAddressPairs"), Interface1AllowedAddressPairsDefinition),
            Interface1FixedIps=deserialize_list(json_data.get("Interface1FixedIps"), Interface1FixedIpsDefinition),
            Interface1Info=deserialize_list(json_data.get("Interface1Info"), Interface1InfoDefinition),
            Interface2AllowedAddressPairs=deserialize_list(json_data.get("Interface2AllowedAddressPairs"), Interface2AllowedAddressPairsDefinition),
            Interface2FixedIps=deserialize_list(json_data.get("Interface2FixedIps"), Interface2FixedIpsDefinition),
            Interface2Info=deserialize_list(json_data.get("Interface2Info"), Interface2InfoDefinition),
            Interface3AllowedAddressPairs=deserialize_list(json_data.get("Interface3AllowedAddressPairs"), Interface3AllowedAddressPairsDefinition),
            Interface3FixedIps=deserialize_list(json_data.get("Interface3FixedIps"), Interface3FixedIpsDefinition),
            Interface3Info=deserialize_list(json_data.get("Interface3Info"), Interface3InfoDefinition),
            Interface4AllowedAddressPairs=deserialize_list(json_data.get("Interface4AllowedAddressPairs"), Interface4AllowedAddressPairsDefinition),
            Interface4FixedIps=deserialize_list(json_data.get("Interface4FixedIps"), Interface4FixedIpsDefinition),
            Interface4Info=deserialize_list(json_data.get("Interface4Info"), Interface4InfoDefinition),
            Interface5AllowedAddressPairs=deserialize_list(json_data.get("Interface5AllowedAddressPairs"), Interface5AllowedAddressPairsDefinition),
            Interface5FixedIps=deserialize_list(json_data.get("Interface5FixedIps"), Interface5FixedIpsDefinition),
            Interface5Info=deserialize_list(json_data.get("Interface5Info"), Interface5InfoDefinition),
            Interface6AllowedAddressPairs=deserialize_list(json_data.get("Interface6AllowedAddressPairs"), Interface6AllowedAddressPairsDefinition),
            Interface6FixedIps=deserialize_list(json_data.get("Interface6FixedIps"), Interface6FixedIpsDefinition),
            Interface6Info=deserialize_list(json_data.get("Interface6Info"), Interface6InfoDefinition),
            Interface7AllowedAddressPairs=deserialize_list(json_data.get("Interface7AllowedAddressPairs"), Interface7AllowedAddressPairsDefinition),
            Interface7FixedIps=deserialize_list(json_data.get("Interface7FixedIps"), Interface7FixedIpsDefinition),
            Interface7Info=deserialize_list(json_data.get("Interface7Info"), Interface7InfoDefinition),
            Interface8AllowedAddressPairs=deserialize_list(json_data.get("Interface8AllowedAddressPairs"), Interface8AllowedAddressPairsDefinition),
            Interface8FixedIps=deserialize_list(json_data.get("Interface8FixedIps"), Interface8FixedIpsDefinition),
            Interface8Info=deserialize_list(json_data.get("Interface8Info"), Interface8InfoDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
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
class Interface1AllowedAddressPairsDefinition(BaseModel):
    IpAddress: Optional[str]
    MacAddress: Optional[str]
    Type: Optional[str]
    Vrid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Interface1AllowedAddressPairsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Interface1AllowedAddressPairsDefinition"]:
        if not json_data:
            return None
        return cls(
            IpAddress=json_data.get("IpAddress"),
            MacAddress=json_data.get("MacAddress"),
            Type=json_data.get("Type"),
            Vrid=json_data.get("Vrid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Interface1AllowedAddressPairsDefinition = Interface1AllowedAddressPairsDefinition


@dataclass
class Interface1FixedIpsDefinition(BaseModel):
    IpAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Interface1FixedIpsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Interface1FixedIpsDefinition"]:
        if not json_data:
            return None
        return cls(
            IpAddress=json_data.get("IpAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Interface1FixedIpsDefinition = Interface1FixedIpsDefinition


@dataclass
class Interface1InfoDefinition(BaseModel):
    Description: Optional[str]
    Name: Optional[str]
    NetworkId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition2"]]

    @classmethod
    def _deserialize(
        cls: Type["_Interface1InfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Interface1InfoDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            NetworkId=json_data.get("NetworkId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition2),
        )


# work around possible type aliasing issues when variable has same name as a model
_Interface1InfoDefinition = Interface1InfoDefinition


@dataclass
class TagsDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition2 = TagsDefinition2


@dataclass
class Interface2AllowedAddressPairsDefinition(BaseModel):
    IpAddress: Optional[str]
    MacAddress: Optional[str]
    Type: Optional[str]
    Vrid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Interface2AllowedAddressPairsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Interface2AllowedAddressPairsDefinition"]:
        if not json_data:
            return None
        return cls(
            IpAddress=json_data.get("IpAddress"),
            MacAddress=json_data.get("MacAddress"),
            Type=json_data.get("Type"),
            Vrid=json_data.get("Vrid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Interface2AllowedAddressPairsDefinition = Interface2AllowedAddressPairsDefinition


@dataclass
class Interface2FixedIpsDefinition(BaseModel):
    IpAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Interface2FixedIpsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Interface2FixedIpsDefinition"]:
        if not json_data:
            return None
        return cls(
            IpAddress=json_data.get("IpAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Interface2FixedIpsDefinition = Interface2FixedIpsDefinition


@dataclass
class Interface2InfoDefinition(BaseModel):
    Description: Optional[str]
    Name: Optional[str]
    NetworkId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition3"]]

    @classmethod
    def _deserialize(
        cls: Type["_Interface2InfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Interface2InfoDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            NetworkId=json_data.get("NetworkId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition3),
        )


# work around possible type aliasing issues when variable has same name as a model
_Interface2InfoDefinition = Interface2InfoDefinition


@dataclass
class TagsDefinition3(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition3"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition3 = TagsDefinition3


@dataclass
class Interface3AllowedAddressPairsDefinition(BaseModel):
    IpAddress: Optional[str]
    MacAddress: Optional[str]
    Type: Optional[str]
    Vrid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Interface3AllowedAddressPairsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Interface3AllowedAddressPairsDefinition"]:
        if not json_data:
            return None
        return cls(
            IpAddress=json_data.get("IpAddress"),
            MacAddress=json_data.get("MacAddress"),
            Type=json_data.get("Type"),
            Vrid=json_data.get("Vrid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Interface3AllowedAddressPairsDefinition = Interface3AllowedAddressPairsDefinition


@dataclass
class Interface3FixedIpsDefinition(BaseModel):
    IpAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Interface3FixedIpsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Interface3FixedIpsDefinition"]:
        if not json_data:
            return None
        return cls(
            IpAddress=json_data.get("IpAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Interface3FixedIpsDefinition = Interface3FixedIpsDefinition


@dataclass
class Interface3InfoDefinition(BaseModel):
    Description: Optional[str]
    Name: Optional[str]
    NetworkId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition4"]]

    @classmethod
    def _deserialize(
        cls: Type["_Interface3InfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Interface3InfoDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            NetworkId=json_data.get("NetworkId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition4),
        )


# work around possible type aliasing issues when variable has same name as a model
_Interface3InfoDefinition = Interface3InfoDefinition


@dataclass
class TagsDefinition4(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition4"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition4 = TagsDefinition4


@dataclass
class Interface4AllowedAddressPairsDefinition(BaseModel):
    IpAddress: Optional[str]
    MacAddress: Optional[str]
    Type: Optional[str]
    Vrid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Interface4AllowedAddressPairsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Interface4AllowedAddressPairsDefinition"]:
        if not json_data:
            return None
        return cls(
            IpAddress=json_data.get("IpAddress"),
            MacAddress=json_data.get("MacAddress"),
            Type=json_data.get("Type"),
            Vrid=json_data.get("Vrid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Interface4AllowedAddressPairsDefinition = Interface4AllowedAddressPairsDefinition


@dataclass
class Interface4FixedIpsDefinition(BaseModel):
    IpAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Interface4FixedIpsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Interface4FixedIpsDefinition"]:
        if not json_data:
            return None
        return cls(
            IpAddress=json_data.get("IpAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Interface4FixedIpsDefinition = Interface4FixedIpsDefinition


@dataclass
class Interface4InfoDefinition(BaseModel):
    Description: Optional[str]
    Name: Optional[str]
    NetworkId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition5"]]

    @classmethod
    def _deserialize(
        cls: Type["_Interface4InfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Interface4InfoDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            NetworkId=json_data.get("NetworkId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition5),
        )


# work around possible type aliasing issues when variable has same name as a model
_Interface4InfoDefinition = Interface4InfoDefinition


@dataclass
class TagsDefinition5(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition5"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition5"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition5 = TagsDefinition5


@dataclass
class Interface5AllowedAddressPairsDefinition(BaseModel):
    IpAddress: Optional[str]
    MacAddress: Optional[str]
    Type: Optional[str]
    Vrid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Interface5AllowedAddressPairsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Interface5AllowedAddressPairsDefinition"]:
        if not json_data:
            return None
        return cls(
            IpAddress=json_data.get("IpAddress"),
            MacAddress=json_data.get("MacAddress"),
            Type=json_data.get("Type"),
            Vrid=json_data.get("Vrid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Interface5AllowedAddressPairsDefinition = Interface5AllowedAddressPairsDefinition


@dataclass
class Interface5FixedIpsDefinition(BaseModel):
    IpAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Interface5FixedIpsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Interface5FixedIpsDefinition"]:
        if not json_data:
            return None
        return cls(
            IpAddress=json_data.get("IpAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Interface5FixedIpsDefinition = Interface5FixedIpsDefinition


@dataclass
class Interface5InfoDefinition(BaseModel):
    Description: Optional[str]
    Name: Optional[str]
    NetworkId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition6"]]

    @classmethod
    def _deserialize(
        cls: Type["_Interface5InfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Interface5InfoDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            NetworkId=json_data.get("NetworkId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition6),
        )


# work around possible type aliasing issues when variable has same name as a model
_Interface5InfoDefinition = Interface5InfoDefinition


@dataclass
class TagsDefinition6(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition6"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition6"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition6 = TagsDefinition6


@dataclass
class Interface6AllowedAddressPairsDefinition(BaseModel):
    IpAddress: Optional[str]
    MacAddress: Optional[str]
    Type: Optional[str]
    Vrid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Interface6AllowedAddressPairsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Interface6AllowedAddressPairsDefinition"]:
        if not json_data:
            return None
        return cls(
            IpAddress=json_data.get("IpAddress"),
            MacAddress=json_data.get("MacAddress"),
            Type=json_data.get("Type"),
            Vrid=json_data.get("Vrid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Interface6AllowedAddressPairsDefinition = Interface6AllowedAddressPairsDefinition


@dataclass
class Interface6FixedIpsDefinition(BaseModel):
    IpAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Interface6FixedIpsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Interface6FixedIpsDefinition"]:
        if not json_data:
            return None
        return cls(
            IpAddress=json_data.get("IpAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Interface6FixedIpsDefinition = Interface6FixedIpsDefinition


@dataclass
class Interface6InfoDefinition(BaseModel):
    Description: Optional[str]
    Name: Optional[str]
    NetworkId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition7"]]

    @classmethod
    def _deserialize(
        cls: Type["_Interface6InfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Interface6InfoDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            NetworkId=json_data.get("NetworkId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition7),
        )


# work around possible type aliasing issues when variable has same name as a model
_Interface6InfoDefinition = Interface6InfoDefinition


@dataclass
class TagsDefinition7(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition7"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition7"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition7 = TagsDefinition7


@dataclass
class Interface7AllowedAddressPairsDefinition(BaseModel):
    IpAddress: Optional[str]
    MacAddress: Optional[str]
    Type: Optional[str]
    Vrid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Interface7AllowedAddressPairsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Interface7AllowedAddressPairsDefinition"]:
        if not json_data:
            return None
        return cls(
            IpAddress=json_data.get("IpAddress"),
            MacAddress=json_data.get("MacAddress"),
            Type=json_data.get("Type"),
            Vrid=json_data.get("Vrid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Interface7AllowedAddressPairsDefinition = Interface7AllowedAddressPairsDefinition


@dataclass
class Interface7FixedIpsDefinition(BaseModel):
    IpAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Interface7FixedIpsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Interface7FixedIpsDefinition"]:
        if not json_data:
            return None
        return cls(
            IpAddress=json_data.get("IpAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Interface7FixedIpsDefinition = Interface7FixedIpsDefinition


@dataclass
class Interface7InfoDefinition(BaseModel):
    Description: Optional[str]
    Name: Optional[str]
    NetworkId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition8"]]

    @classmethod
    def _deserialize(
        cls: Type["_Interface7InfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Interface7InfoDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            NetworkId=json_data.get("NetworkId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition8),
        )


# work around possible type aliasing issues when variable has same name as a model
_Interface7InfoDefinition = Interface7InfoDefinition


@dataclass
class TagsDefinition8(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition8"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition8"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition8 = TagsDefinition8


@dataclass
class Interface8AllowedAddressPairsDefinition(BaseModel):
    IpAddress: Optional[str]
    MacAddress: Optional[str]
    Type: Optional[str]
    Vrid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Interface8AllowedAddressPairsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Interface8AllowedAddressPairsDefinition"]:
        if not json_data:
            return None
        return cls(
            IpAddress=json_data.get("IpAddress"),
            MacAddress=json_data.get("MacAddress"),
            Type=json_data.get("Type"),
            Vrid=json_data.get("Vrid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Interface8AllowedAddressPairsDefinition = Interface8AllowedAddressPairsDefinition


@dataclass
class Interface8FixedIpsDefinition(BaseModel):
    IpAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Interface8FixedIpsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Interface8FixedIpsDefinition"]:
        if not json_data:
            return None
        return cls(
            IpAddress=json_data.get("IpAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Interface8FixedIpsDefinition = Interface8FixedIpsDefinition


@dataclass
class Interface8InfoDefinition(BaseModel):
    Description: Optional[str]
    Name: Optional[str]
    NetworkId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition9"]]

    @classmethod
    def _deserialize(
        cls: Type["_Interface8InfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Interface8InfoDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            NetworkId=json_data.get("NetworkId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition9),
        )


# work around possible type aliasing issues when variable has same name as a model
_Interface8InfoDefinition = Interface8InfoDefinition


@dataclass
class TagsDefinition9(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition9"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition9"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition9 = TagsDefinition9


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


