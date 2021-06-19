# TF::PrismaCloud::CloudAccount

Manage a cloud account on the Prisma Cloud platform.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::PrismaCloud::CloudAccount",
    "Properties" : {
        "<a href="#alibabacloud" title="AlibabaCloud">AlibabaCloud</a>" : <i>[ <a href="alibabaclouddefinition.md">AlibabaCloudDefinition</a>, ... ]</i>,
        "<a href="#aws" title="Aws">Aws</a>" : <i>[ <a href="awsdefinition.md">AwsDefinition</a>, ... ]</i>,
        "<a href="#azure" title="Azure">Azure</a>" : <i>[ <a href="azuredefinition.md">AzureDefinition</a>, ... ]</i>,
        "<a href="#gcp" title="Gcp">Gcp</a>" : <i>[ <a href="gcpdefinition.md">GcpDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::PrismaCloud::CloudAccount
Properties:
    <a href="#alibabacloud" title="AlibabaCloud">AlibabaCloud</a>: <i>
      - <a href="alibabaclouddefinition.md">AlibabaCloudDefinition</a></i>
    <a href="#aws" title="Aws">Aws</a>: <i>
      - <a href="awsdefinition.md">AwsDefinition</a></i>
    <a href="#azure" title="Azure">Azure</a>: <i>
      - <a href="azuredefinition.md">AzureDefinition</a></i>
    <a href="#gcp" title="Gcp">Gcp</a>: <i>
      - <a href="gcpdefinition.md">GcpDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AlibabaCloud

_Required_: No

_Type_: List of <a href="alibabaclouddefinition.md">AlibabaCloudDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Aws

_Required_: No

_Type_: List of <a href="awsdefinition.md">AwsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Azure

_Required_: No

_Type_: List of <a href="azuredefinition.md">AzureDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gcp

_Required_: No

_Type_: List of <a href="gcpdefinition.md">GcpDefinition</a>

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

#### Id

Returns the <code>Id</code> value.

