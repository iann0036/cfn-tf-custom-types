# TF::Wavefront::Dashboard

CloudFormation equivalent of wavefront_dashboard

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Wavefront::Dashboard",
    "Properties" : {
        "<a href="#canmodify" title="CanModify">CanModify</a>" : <i>[ String, ... ]</i>,
        "<a href="#canview" title="CanView">CanView</a>" : <i>[ String, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayqueryparameters" title="DisplayQueryParameters">DisplayQueryParameters</a>" : <i>Boolean</i>,
        "<a href="#displaysectiontableofcontents" title="DisplaySectionTableOfContents">DisplaySectionTableOfContents</a>" : <i>Boolean</i>,
        "<a href="#eventfiltertype" title="EventFilterType">EventFilterType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#url" title="Url">Url</a>" : <i>String</i>,
        "<a href="#parameterdetails" title="ParameterDetails">ParameterDetails</a>" : <i>[ <a href="parameterdetailsdefinition.md">ParameterDetailsDefinition</a>, ... ]</i>,
        "<a href="#section" title="Section">Section</a>" : <i>[ <a href="sectiondefinition.md">SectionDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Wavefront::Dashboard
Properties:
    <a href="#canmodify" title="CanModify">CanModify</a>: <i>
      - String</i>
    <a href="#canview" title="CanView">CanView</a>: <i>
      - String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayqueryparameters" title="DisplayQueryParameters">DisplayQueryParameters</a>: <i>Boolean</i>
    <a href="#displaysectiontableofcontents" title="DisplaySectionTableOfContents">DisplaySectionTableOfContents</a>: <i>Boolean</i>
    <a href="#eventfiltertype" title="EventFilterType">EventFilterType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#url" title="Url">Url</a>: <i>String</i>
    <a href="#parameterdetails" title="ParameterDetails">ParameterDetails</a>: <i>
      - <a href="parameterdetailsdefinition.md">ParameterDetailsDefinition</a></i>
    <a href="#section" title="Section">Section</a>: <i>
      - <a href="sectiondefinition.md">SectionDefinition</a></i>
</pre>

## Properties

#### CanModify

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CanView

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayQueryParameters

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplaySectionTableOfContents

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventFilterType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParameterDetails

_Required_: No

_Type_: List of <a href="parameterdetailsdefinition.md">ParameterDetailsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Section

_Required_: No

_Type_: List of <a href="sectiondefinition.md">SectionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

