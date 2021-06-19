# TF::OpsGenie::IncidentTemplate

Manages an Incident Template within Opsgenie.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OpsGenie::IncidentTemplate",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#details" title="Details">Details</a>" : <i>[ <a href="detailsdefinition.md">DetailsDefinition</a>, ... ]</i>,
        "<a href="#impactedservices" title="ImpactedServices">ImpactedServices</a>" : <i>[ String, ... ]</i>,
        "<a href="#message" title="Message">Message</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#priority" title="Priority">Priority</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#stakeholderproperties" title="StakeholderProperties">StakeholderProperties</a>" : <i>[ <a href="stakeholderpropertiesdefinition.md">StakeholderPropertiesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OpsGenie::IncidentTemplate
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#details" title="Details">Details</a>: <i>
      - <a href="detailsdefinition.md">DetailsDefinition</a></i>
    <a href="#impactedservices" title="ImpactedServices">ImpactedServices</a>: <i>
      - String</i>
    <a href="#message" title="Message">Message</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#priority" title="Priority">Priority</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#stakeholderproperties" title="StakeholderProperties">StakeholderProperties</a>: <i>
      - <a href="stakeholderpropertiesdefinition.md">StakeholderPropertiesDefinition</a></i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Details

_Required_: No

_Type_: List of <a href="detailsdefinition.md">DetailsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImpactedServices

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Message

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StakeholderProperties

_Required_: No

_Type_: List of <a href="stakeholderpropertiesdefinition.md">StakeholderPropertiesDefinition</a>

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

