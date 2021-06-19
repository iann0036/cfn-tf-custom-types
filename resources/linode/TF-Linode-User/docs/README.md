# TF::Linode::User

Manages a Linode User.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Linode::User",
    "Properties" : {
        "<a href="#email" title="Email">Email</a>" : <i>String</i>,
        "<a href="#restricted" title="Restricted">Restricted</a>" : <i>Boolean</i>,
        "<a href="#username" title="Username">Username</a>" : <i>String</i>,
        "<a href="#domaingrant" title="DomainGrant">DomainGrant</a>" : <i>[ <a href="domaingrantdefinition.md">DomainGrantDefinition</a>, ... ]</i>,
        "<a href="#globalgrants" title="GlobalGrants">GlobalGrants</a>" : <i>[ <a href="globalgrantsdefinition.md">GlobalGrantsDefinition</a>, ... ]</i>,
        "<a href="#imagegrant" title="ImageGrant">ImageGrant</a>" : <i>[ <a href="imagegrantdefinition.md">ImageGrantDefinition</a>, ... ]</i>,
        "<a href="#linodegrant" title="LinodeGrant">LinodeGrant</a>" : <i>[ <a href="linodegrantdefinition.md">LinodeGrantDefinition</a>, ... ]</i>,
        "<a href="#longviewgrant" title="LongviewGrant">LongviewGrant</a>" : <i>[ <a href="longviewgrantdefinition.md">LongviewGrantDefinition</a>, ... ]</i>,
        "<a href="#nodebalancergrant" title="NodebalancerGrant">NodebalancerGrant</a>" : <i>[ <a href="nodebalancergrantdefinition.md">NodebalancerGrantDefinition</a>, ... ]</i>,
        "<a href="#stackscriptgrant" title="StackscriptGrant">StackscriptGrant</a>" : <i>[ <a href="stackscriptgrantdefinition.md">StackscriptGrantDefinition</a>, ... ]</i>,
        "<a href="#volumegrant" title="VolumeGrant">VolumeGrant</a>" : <i>[ <a href="volumegrantdefinition.md">VolumeGrantDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Linode::User
Properties:
    <a href="#email" title="Email">Email</a>: <i>String</i>
    <a href="#restricted" title="Restricted">Restricted</a>: <i>Boolean</i>
    <a href="#username" title="Username">Username</a>: <i>String</i>
    <a href="#domaingrant" title="DomainGrant">DomainGrant</a>: <i>
      - <a href="domaingrantdefinition.md">DomainGrantDefinition</a></i>
    <a href="#globalgrants" title="GlobalGrants">GlobalGrants</a>: <i>
      - <a href="globalgrantsdefinition.md">GlobalGrantsDefinition</a></i>
    <a href="#imagegrant" title="ImageGrant">ImageGrant</a>: <i>
      - <a href="imagegrantdefinition.md">ImageGrantDefinition</a></i>
    <a href="#linodegrant" title="LinodeGrant">LinodeGrant</a>: <i>
      - <a href="linodegrantdefinition.md">LinodeGrantDefinition</a></i>
    <a href="#longviewgrant" title="LongviewGrant">LongviewGrant</a>: <i>
      - <a href="longviewgrantdefinition.md">LongviewGrantDefinition</a></i>
    <a href="#nodebalancergrant" title="NodebalancerGrant">NodebalancerGrant</a>: <i>
      - <a href="nodebalancergrantdefinition.md">NodebalancerGrantDefinition</a></i>
    <a href="#stackscriptgrant" title="StackscriptGrant">StackscriptGrant</a>: <i>
      - <a href="stackscriptgrantdefinition.md">StackscriptGrantDefinition</a></i>
    <a href="#volumegrant" title="VolumeGrant">VolumeGrant</a>: <i>
      - <a href="volumegrantdefinition.md">VolumeGrantDefinition</a></i>
</pre>

## Properties

#### Email

The email address of the user.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Restricted

If true, this user will only have explicit permissions granted.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

The username of the user.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainGrant

_Required_: No

_Type_: List of <a href="domaingrantdefinition.md">DomainGrantDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GlobalGrants

_Required_: No

_Type_: List of <a href="globalgrantsdefinition.md">GlobalGrantsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageGrant

_Required_: No

_Type_: List of <a href="imagegrantdefinition.md">ImageGrantDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinodeGrant

_Required_: No

_Type_: List of <a href="linodegrantdefinition.md">LinodeGrantDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LongviewGrant

_Required_: No

_Type_: List of <a href="longviewgrantdefinition.md">LongviewGrantDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodebalancerGrant

_Required_: No

_Type_: List of <a href="nodebalancergrantdefinition.md">NodebalancerGrantDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StackscriptGrant

_Required_: No

_Type_: List of <a href="stackscriptgrantdefinition.md">StackscriptGrantDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeGrant

_Required_: No

_Type_: List of <a href="volumegrantdefinition.md">VolumeGrantDefinition</a>

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

#### SshKeys

Returns the <code>SshKeys</code> value.

#### TfaEnabled

Returns the <code>TfaEnabled</code> value.

