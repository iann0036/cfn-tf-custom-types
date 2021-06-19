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
    CutoffOption: Optional[str]
    CutoffTime: Optional[str]
    Day: Optional[str]
    Description: Optional[str]
    DynamicSortSubtable: Optional[str]
    EmailRecipients: Optional[str]
    EmailSend: Optional[str]
    Format: Optional[str]
    Id: Optional[str]
    MaxPdfReport: Optional[float]
    Name: Optional[str]
    Options: Optional[str]
    ScheduleType: Optional[str]
    StyleTheme: Optional[str]
    Subtitle: Optional[str]
    Time: Optional[str]
    Title: Optional[str]
    Vdomparam: Optional[str]
    BodyItem: Optional[Sequence["_BodyItemDefinition"]]
    Page: Optional[Sequence["_PageDefinition"]]

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
            CutoffOption=json_data.get("CutoffOption"),
            CutoffTime=json_data.get("CutoffTime"),
            Day=json_data.get("Day"),
            Description=json_data.get("Description"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            EmailRecipients=json_data.get("EmailRecipients"),
            EmailSend=json_data.get("EmailSend"),
            Format=json_data.get("Format"),
            Id=json_data.get("Id"),
            MaxPdfReport=json_data.get("MaxPdfReport"),
            Name=json_data.get("Name"),
            Options=json_data.get("Options"),
            ScheduleType=json_data.get("ScheduleType"),
            StyleTheme=json_data.get("StyleTheme"),
            Subtitle=json_data.get("Subtitle"),
            Time=json_data.get("Time"),
            Title=json_data.get("Title"),
            Vdomparam=json_data.get("Vdomparam"),
            BodyItem=deserialize_list(json_data.get("BodyItem"), BodyItemDefinition),
            Page=deserialize_list(json_data.get("Page"), PageDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BodyItemDefinition(BaseModel):
    Chart: Optional[str]
    ChartOptions: Optional[str]
    Column: Optional[float]
    Content: Optional[str]
    Description: Optional[str]
    DrillDownItems: Optional[str]
    DrillDownTypes: Optional[str]
    Hide: Optional[str]
    Id: Optional[float]
    ImgSrc: Optional[str]
    ListComponent: Optional[str]
    MiscComponent: Optional[str]
    Style: Optional[str]
    TableCaptionStyle: Optional[str]
    TableColumnWidths: Optional[str]
    TableEvenRowStyle: Optional[str]
    TableHeadStyle: Optional[str]
    TableOddRowStyle: Optional[str]
    TextComponent: Optional[str]
    Title: Optional[str]
    TopN: Optional[float]
    Type: Optional[str]
    List: Optional[Sequence["_ListDefinition"]]
    Parameters: Optional[Sequence["_ParametersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BodyItemDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BodyItemDefinition"]:
        if not json_data:
            return None
        return cls(
            Chart=json_data.get("Chart"),
            ChartOptions=json_data.get("ChartOptions"),
            Column=json_data.get("Column"),
            Content=json_data.get("Content"),
            Description=json_data.get("Description"),
            DrillDownItems=json_data.get("DrillDownItems"),
            DrillDownTypes=json_data.get("DrillDownTypes"),
            Hide=json_data.get("Hide"),
            Id=json_data.get("Id"),
            ImgSrc=json_data.get("ImgSrc"),
            ListComponent=json_data.get("ListComponent"),
            MiscComponent=json_data.get("MiscComponent"),
            Style=json_data.get("Style"),
            TableCaptionStyle=json_data.get("TableCaptionStyle"),
            TableColumnWidths=json_data.get("TableColumnWidths"),
            TableEvenRowStyle=json_data.get("TableEvenRowStyle"),
            TableHeadStyle=json_data.get("TableHeadStyle"),
            TableOddRowStyle=json_data.get("TableOddRowStyle"),
            TextComponent=json_data.get("TextComponent"),
            Title=json_data.get("Title"),
            TopN=json_data.get("TopN"),
            Type=json_data.get("Type"),
            List=deserialize_list(json_data.get("List"), ListDefinition),
            Parameters=deserialize_list(json_data.get("Parameters"), ParametersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BodyItemDefinition = BodyItemDefinition


@dataclass
class ListDefinition(BaseModel):
    Content: Optional[str]
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ListDefinition"]:
        if not json_data:
            return None
        return cls(
            Content=json_data.get("Content"),
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ListDefinition = ListDefinition


@dataclass
class ParametersDefinition(BaseModel):
    Id: Optional[float]
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParametersDefinition = ParametersDefinition


@dataclass
class PageDefinition(BaseModel):
    ColumnBreakBefore: Optional[str]
    Options: Optional[str]
    PageBreakBefore: Optional[str]
    Paper: Optional[str]
    Footer: Optional[Sequence["_FooterDefinition"]]
    Header: Optional[Sequence["_HeaderDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PageDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PageDefinition"]:
        if not json_data:
            return None
        return cls(
            ColumnBreakBefore=json_data.get("ColumnBreakBefore"),
            Options=json_data.get("Options"),
            PageBreakBefore=json_data.get("PageBreakBefore"),
            Paper=json_data.get("Paper"),
            Footer=deserialize_list(json_data.get("Footer"), FooterDefinition),
            Header=deserialize_list(json_data.get("Header"), HeaderDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PageDefinition = PageDefinition


@dataclass
class FooterDefinition(BaseModel):
    Style: Optional[str]
    FooterItem: Optional[Sequence["_FooterItemDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FooterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FooterDefinition"]:
        if not json_data:
            return None
        return cls(
            Style=json_data.get("Style"),
            FooterItem=deserialize_list(json_data.get("FooterItem"), FooterItemDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FooterDefinition = FooterDefinition


@dataclass
class FooterItemDefinition(BaseModel):
    Content: Optional[str]
    Description: Optional[str]
    Id: Optional[float]
    ImgSrc: Optional[str]
    Style: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FooterItemDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FooterItemDefinition"]:
        if not json_data:
            return None
        return cls(
            Content=json_data.get("Content"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            ImgSrc=json_data.get("ImgSrc"),
            Style=json_data.get("Style"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FooterItemDefinition = FooterItemDefinition


@dataclass
class HeaderDefinition(BaseModel):
    Style: Optional[str]
    HeaderItem: Optional[Sequence["_HeaderItemDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HeaderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeaderDefinition"]:
        if not json_data:
            return None
        return cls(
            Style=json_data.get("Style"),
            HeaderItem=deserialize_list(json_data.get("HeaderItem"), HeaderItemDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeaderDefinition = HeaderDefinition


@dataclass
class HeaderItemDefinition(BaseModel):
    Content: Optional[str]
    Description: Optional[str]
    Id: Optional[float]
    ImgSrc: Optional[str]
    Style: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeaderItemDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeaderItemDefinition"]:
        if not json_data:
            return None
        return cls(
            Content=json_data.get("Content"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            ImgSrc=json_data.get("ImgSrc"),
            Style=json_data.get("Style"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeaderItemDefinition = HeaderItemDefinition


