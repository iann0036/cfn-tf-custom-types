# TF::Dynatrace::AzureCredentials

CloudFormation equivalent of dynatrace_azure_credentials

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Dynatrace::AzureCredentials",
    "Properties" : {
        "<a href="#active" title="Active">Active</a>" : <i>Boolean</i>,
        "<a href="#appid" title="AppId">AppId</a>" : <i>String</i>,
        "<a href="#autotagging" title="AutoTagging">AutoTagging</a>" : <i>Boolean</i>,
        "<a href="#directoryid" title="DirectoryId">DirectoryId</a>" : <i>String</i>,
        "<a href="#key" title="Key">Key</a>" : <i>String</i>,
        "<a href="#label" title="Label">Label</a>" : <i>String</i>,
        "<a href="#monitoronlytaggedentities" title="MonitorOnlyTaggedEntities">MonitorOnlyTaggedEntities</a>" : <i>Boolean</i>,
        "<a href="#unknowns" title="Unknowns">Unknowns</a>" : <i>String</i>,
        "<a href="#monitoronlytagpairs" title="MonitorOnlyTagPairs">MonitorOnlyTagPairs</a>" : <i>[ <a href="monitoronlytagpairsdefinition.md">MonitorOnlyTagPairsDefinition</a>, ... ]</i>,
        "<a href="#supportingservices" title="SupportingServices">SupportingServices</a>" : <i>[ <a href="supportingservicesdefinition.md">SupportingServicesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Dynatrace::AzureCredentials
Properties:
    <a href="#active" title="Active">Active</a>: <i>Boolean</i>
    <a href="#appid" title="AppId">AppId</a>: <i>String</i>
    <a href="#autotagging" title="AutoTagging">AutoTagging</a>: <i>Boolean</i>
    <a href="#directoryid" title="DirectoryId">DirectoryId</a>: <i>String</i>
    <a href="#key" title="Key">Key</a>: <i>String</i>
    <a href="#label" title="Label">Label</a>: <i>String</i>
    <a href="#monitoronlytaggedentities" title="MonitorOnlyTaggedEntities">MonitorOnlyTaggedEntities</a>: <i>Boolean</i>
    <a href="#unknowns" title="Unknowns">Unknowns</a>: <i>String</i>
    <a href="#monitoronlytagpairs" title="MonitorOnlyTagPairs">MonitorOnlyTagPairs</a>: <i>
      - <a href="monitoronlytagpairsdefinition.md">MonitorOnlyTagPairsDefinition</a></i>
    <a href="#supportingservices" title="SupportingServices">SupportingServices</a>: <i>
      - <a href="supportingservicesdefinition.md">SupportingServicesDefinition</a></i>
</pre>

## Properties

#### Active

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoTagging

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DirectoryId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Key

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Label

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonitorOnlyTaggedEntities

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Unknowns

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonitorOnlyTagPairs

_Required_: No

_Type_: List of <a href="monitoronlytagpairsdefinition.md">MonitorOnlyTagPairsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SupportingServices

_Required_: No

_Type_: List of <a href="supportingservicesdefinition.md">SupportingServicesDefinition</a>

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

