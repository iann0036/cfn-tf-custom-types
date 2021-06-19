# TF::FortiOS::UserNacpolicy

Configure NAC policy matching pattern to identify matching NAC devices. Applies to FortiOS Version `>= 6.4.0`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::UserNacpolicy",
    "Properties" : {
        "<a href="#category" title="Category">Category</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#emstag" title="EmsTag">EmsTag</a>" : <i>String</i>,
        "<a href="#family" title="Family">Family</a>" : <i>String</i>,
        "<a href="#host" title="Host">Host</a>" : <i>String</i>,
        "<a href="#hwvendor" title="HwVendor">HwVendor</a>" : <i>String</i>,
        "<a href="#hwversion" title="HwVersion">HwVersion</a>" : <i>String</i>,
        "<a href="#mac" title="Mac">Mac</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#os" title="Os">Os</a>" : <i>String</i>,
        "<a href="#src" title="Src">Src</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#swversion" title="SwVersion">SwVersion</a>" : <i>String</i>,
        "<a href="#switchautoauth" title="SwitchAutoAuth">SwitchAutoAuth</a>" : <i>String</i>,
        "<a href="#switchfortilink" title="SwitchFortilink">SwitchFortilink</a>" : <i>String</i>,
        "<a href="#switchmacpolicy" title="SwitchMacPolicy">SwitchMacPolicy</a>" : <i>String</i>,
        "<a href="#switchportpolicy" title="SwitchPortPolicy">SwitchPortPolicy</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#user" title="User">User</a>" : <i>String</i>,
        "<a href="#usergroup" title="UserGroup">UserGroup</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#switchscope" title="SwitchScope">SwitchScope</a>" : <i>[ <a href="switchscopedefinition.md">SwitchScopeDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::UserNacpolicy
Properties:
    <a href="#category" title="Category">Category</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#emstag" title="EmsTag">EmsTag</a>: <i>String</i>
    <a href="#family" title="Family">Family</a>: <i>String</i>
    <a href="#host" title="Host">Host</a>: <i>String</i>
    <a href="#hwvendor" title="HwVendor">HwVendor</a>: <i>String</i>
    <a href="#hwversion" title="HwVersion">HwVersion</a>: <i>String</i>
    <a href="#mac" title="Mac">Mac</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#os" title="Os">Os</a>: <i>String</i>
    <a href="#src" title="Src">Src</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#swversion" title="SwVersion">SwVersion</a>: <i>String</i>
    <a href="#switchautoauth" title="SwitchAutoAuth">SwitchAutoAuth</a>: <i>String</i>
    <a href="#switchfortilink" title="SwitchFortilink">SwitchFortilink</a>: <i>String</i>
    <a href="#switchmacpolicy" title="SwitchMacPolicy">SwitchMacPolicy</a>: <i>String</i>
    <a href="#switchportpolicy" title="SwitchPortPolicy">SwitchPortPolicy</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#user" title="User">User</a>: <i>String</i>
    <a href="#usergroup" title="UserGroup">UserGroup</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#switchscope" title="SwitchScope">SwitchScope</a>: <i>
      - <a href="switchscopedefinition.md">SwitchScopeDefinition</a></i>
</pre>

## Properties

#### Category

Category of NAC policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description for the NAC policy matching pattern.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmsTag

NAC policy matching EMS tag.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Family

NAC policy matching family.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Host

NAC policy matching host.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HwVendor

NAC policy matching hardware vendor.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HwVersion

NAC policy matching hardware version.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mac

NAC policy matching MAC address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

NAC policy name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Os

NAC policy matching operating system.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Src

NAC policy matching source.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable NAC policy. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SwVersion

NAC policy matching software version.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SwitchAutoAuth

NAC device auto authorization when discovered and nac-policy matched. Valid values: `global`, `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SwitchFortilink

FortiLink interface for which this NAC policy belongs to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SwitchMacPolicy

switch-mac-policy to be applied on the matched NAC policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SwitchPortPolicy

switch-port-policy to be applied on the matched NAC policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

NAC policy matching type.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### User

NAC policy matching user.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserGroup

NAC policy matching user group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SwitchScope

_Required_: No

_Type_: List of <a href="switchscopedefinition.md">SwitchScopeDefinition</a>

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

