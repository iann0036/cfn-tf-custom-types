# TF::GoogleBeta::GoogleComputeFirewall

CloudFormation equivalent of google_compute_firewall

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GoogleBeta::GoogleComputeFirewall",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#destinationranges" title="DestinationRanges">DestinationRanges</a>" : <i>[ String, ... ]</i>,
        "<a href="#direction" title="Direction">Direction</a>" : <i>String</i>,
        "<a href="#disabled" title="Disabled">Disabled</a>" : <i>Boolean</i>,
        "<a href="#enablelogging" title="EnableLogging">EnableLogging</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#network" title="Network">Network</a>" : <i>String</i>,
        "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#sourceranges" title="SourceRanges">SourceRanges</a>" : <i>[ String, ... ]</i>,
        "<a href="#sourceserviceaccounts" title="SourceServiceAccounts">SourceServiceAccounts</a>" : <i>[ String, ... ]</i>,
        "<a href="#sourcetags" title="SourceTags">SourceTags</a>" : <i>[ String, ... ]</i>,
        "<a href="#targetserviceaccounts" title="TargetServiceAccounts">TargetServiceAccounts</a>" : <i>[ String, ... ]</i>,
        "<a href="#targettags" title="TargetTags">TargetTags</a>" : <i>[ String, ... ]</i>,
        "<a href="#allow" title="Allow">Allow</a>" : <i>[ <a href="allowdefinition.md">AllowDefinition</a>, ... ]</i>,
        "<a href="#deny" title="Deny">Deny</a>" : <i>[ <a href="denydefinition.md">DenyDefinition</a>, ... ]</i>,
        "<a href="#logconfig" title="LogConfig">LogConfig</a>" : <i>[ <a href="logconfigdefinition.md">LogConfigDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::GoogleBeta::GoogleComputeFirewall
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#destinationranges" title="DestinationRanges">DestinationRanges</a>: <i>
      - String</i>
    <a href="#direction" title="Direction">Direction</a>: <i>String</i>
    <a href="#disabled" title="Disabled">Disabled</a>: <i>Boolean</i>
    <a href="#enablelogging" title="EnableLogging">EnableLogging</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#network" title="Network">Network</a>: <i>String</i>
    <a href="#priority" title="Priority">Priority</a>: <i>Double</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#sourceranges" title="SourceRanges">SourceRanges</a>: <i>
      - String</i>
    <a href="#sourceserviceaccounts" title="SourceServiceAccounts">SourceServiceAccounts</a>: <i>
      - String</i>
    <a href="#sourcetags" title="SourceTags">SourceTags</a>: <i>
      - String</i>
    <a href="#targetserviceaccounts" title="TargetServiceAccounts">TargetServiceAccounts</a>: <i>
      - String</i>
    <a href="#targettags" title="TargetTags">TargetTags</a>: <i>
      - String</i>
    <a href="#allow" title="Allow">Allow</a>: <i>
      - <a href="allowdefinition.md">AllowDefinition</a></i>
    <a href="#deny" title="Deny">Deny</a>: <i>
      - <a href="denydefinition.md">DenyDefinition</a></i>
    <a href="#logconfig" title="LogConfig">LogConfig</a>: <i>
      - <a href="logconfigdefinition.md">LogConfigDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationRanges

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Direction

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableLogging

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Network

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceRanges

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceServiceAccounts

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceTags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetServiceAccounts

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetTags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Allow

_Required_: No

_Type_: List of <a href="allowdefinition.md">AllowDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Deny

_Required_: No

_Type_: List of <a href="denydefinition.md">DenyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogConfig

_Required_: No

_Type_: List of <a href="logconfigdefinition.md">LogConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreationTimestamp

Returns the <code>CreationTimestamp</code> value.

#### Id

Returns the <code>Id</code> value.

#### SelfLink

Returns the <code>SelfLink</code> value.

