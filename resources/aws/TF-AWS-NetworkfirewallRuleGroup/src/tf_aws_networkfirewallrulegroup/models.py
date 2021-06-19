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
    Arn: Optional[str]
    Capacity: Optional[float]
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Rules: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Type: Optional[str]
    UpdateToken: Optional[str]
    RuleGroup: Optional[Sequence["_RuleGroupDefinition"]]

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
            Arn=json_data.get("Arn"),
            Capacity=json_data.get("Capacity"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Rules=json_data.get("Rules"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Type=json_data.get("Type"),
            UpdateToken=json_data.get("UpdateToken"),
            RuleGroup=deserialize_list(json_data.get("RuleGroup"), RuleGroupDefinition),
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
class RuleGroupDefinition(BaseModel):
    RuleVariables: Optional[Sequence["_RuleVariablesDefinition"]]
    RulesSource: Optional[Sequence["_RulesSourceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RuleGroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleGroupDefinition"]:
        if not json_data:
            return None
        return cls(
            RuleVariables=deserialize_list(json_data.get("RuleVariables"), RuleVariablesDefinition),
            RulesSource=deserialize_list(json_data.get("RulesSource"), RulesSourceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleGroupDefinition = RuleGroupDefinition


@dataclass
class RuleVariablesDefinition(BaseModel):
    IpSets: Optional[Sequence["_IpSetsDefinition"]]
    PortSets: Optional[Sequence["_PortSetsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RuleVariablesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleVariablesDefinition"]:
        if not json_data:
            return None
        return cls(
            IpSets=deserialize_list(json_data.get("IpSets"), IpSetsDefinition),
            PortSets=deserialize_list(json_data.get("PortSets"), PortSetsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleVariablesDefinition = RuleVariablesDefinition


@dataclass
class IpSetsDefinition(BaseModel):
    Key: Optional[str]
    IpSet: Optional[Sequence["_IpSetDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IpSetsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpSetsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            IpSet=deserialize_list(json_data.get("IpSet"), IpSetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpSetsDefinition = IpSetsDefinition


@dataclass
class IpSetDefinition(BaseModel):
    Definition: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_IpSetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpSetDefinition"]:
        if not json_data:
            return None
        return cls(
            Definition=json_data.get("Definition"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpSetDefinition = IpSetDefinition


@dataclass
class PortSetsDefinition(BaseModel):
    Key: Optional[str]
    PortSet: Optional[Sequence["_PortSetDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PortSetsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortSetsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            PortSet=deserialize_list(json_data.get("PortSet"), PortSetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortSetsDefinition = PortSetsDefinition


@dataclass
class PortSetDefinition(BaseModel):
    Definition: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PortSetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortSetDefinition"]:
        if not json_data:
            return None
        return cls(
            Definition=json_data.get("Definition"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortSetDefinition = PortSetDefinition


@dataclass
class RulesSourceDefinition(BaseModel):
    RulesString: Optional[str]
    RulesSourceList: Optional[Sequence["_RulesSourceListDefinition"]]
    StatefulRule: Optional[Sequence["_StatefulRuleDefinition"]]
    StatelessRulesAndCustomActions: Optional[Sequence["_StatelessRulesAndCustomActionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RulesSourceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RulesSourceDefinition"]:
        if not json_data:
            return None
        return cls(
            RulesString=json_data.get("RulesString"),
            RulesSourceList=deserialize_list(json_data.get("RulesSourceList"), RulesSourceListDefinition),
            StatefulRule=deserialize_list(json_data.get("StatefulRule"), StatefulRuleDefinition),
            StatelessRulesAndCustomActions=deserialize_list(json_data.get("StatelessRulesAndCustomActions"), StatelessRulesAndCustomActionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RulesSourceDefinition = RulesSourceDefinition


@dataclass
class RulesSourceListDefinition(BaseModel):
    GeneratedRulesType: Optional[str]
    TargetTypes: Optional[Sequence[str]]
    Targets: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_RulesSourceListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RulesSourceListDefinition"]:
        if not json_data:
            return None
        return cls(
            GeneratedRulesType=json_data.get("GeneratedRulesType"),
            TargetTypes=json_data.get("TargetTypes"),
            Targets=json_data.get("Targets"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RulesSourceListDefinition = RulesSourceListDefinition


@dataclass
class StatefulRuleDefinition(BaseModel):
    Action: Optional[str]
    Header: Optional[Sequence["_HeaderDefinition"]]
    RuleOption: Optional[Sequence["_RuleOptionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_StatefulRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatefulRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Header=deserialize_list(json_data.get("Header"), HeaderDefinition),
            RuleOption=deserialize_list(json_data.get("RuleOption"), RuleOptionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatefulRuleDefinition = StatefulRuleDefinition


@dataclass
class HeaderDefinition(BaseModel):
    Destination: Optional[str]
    DestinationPort: Optional[str]
    Direction: Optional[str]
    Protocol: Optional[str]
    Source: Optional[str]
    SourcePort: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeaderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeaderDefinition"]:
        if not json_data:
            return None
        return cls(
            Destination=json_data.get("Destination"),
            DestinationPort=json_data.get("DestinationPort"),
            Direction=json_data.get("Direction"),
            Protocol=json_data.get("Protocol"),
            Source=json_data.get("Source"),
            SourcePort=json_data.get("SourcePort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeaderDefinition = HeaderDefinition


@dataclass
class RuleOptionDefinition(BaseModel):
    Keyword: Optional[str]
    Settings: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_RuleOptionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleOptionDefinition"]:
        if not json_data:
            return None
        return cls(
            Keyword=json_data.get("Keyword"),
            Settings=json_data.get("Settings"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleOptionDefinition = RuleOptionDefinition


@dataclass
class StatelessRulesAndCustomActionsDefinition(BaseModel):
    CustomAction: Optional[Sequence["_CustomActionDefinition"]]
    StatelessRule: Optional[Sequence["_StatelessRuleDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_StatelessRulesAndCustomActionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatelessRulesAndCustomActionsDefinition"]:
        if not json_data:
            return None
        return cls(
            CustomAction=deserialize_list(json_data.get("CustomAction"), CustomActionDefinition),
            StatelessRule=deserialize_list(json_data.get("StatelessRule"), StatelessRuleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatelessRulesAndCustomActionsDefinition = StatelessRulesAndCustomActionsDefinition


@dataclass
class CustomActionDefinition(BaseModel):
    ActionName: Optional[str]
    ActionDefinition: Optional[Sequence["_ActionDefinitionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CustomActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomActionDefinition"]:
        if not json_data:
            return None
        return cls(
            ActionName=json_data.get("ActionName"),
            ActionDefinition=deserialize_list(json_data.get("ActionDefinition"), ActionDefinitionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomActionDefinition = CustomActionDefinition


@dataclass
class ActionDefinitionDefinition(BaseModel):
    PublishMetricAction: Optional[Sequence["_PublishMetricActionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ActionDefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionDefinitionDefinition"]:
        if not json_data:
            return None
        return cls(
            PublishMetricAction=deserialize_list(json_data.get("PublishMetricAction"), PublishMetricActionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionDefinitionDefinition = ActionDefinitionDefinition


@dataclass
class PublishMetricActionDefinition(BaseModel):
    Dimension: Optional[Sequence["_DimensionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PublishMetricActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublishMetricActionDefinition"]:
        if not json_data:
            return None
        return cls(
            Dimension=deserialize_list(json_data.get("Dimension"), DimensionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublishMetricActionDefinition = PublishMetricActionDefinition


@dataclass
class DimensionDefinition(BaseModel):
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DimensionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DimensionDefinition"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DimensionDefinition = DimensionDefinition


@dataclass
class StatelessRuleDefinition(BaseModel):
    Priority: Optional[float]
    RuleDefinition: Optional[Sequence["_RuleDefinitionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_StatelessRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatelessRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Priority=json_data.get("Priority"),
            RuleDefinition=deserialize_list(json_data.get("RuleDefinition"), RuleDefinitionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatelessRuleDefinition = StatelessRuleDefinition


@dataclass
class RuleDefinitionDefinition(BaseModel):
    Actions: Optional[Sequence[str]]
    MatchAttributes: Optional[Sequence["_MatchAttributesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RuleDefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleDefinitionDefinition"]:
        if not json_data:
            return None
        return cls(
            Actions=json_data.get("Actions"),
            MatchAttributes=deserialize_list(json_data.get("MatchAttributes"), MatchAttributesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleDefinitionDefinition = RuleDefinitionDefinition


@dataclass
class MatchAttributesDefinition(BaseModel):
    Protocols: Optional[Sequence[float]]
    Destination: Optional[Sequence["_DestinationDefinition"]]
    DestinationPort: Optional[Sequence["_DestinationPortDefinition"]]
    Source: Optional[Sequence["_SourceDefinition"]]
    SourcePort: Optional[Sequence["_SourcePortDefinition"]]
    TcpFlag: Optional[Sequence["_TcpFlagDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MatchAttributesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchAttributesDefinition"]:
        if not json_data:
            return None
        return cls(
            Protocols=json_data.get("Protocols"),
            Destination=deserialize_list(json_data.get("Destination"), DestinationDefinition),
            DestinationPort=deserialize_list(json_data.get("DestinationPort"), DestinationPortDefinition),
            Source=deserialize_list(json_data.get("Source"), SourceDefinition),
            SourcePort=deserialize_list(json_data.get("SourcePort"), SourcePortDefinition),
            TcpFlag=deserialize_list(json_data.get("TcpFlag"), TcpFlagDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchAttributesDefinition = MatchAttributesDefinition


@dataclass
class DestinationDefinition(BaseModel):
    AddressDefinition: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DestinationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestinationDefinition"]:
        if not json_data:
            return None
        return cls(
            AddressDefinition=json_data.get("AddressDefinition"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestinationDefinition = DestinationDefinition


@dataclass
class DestinationPortDefinition(BaseModel):
    FromPort: Optional[float]
    ToPort: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DestinationPortDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestinationPortDefinition"]:
        if not json_data:
            return None
        return cls(
            FromPort=json_data.get("FromPort"),
            ToPort=json_data.get("ToPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestinationPortDefinition = DestinationPortDefinition


@dataclass
class SourceDefinition(BaseModel):
    AddressDefinition: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceDefinition"]:
        if not json_data:
            return None
        return cls(
            AddressDefinition=json_data.get("AddressDefinition"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceDefinition = SourceDefinition


@dataclass
class SourcePortDefinition(BaseModel):
    FromPort: Optional[float]
    ToPort: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SourcePortDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourcePortDefinition"]:
        if not json_data:
            return None
        return cls(
            FromPort=json_data.get("FromPort"),
            ToPort=json_data.get("ToPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourcePortDefinition = SourcePortDefinition


@dataclass
class TcpFlagDefinition(BaseModel):
    Flags: Optional[Sequence[str]]
    Masks: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_TcpFlagDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TcpFlagDefinition"]:
        if not json_data:
            return None
        return cls(
            Flags=json_data.get("Flags"),
            Masks=json_data.get("Masks"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TcpFlagDefinition = TcpFlagDefinition


