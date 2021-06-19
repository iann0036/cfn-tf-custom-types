# TF::Dynatrace::AwsCredentials

CloudFormation equivalent of dynatrace_aws_credentials

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Dynatrace::AwsCredentials",
    "Properties" : {
        "<a href="#label" title="Label">Label</a>" : <i>String</i>,
        "<a href="#partitiontype" title="PartitionType">PartitionType</a>" : <i>String</i>,
        "<a href="#taggedonly" title="TaggedOnly">TaggedOnly</a>" : <i>Boolean</i>,
        "<a href="#unknowns" title="Unknowns">Unknowns</a>" : <i>String</i>,
        "<a href="#authenticationdata" title="AuthenticationData">AuthenticationData</a>" : <i>[ <a href="authenticationdatadefinition.md">AuthenticationDataDefinition</a>, ... ]</i>,
        "<a href="#supportingservicestomonitor" title="SupportingServicesToMonitor">SupportingServicesToMonitor</a>" : <i>[ <a href="supportingservicestomonitordefinition.md">SupportingServicesToMonitorDefinition</a>, ... ]</i>,
        "<a href="#tagstomonitor" title="TagsToMonitor">TagsToMonitor</a>" : <i>[ <a href="tagstomonitordefinition.md">TagsToMonitorDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Dynatrace::AwsCredentials
Properties:
    <a href="#label" title="Label">Label</a>: <i>String</i>
    <a href="#partitiontype" title="PartitionType">PartitionType</a>: <i>String</i>
    <a href="#taggedonly" title="TaggedOnly">TaggedOnly</a>: <i>Boolean</i>
    <a href="#unknowns" title="Unknowns">Unknowns</a>: <i>String</i>
    <a href="#authenticationdata" title="AuthenticationData">AuthenticationData</a>: <i>
      - <a href="authenticationdatadefinition.md">AuthenticationDataDefinition</a></i>
    <a href="#supportingservicestomonitor" title="SupportingServicesToMonitor">SupportingServicesToMonitor</a>: <i>
      - <a href="supportingservicestomonitordefinition.md">SupportingServicesToMonitorDefinition</a></i>
    <a href="#tagstomonitor" title="TagsToMonitor">TagsToMonitor</a>: <i>
      - <a href="tagstomonitordefinition.md">TagsToMonitorDefinition</a></i>
</pre>

## Properties

#### Label

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PartitionType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaggedOnly

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Unknowns

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthenticationData

_Required_: No

_Type_: List of <a href="authenticationdatadefinition.md">AuthenticationDataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SupportingServicesToMonitor

_Required_: No

_Type_: List of <a href="supportingservicestomonitordefinition.md">SupportingServicesToMonitorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsToMonitor

_Required_: No

_Type_: List of <a href="tagstomonitordefinition.md">TagsToMonitorDefinition</a>

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

